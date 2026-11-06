const {chromium}=require('playwright');const fs=require('fs');
const FD='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad/fonts2/';
const LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png';
const F=`@font-face{font-family:'Alx';font-weight:100 900;src:url(file://${FD}Alexandria.ttf)}
@font-face{font-family:'Pop';font-weight:300;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf)}
@font-face{font-family:'Pop';font-weight:600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}
*{margin:0;padding:0}body{width:1080px;height:1920px;background:transparent;position:relative;color:#fff}`;
const txt=`<style>${F}
.lg{position:absolute;top:205px;left:50%;transform:translateX(-50%);height:46px}
.h{position:absolute;top:285px;left:0;right:0;text-align:center;direction:rtl;font-family:Alx;font-weight:700;font-size:88px;line-height:1.1;letter-spacing:-1px}
.h span{font-family:Pop;font-weight:600;letter-spacing:0}
.b{position:absolute;top:1470px;left:0;right:0;text-align:center;direction:rtl;font-family:Alx;font-weight:600;font-size:44px;color:#0E2A47}
.s{position:absolute;top:420px;left:0;right:0;text-align:center;font-family:Alx;font-weight:400;font-size:34px;opacity:.92;direction:rtl}
</style><img class="lg" src="file://${LOGO}"><div class="h">كم لون فالفيديو؟</div><div class="s">سيور Whoop سيليكون</div><div class="b">جاوب صح.. وبتوصلك مفاجأة على الخاص 🎁</div>`;
const cnt=n=>`<style>${F}
.c{display:none;position:absolute;top:1475px;left:0;right:0;text-align:center;font-family:Pop;font-weight:300;font-size:34px;letter-spacing:6px}
.c b{font-weight:600}
</style><div class="c"><b>${String(n).padStart(2,'0')}</b> / 21</div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const items=[['txt',txt],...Array.from({length:21},(_,i)=>['cnt'+String(i+1).padStart(2,'0'),cnt(i+1)])];
for(const [n,h] of items){fs.writeFileSync(n+'.html','<meta charset=utf-8>'+h);await p.goto('file://'+process.cwd()+'/'+n+'.html');await p.waitForTimeout(250);await p.screenshot({path:n+'.png',omitBackground:true});}
await b.close()})()
