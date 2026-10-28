const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const FONTS='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Permanent+Marker&family=Anton&family=Space+Mono:wght@400;700&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Archivo+Narrow:wght@400;700&family=Archivo:wght@400;700;900&family=Oswald:wght@500;700&family=Pirata+One&family=Pinyon+Script&family=Dancing+Script:wght@600&family=Special+Elite&display=block';
(async()=>{
  const proxy=process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined;
  const b=await chromium.launch({proxy}); const ctx=await b.newContext({viewport:{width:1200,height:1500},deviceScaleFactor:1.5,ignoreHTTPSErrors:true}); const p=await ctx.newPage();
  const files=process.argv.slice(3);
  for(const f of files){
    const svg=fs.readFileSync(f,'utf8').replace(/<\?xml[^>]*\?>/,'');
    await p.setContent(`<html><head><link rel="stylesheet" href="${FONTS}"><style>body{margin:0}svg{display:block;width:1200px;height:1500px}</style></head><body>${svg}</body></html>`,{waitUntil:'networkidle'});
    await p.evaluate(()=>document.fonts.ready);
    const out=path.join(process.argv[2], f.split('/').slice(-3,-2)[0]+'-'+path.basename(f,'.svg')+'.jpg');
    await p.screenshot({path:out,type:'jpeg',quality:86});
    const ok=await p.evaluate(()=>document.fonts.check('16px Anton')); console.log(path.basename(out),'fonts',ok);
  }
  await b.close();
})();
