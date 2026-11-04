import subprocess, math
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R='/home/claude/974-social/products/'
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''
LOGO_W='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
LOGO_C='/home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'

# ---------- A: CIRQA silicone 2.0 (sport / breathable) ----------
A=R+'garmin-cirqa-silicone-v2/src/'
acols=[('Black','black'),('Starlight','starlight'),('Lime','lime'),('Midnight Blue','midnight-blue'),('Army Green','green'),('Sea Mist Blue','sea-mist-blue'),('Mousse Pink','mousse-pink'),('Orange','orange'),('White','white'),('Light Gray','light-gray')]
def pageA(W,H,story,price):
    top=H*0.52 if not story else H*0.50
    hero_h=520 if not story else 600
    cell=180 if not story else 186
    imgh=150 if not story else 190
    cards=''.join(f'<div class="c"><img src="file://{A}{f}-crop.png"><span>{n}</span></div>' for n,f in acols)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:#F3F4EE;font-family:Cairo;color:#141414;position:relative;overflow:hidden}}
.panel{{position:absolute;left:0;top:0;width:{W}px;height:{top}px;background:#D9E33A;overflow:hidden}}
.panel:after{{content:'';position:absolute;left:-120px;bottom:-160px;width:520px;height:520px;border-radius:50%;border:70px solid rgba(20,20,20,.06)}}
.logo{{position:absolute;top:{56 if not story else 140}px;left:56px;height:50px}}
.tag{{position:absolute;top:{66 if not story else 150}px;right:56px;font-family:Poppins;font-weight:700;font-size:18px;letter-spacing:3px;background:#141414;color:#D9E33A;padding:8px 18px;border-radius:30px}}
.hero{{position:absolute;left:{30 if not story else 20}px;top:{top-hero_h-10}px;height:{hero_h}px;z-index:2;filter:drop-shadow(0 30px 30px rgba(0,0,0,.35));transform:rotate(-8deg)}}
h1{{position:absolute;right:56px;top:{150 if not story else 260}px;width:{520 if not story else 480}px;text-align:right;direction:rtl;font-weight:900;font-size:{72 if not story else 76}px;line-height:1.05}}
.sub{{position:absolute;right:56px;top:{345 if not story else 500}px;width:440px;direction:rtl;text-align:right;font-weight:700;font-size:{26 if not story else 30}px;line-height:1.45}}
.sub b{{font-family:Poppins}}
.holes{{position:absolute;right:56px;top:{450 if not story else 620}px;display:flex;gap:10px}}
.holes i{{width:22px;height:22px;border-radius:50%;background:#141414;opacity:.85}}
.grid{{position:absolute;top:{top+(36 if not story else 60)}px;left:50%;transform:translateX(-50%);display:grid;grid-template-columns:repeat(5,{cell}px);gap:{14 if not story else 30}px 16px}}
.c{{display:flex;flex-direction:column;align-items:center}}
.c img{{height:{imgh}px;max-width:{cell-10}px;object-fit:contain;filter:drop-shadow(0 10px 10px rgba(0,0,0,.18))}}
.c span{{font-family:Poppins;font-weight:500;font-size:{17 if not story else 20}px;margin-top:6px;white-space:nowrap;color:#3a3a3a}}
.foot{{position:absolute;left:56px;right:56px;bottom:{44 if not story else 110}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#141414;color:#D9E33A;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;background:#D9E33A;padding:0 8px;border-radius:8px}}
</style></head><body>
<div class="panel"></div>
<img class="logo" src="file://{LOGO_C}"><div class="tag">CIRQA 2.0</div>
<img class="hero" src="file://{A}black-crop.png">
<h1>يتنفّس معك<br>في كل تمرين</h1>
<div class="sub">سيليكون رياضي بفتحات تهوية<br>سير <b>Garmin CIRQA</b> · 10 ألوان</div>
<div class="holes"><i></i><i></i><i></i><i></i><i></i></div>
<div class="grid">{cards}</div>
<div class="foot"><div class="cta">علّق <em>«قارمن»</em> ونرسل لك الرابط 📩</div><div class="price"><b>{price}</b> ر.ق</div></div>
</body></html>'''

def pageC(W,H,story,price):
    top=H*0.52 if not story else H*0.50
    hero_h=520 if not story else 600
    cell=180 if not story else 186
    imgh=150 if not story else 190
    cards=''.join(f'<div class="c"><img src="file://{B}{f}-crop.png"><span>{n}</span></div>' for n,f in bcols)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:#F3F4EE;font-family:Cairo;color:#141414;position:relative;overflow:hidden}}
.panel{{position:absolute;left:0;top:0;width:{W}px;height:{top}px;background:#F59A2F;overflow:hidden}}
.panel:after{{content:'';position:absolute;left:-120px;bottom:-160px;width:520px;height:520px;border-radius:50%;border:70px solid rgba(20,20,20,.06)}}
.logo{{position:absolute;top:{56 if not story else 140}px;left:56px;height:50px}}
.tag{{position:absolute;top:{66 if not story else 150}px;right:56px;font-family:Poppins;font-weight:700;font-size:18px;letter-spacing:3px;background:#141414;color:#F59A2F;padding:8px 18px;border-radius:30px}}
.hero{{position:absolute;left:{30 if not story else 20}px;top:{top-hero_h-10}px;height:{hero_h}px;z-index:2;filter:drop-shadow(0 30px 30px rgba(0,0,0,.35));transform:rotate(-8deg)}}
h1{{position:absolute;right:56px;top:{150 if not story else 260}px;width:auto;text-align:right;direction:rtl;font-weight:900;font-size:{62 if not story else 66}px;white-space:nowrap;line-height:1.05}}
.sub{{position:absolute;right:56px;top:{345 if not story else 500}px;width:auto;white-space:nowrap;direction:rtl;text-align:right;font-weight:700;font-size:{26 if not story else 30}px;line-height:1.45}}
.sub b{{font-family:Poppins}}
.holes{{position:absolute;right:56px;top:{450 if not story else 620}px;display:flex;gap:10px}}
.holes i{{width:40px;height:10px;border-radius:5px;background:#141414;opacity:.85}}
.grid{{position:absolute;top:{top+(36 if not story else 60)}px;left:50%;transform:translateX(-50%);display:grid;grid-template-columns:repeat(5,{cell}px);gap:{14 if not story else 30}px 16px}}
.c{{display:flex;flex-direction:column;align-items:center}}
.c img{{height:{imgh}px;max-width:{cell-10}px;object-fit:contain;filter:drop-shadow(0 10px 10px rgba(0,0,0,.18))}}
.c span{{font-family:Poppins;font-weight:500;font-size:{17 if not story else 20}px;margin-top:6px;white-space:nowrap;color:#3a3a3a}}
.foot{{position:absolute;left:56px;right:56px;bottom:{44 if not story else 110}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#141414;color:#F59A2F;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;background:#F59A2F;padding:0 8px;border-radius:8px}}
</style></head><body>
<div class="panel"></div>
<img class="logo" src="file://{LOGO_C}"><div class="tag">MAGNETIC</div>
<img class="hero" src="file://{B}black-crop.png">
<h1>بدون قفل..<br>يتسكّر بالمغناطيس</h1>
<div class="sub">سيليكون ناعم · يتضبط على أي معصم<br>سير <b>Garmin CIRQA</b> · 10 ألوان</div>
<div class="holes"><i class="bar"></i><i class="bar"></i><i class="bar"></i><i class="bar"></i><i class="bar"></i></div>
<div class="grid">{cards}</div>
<div class="foot"><div class="cta">علّق <em>«قارمن»</em> ونرسل لك الرابط 📩</div><div class="price"><b>{price}</b> ر.ق</div></div>
</body></html>'''

# ---------- B: CIRQA magnetic (ring of colours) ----------
B=R+'garmin-cirqa-magnetic/src/'
bcols=[('Black','black'),('White','white'),('Starlight','starlight'),('Grey','grey'),('Dark Blue','dark-blue'),('Wine Red','wine-red'),('Pink','pink'),('Orange','orange'),('Lime','lime'),('Army Green','army-green')]
def pageB(W,H,story,price):
    cx=W/2; cy=(H*0.56) if not story else H*0.53
    rad=330 if not story else 360
    sz=150 if not story else 165
    items=''
    for i,(n,f) in enumerate(bcols):
        a=-math.pi/2+i*2*math.pi/len(bcols)
        x=cx+rad*math.cos(a); y=cy+rad*math.sin(a)
        items+=f'<div class="b" style="left:{x-sz/2:.0f}px;top:{y-sz/2-10:.0f}px"><img src="file://{B}{f}-crop.png"><span>{n}</span></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:radial-gradient(circle at 50% {cy/H*100:.0f}%,#7A1428 0%,#4A0A17 45%,#22040A 100%);font-family:Cairo;color:#F7EDEF;position:relative;overflow:hidden}}
.logo{{position:absolute;top:{56 if not story else 140}px;left:50%;transform:translateX(-50%);height:46px}}
h1{{position:absolute;top:{130 if not story else 230}px;left:40px;right:40px;text-align:center;direction:rtl;font-weight:900;font-size:{64 if not story else 66}px;line-height:1.1;white-space:nowrap}}
h1 i{{font-style:normal;color:#C9A24B}}
.sub{{position:absolute;top:{215 if not story else 330}px;left:40px;right:40px;text-align:center;direction:rtl;font-weight:600;font-size:{25 if not story else 29}px;color:#E5C9CF}}
.sub b{{font-family:Poppins;font-weight:700}}
.ring{{position:absolute;left:{cx-rad+40}px;top:{cy-rad+40}px;width:{2*rad-80}px;height:{2*rad-80}px;border-radius:50%;border:2px dashed rgba(201,162,75,.45)}}
.mid{{position:absolute;left:{cx-150}px;top:{cy-150}px;width:300px;height:300px;border-radius:50%;background:rgba(255,255,255,.06);display:flex;flex-direction:column;align-items:center;justify-content:center;direction:rtl}}
.mid .mg{{font-size:64px;line-height:1}}
.mid .n{{font-weight:900;font-size:40px;margin-top:6px}}
.mid .m{{font-family:Poppins;font-weight:500;letter-spacing:3px;font-size:15px;color:#C9A24B}}
.b{{position:absolute;width:{sz}px;display:flex;flex-direction:column;align-items:center}}
.b img{{height:{sz-30}px;max-width:{sz}px;object-fit:contain;filter:drop-shadow(0 12px 14px rgba(0,0,0,.5))}}
.b span{{font-family:Poppins;font-weight:500;font-size:{15 if not story else 17}px;margin-top:4px;white-space:nowrap;color:#F0DDE1}}
.foot{{position:absolute;left:56px;right:56px;bottom:{44 if not story else 110}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#C9A24B;color:#22040A;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;color:#C9A24B}}
</style></head><body>
<img class="logo" src="file://{LOGO_W}">
<h1>بدون قفل<i>..</i> يتسكّر بالمغناطيس</h1>
<div class="sub">سيليكون ناعم يتضبط على أي معصم · سير <b>Garmin CIRQA</b></div>
<div class="ring"></div>
<div class="mid"><div class="mg">🧲</div><div class="n">10 ألوان</div><div class="m">MAGNETIC</div></div>
{items}
<div class="foot"><div class="cta">علّق <em>«قارمن»</em> ونرسل لك الرابط 📩</div><div class="price"><b>{price}</b> ر.ق</div></div>
</body></html>'''

jobs=[('974-cirqa-silicone-2-post',pageA,1080,1350,False,'89'),('974-cirqa-silicone-2-story',pageA,1080,1920,True,'89'),
      ('974-cirqa-magnetic-post',pageC,1080,1350,False,'99'),('974-cirqa-magnetic-story',pageC,1080,1920,True,'99')]
for name,fn,W,H,st,pr in jobs:
    open(name+'.html','w').write(fn(W,H,st,pr))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print('ok')
