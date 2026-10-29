"""Composite flat artwork onto a blank product photo with fabric shading and displacement.
usage: composite.py blank.png art.png out.jpg cx cy width_px [mode] [opacity]
cx,cy = center of the art on the photo (fractions 0..1 or px); width_px = art width on photo (px or fraction of photo width)
mode: print (default, ink takes fabric shading), emboss (deboss/engrave: darkens with shading), reflect
"""
import sys, numpy as np
from PIL import Image, ImageFilter
def load(p): return Image.open(p)
blank=load(sys.argv[1]).convert('RGB'); art=load(sys.argv[2]).convert('RGBA')
W,H=blank.size
def v(x,ref): x=float(x); return x*ref if x<=1.0 else x
cx=v(sys.argv[4],W); cy=v(sys.argv[5],H); aw=int(v(sys.argv[6],W))
mode=sys.argv[7] if len(sys.argv)>7 else 'print'; op=float(sys.argv[8]) if len(sys.argv)>8 else 0.94
rot=float(sys.argv[9]) if len(sys.argv)>9 else 0.0
keep=float(sys.argv[10]) if len(sys.argv)>10 else 0.0
ah=int(art.height*aw/art.width)
art=art.resize((aw,ah),Image.LANCZOS)
if rot: art=art.rotate(rot,resample=Image.BICUBIC,expand=True); aw,ah=art.size
x0=int(cx-aw/2); y0=int(cy-ah/2)
B=np.asarray(blank).astype(np.float32)/255
lum=(0.299*B[...,0]+0.587*B[...,1]+0.114*B[...,2])
# shading map: fabric luminance relative to a heavy blur (keeps wrinkles, drops overall color)
blur=np.asarray(Image.fromarray((lum*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(40))).astype(np.float32)/255
import os
SS=float(os.environ.get('SHADE','1.0'))
shade=1+(np.clip(lum/np.maximum(blur,1e-3),0.6,1.4)-1)*SS
# displacement from fabric gradient
gy,gx=np.gradient(np.asarray(Image.fromarray((lum*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32)/255)
A=np.zeros((H,W,4),np.float32)
a=np.asarray(art).astype(np.float32)/255
ys=slice(max(y0,0),min(y0+ah,H)); xs=slice(max(x0,0),min(x0+aw,W))
A[ys,xs]=a[ys.start-y0:ys.stop-y0, xs.start-x0:xs.stop-x0]
k=W*0.012
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
sy=np.clip(yy+gy*k*40,0,H-1).astype(int); sx=np.clip(xx+gx*k*40,0,W-1).astype(int)
A=A[sy,sx]
rgb=A[...,:3]; al=A[...,3]*op
if mode=='print':
    ink=rgb*shade[...,None]
    # let fabric texture through: mix a little of the fabric's high-frequency luminance
    out=B*(1-al[...,None])+np.clip(ink,0,1)*al[...,None]
elif mode=='emboss':
    m=al
    d=int(max(1,W*0.0015))
    hi=np.clip(np.roll(np.roll(m,-d,0),-d,1)-m,0,1)  # upper-left rim catches light
    lo=np.clip(np.roll(np.roll(m,d,0),d,1)-m,0,1)
    dark=B*float(os.environ.get('DEPTH','0.6'))
    out=B*(1-m[...,None])+dark*m[...,None]
    out=out*(1-0.35*lo[...,None])+0.35*hi[...,None]*np.minimum(1,B*1.35)
elif mode=='reflect':
    ink=np.clip(rgb*shade[...,None],0,1)
    out=B*(1-al[...,None])+ink*al[...,None]
if keep>0:
    km=(lum>keep).astype(np.float32)
    km=np.asarray(Image.fromarray((km*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)/255
    out=out*(1-km[...,None])+B*km[...,None]
out=Image.fromarray((np.clip(out,0,1)*255).astype(np.uint8))
out.save(sys.argv[3],quality=92)
print('ok',out.size,(x0,y0,aw,ah))
