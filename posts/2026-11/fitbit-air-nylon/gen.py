import subprocess
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'; P='/home/claude/974-social/products/fitbit-air-nylon-v2/'
cols=[('Phantom Silver','phantom-silver'),('Deep Sea Blue','deep-sea-blue'),('Army Green','army-green'),('Royal Blue','royal-blue'),('Light Plum','light-plum'),('Starlight','starlight'),('Ice Mint','ice-mint'),('Seashell','seashell'),('Deep Black','deep-black')]
def page(W,H,story):
    tile=292 if not story else 330
    top=70 if not story else 150
    cards=''.join(f'<div class="c"><div class="t"><img src="file://{P}{f}.jpg"></div><span>{n}</span></div>' for n,f in cols)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#EFEBE6;font-family:Cairo;color:#1E1A1C;position:relative;overflow:hidden}}
.head{{position:absolute;top:{top}px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center}}
.head img{{height:52px}} .head span{{font-family:Poppins;font-weight:500;letter-spacing:4px;font-size:20px;color:#E8741E}}
h1{{position:absolute;top:{top+80}px;right:60px;left:60px;text-align:right;direction:rtl;font-weight:900;font-size:{70 if story else 62}px;line-height:1.15}}
h1 i{{font-style:normal;color:#E8741E}}
.sub{{position:absolute;top:{top+(250 if story else 165)}px;right:60px;left:60px;direction:rtl;text-align:right;font-weight:700;font-size:{32 if story else 28}px;color:#5a5154}}
.sub b{{font-family:Poppins;font-weight:700}}
.grid{{position:absolute;top:{top+(350 if story else 242)}px;left:50%;transform:translateX(-50%);display:grid;grid-template-columns:repeat(3,{tile}px);gap:{22 if story else 18}px}}
.c{{display:flex;flex-direction:column;align-items:center}}
.t{{width:{tile}px;height:{tile-60 if not story else tile-30}px;background:#fff;border-radius:26px;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.t img{{height:{tile-60 if not story else tile-36}px;mix-blend-mode:multiply}}
.c span{{font-family:Poppins;font-weight:500;font-size:{24 if story else 21}px;margin-top:6px}}
.foot{{position:absolute;left:60px;right:60px;bottom:{110 if story else 48}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#1E1A1C;color:#fff;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{48 if story else 40}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{30 if story else 26}px;color:#1E1A1C}}
.cta em{{font-style:normal;color:#E8741E}}
</style></head><body>
<div class="head"><img src="file:///home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png"><span>FITBIT AIR · NYLON LOOP</span></div>
<h1>9 ألوان<i>..</i> خفيف وتنساه بيدك</h1>
<div class="sub">نايلون منسوج يتنفس · فيلكرو يناسب كل المقاسات · سير <b>Fitbit Air</b></div>
<div class="grid">{cards}</div>
<div class="foot"><div class="cta">علّق <em>«فت بت»</em> ونرسل لك الرابط 📩</div><div class="price"><b>79</b> ر.ق</div></div>
</body></html>'''
for name,W,H,st in (('974-fitbit-air-nylon-post',1080,1350,False),('974-fitbit-air-nylon-story',1080,1920,True)):
    open(name+'.html','w').write(page(W,H,st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(800);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print('ok')
