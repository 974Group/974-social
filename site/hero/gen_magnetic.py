# Home banner slide: Garmin CIRQA magnetic (replaces "all CIRQA" slide). 18 Nov 2026
import subprocess, os
os.chdir('/home/claude/974-social/site/hero')
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
P = '/home/claude/974-social/products/garmin-cirqa-magnetic/src/'
MARK_W = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
GOLD = '#C9A24B'
cols = ['black', 'white', 'starlight', 'grey', 'dark-blue', 'wine-red', 'pink', 'orange', 'lime', 'army-green']
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''


def page(W, H):
    mob = W < 2000
    cw, ch, gx, gy = (102, 138, 6, 14) if mob else (196, 258, 18, 22)
    gw = 5 * cw + 4 * gx; gh = 2 * ch + gy
    left = 34 if mob else 110
    top = (H - gh) // 2
    bands = ''
    for i, c in enumerate(cols):
        r, k = divmod(i, 5)
        bands += f'<div class="b" style="left:{k*(cw+gx)}px;top:{r*(ch+gy)}px;width:{cw}px;height:{ch}px"><img src="file://{P}{c}-crop.png"></div>'
    # magnetic field arcs behind the grid
    arcs = ''.join(f'<div style="position:absolute;left:{left+gw/2-(140+i*110)*(0.55 if mob else 1)}px;top:{H/2-(140+i*110)*(0.55 if mob else 1)}px;width:{(280+i*220)*(0.55 if mob else 1)}px;height:{(280+i*220)*(0.55 if mob else 1)}px;border:2px solid rgba(201,162,75,{0.22-i*0.04});border-radius:50%"></div>' for i in range(5))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;color:#fff;
background:radial-gradient(ellipse at 28% 50%,#3A3F49 0%,#23262D 45%,#15171B 100%)}}
.g{{position:absolute;left:{left}px;top:{top}px;width:{gw}px;height:{gh}px}}
.b{{position:absolute;display:flex;align-items:center;justify-content:center}}
.b img{{max-width:100%;max-height:100%;object-fit:contain;filter:drop-shadow(0 {8 if mob else 14}px {8 if mob else 14}px rgba(0,0,0,.5))}}
.t{{position:absolute;right:{40 if mob else 120}px;top:50%;transform:translateY(-50%);text-align:right;direction:rtl;width:{470 if mob else 820}px}}
.top{{display:flex;justify-content:flex-start;align-items:center;gap:{12 if mob else 18}px}}
.lg{{height:{36 if mob else 54}px}}
.new{{background:{GOLD};color:#15171B;font-weight:900;border-radius:40px;padding:{2 if mob else 4}px {14 if mob else 22}px {5 if mob else 7}px;font-size:{20 if mob else 30}px}}
.eb{{font-family:Poppins;font-weight:700;letter-spacing:{4 if mob else 6}px;font-size:{17 if mob else 25}px;color:{GOLD};direction:ltr;text-align:right;margin-top:{12 if mob else 20}px}}
h2{{font-weight:900;font-size:{58 if mob else 112}px;line-height:1.08;margin-top:{2 if mob else 6}px;white-space:nowrap}}
h2 em{{font-style:normal;color:{GOLD}}}
.sub{{font-weight:700;font-size:{24 if mob else 38}px;opacity:.85;margin-top:{6 if mob else 12}px}}
.row{{display:flex;gap:{12 if mob else 20}px;align-items:center;margin-top:{18 if mob else 32}px}}
.btn{{background:{GOLD};color:#15171B;border-radius:60px;padding:{6 if mob else 10}px {24 if mob else 40}px {9 if mob else 14}px;font-weight:800;font-size:{23 if mob else 36}px}}
.pr{{font-weight:900;font-size:{30 if mob else 48}px}}
.pr b{{font-family:Poppins}}
</style></head><body>
{arcs}
<div class="g">{bands}</div>
<div class="t"><div class="top"><img class="lg" src="file://{MARK_W}"><span class="new">جديد</span></div>
<div class="eb">GARMIN CIRQA · MAGNETIC</div>
<h2>يتسكر <em>بالمغناطيس</em></h2>
<div class="sub">بدون قفل · 10 ألوان · سيليكون ناعم</div>
<div class="row"><div class="btn">تسوّق الحين ←</div><div class="pr"><b>99</b> ر.ق</div></div></div>
</body></html>'''


for nm, W, H in (('desktop', 2400, 630), ('mobile', 1200, 630)):
    name = f'cirqa-magnetic-{nm}'
    open(name + '.html', 'w').write(page(W, H))
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True)
    from PIL import Image
    Image.open(name + '.png').convert('RGB').save(f'{name}-v1.jpg', quality=90)
print('ok')
