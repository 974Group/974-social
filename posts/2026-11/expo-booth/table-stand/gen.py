# Acrylic T-stand insert for expos: A5 portrait 148 x 210 mm + 3 mm bleed, vector PDF. 22 Nov 2026.
# One big "scan & shop" QR (utm_medium=stand) + Instagram line, bilingual, no prices.
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/expo-booth/counter-card'); import gen as C
D = '/home/claude/974-social/posts/2026-11/expo-booth/table-stand/'
WEB = 'https://974group.net/?utm_source=expo&utm_medium=stand&utm_campaign=expo'
BW, BH, B = 148, 210, 3


def page():
    W, H = BW + 2 * B, BH + 2 * B
    w0, h0 = map(float, C.vb.split()[2:])
    lh = 15
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{C.SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{C.SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:{W}mm {H}mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{background:{C.DK};overflow:hidden;width:{W}mm;height:{H}mm}}
body{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;font-family:Cairo;color:#fff;
background:radial-gradient(ellipse 110mm 80mm at 50% 30%,#9A1460 0%,rgba(154,20,96,0) 70%),linear-gradient(180deg,{C.M} 0%,{C.DK} 100%)}}
.wave{{position:absolute;left:0;right:0;top:{B+78}mm;height:{H}mm;background:#fff;border-radius:60% 40% 0 0 / 14mm 10mm 0 0}}
.c{{position:absolute;left:0;right:0;text-align:center}}
.logo{{top:{B+11}mm}}
.t1{{top:{B+30}mm;font-family:Poppins;font-weight:900;font-size:10mm;letter-spacing:.6mm}}
.t2{{top:{B+42}mm;font-weight:900;font-size:9mm;direction:rtl;color:{C.GOLD}}}
.cats{{top:{B+60}mm;font-family:Poppins;font-weight:700;font-size:2.9mm;letter-spacing:.7mm;opacity:.85}}
.cats2{{top:{B+65}mm;font-weight:700;font-size:3.6mm;direction:rtl;opacity:.85}}
.qrbox{{top:{B+90}mm}}
.qrbox .f{{display:inline-block;padding:4mm;border:1.2mm solid {C.M};border-radius:5mm}}
.sc{{top:{B+152}mm;color:{C.M};font-family:Poppins;font-weight:900;font-size:5mm;letter-spacing:1mm}}
.sc2{{top:{B+158}mm;color:{C.INK};font-weight:900;font-size:5mm;direction:rtl}}
.sc3{{top:{B+167.5}mm;color:{C.INK};font-family:Poppins;font-weight:700;font-size:2.8mm;letter-spacing:.6mm;opacity:.7}}
.ig{{top:{B+176}mm;color:{C.INK};display:flex;justify-content:center;align-items:center;gap:2.5mm;font-family:Poppins;font-weight:700;font-size:4.6mm}}
.web{{top:{B+184}mm;color:{C.M};font-family:Poppins;font-weight:700;font-size:3.6mm}}
.ty{{bottom:{B+6}mm;color:{C.INK};font-weight:800;font-size:3.6mm;direction:rtl;opacity:.75}}
</style></head><body>
<div class="wave"></div>
<div class="c logo"><svg viewBox="{C.vb}" style="height:{lh}mm;width:{lh*w0/h0:.1f}mm"><path fill-rule="evenodd" fill="#fff" d="{C.lpath}"/></svg></div>
<div class="c t1">SCAN &amp; SHOP</div>
<div class="c t2">امسح.. وتسوّق أونلاين</div>
<div class="c cats">BANDS · GOGGLES · SUNGLASSES · SOCKS</div>
<div class="c cats2">سيور · نظارات البر · نظارات شمسية · دلاغات</div>
<div class="c qrbox"><div class="f">{C.qr(WEB, 46)}</div></div>
<div class="c sc">974GROUP.NET</div>
<div class="c sc2">نوصلك لين باب البيت 🚚</div>
<div class="c sc3">WE DELIVER TO YOUR DOOR</div>
<div class="c ig">{C.ig_icon(6, C.M)} @974.group</div>
<div class="c web">FOLLOW US · تابعنا</div>
<div class="c ty">A QATARI BRAND · براند قطري</div>
</body></html>'''


def run():
    p = D + 'stand.html'; open(p, 'w').write(page())
    W, H = BW + 2 * B, BH + 2 * B
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{round(W*96/25.4)},height:{round(H*96/25.4)}}},deviceScaleFactor:3}});"
          f"await p.goto('file://{p}');await p.waitForTimeout(1200);"
          f"await p.pdf({{path:'{D}974-table-stand-A5-3mm-bleed.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});"
          f"await p.screenshot({{path:'{D}974-table-stand-preview.png'}});await b.close();}})()")
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    run(); print('ok')
