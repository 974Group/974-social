# Sticker order file for the printer: page 1 = order sheet (colour, barcode, quantity, spec), page 2 = artwork with cut lines.
import sys, importlib.util, shutil
spec = importlib.util.spec_from_file_location('ex', '/home/claude/974-social/packaging/fitbit-fabric/export_ai.py')
src = open(spec.origin).read().rsplit('\nwith sync_playwright() as p:', 1)[0]
g = {}; exec(src, g)
from playwright.sync_api import sync_playwright
QTY = {'Black': 60, 'Grey': 140, 'Pinky Red': 160, 'Brown': 70, 'Blue': 150, 'Fog': 170, 'Beige': 60, 'Navy': 60,
       'Olive green': 60, 'Light pink': 140, 'Purple': 50, 'Blush Pink': 170}
COLS = g['COLS']; SW, SH = g['SW_'], g['SH_']; c128 = g['c128_svg']
total = sum(QTY.values())
rows = ''.join(f'<tr><td>{i+1}</td><td><b>{n}</b></td><td class="en">{c}</td><td class="q">{QTY[n]}</td></tr>' for i, (n, c) in enumerate(COLS))
cells = ''
for i, (name, code) in enumerate(COLS):
    col, row = i % 4, i // 4
    x = 20 + col*(SW + 22); y = 40 + row*(SH + 24)
    cells += f'''<div class="st" style="left:{x}mm;top:{y}mm"><div class="bcd">{c128(code, 21, 6.5)}</div><div class="num">{code}</div><div class="nm">{name.upper()}</div></div>
<div class="lbl" style="left:{x}mm;top:{y+SH+2}mm"><b>{name}</b> · Qty {QTY[name]}</div>'''
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{g["g"]["FONTS"]}
@page{{size:210mm 297mm;margin:0}} *{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Poppins;color:#111}} .pg{{width:210mm;height:297mm;position:relative;page-break-after:always;overflow:hidden}}
h1{{position:absolute;left:20mm;top:16mm;font-size:6mm}} .ar{{font-family:Cairo;direction:rtl}}
.sub{{position:absolute;left:20mm;top:25mm;font-size:3.2mm;color:#555}}
table{{position:absolute;left:20mm;top:58mm;width:170mm;border-collapse:collapse;font-size:3.6mm}}
th,td{{border-bottom:.3mm solid #ddd;padding:2.2mm 3mm;text-align:left}} th{{background:#111;color:#fff;font-size:3mm;letter-spacing:.4mm}}
td.q{{font-weight:700;text-align:right}} th.q{{text-align:right}} tr.tot td{{border-top:.6mm solid #111;font-weight:800;font-size:4mm}}
.spec{{position:absolute;left:20mm;top:36mm;width:170mm;font-size:3.2mm;line-height:1.6;background:#F4F1F2;border-radius:2mm;padding:3mm 4mm}}
.spec b{{color:#720842}}
.note{{position:absolute;left:20mm;right:20mm;bottom:18mm;font-size:3.6mm;line-height:1.7;text-align:right}}
.st{{position:absolute;width:{SW}mm;height:{SH}mm;background:#fff;border-radius:1.2mm;outline:.25mm dashed #E4007C;padding:1.2mm 2mm 0;text-align:center}}
.bcd svg{{display:block;margin:0 auto}} .num{{font-weight:600;font-size:2.1mm;letter-spacing:.6mm;margin-top:.4mm}}
.nm{{font-weight:700;font-size:1.8mm;letter-spacing:.25mm;margin-top:.3mm;white-space:nowrap}} .lbl{{position:absolute;font-size:2.4mm;color:#666}}
</style></head><body>
<div class="pg">
 <h1>974Group · Barcode sticker order</h1>
 <div class="sub">Fitbit Air FABRIC band boxes · 18 Nov 2026 · artwork on page 2</div>
 <div class="spec"><b>Size</b> 25 × 15 mm · <b>Material</b> white matte paper sticker · <b>Corners</b> rounded 1.2 mm · <b>Cut</b> kiss-cut (pink dashed line on page 2) · <b>Print</b> black only (1 colour) · barcodes are Code 128 — please do not resize or redraw them</div>
 <table><tr><th>#</th><th>COLOUR</th><th>BARCODE</th><th class="q">QUANTITY</th></tr>{rows}
 <tr class="tot"><td></td><td>TOTAL</td><td></td><td class="q">{total}</td></tr></table>
 <div class="note ar">الكمية لكل لون مكتوبة في الجدول · المقاس 25 × 15 ملم · ورق ستيكر أبيض مطفي · طباعة أسود بس · القص على الخط الوردي المتقطع<br>رجاءً لا تكبّرون ولا تصغّرون الباركود عشان يقرأه الجهاز.</div>
</div>
<div class="pg"><h1 style="font-size:5mm;top:14mm">Artwork · 12 designs (one per colour)</h1>
 <div class="sub" style="top:22mm">Each design is printed in the quantity shown under it. Pink dashed line = cut line (do not print).</div>{cells}</div>
</body></html>'''
open('stickers-order.html', 'w').write(html)
OUT = '/mnt/user-data/outputs/packaging/974-fitbit-fabric-stickers-ORDER'
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page()
    pg.goto('file:///home/claude/974-social/packaging/fitbit-fabric/stickers-order.html'); pg.wait_for_timeout(600)
    pg.pdf(path=OUT + '.pdf', width='210mm', height='297mm', print_background=True)
    br.close()
shutil.copy(OUT + '.pdf', OUT + '.ai')
print(total)
