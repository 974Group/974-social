import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R='/home/claude/974-social/'
LOGOW=R+'posts/2026-11/pilates-socks/src/logo-white.png'
W5=R+'posts/2026-11/whoop5-silicone-restock/cut/'
CQ=R+'site/hero/cut/'
FA=SP+'/fa/'
GG=R+'posts/2026-11/goggles-26-27/src/cut/'
MK=R+'posts/2026-11/face-mask/src/cut/'
HEAD=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Cairo}}
.logo{{position:absolute;top:190px;left:50%;transform:translateX(-50%);height:58px}}
{payfoot.css(1.2)}
.info{{position:absolute;left:60px;right:60px;top:1330px;border-radius:30px;padding:22px 26px 24px;direction:rtl}}
.ship{{display:flex;justify-content:space-between;align-items:center;gap:14px}}
.ship div{{flex:1;border-radius:20px;padding:10px 16px 12px;text-align:center}}
.ship b{{display:block;font-weight:900;font-size:30px;line-height:1.25}}
.ship i{{display:block;font-style:normal;font-weight:700;font-size:22px;opacity:.85}}
.ship .fl{{font-size:24px;letter-spacing:0;white-space:nowrap;font-family:'Noto Color Emoji'}}
.payrow{{display:flex;justify-content:center;margin-top:18px}}
.payrow .payfoot{{justify-content:center}}
.site{{position:absolute;left:0;right:0;top:1585px;text-align:center;font-family:Poppins;font-weight:700;font-size:26px;letter-spacing:3px}}
.price{{display:inline-flex;align-items:baseline;gap:10px;border-radius:50px;padding:6px 40px 14px;font-weight:900;font-size:66px;direction:rtl;white-space:nowrap}}
.price b{{font-family:Poppins;font-weight:800}}
.price small{{font-size:30px;font-weight:800}}
.price s{{font-family:Poppins;font-size:32px;opacity:.6;font-weight:600}}
'''
def info(card_bg,chip_bg,txt,acc):
    return f'''<div class="info" style="background:{card_bg};color:{txt}">
<div class="ship"><div style="background:{chip_bg}"><b>🚚 شحن لكل الخليج</b><i class="fl">🇶🇦 🇸🇦 🇦🇪 🇰🇼 🇧🇭 🇴🇲</i></div>
<div style="background:{chip_bg}"><b>⚡ توصيل نفس اليوم</b><i>داخل قطر</i></div></div>
<div class="payrow"><div class="payfoot"><div class="pills">{payfoot.PILLS}</div></div></div></div>'''

def ad1():  # Whoop 5 silicone - pastel
    cs=['pink','yellow','babyblue','iceblue','black']
    pos=[(85,530),(410,510),(735,530),(250,875),(575,875)]
    imgs=''.join(f'<img class="b" style="left:{x}px;top:{y}px" src="file://{W5}{c}.png">' for c,(x,y) in zip(cs,pos))
    return f'''<style>{HEAD}
body{{background:linear-gradient(170deg,#FFE3EC 0%,#FFF6CF 45%,#D9F1FF 100%);color:#51022D}}
.h{{position:absolute;top:290px;left:0;right:0;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:84px;line-height:1.15}}
.h b em{{font-style:normal;font-family:Poppins;font-weight:900}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:36px;margin-top:6px;color:#7E3D5C}}
.b{{position:absolute;width:260px;filter:drop-shadow(0 18px 18px rgba(81,2,45,.18))}}
.pr{{position:absolute;top:1200px;left:0;right:0;text-align:center}}
</style><body>
<img class="logo" src="file://{R}posts/2026-11/waterproof/src/mark-c.png" style="height:64px">
<div class="h"><b>سيور <em>Whoop</em> سيليكون</b><i>ناعمة.. ومريحة طول اليوم</i></div>
{imgs}
<div class="pr"><span class="price" style="background:#51022D;color:#fff"><b>99</b><small>ر.ق</small></span></div>
{info('rgba(255,255,255,.75)','#fff','#51022D','#720842')}
<div class="site" style="color:#51022D">974GROUP.NET</div></body>'''

def ad2():  # CIRQA - deep navy
    cs=['c_f1_blue','c_s2_lime','c_f3_orange','c_f2_whitegrey','c_f1_pink','c_s1_beige']
    imgs=''.join(f'<div class="cell"><img src="file://{CQ}{c}.png"></div>' for c in cs)
    return f'''<style>{HEAD}
body{{background:radial-gradient(ellipse at 50% 35%,#1E3A6E 0%,#0A1530 75%);color:#fff}}
.h{{position:absolute;top:290px;left:0;right:0;text-align:center}}
.h .t{{font-family:Poppins;font-weight:900;font-size:96px;letter-spacing:4px;line-height:1}}
.h .k{{font-family:Poppins;font-weight:700;font-size:30px;letter-spacing:10px;color:#9EC3FF;margin-top:4px}}
.h i{{display:block;font-style:normal;font-weight:800;font-size:38px;margin-top:14px;direction:rtl}}
.grid{{position:absolute;left:70px;right:70px;top:560px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px 18px}}
.cell{{height:300px;display:flex;align-items:center;justify-content:center}}
.cell img{{max-height:100%;max-width:100%;filter:drop-shadow(0 18px 18px rgba(0,0,0,.45))}}
.pr{{position:absolute;top:1220px;left:0;right:0;text-align:center}}
</style><body>
<img class="logo" src="file://{LOGOW}">
<div class="h"><div class="k">GARMIN</div><div class="t">CIRQA</div><i>سيور قماش وسيليكون.. اختار ستايلك</i></div>
<div class="grid">{imgs}</div>
<div class="pr"><span class="price" style="background:#9EC3FF;color:#0A1530"><small>من</small><b>89</b><small>ر.ق</small></span></div>
{info('rgba(255,255,255,.08)','rgba(255,255,255,.1)','#fff','#9EC3FF')}
<div class="site" style="color:#9EC3FF">974GROUP.NET</div></body>'''

def ad3():  # Fitbit Air + Whoop band
    return f'''<style>{HEAD}
body{{background:linear-gradient(180deg,#F4F1F2 0%,#E2E2E2 100%);color:#1A1A1A}}
.h{{position:absolute;top:290px;left:0;right:0;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:86px;line-height:1.15}}
.h b em{{font-style:normal;font-family:Poppins;font-weight:900;color:#720842}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:38px;margin-top:6px;color:#444}}
.hero{{position:absolute;left:270px;top:540px;width:440px;filter:drop-shadow(0 26px 26px rgba(0,0,0,.25))}}
.ad{{position:absolute;right:80px;top:640px;width:250px;text-align:center;direction:rtl}}
.ad img{{width:230px;filter:drop-shadow(0 14px 14px rgba(0,0,0,.25))}}
.ad b{{display:block;font-weight:900;font-size:30px;margin-top:6px}}
.ad i{{display:block;font-style:normal;font-weight:700;font-size:22px;color:#555}}
.fr{{position:absolute;left:70px;top:860px;width:230px;text-align:center;direction:rtl}}
.fr .pl{{width:120px;height:120px;border-radius:50%;background:#720842;color:#fff;font-family:Poppins;font-weight:900;font-size:56px;display:flex;align-items:center;justify-content:center;margin:0 auto}}
.fr b{{display:block;font-weight:900;font-size:30px;margin-top:8px}}
.fr i{{display:block;font-style:normal;font-weight:700;font-size:22px;color:#555}}
.pr{{position:absolute;top:1220px;left:0;right:0;text-align:center}}
</style><body>
<img class="logo" src="file://{FA}logo-black.png">
<div class="h"><b>عندك <em>Fitbit Air</em>؟</b><i>لبّسه أي سير Whoop تحبه</i></div>
<img class="hero" src="file://{FA}c0t.png">
<div class="ad"><img src="file://{FA}c2t.png"><b>أدابتر يركب</b><i>على أي سير Whoop</i></div>
<div class="fr"><div class="pl">+1</div><b>سير مجاني</b><i>تختاره بنفسك</i></div>
<div class="pr"><span class="price" style="background:#720842;color:#fff"><s>149</s><b>119</b><small>ر.ق</small></span></div>
{info('#fff','#F4F1F2','#1A1A1A','#720842')}
<div class="site" style="color:#720842">974GROUP.NET</div></body>'''

def ad4():  # winter goggles + masks
    return f'''<style>{HEAD}
body{{background:linear-gradient(180deg,#1B1430 0%,#5A2A3A 45%,#C9763E 78%,#E8A55C 100%);color:#fff}}
.h{{position:absolute;top:290px;left:0;right:0;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:90px;line-height:1.15}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:36px;margin-top:4px;color:#FFD9A8}}
.row{{position:absolute;left:50px;right:50px;display:flex;justify-content:space-between;align-items:flex-end;direction:rtl}}
.it{{display:flex;flex-direction:column;align-items:center}}
.it img{{filter:drop-shadow(0 20px 20px rgba(0,0,0,.45))}}
.tag{{margin-top:8px;background:rgba(0,0,0,.35);border-radius:30px;padding:4px 22px 8px;font-weight:800;font-size:26px;white-space:nowrap;direction:rtl}}
.tag b{{font-family:Poppins;color:#FFD9A8}}
.sec{{position:absolute;left:0;right:0;text-align:center;font-weight:900;font-size:34px;direction:rtl}}
</style><body>
<img class="logo" src="file://{LOGOW}">
<div class="h"><b>جاهز للبر؟ 🏜️</b><i>نظارات الموسم الجديد + ماسكات 974</i></div>
<div class="row" style="top:540px"><div class="it"><img src="file://{GG}ph1.png" style="width:450px"><div class="tag"><span style="font-family:Poppins;font-weight:700">Photochromic</span> <b>349</b> ر.ق</div></div>
<div class="it"><img src="file://{GG}br1.png" style="width:450px"><div class="tag"><span style="font-family:Poppins;font-weight:700">Brown</span> <b>319</b> ر.ق</div></div></div>
<div class="row" style="top:930px;left:110px;right:110px"><div class="it"><img src="file://{MK}beige.png" style="height:230px"></div><div class="it"><img src="file://{MK}black.png" style="height:250px"></div><div class="it"><img src="file://{MK}orange.png" style="height:230px"></div></div>
<div class="sec" style="top:1205px"><span class="tag" style="font-size:32px;padding:6px 30px 10px">ماسك 974 · 23 لون · <b>39</b> ر.ق</span></div>
{info('rgba(20,10,25,.55)','rgba(255,255,255,.1)','#fff','#FFD9A8')}
<div class="site" style="color:#fff">974GROUP.NET</div></body>'''
ADS=dict(whoop5_silicone=ad1,garmin_cirqa=ad2,fitbit_air_whoop=ad3,winter_goggles_masks=ad4)
for n,f in ADS.items():
    if sys.argv[1:] and n not in sys.argv[1:]: continue
    name=f'974-snap-{n}'
    open(name+'.html','w').write('<!doctype html><html><head><meta charset="utf-8"></head>'+f()+'</html>')
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1920}}}});await pg.goto('file://'+process.cwd()+'/{name}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
