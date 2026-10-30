"""Minimal Processing-to-Java preprocessor for QR_STENCILER (sketch dir -> one Java file)."""
import sys, re, os, glob
src=sys.argv[1]; out=sys.argv[2]
files=sorted(glob.glob(os.path.join(src,'*.pde')), key=lambda f:(os.path.basename(f)!='QR_STENCILER.pde', f))
code=''.join(open(f,encoding='utf-8').read()+'\n' for f in files)
imports=sorted(set(re.findall(r'^\s*import\s+[^;]+;',code,re.M)))
code=re.sub(r'^\s*import\s+[^;]+;\s*$','',code,flags=re.M)
def transform(seg):
    seg=re.sub(r'\bcolor(\s*\[\s*\])?(?=\s+[A-Za-z_])',lambda m:'int'+(m.group(1) or ''),seg)
    seg=re.sub(r'\(\s*color\s*\)','(int)',seg)
    seg=re.sub(r'(?<![\w.])(\d+\.\d*|\.\d+)([eE][-+]?\d+)?(?![fFdD\w.])',lambda m:m.group(0)+'f',seg)
    seg=re.sub(r'(?<![\w.])int\s*\(','PApplet.parseInt(',seg)
    seg=re.sub(r'(?<![\w.])float\s*\(','PApplet.parseFloat(',seg)
    seg=re.sub(r'#([0-9A-Fa-f]{6})\b',lambda m:'0xFF'+m.group(1),seg)
    return seg
# split into code / string / comment tokens
tok=re.compile(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|//[^\n]*|/\*.*?\*/)',re.S)
parts=tok.split(code)
code=''.join(p if i%2 else transform(p) for i,p in enumerate(parts))
# Processing 3: size()/pixelDensity() belong in settings()
code=code.replace('size (1000, 750, JAVA2D);','').replace('pixelDensity(1); // Required after Processing 4.4.6+','')
code=code.replace('void setup() {','public void settings() { size(1000, 750, JAVA2D); pixelDensity(1); }\npublic void setup() {',1)
code=re.sub(r'\bvoid draw\(\)','public void draw()',code)
code=re.sub(r'\bvoid keyPressed\(\)','public void keyPressed()',code)
code=re.sub(r'(?<!public )\bint compareTo\(','public int compareTo(',code)
# headless run: take the input image from -Dqr=..., quit when done
code=code.replace('QRImageFilename = getUserSelectedQRCodeImageFilename(); // See FileLoading.pde','QRImageFilename = System.getProperty("qr");')
code=code.replace('    doMainProcess();\n    bCompleted = true;','    doMainProcess();\n    bCompleted = true;\n    exit();')
if True:
    code=code.replace('  strokeWeight (PDF_LINE_THICKNESS);\n  stroke(0, 0, 0);\n  noFill();','  if (System.getProperty("filled")!=null) { noStroke(); fill(0); } else { strokeWeight (PDF_LINE_THICKNESS); stroke(0, 0, 0); noFill(); }')
    code=code.replace('  boolean bDrawTitleText = true;','  boolean bDrawTitleText = (System.getProperty("filled")==null);')
    code=code.replace('  QR_PdfFullFilename += ".pdf";','  if (System.getProperty("filled")!=null) QR_PdfFullFilename += "_print";\n  QR_PdfFullFilename += ".pdf";')
java='\n'.join(['import processing.core.*;','import java.util.*;','import java.io.*;']+imports)+'\n\npublic class QR_STENCILER extends PApplet {\n'+code+'\n  public static void main(String[] a){ PApplet.main("QR_STENCILER"); }\n}\n'
open(out,'w',encoding='utf-8').write(java)
print('wrote',out,len(java))
