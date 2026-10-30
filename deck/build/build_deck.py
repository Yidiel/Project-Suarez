import json, sys, os, re, html
root=sys.argv[1]  # deck/
out=sys.argv[2]
files=sys.argv[3:]
S=[]
for f in files: S+=json.load(open(f,encoding="utf-8"))
S.sort(key=lambda s:s["n"])
e=html.escape
def inl(t):
    t=e(t or "")
    t=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
    return t
def render_src(svg):  # concepts svg path -> render jpg
    lane=svg.split("/")[0]; base=os.path.basename(svg)[:-4]
    return f"renders/r2/{lane}-{base}.jpg"
LANE={"streetwear":"#A42F2C","performance":"#147CB2","objects":"#F58B88","western":"#D24B27","latino":"#F29F1F"}
def part_of(n):
    if n<=4: return "open"
    if n<=20: return "context"
    if n<=32: return "foundation"
    if n<=52: return "exec"
    return "build"
def lane_of(n):
    for a,b,l in [(33,35,"streetwear"),(36,38,"performance"),(39,42,"objects"),(43,46,"western"),(47,50,"latino")]:
        if a<=n<=b: return l
    return None
used=set()
def imgs_html(imgs,cls="g"):
    o=[]
    for i in imgs or []:
        src=i["src"]
        if not os.path.exists(os.path.join(root,src)): continue
        used.add(src)
        o.append(f'<figure class="{cls}"><img src="{e(src)}" alt="{e(i.get("caption",""))}" loading="lazy"><figcaption>{inl(i.get("caption",""))}</figcaption></figure>')
    return "".join(o)
def pts(p):
    return "<ul class='pts'>"+"".join(f"<li>{inl(x)}</li>" for x in p)+"</ul>" if p else ""
def table(t):
    if not t: return ""
    h="".join(f"<th>{inl(x)}</th>" for x in t["head"])
    r="".join("<tr>"+"".join(f"<td>{inl(c)}</td>" for c in row)+"</tr>" for row in t["rows"])
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'
def srcs(s):
    return f'<p class="src">{" · ".join(e(x) for x in s)}</p>' if s else ""
def body(s): return f'<p class="body">{inl(s.get("body"))}</p>' if s.get("body") else ""
slides=[]
for idx,s in enumerate(S,1):
    n=s["n"]; L=s.get("layout","points"); lane=lane_of(n)
    style=f' style="--lane:{LANE[lane]}"' if lane else ""
    t=f'<h2>{inl(s.get("title"))}</h2>' if s.get("title") else ""
    q=s.get("quote")
    if L=="section":
        inner=f'<div class="sec"><h1>{inl(s["title"])}</h1>{body(s)}</div>'
    elif L=="statement":
        inner=f'<div class="stmt"><h1>{inl(s["title"])}</h1>{body(s)}{pts(s.get("points"))}{imgs_html(s.get("images"),"g small")}{srcs(s.get("sources"))}</div>'
    elif L=="big":
        inner=f'<div class="bigl">{t}<div class="bignum">{inl(s.get("big"))}</div>{body(s)}{pts(s.get("points"))}{srcs(s.get("sources"))}</div>'
    elif L=="quote":
        inner=f'<div class="ql">{t}<blockquote>{inl(q["text"])}</blockquote><p class="who">{inl(q.get("who"))}</p>{body(s)}{srcs(s.get("sources"))}</div>' if q else f'<div class="stmt">{t}{body(s)}</div>'
    elif L in ("text-image",):
        inner=f'<div class="ti"><div class="txt">{t}{body(s)}{pts(s.get("points"))}{(f"<blockquote class=sq>{inl(q[chr(116)+chr(101)+chr(120)+chr(116)])}</blockquote><p class=who>{inl(q.get(chr(119)+chr(104)+chr(111)))}</p>" if q else "")}{srcs(s.get("sources"))}</div><div class="pic">{imgs_html(s.get("images"),"g one")}</div></div>'
    elif L=="grid" or L=="lane":
        k=len([i for i in s.get("images",[]) if os.path.exists(os.path.join(root,i["src"]))])
        inner=f'<div class="gr {"lanes" if L=="lane" else ""}"><div class="txt">{t}{body(s)}{pts(s.get("points"))}{srcs(s.get("sources"))}</div><div class="grid c{min(max(k,1),6)}">{imgs_html(s.get("images"))}</div></div>'
    elif L=="table":
        inner=f'<div class="tl{" dense" if s.get("table") and len(s["table"]["rows"])>8 else ""}">{t}{body(s)}{table(s.get("table"))}{pts(s.get("points"))}{srcs(s.get("sources"))}</div>'
    elif L=="piece":
        src=render_src(s["svg"]); used.add(src)
        inner=f'<div class="pc"><figure class="sheet"><img src="{src}" alt="{e(s["title"])} concept sheet"></figure><div class="txt">{t}{body(s)}{pts(s.get("points"))}<p class="price">{inl(s.get("big"))}</p><blockquote class="sq">{inl(q["text"])}</blockquote></div></div>'
    elif L=="lineup":
        cells="".join(f'<figure><img src="{render_src(v)}" alt="" loading="lazy"></figure>' for v in s["svgs"])
        for v in s["svgs"]: used.add(render_src(v))
        inner=f'<div class="lu">{t}{body(s)}<div class="lugrid">{cells}</div></div>'
    else:
        dense=" dense" if sum(len(x) for x in s.get("points") or [])>650 else ""
        inner=f'<div class="pl{dense}">{t}{body(s)}{pts(s.get("points"))}{imgs_html(s.get("images"),"g small")}{table(s.get("table"))}{srcs(s.get("sources"))}</div>'
    notes=s.get("notes","")
    slides.append(f'<section class="slide {part_of(n)} L-{L}" id="s{idx}"{style}><div class="in">{inner}</div><span class="pg">{idx}</span><aside class="notes"><p>{inl(notes)}</p></aside></section>')
CSS=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"deck.css")).read()
title=S[0].get("title","VSL Merch")
page=f'''<title>Salt Lake Merch Deck R1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap">
<style>{CSS}</style>
<div class="bar"><span>Round 1 · {len(S)} slides</span><label class="tg"><input type="checkbox" id="shownotes"> Speaker notes</label></div>
<main class="deck">{"".join(slides)}</main>
<script>
(function(){{var c=document.getElementById('shownotes');function ap(){{document.body.classList.toggle('shownotes',c.checked);}}
try{{c.checked=localStorage.getItem('vsl-deck-notes')==='1';}}catch(e){{}} ap();
c.addEventListener('change',function(){{ap();try{{localStorage.setItem('vsl-deck-notes',c.checked?'1':'0');}}catch(e){{}}}});}})();
</script>'''
open(out,"w",encoding="utf-8").write(page)
json.dump(sorted(used),open(out+".files.json","w"))
print("slides",len(S),"assets",len(used),"bytes",len(page))
