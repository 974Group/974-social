# Vector exports: (1) the box without barcode as PDF/.ai, (2) A4 barcode-sticker sheet as PDF/.ai
import sys, os, shutil
sys.path.insert(0, '/home/claude/974-social/packaging/fitbit-fabric')
import importlib.util
spec = importlib.util.spec_from_file_location('gw', '/home/claude/974-social/packaging/fitbit-fabric/gen_window.py')
src = open(spec.origin).read().split('with sync_playwright() as p:')[0]   # import helpers only
g = {}; exec(src, g)
from playwright.sync_api import sync_playwright
sys.path.insert(0, '/home/claude/974-social/packaging/fitbit-box'); from c128 import P
D = '/home/claude/974-social/packaging/fitbit-fabric/'
OUT = '/mnt/user-data/outputs/packaging/'
PX = 300/25.4

def c128_svg(digits, w_mm, h_mm):
    vals = [105] + [int(digits[i:i+2]) for i in range(0, len(digits), 2)]
    chk = (vals[0] + sum(v*(i+1) for i, v in enumerate(vals[1:]))) % 103
    seq = ''.join(P[v] for v in vals + [chk]) + P[106]
    mods = sum(int(c) for c in seq) + 20          # 10-module quiet zone each side
    m = w_mm / mods; x = 10*m; r = []
    for i, c in enumerate(seq):
        wd = int(c)*m
        if i % 2 == 0: r.append(f'<rect x="{x:.3f}" y="0" width="{wd:.3f}" height="{h_mm}" fill="#000"/>')
        x += wd
    return f'<svg width="{w_mm}mm" height="{h_mm}mm" viewBox="0 0 {w_mm} {h_mm}">{"".join(r)}</svg>'

COLS = [('Black','29740048'),('Grey','29740024'),('Pinky Red','29740116'),('Brown','29740055'),('Blue','29740086'),('Fog','29740000'),
        ('Beige','29740314'),('Navy','29740383'),('Olive green','29740437'),('Light pink','29740376'),('Purple','29740390'),('Blush Pink','29750597')]
SW_, SH_ = 25, 15   # sticker mm
def sticker_sheet():
    cells = ''
    for i, (name, code) in enumerate(COLS):
        col, row = i % 4, i // 4
        x = 20 + col*(SW_ + 22); y = 40 + row*(SH_ + 22)
        cells += f'''<div class="st" style="left:{x}mm;top:{y}mm">
  <div class="bcd">{c128_svg(code, 21, 6.5)}</div><div class="num">{code}</div>
  <div class="nm">{name.upper()}</div></div>
  <div class="lbl" style="left:{x}mm;top:{y+SH_+2}mm">{name} · {code}</div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{g["FONTS"]}
@page{{size:210mm 297mm;margin:0}} *{{margin:0;padding:0;box-sizing:border-box}}
body{{width:210mm;height:297mm;position:relative;font-family:Poppins;background:#fff}}
h1{{position:absolute;left:20mm;top:14mm;font-size:5mm;color:#111}} p.s{{position:absolute;left:20mm;top:21mm;font-size:3mm;color:#555}}
.st{{position:absolute;width:{SW_}mm;height:{SH_}mm;background:#fff;border-radius:1.2mm;outline:.25mm dashed #E4007C;outline-offset:0;padding:1.2mm 2mm 0;text-align:center}}
.bcd svg{{display:block;margin:0 auto}} .num{{font-weight:600;font-size:2.1mm;letter-spacing:.6mm;color:#000;margin-top:.4mm}}
.nm{{font-weight:700;font-size:1.8mm;letter-spacing:.25mm;color:#000;margin-top:.3mm;white-space:nowrap}} .nm b{{font-weight:800}}
.lbl{{position:absolute;font-size:2.2mm;color:#888}}</style></head><body>
<h1>974Group · Fitbit Air FABRIC band — barcode stickers</h1>
<p class="s">Sticker {SW_} × {SH_} mm, white matte, rounded corners 1.2 mm · pink dashed line = cut (kiss-cut) · goes on the back, bottom-right · one design per colour, print the quantity per colour</p>
{cells}</body></html>'''

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page()
    # box without barcode, vector: 898 x 2729 px @300dpi -> mm; CSS px are 1/96 in, so scale 96/300
    html = g['page'](g['die'](None)).replace('body{background:#333;', 'body{background:#fff;').replace('padding:40px;', 'padding:0;')
    open(D + 'box-nobarcode.html', 'w').write(html)
    pg.goto('file://' + D + 'box-nobarcode.html'); pg.wait_for_timeout(600)
    pg.pdf(path=OUT + '974-fitbit-fabric-box-no-barcode.pdf', width=f'{898/PX:.2f}mm', height=f'{2729/PX:.2f}mm', scale=96/300, print_background=True)
    open(D + 'stickers.html', 'w').write(sticker_sheet())
    pg.goto('file://' + D + 'stickers.html'); pg.wait_for_timeout(500)
    pg.pdf(path=OUT + '974-fitbit-fabric-barcode-stickers.pdf', width='210mm', height='297mm', print_background=True)
    pg2 = br.new_page(viewport={'width': 794, 'height': 1123}, device_scale_factor=2)
    pg2.goto('file://' + D + 'stickers.html'); pg2.wait_for_timeout(500); pg2.screenshot(path='/tmp/stickers.png')
    br.close()
for n in ['974-fitbit-fabric-box-no-barcode', '974-fitbit-fabric-barcode-stickers']:
    shutil.copy(OUT + n + '.pdf', OUT + n + '.ai')
    shutil.copy(OUT + n + '.pdf', D + n + '.pdf'); shutil.copy(OUT + n + '.pdf', D + n + '.ai')
print('ok')
