# Designy "Winter vibes" hoodie — post (1080x1350) + story (1080x1920), Designy identity (blue)
import subprocess, os
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
H='/home/claude/974-social/tshirts/hoodie/'
LOGO='/home/claude/974-social/tshirts/designy/designy-logo-white-hd.png'
BLUE='#2560a4'; DEEP='#173f72'; SKY='#01a7e1'; MINT='#edf7f6'
GRAIN="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"
CSS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}} .ar{{direction:rtl;text-align:right}}
body{{width:1080px;background:radial-gradient(120% 80% at 50% 38%,#2d6cb4 0%,{BLUE} 45%,{DEEP} 100%);color:#fff;font-family:Cairo;position:relative;overflow:hidden}}
.grain{{position:absolute;inset:0;background:{GRAIN};opacity:.12;mix-blend-mode:soft-light}}
.hood{{filter:drop-shadow(0 30px 40px rgba(5,20,45,.45))}}
.lbl{{font-family:Poppins;font-weight:700;font-size:14px;letter-spacing:5px;opacity:.7;text-align:center}}
.sz{{display:flex;gap:10px;direction:ltr}} .sz span{{font-family:Poppins;font-weight:700;font-size:22px;border:2px solid rgba(255,255,255,.85);border-radius:30px;padding:3px 18px}}
.price{{background:#fff;color:{BLUE};border-radius:44px;padding:4px 30px 8px;font-weight:900;white-space:nowrap}} .price b{{font-family:Poppins}}
.ring{{border-radius:50%;overflow:hidden;border:5px solid #fff;box-shadow:0 14px 30px rgba(5,20,45,.4)}} .ring img{{width:100%;height:100%;object-fit:cover}}
.det{{display:flex;align-items:center;gap:16px;direction:rtl}} .det i{{width:12px;height:12px;border-radius:50%;background:{SKY};flex:none}}
'''
def post():
    body=f'''
<div class="abs en" style="left:-20px;top:70px;font-weight:700;font-size:220px;line-height:.82;letter-spacing:-9px;-webkit-text-stroke:2px rgba(255,255,255,.16);color:transparent;white-space:nowrap">WINTER<br>VIBES</div>
<img class="abs" src="file://{LOGO}" style="left:52px;top:48px;height:70px">
<div class="abs ar" style="right:52px;top:52px;width:520px">
 <div class="en" style="font-weight:700;font-size:58px;line-height:1;text-align:right">Winter vibes</div>
 <div style="font-weight:800;font-size:28px;margin-top:8px;opacity:.9">هودي مطرّز.. وقبعته مبطّنة بالسدو</div>
</div>
<img class="abs hood" src="file://{H}cut/front.png" style="left:40px;top:240px;height:690px">
<img class="abs hood" src="file://{H}cut/back.png" style="right:40px;top:302px;height:600px">
<div class="abs lbl" style="left:40px;width:450px;top:950px">FRONT</div>
<div class="abs lbl" style="right:40px;width:460px;top:950px">BACK</div>
<div class="abs ring" style="left:52px;top:1020px;width:200px;height:200px"><img src="file://{H}cut/lining-sq.jpg"></div>
<div class="abs ar" style="left:280px;top:1040px;right:52px">
 <div style="font-weight:900;font-size:34px;line-height:1.2">بطانة سدو.. تطلع لك كل ما لبست القبعة</div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px;direction:rtl">
  <div class="sz"><span>S</span><span>M</span><span>L</span><span>XL</span></div>
  <div class="price" style="font-size:36px"><b>349</b> ر.ق</div>
 </div>
</div>
<div class="abs ar" style="right:52px;left:52px;bottom:44px;font-weight:700;font-size:25px;opacity:.9">للطلب راسلنا على الخاص 📩</div>'''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{height:1350px}}</style></head><body>{body}<div class="grain"></div></body></html>'

def story():
    body=f'''
<div class="abs en" style="left:-24px;top:300px;font-weight:700;font-size:250px;line-height:.82;letter-spacing:-10px;-webkit-text-stroke:2px rgba(255,255,255,.14);color:transparent;white-space:nowrap">WINTER<br>VIBES</div>
<img class="abs" src="file://{LOGO}" style="left:50%;transform:translateX(-50%);top:205px;height:86px">
<div class="abs" style="left:0;right:0;top:322px;text-align:center">
 <div class="en" style="font-weight:700;font-size:76px;line-height:1">Winter vibes</div>
 <div style="font-weight:800;font-size:32px;margin-top:10px;opacity:.9">سيلين.. دايماً فكرة حلوة</div>
</div>
<img class="abs hood" src="file://{H}cut/front.png" style="left:40px;top:500px;height:660px">
<img class="abs hood" src="file://{H}cut/back.png" style="right:40px;top:560px;height:574px">
<div class="abs lbl" style="left:40px;width:430px;top:1176px">FRONT</div>
<div class="abs lbl" style="right:40px;width:440px;top:1176px">BACK</div>
<div class="abs ring" style="right:56px;top:1240px;width:220px;height:220px"><img src="file://{H}cut/lining-sq.jpg"></div>
<div class="abs ar" style="right:300px;left:56px;top:1236px">
 <div style="font-weight:900;font-size:30px;margin-bottom:14px">تفاصيل الهودي</div>
 <div class="det" style="font-weight:700;font-size:25px;margin-bottom:10px"><i></i>قبعة مبطّنة بقماش السدو</div>
 <div class="det" style="font-weight:700;font-size:25px;margin-bottom:10px"><i></i>تطريز على الصدر والظهر</div>
 <div class="det" style="font-weight:700;font-size:25px"><i></i>أبيض · قصّة أوفرسايز</div>
</div>
<div class="abs" style="left:56px;right:56px;top:1500px;display:flex;justify-content:space-between;align-items:center;direction:rtl">
 <div class="price" style="font-size:44px"><b>349</b> ر.ق</div>
 <div class="sz"><span>S</span><span>M</span><span>L</span><span>XL</span></div>
</div>
<div class="abs ar" style="right:56px;left:56px;top:1592px;font-weight:700;font-size:27px;opacity:.9;text-align:center">للطلب راسلنا على الخاص 📩</div>'''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{height:1920px}}</style></head><body>{body}<div class="grain"></div></body></html>'

def shot(n,html,Hh):
    os.makedirs('out',exist_ok=True); open(f'out/{n}.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{Hh}}}}});await pg.goto('file://'+process.cwd()+'/out/{n}.html');await pg.waitForTimeout(900);await pg.screenshot({{path:'out/{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
shot('designy-winter-vibes-post',post(),1350)
shot('designy-winter-vibes-story',story(),1920)
