# Designy story overlay (transparent PNG, 1080x1920) for the hoodie spin video
import subprocess, os
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D='/home/claude/974-social/tshirts/designy/'
LB='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
BLUE='#2560a4'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1920px;background:transparent;position:relative;overflow:hidden;font-family:Poppins;color:{BLUE}}}
.abs{{position:absolute}}
</style></head><body>
<img class="abs" src="file://{D}designy-logo-blue-hd.png" style="left:50%;transform:translateX(-50%);top:210px;height:100px">
<div class="abs" style="left:0;right:0;top:1462px;text-align:center">
 <div style="font-weight:700;font-size:64px;letter-spacing:-1px;line-height:1">Winter vibes</div>
 <div style="font-family:Cairo;font-weight:800;font-size:34px;direction:rtl;margin-top:10px;color:#434053">سيلين.. دايماً فكرة حلوة</div>
 <div style="font-weight:700;font-size:15px;letter-spacing:6px;margin-top:16px;opacity:.75">HOODIE · DESIGNY</div>
</div>
</body></html>'''
open('overlay.html','w').write(html)
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.cwd()+'/overlay.html');await p.waitForTimeout(800);await p.screenshot({path:'overlay.png',omitBackground:true});await b.close();})()"
subprocess.run(['node','-e',js],check=True)
