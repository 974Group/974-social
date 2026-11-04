import subprocess
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
P='/home/claude/974-social/products/fitbit-fabric-blush/src/'
LOGO='/home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'
others=[('Black','black'),('Grey','grey'),('Fog','fog'),('Blue','blue'),('Pinky Red','pinky-red'),('Lime green','lime')]
def page(W,H,story):
    hero=640 if not story else 820
    heroTop=330 if not story else 520
    strip_top=H-(395 if not story else 600)
    sz=120 if not story else 128
    cards=''.join(f'<div class="o"><img src="file://{P}{f}-crop.png"><span>{n}</span></div>' for n,f in others)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:linear-gradient(180deg,#F9E3EB 0%,#F2C6D5 100%);font-family:Cairo;color:#4A1630;position:relative;overflow:hidden}}
.logo{{position:absolute;top:{50 if not story else 130}px;left:56px;height:46px}}
.eb{{position:absolute;top:{62 if not story else 142}px;right:56px;font-family:Poppins;font-weight:500;letter-spacing:4px;font-size:18px;color:#A2577A}}
h1{{position:absolute;top:{120 if not story else 230}px;left:0;right:0;text-align:center;direction:rtl;font-weight:900;font-size:{70 if not story else 80}px;line-height:1.1}}
h1 b{{font-family:Poppins;font-weight:700;color:#D46A97}}
.sub{{position:absolute;top:{215 if not story else 340}px;left:0;right:0;text-align:center;direction:rtl;font-weight:600;font-size:{27 if not story else 31}px;color:#7E3D5C}}
.sub b{{font-family:Poppins;font-weight:700}}
.disc{{position:absolute;left:50%;top:{heroTop+hero*0.08}px;width:{hero*0.9}px;height:{hero*0.9}px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(circle,#FFFFFF 0%,rgba(255,255,255,.55) 45%,rgba(255,255,255,0) 70%)}}
.hero{{position:absolute;left:50%;top:{heroTop}px;height:{hero*0.82}px;transform:translateX(-50%) rotate(6deg);filter:drop-shadow(0 30px 28px rgba(110,30,70,.28))}}
.new{{position:absolute;top:{heroTop+30}px;right:{110 if not story else 90}px;width:150px;height:150px;border-radius:50%;background:#C9A24B;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(12deg);box-shadow:0 10px 24px rgba(0,0,0,.15)}}
.new b{{font-weight:900;font-size:36px;line-height:1}} .new s{{text-decoration:none;font-family:Poppins;font-weight:700;font-size:15px;letter-spacing:2px}}
.strip{{position:absolute;left:40px;right:40px;top:{strip_top}px;background:rgba(255,255,255,.75);border-radius:30px;padding:16px 18px 14px}}
.strip h3{{direction:rtl;text-align:right;font-weight:800;font-size:{22 if not story else 26}px;margin:0 8px 6px;color:#7E3D5C}}
.row{{display:flex;justify-content:space-between}}
.o{{display:flex;flex-direction:column;align-items:center;width:{sz+20}px}}
.o img{{height:{sz}px;max-width:{sz+10}px;object-fit:contain;filter:drop-shadow(0 8px 8px rgba(0,0,0,.18))}}
.o span{{font-family:Poppins;font-weight:500;font-size:{15 if not story else 17}px;margin-top:4px;white-space:nowrap}}
.foot{{position:absolute;left:56px;right:56px;bottom:{40 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#4A1630;color:#F9E3EB;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;color:#D46A97}}
</style></head><body>
<img class="logo" src="file://{LOGO}"><div class="eb">FITBIT AIR · FABRIC</div>
<h1>لون جديد.. <b>Blush Pink</b></h1>
<div class="sub">سير قماش مطاطي ناعم لـ <b>Fitbit Air</b></div>
<div class="disc"></div>
<img class="hero" src="file://{P}blush-crop.png">
<div class="new"><b>جديد</b><s>NEW</s></div>
<div class="strip"><h3>ومتوفر بعد بالألوان:</h3><div class="row">{cards}</div></div>
<div class="foot"><div class="cta">علّق <em>«فت بت»</em> ونرسل لك الرابط 📩</div><div class="price"><b>74</b> ر.ق</div></div>
</body></html>'''
for name,W,H,st in (('974-fitbit-fabric-blush-post',1080,1350,False),('974-fitbit-fabric-blush-story',1080,1920,True)):
    open(name+'.html','w').write(page(W,H,st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print('ok')
