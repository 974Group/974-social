import subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
C = '/home/claude/974-social/posts/2026-11/exotic-leather/cut/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
FD = '/home/claude/974-social/reels/2026-11/nov-deals/assets/fonts/'
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{FD}cairo-ar.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{FD}cairo-lat.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''
GOLD = '#C9A24B'
BANDS = [('himalayan', 'هملايا'), ('black-python', 'ثعبان'), ('holographic-croc', 'تمساح'),
         ('pink-lizard', 'سحلية'), ('ivory-ostrich', 'نعام')]
BG = 'radial-gradient(ellipse at 28% 50%,#8A1450 0%,#720842 30%,#51022D 68%,#2E0119 100%)'


def bands(x0, top, h, gap, lab):
    w = round(h * 0.382)
    out = ''
    for i, (f, n) in enumerate(BANDS):
        x = x0 + i * (w + gap)
        out += f'''<div class="spot" style="left:{x - w*0.6}px;top:{top + h*0.55}px;width:{w*2.2}px;height:{h*0.6}px"></div>
<img class="bd" src="file://{C}{f}.png" style="left:{x}px;top:{top}px;height:{h}px;width:{w}px">
<div class="lb" style="left:{x - 40}px;width:{w + 80}px;top:{top + h + lab[0]}px;font-size:{lab[1]}px">{n}</div>'''
    return out, 5 * w + 4 * gap


def page(mob, W, H):
    if not mob:
        bh, gap, by = 440, 40, 52
        row, bw = bands(0, 0, bh, gap, (16, 34))
        bx = 100
        txt = f'''<div class="t" style="right:120px;top:50%;transform:translateY(-50%);width:900px">
<img class="lg" src="file://{LOGO}" style="height:56px;margin-bottom:18px">
<div class="eb" style="font-size:26px;letter-spacing:7px">EXOTIC LEATHER · WHOOP 5.0 / MG</div>
<h2 style="font-size:90px;margin-top:4px">خمس جلود.. <em>ستايل واحد</em></h2>
<div class="sub" style="font-size:36px;margin-top:8px;white-space:nowrap">موديلات جديدة وألوان رجعت · الكمية محدودة</div>
<div class="row" style="margin-top:32px;gap:20px"><div class="btn" style="font-size:36px;padding:10px 42px 14px">تسوّق الحين ←</div>
<div class="pr" style="font-size:44px">من <b>199</b> ر.ق</div></div></div>'''
        grid = f'<div class="g" style="left:{bx}px;top:{by}px;width:{bw}px;height:{H}px">{row}</div>'
    else:
        bh, gap = 330, 44
        row, bw = bands(0, 0, bh, gap, (10, 30))
        bx = (W - bw) // 2
        txt = f'''<div class="t" style="right:48px;top:34px;width:{W-96}px">
<div style="display:flex;justify-content:space-between;align-items:flex-start">
<div><div class="eb" style="font-size:20px;letter-spacing:5px">EXOTIC LEATHER</div>
<h2 style="font-size:62px;margin-top:0">خمس جلود.. <em>ستايل واحد</em></h2></div>
<div style="display:flex;flex-direction:column;align-items:flex-start;gap:6px;margin-top:8px">
<div class="btn" style="font-size:28px;padding:6px 30px 10px">تسوّق الحين ←</div>
<div class="pr" style="font-size:28px;align-self:center">من <b>199</b> ر.ق</div></div></div></div>'''
        grid = f'<div class="g" style="left:{bx}px;top:200px;width:{bw}px;height:{H}px">{row}</div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:{BG};font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.wm{{position:absolute;left:0;right:0;bottom:{-40 if not mob else -30}px;text-align:{'left' if not mob else 'center'};padding-left:{60 if not mob else 0}px;font-family:Poppins;font-weight:700;font-size:{300 if not mob else 190}px;letter-spacing:-6px;color:rgba(255,255,255,.035);line-height:1}}
.g{{position:absolute}}
.spot{{position:absolute;background:radial-gradient(50% 50% at 50% 50%,rgba(201,162,75,.22),transparent 70%)}}
.bd{{position:absolute;object-fit:contain;filter:drop-shadow(0 {18 if not mob else 12}px {20 if not mob else 14}px rgba(0,0,0,.5))}}
.lb{{position:absolute;text-align:center;font-weight:800;color:{GOLD}}}
.t{{position:absolute;text-align:right;direction:rtl}}
.eb{{font-family:Poppins;font-weight:700;color:{GOLD};direction:ltr;text-align:right}}
h2{{font-weight:900;line-height:1.15;white-space:nowrap}}
h2 em{{font-style:normal;color:{GOLD}}}
.sub{{font-weight:700;opacity:.82}}
.row{{display:flex;align-items:center}}
.pr{{font-weight:900}} .pr b{{font-family:Poppins}}
.btn{{background:{GOLD};color:#2E0119;border-radius:60px;font-weight:800;white-space:nowrap}}
</style></head><body><div class="wm">EXOTIC</div>{grid}{txt}</body></html>'''


for nm, W, H, mob in (('desktop', 2400, 630, False), ('mobile', 1200, 630, True)):
    name = f'leather-{nm}'
    open(name + '.html', 'w').write(page(mob, W, H))
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True)
    subprocess.run(['python3', '-c', f"from PIL import Image;Image.open('{name}.png').convert('RGB').save('{name}.jpg',quality=88)"], check=True)
print('ok')
