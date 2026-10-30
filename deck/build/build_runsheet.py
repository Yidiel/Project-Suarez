import sys, html, json, os
sys.path.insert(0, os.path.dirname(__file__))
from pieces import P
e=html.escape
root=sys.argv[1]; out=sys.argv[2]
MASTER = """You are running the Visit Salt Lake merch mockup pipeline in Chrome for Yid, the creative director. The ideas are approved. Your job is execution through two image models he pays for, driven hard by references.

SETUP
1. In the Project-Suarez repo on this Mac, run: git fetch origin && git checkout claude/vsl-merch-deck && git pull. Open deck/runsheet.html in Chrome (file path: <repo>/deck/runsheet.html). Every reference file named on it is in the repo, relative to <repo>/deck/.
2. Make sure you are signed in at midjourney.com and gemini.google.com in this Chrome profile. If not, stop and ask Yid to sign in. Never ask for or type a password.

THE WORKFLOW, PER CARD, IN ORDER
Stage 1, Midjourney makes the design.
 a. Open midjourney.com/imagine. Upload the card's sketch as an Image Prompt and its design references as Style References (drag the files from <repo>/deck/ or use the upload button). If uploading files is blocked for you, stop and ask Yid to drag in the exact files listed on the card.
 b. Paste the card's Midjourney prompt, then its parameters. Replace the [upload ...] placeholder with the uploaded style references (in the web UI, setting an image as Style Reference does this for you).
 c. Generate. Pick the best of the four against the card's checks. If none pass, adjust once and rerun. Maximum 3 runs per card.
 d. Upscale the pick (Subtle) and download it as deck/mockups/final/<ID>/<ID>-mj.png.
Stage 2, Gemini makes the art-directed shot.
 e. Open a new chat at gemini.google.com and use the image model (Nano Banana). Upload the Midjourney result first (that is "image 1"), then the card's shot references in order (image 2, image 3).
 f. Paste the first Gemini prompt. Check the result: exact text, the design matches image 1, no logos. Up to 3 attempts. Then the next Gemini prompt in the same chat.
 g. Download each result as deck/mockups/final/<ID>/<ID>-shot-1.png, -shot-2.png, and so on.
Stage 3, log and save.
 h. Append to deck/mockups/final/LOG.md: the card ID, the final prompts you actually used, the Midjourney job link, which variant you picked and why, and any problem.
 i. git add, commit with a message naming the card, and push to claude/vsl-merch-deck.

RULES
- Text must be spelled exactly as on the card. If Midjourney garbles it, regenerate the design without text and have Gemini add the exact text.
- Never add brand logos (no Nike swoosh, no Arc'teryx bird, no Online Ceramics marks). The references are for style only.
- Never show Olympic rings, the word Olympic, 2034, Ski Utah, "Greatest Snow on Earth", the Utah state flag, the Visit Salt Lake logo, or the words Park City.
- Pilot first: run S1, P1 and W1, then stop and send Yid the results for review before running the rest.
- Keep going on your own between pieces. Only stop for a login, a blocked upload, a credit limit, or the pilot review.
- When all cards are done, write a one-paragraph summary at the top of LOG.md and push."""
def card(p):
    refs="".join(f'<figure><img src="{e(f)}" alt="" loading="lazy"><figcaption><code>{e(f)}</code><br>{e(r)}</figcaption></figure>' for f,r in p["design_refs"])
    shots="".join(f'<figure><img src="{e(f)}" alt="" loading="lazy"><figcaption><code>{e(f)}</code><br>{e(r)}</figcaption></figure>' for f,r in p["shot_refs"])
    gem="".join(f'<div class="pr"><div class="prh">Gemini prompt {i+1}<button class="cp" type="button">Copy</button></div><pre>{e(g)}</pre></div>' for i,g in enumerate(p["gemini"]))
    return f'''<article class="card" id="{e(p["id"])}">
<header><span class="id">{e(p["id"])}</span><h2>{e(p["name"])}</h2><p class="lane">{e(p["lane"])}</p><label class="done"><input type="checkbox" data-id="{e(p["id"])}"> Done</label></header>
<p class="idea">{e(p["idea"])}</p>
<div class="stage"><h3>Stage 1 · Midjourney design</h3>
<div class="refs"><figure class="sk"><img src="{e(p["sketch"])}" alt="" loading="lazy"><figcaption><code>{e(p["sketch"])}</code><br>Image Prompt: our concept sketch, composition only</figcaption></figure>{refs}</div>
<div class="pr"><div class="prh">Midjourney prompt<button class="cp" type="button">Copy</button></div><pre>{e(p["mj"])} {e(p["mj_params"])}</pre></div>
</div>
<div class="stage"><h3>Stage 2 · Gemini shot</h3>
<div class="refs">{shots}</div>{gem}</div>
<dl class="chk"><dt>Text must read</dt><dd>{e(p["text"])}</dd><dt>Save as</dt><dd><code>deck/mockups/final/{e(p["id"])}/{e(p["id"])}-mj.png</code> and <code>{e(p["id"])}-shot-N.png</code></dd>{f'<dt>Note</dt><dd>{e(p["note"])}</dd>' if p["note"] else ""}</dl>
</article>'''
CSS="""
:root{--bg:#141312;--panel:#1d1c1a;--fg:#f4efe8;--muted:#aaa196;--rule:#34312d;--accent:#f58b88;--ok:#1a854c;--display:'Archivo',system-ui,sans-serif;--mono:'JetBrains Mono',ui-monospace,monospace;color-scheme:dark}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f6f1ec;--panel:#fff;--fg:#1e1d1b;--muted:#5d5852;--rule:#e1d9cf;--accent:#c4423d;color-scheme:light}}
:root[data-theme="light"]{--bg:#f6f1ec;--panel:#fff;--fg:#1e1d1b;--muted:#5d5852;--rule:#e1d9cf;--accent:#c4423d;color-scheme:light}
body{background:var(--bg);color:var(--fg);font-family:var(--display);font-size:15px;line-height:1.5;margin:0}
.wrap{max-width:1100px;margin:0 auto;padding-block:36px 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:28px}
h1{font-weight:900;font-stretch:80%;font-size:clamp(36px,6vw,64px);line-height:.95;margin:0;letter-spacing:-.02em;text-wrap:balance}
.lede{color:var(--muted);max-width:66ch;margin:0}
.flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.flow div{background:var(--panel);border:1px solid var(--rule);padding:14px}
.flow b{display:block;font-size:17px;margin-bottom:4px}
.master{background:var(--panel);border:1px solid var(--rule);border-top:3px solid var(--accent)}
.prh{display:flex;justify-content:space-between;align-items:center;gap:12px;font-weight:700;padding:10px 14px;border-bottom:1px solid var(--rule)}
pre{margin:0;padding:14px;white-space:pre-wrap;word-break:break-word;font:13px/1.55 var(--mono);max-height:520px;overflow:auto}
.cp{font:600 13px var(--display);background:var(--fg);color:var(--bg);border:0;border-radius:999px;padding:6px 14px;cursor:pointer}
.cp:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
nav{display:flex;flex-wrap:wrap;gap:6px}
nav a{text-decoration:none;color:var(--fg);border:1px solid var(--rule);border-radius:999px;padding:5px 11px;font-size:13px;font-weight:600}
.card{background:var(--panel);border:1px solid var(--rule);padding:18px;display:grid;gap:16px;min-width:0}
.card.isdone{opacity:.55}
.card header{display:grid;grid-template-columns:auto 1fr auto;gap:4px 12px;align-items:baseline}
.id{font:700 14px var(--mono);color:var(--accent)}
.card h2{margin:0;font-size:24px;line-height:1.1;letter-spacing:-.01em}
.lane{grid-column:2;margin:0;color:var(--muted);font-size:13px}
.done{grid-row:1;grid-column:3;font-size:13px;display:flex;gap:6px;align-items:center;cursor:pointer}
.idea{margin:0;max-width:72ch}
.stage{display:grid;gap:10px;min-width:0}
.stage h3{margin:0;font-size:15px}
.refs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.refs figure{margin:0;min-width:0}
.refs img{display:block;width:100%;aspect-ratio:1;object-fit:cover;max-width:100%;border:1px solid var(--rule)}
.refs .sk img{object-fit:contain;background:#f6f1ec}
figcaption{font-size:12px;color:var(--muted);margin-top:4px;line-height:1.35;word-break:break-word}
code{font:12px var(--mono)}
.pr{border:1px solid var(--rule);min-width:0}
.chk{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px;margin:0;font-size:14px}
.chk dt{font-weight:700} .chk dd{margin:0;min-width:0;word-break:break-word}
.toast{position:fixed;left:50%;bottom:calc(20px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:var(--fg);color:var(--bg);padding:9px 16px;border-radius:999px;font-size:13px;font-weight:600}
"""
JS="""
(function(){
function toast(t){var d=document.createElement('div');d.className='toast';d.textContent=t;document.body.appendChild(d);setTimeout(function(){d.remove();},1500);}
document.querySelectorAll('.cp').forEach(function(b){b.addEventListener('click',function(){var pre=b.closest('.pr,.master').querySelector('pre');var t=pre.textContent;
 if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){toast('Copied');},function(){sel(pre);});}else sel(pre);});});
function sel(el){var r=document.createRange();r.selectNodeContents(el);var s=window.getSelection();s.removeAllRanges();s.addRange(r);toast('Selected, press copy');}
var K='vsl-runsheet-done',d={};try{d=JSON.parse(localStorage.getItem(K)||'{}')||{};}catch(e){}
document.querySelectorAll('.done input').forEach(function(c){var id=c.dataset.id;c.checked=!!d[id];c.closest('.card').classList.toggle('isdone',c.checked);
 c.addEventListener('change',function(){d[id]=c.checked;try{localStorage.setItem(K,JSON.stringify(d));}catch(e){}c.closest('.card').classList.toggle('isdone',c.checked);});});
})();
"""
cards="".join(card(p) for p in P)
page=f'''<title>Merch Mockup Run Sheet</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=JetBrains+Mono:wght@400;700&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header style="display:grid;gap:12px"><h1>Merch Mockup Run Sheet</h1>
<p class="lede">The approved Visit Salt Lake merch ideas, set up for a Claude session that drives Chrome on Yid's Mac. Midjourney makes each design from real references and our concept sketch. Gemini then places that design into a shot art-directed from the brands we're emulating. {len(P)} cards, with your PDF comments applied.</p></header>
<div class="flow"><div><b>1. References</b>Concept sketch as Image Prompt, approved mood-board picks as Style References.</div><div><b>2. Midjourney</b>Makes the design. Best of four, upscaled, saved.</div><div><b>3. Gemini</b>Puts the design on the product, shot like the brand references.</div><div><b>4. Log and push</b>Prompts, picks and files into the repo, one commit per card.</div></div>
<section class="master"><div class="prh">Paste this into the Chrome session<button class="cp" type="button">Copy</button></div><pre>{e(MASTER)}</pre></section>
<nav>{"".join(f'<a href="#{e(p["id"])}">{e(p["id"])} {e(p["name"].split(" (")[0].split(":")[0])}</a>' for p in P)}</nav>
{cards}
</div>
<script>{JS}</script>'''
open(out,"w",encoding="utf-8").write(page)
used=sorted({p["sketch"] for p in P}|{f for p in P for f,_ in p["design_refs"]+p["shot_refs"]})
missing=[f for f in used if not os.path.exists(os.path.join(root,f))]
json.dump([{"path":f} for f in used],open(out+".files.json","w"))
print("cards",len(P),"refs",len(used),"missing",missing)
open(os.path.join(root,"mockups","MASTER-PROMPT.txt"),"w").write(MASTER)
