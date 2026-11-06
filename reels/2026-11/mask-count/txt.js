const {chromium}=require('playwright');const fs=require('fs');
const FD='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad/fonts2/';
const LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png';
const h=`<style>@font-face{font-family:'Alx';font-weight:100 900;src:url(file://${FD}Alexandria.ttf)}
*{margin:0;padding:0}body{width:1080px;height:1920px;background:transparent;position:relative;color:#3A1424}
.lg{position:absolute;top:205px;left:50%;transform:translateX(-50%);height:46px;opacity:.9}
.h{position:absolute;top:285px;left:0;right:0;text-align:center;direction:rtl;font-family:Alx;font-weight:700;font-size:86px;line-height:1.1;letter-spacing:-1px}
.s{position:absolute;top:400px;left:0;right:0;text-align:center;font-family:Alx;font-weight:400;font-size:34px;direction:rtl;opacity:.85}
.b{position:absolute;top:1440px;left:0;right:0;text-align:center;direction:rtl;font-family:Alx;font-weight:600;font-size:46px}
</style><img class="lg" src="file://${LOGO}"><div class="h">كم ماسك في الفيديو؟</div><div class="s">ماسكات 974</div><div class="b">جاوب صح.. واحصل على ڤاوتشر 🎁</div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
fs.writeFileSync('txt.html','<meta charset=utf-8>'+h);await p.goto('file://'+process.cwd()+'/txt.html');await p.waitForTimeout(400);await p.screenshot({path:'txt.png',omitBackground:true});await b.close()})()
