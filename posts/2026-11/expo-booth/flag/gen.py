# Teardrop flag 60 x 240 cm (single-side print, mirror on the back; pole 350 cm, ~300 cm assembled). 22 Nov 2026.
# Bilingual (expo rule), no prices/discounts, "A QATARI BRAND" (never "Made in Qatar").
# Output: full-size vector PDF 600 x 2400 mm (images embedded) + a teardrop-shaped preview PNG.
# Safe area: pole sleeve on the left (~80 mm), curved top (~480 mm) and base area (~220 mm) kept clear of key content.
import subprocess, re, sys
sys.path.insert(0, '/home/claude/974-social/templates')
D = '/home/claude/974-social/posts/2026-11/expo-booth/flag/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R = '/home/claude/974-social/posts/2026-11/'
LOGO = open('/home/claude/974-social/posts/2026-11/expo-booth/backwall/logo-974.svg').read()
vb = re.search(r'viewBox="([^"]+)"', LOGO).group(1)
lpath = re.search(r'<path[^>]*d="([^"]+)"', LOGO).group(1)
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'
W, H = 600, 2400
# teardrop outline (mm): straight pole edge on the left, big curve over the top, tapering right edge
k = 96 / 25.4
TEAR = "path('" + ' '.join(t if t.isalpha() else f'{float(t)*k:.1f}' for t in f'M 0 {H} L 0 300 C 0 120 160 0 330 0 C 520 0 {W} 160 {W} 420 L {W} 1500 C {W} 1900 560 2200 470 {H} Z'.split()) + "')"
ITEMS = [
    (R + 'full-range/cut/w-sil.png', 'SMARTWATCH BANDS', 'سيور ساعات ذكية', 'WHOOP · GARMIN · FITBIT · APPLE WATCH', 185),
    (R + 'summer-goggles/cut/red.png', 'GOGGLES', 'نظارات البر', '', 300),
    (R + 'sunglasses/cut/lusail-hero.png', 'SUNGLASSES', 'نظارات شمسية', '', 285),
    (R + 'full-range/cut/sock-white.png', 'SOCKS', 'دلاغات', 'RUNNING · GRIP · PILATES', 115),
]


def page(clip):
    w0, h0 = map(float, vb.split()[2:])
    rows = ''
    for img, en, ar, sub, wmm in ITEMS:
        rows += f'''<div class="it"><img src="file://{img}" style="width:{wmm}mm">
<div class="en">{en}</div><div class="ar">{ar}</div>{f'<div class="sub">{sub}</div>' if sub else ''}</div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:{W}mm {H}mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{overflow:hidden;width:{W}mm;height:{H}mm;background:{'transparent' if clip else DK}}}
body{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;font-family:Cairo;color:#fff;
background:radial-gradient(ellipse 500mm 700mm at 55% 30%,#9A1460 0%,rgba(154,20,96,0) 70%),linear-gradient(180deg,{M} 0%,{DK} 100%);{f'clip-path:{TEAR};' if clip else ''}}}
.c{{position:absolute;left:90mm;right:45mm;text-align:center}}
.logo{{top:330mm}}
.tag{{top:540mm;font-family:Poppins;font-weight:700;font-size:22mm;letter-spacing:5mm;color:{GOLD}}}
.tagar{{top:570mm;font-weight:900;font-size:40mm;direction:rtl}}
.line{{top:658mm;height:3mm;background:{GOLD};left:200mm;right:155mm}}
.list{{top:700mm;display:flex;flex-direction:column;align-items:center;gap:30mm}}
.it{{display:flex;flex-direction:column;align-items:center}}
.it img{{filter:drop-shadow(0 8mm 10mm rgba(0,0,0,.45))}}
.it .en{{font-family:Poppins;font-weight:900;font-size:24mm;letter-spacing:2mm;margin-top:10mm;white-space:nowrap}}
.it .ar{{font-weight:900;font-size:34mm;direction:rtl;color:{GOLD};margin-top:-4mm}}
.it .sub{{font-family:Poppins;font-weight:700;font-size:12.5mm;letter-spacing:1mm;opacity:.8;margin-top:2mm;white-space:nowrap}}
.foot{{top:2120mm;font-family:Poppins;font-weight:900;font-size:30mm}}
.foot2{{top:2162mm;font-family:Poppins;font-weight:700;font-size:22mm;color:{GOLD}}}
</style></head><body>
<div class="c logo"><svg viewBox="{vb}" style="width:330mm;height:{330*h0/w0:.1f}mm"><path fill-rule="evenodd" fill="#fff" d="{lpath}"/></svg></div>
<div class="c tag">A QATARI BRAND</div>
<div class="c tagar">براند قطري</div>
<div class="c line"></div>
<div class="c list">{rows}</div>
<div class="c foot">@974.group</div>
<div class="c foot2">974group.net</div>
</body></html>'''


def run():
    for clip, name in [(False, 'print'), (True, 'preview')]:
        p = D + f'flag-{name}.html'; open(p, 'w').write(page(clip))
    pw, ph = round(W * 96 / 25.4), round(H * 96 / 25.4)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"let p=await b.newPage({{viewport:{{width:{pw},height:{ph}}}}});await p.goto('file://{D}flag-print.html');await p.waitForTimeout(1500);"
          f"await p.pdf({{path:'{D}974-teardrop-flag-600x2400mm.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});"
          f"p=await b.newPage({{viewport:{{width:{pw},height:{ph}}},deviceScaleFactor:1}});await p.goto('file://{D}flag-preview.html');await p.waitForTimeout(1500);"
          f"await p.screenshot({{path:'{D}flag-preview-raw.png',omitBackground:true}});await b.close();}})()")
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    run(); print('ok')
