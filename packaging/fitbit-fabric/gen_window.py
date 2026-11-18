# Universal Fitbit Air FABRIC box — same die as the nylon-loop box (packaging/fitbit-box):
# 70 W x 75 H x 30 D mm, 300 dpi, panels stacked: flap / front / side / back (rotated) / glue.
# New: a vertical window cut in the middle of the front so the band colour shows; colour goes on a sticker.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import FONTS
from playwright.sync_api import sync_playwright
B = '/home/claude/974-social/packaging/fitbit-box/'
LW = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
ANTON = '/home/claude/974-social/posts/2026-11/gta/fonts/anton.woff2'
BAND = '/home/claude/974-social/products/fitbit-fabric-blush/src/'
PX = 300/25.4                      # px per mm
BG, FG, STRIPE, GOLD = '#141414', '#F2F2F2', '#E9E9E9', '#C9A24B'
# window in FRONT-panel coordinates (px); front panel = 898 x 886 incl. 35 px side bleed
WIN_W, WIN_H = round(22*PX), round(44*PX)
WIN_X = (898 - WIN_W)//2; WIN_Y = 205

def stripes(h=355):
    # same rounded "loop" stripes as the nylon box side panel
    n = 14; gap = 898/n
    return ''.join(f'<i style="left:{i*gap + gap*0.22:.0f}px;width:{gap*0.56:.0f}px;top:40px;height:{h-80}px"></i>' for i in range(n))

def front(band=None):
    win_inner = (f'<img src="file://{band}" style="position:absolute;height:120%;left:50%;top:50%;transform:translate(-40%,-50%)">' if band
                 else f'<span>WINDOW<br>22 × 44 mm<br>+ clear PET</span>')
    return f'''<img class="abs" src="file://{LW}" style="left:52px;top:52px;width:250px">
<div class="abs en" style="right:52px;top:62px;text-align:right;font-weight:700;font-size:24px;letter-spacing:6px">FABRIC BAND</div>
<div class="abs ar" style="right:52px;top:100px;font-size:26px;font-weight:700;opacity:.75">سير فابريك لـ <span class="en">Fitbit Air</span></div>
<div class="win" style="left:{WIN_X}px;top:{WIN_Y}px;width:{WIN_W}px;height:{WIN_H}px">{win_inner}</div>
<div class="abs ar" style="right:52px;bottom:60px;font-size:24px;font-weight:700;opacity:.8">يتسكر باللزقة · خفيف</div>
<div class="abs tag" style="left:52px;bottom:52px"><span>COLOUR</span><b></b></div>'''

def die(band=None):
    return f'''<div class="die">
 <div class="p flap"><div class="abs tag2" style="left:87px;top:50%;transform:translateY(-50%)">FABRIC · FITBIT AIR</div>
   <img class="abs" src="file://{LW}" style="right:87px;top:50%;transform:translateY(-50%);width:150px"></div>
 <div class="p front">{front(band)}</div>
 <div class="p side"><div class="loops">{stripes()}</div>
   <div class="abs pill">FABRIC · FITBIT AIR</div></div>
 <div class="p back"><div class="rot">
  <img class="abs" src="file://{LW}" style="left:87px;top:56px;width:170px">
  <div class="abs ar" style="left:87px;right:87px;top:170px;font-size:28px;font-weight:800;line-height:1.7">
   صُنع بفخر من قطر.<br><span style="font-weight:500;opacity:.8">سيور بجودة عالية ترفع ستايلك اليومي. شكراً إنك تدعم مشروع محلي.</span></div>
  <div class="abs en" style="left:87px;right:87px;top:420px;font-size:18px;font-weight:500;line-height:1.55;opacity:.8">
   Proudly founded in Qatar. Premium bands that elevate your everyday style. Thank you for supporting a local business.</div>
  <div class="qr" style="left:87px;bottom:60px;width:210px"><img src="file://{B}qr.png"></div>
  <div class="abs ar" style="left:325px;bottom:215px;font-size:20px;font-weight:700;opacity:.85">امسح وتسوّق مباشرة</div>
  <div class="abs en" style="left:325px;bottom:112px;font-weight:700;font-size:18px;line-height:1.6">974GROUP.NET<br>+974 5555 6278<br>@974.Group</div>
  <div class="abs bc" style="right:87px;bottom:40px"><span>BARCODE<br>STICKER</span></div>
  <div class="abs en" style="left:325px;bottom:58px;font-size:11px;letter-spacing:2px;opacity:.6">MADE IN CHINA · DESIGNED IN QATAR</div>
 </div></div>
 <div class="p glue"></div>
 <svg class="cut" width="898" height="2729"><rect x="{WIN_X}" y="{390+WIN_Y}" width="{WIN_W}" height="{WIN_H}" rx="{round(4*PX)}" fill="none" stroke="#E3001B" stroke-width="2"/></svg>
</div>'''

CSS = f'''{FONTS}
@font-face{{font-family:Anton;src:url(file://{ANTON})}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#333;font-family:Cairo;display:flex;gap:60px;padding:40px;align-items:flex-start}}
.die{{position:relative;width:898px;height:2729px;overflow:hidden;background:{BG};color:{FG}}}
.p{{position:absolute;left:0;width:898px;overflow:hidden}}
.flap{{top:0;height:390px}} .front{{top:390px;height:886px}} .side{{top:1276px;height:355px}} .back{{top:1631px;height:886px}} .glue{{top:2517px;height:212px;background:#E2E2E2}}
.back .rot{{position:absolute;inset:0;transform:rotate(180deg)}}
.abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}} .ar{{direction:rtl}}
.tag2{{font-family:Poppins;font-weight:700;letter-spacing:4px;font-size:18px}}
.tag{{display:flex;align-items:center;gap:14px}} .tag span{{font-family:Poppins;font-weight:700;letter-spacing:4px;font-size:18px;color:{GOLD}}}
.tag b{{display:block;width:200px;height:52px;border:3px solid {GOLD};border-radius:26px}}
.win{{position:absolute;border-radius:{round(4*PX)}px;overflow:hidden;background:#F4F1F2;outline:5px solid {GOLD};outline-offset:12px;display:flex;align-items:center;justify-content:center}}
.win span{{font-family:Poppins;color:#999;font-size:22px;text-align:center;line-height:1.5}}
.loops{{position:absolute;inset:0}} .loops i{{position:absolute;background:{STRIPE};border-radius:999px}}
.pill{{left:50%;top:50%;transform:translate(-50%,-50%);background:{BG};padding:14px 36px;border-radius:999px;font-family:Poppins;font-weight:700;letter-spacing:4px;font-size:20px;white-space:nowrap}}
.qr{{position:absolute;background:#fff;border-radius:14px;padding:10px}} .qr img{{display:block;width:100%}}
.bc{{width:220px;height:130px;background:#fff;border-radius:10px;display:flex;align-items:center;justify-content:center}} .bc span{{font-family:Poppins;color:#bbb;font-size:16px;letter-spacing:3px;text-align:center}}
.cut{{position:absolute;left:0;top:0;pointer-events:none}}
.mk{{position:relative;width:898px;height:886px;overflow:hidden;background:{BG};color:{FG};box-shadow:0 30px 60px rgba(0,0,0,.4)}}'''

def page(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{inner}</body></html>'

with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={'width': 1000, 'height': 2850})
    open('box-window.html', 'w').write(page(die()))
    pg.goto('file:///home/claude/974-social/packaging/fitbit-fabric/box-window.html'); pg.wait_for_timeout(600)
    pg.locator('.die').screenshot(path='974-fitbit-fabric-window-box-dieline-300dpi.png')
    cols = ['grey', 'blush', 'fog', 'olive']
    mk = ''.join(f'<div class="mk">{front(BAND + c + "-cut.png")}</div>' for c in cols)
    open('box-window-mock.html', 'w').write(page(mk).replace('body{', 'body{background:#EFE9E4;'))
    pg2 = br.new_page(viewport={'width': 4*898 + 5*60, 'height': 886 + 80})
    pg2.goto('file:///home/claude/974-social/packaging/fitbit-fabric/box-window-mock.html'); pg2.wait_for_timeout(600)
    pg2.screenshot(path='974-fitbit-fabric-window-box-mockup.png')
    br.close()
from PIL import Image
im = Image.open('974-fitbit-fabric-window-box-dieline-300dpi.png').convert('RGB')
im.save('974-fitbit-fabric-window-box-dieline.pdf', resolution=300)
print(im.size)
