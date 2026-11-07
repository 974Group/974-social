# Render text layers (transparent PNGs) with Cairo/Poppins via Playwright
import json, subprocess, os
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
CSS=f'''
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
*{{margin:0;padding:0}} body{{width:1080px;height:1920px;background:transparent;font-family:Cairo;color:#F4F1F2;position:relative;direction:rtl}}
.abs{{position:absolute;left:0;right:0;text-align:center}}
.en{{font-family:Poppins;direction:ltr}}
.title{{top:250px;font-weight:900;font-size:78px}} .title b{{font-family:Poppins;color:#C9A24B;font-weight:700;letter-spacing:1px}}
.rule{{position:absolute;left:90px;right:90px;top:360px;height:2px;background:rgba(244,241,242,.18)}}
.rule:before{{content:'';position:absolute;right:0;top:0;width:120px;height:2px;background:#C9A24B}}
.cap{{top:1500px;font-weight:800;font-size:44px;color:#F4F1F2}} .cap.gold{{color:#C9A24B}} .cap.mar{{color:#E04A86}}
.sub{{top:1562px;font-weight:600;font-size:26px;opacity:.6}}
.handle{{top:375px;font-weight:700;font-size:20px;letter-spacing:4px;opacity:.5}}
'''
L={
 'title':'<div class="abs title">تابع الـ <b>MAROON</b></div><div class="rule"></div><div class="abs en handle">@974.GROUP · SILICONE BANDS</div>',
 'c1':'<div class="abs cap">سير واحد بيصير <span class="en" style="color:#E04A86">Maroon</span></div>',
 'c2':'<div class="abs cap mar">احفظ مكانه زين</div>',
 'c3':'<div class="abs cap">الحين صار أبيض.. لا تضيّعه</div>',
 'c4':'<div class="abs cap" style="opacity:.75">تابعه</div>',
 'c5':'<div class="abs cap gold">الألوان ما بتساعدك</div>',
 'c6':'<div class="abs cap" style="opacity:.75">رجعنا أبيض.. وأسرع</div>',
 'c7':'<div class="abs cap" style="font-size:60px;font-weight:900">وقف.</div>',
 'c8':'<div class="abs cap gold">أي رقم كان الـ <span class="en">Maroon</span>؟</div>',
 'c9':'<div class="abs cap" style="top:1470px">جاوب صح في التعليقات 👇</div><div class="abs cap gold" style="top:1532px;font-size:40px">واحصل على <span class="en" style="letter-spacing:1px">Voucher</span> هدية 🎁</div><div class="abs en handle" style="top:1592px;opacity:.55;font-size:18px">23 SILICONE COLOURS · 974GROUP.NET</div>',
}
os.makedirs('txt',exist_ok=True)
for k,v in L.items():
    open(f'txt/{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{v}</body></html>')
js="""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const k of %s){await p.goto('file://'+process.cwd()+'/txt/'+k+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);await p.screenshot({path:'txt/'+k+'.png',omitBackground:true});}
await b.close();})()"""%json.dumps(list(L))
subprocess.run(['node','-e',js],check=True); print('ok')
