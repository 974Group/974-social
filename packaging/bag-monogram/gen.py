# 974 shopping bag — design 4 "Monogram" (white). Real size in mm, vector, text outlined → .ai (PDF-compatible) + .pdf
import json, re, subprocess, os, sys
sys.path.insert(0, '/home/claude/974-social/packaging/playing-cards')
from gen import logo, LOGO_RATIO, FONTS, T, igicon, globe, LOGO_D, P
FONTS += "@font-face{font-family:'Lexend Exa';font-weight:100 900;src:url(file:///home/claude/974-social/packaging/bag-monogram/LexendExa.ttf)}"
_n = [0]
def logo2(x, y, w, light='#720842', dark='#51022D'):
    # brand two-tone 974: tail of the 9, left notch of the 7, and the 4's upper body in the darker tone
    _n[0] += 1; i = _n[0]; sc = w / P['w']
    d9, d7, d4 = (' '.join(g) for g in P['d'])
    def L(d, c, clip=None): return f'<path d="{d}" fill="{c}" fill-rule="evenodd"' + (f' clip-path="url(#{clip}{i})"' if clip else '') + '/>'
    defs = (f'<clipPath id="a{i}"><rect x="0" y="640" width="1140" height="1100"/></clipPath>'
            f'<clipPath id="b{i}"><circle cx="563" cy="563" r="563"/></clipPath>'
            f'<clipPath id="c{i}"><polygon points="0,0 1631,0 967,1616 0,1616"/></clipPath>'
            f'<clipPath id="e{i}"><polygon points="2240,0 2865,0 2865,1261 1740,1261"/></clipPath>')
    return (f'<g transform="translate({x},{y}) scale({sc})"><defs>{defs}</defs>'
            + L(d9, light) + L(d9, dark, 'a') + L(d9, light, 'b')
            + L(d7, light) + L(d7, dark, 'c') + L(d4, light) + L(d4, dark, 'e') + '</g>')
D = os.path.dirname(os.path.abspath(__file__)) + '/'
BUR, DARK, GOLD, WM = '#720842', '#51022D', '#C9A24B', '#EFE7EB'

def brackets(x, y, w, h, inset, arm, c=GOLD, sw=2.2):
    s = ''
    for (cx, cy, dx, dy) in [(x+inset, y+inset, 1, 1), (x+w-inset, y+inset, -1, 1), (x+inset, y+h-inset, 1, -1), (x+w-inset, y+h-inset, -1, -1)]:
        s += f'<path d="M{cx},{cy+dy*arm} L{cx},{cy} L{cx+dx*arm},{cy}" fill="none" stroke="{c}" stroke-width="{sw}"/>'
    return s

def wa(x, y, s, c):  # simple WhatsApp-style glyph
    k = s*.1; cx, cy, r = x+s/2, y+s/2, s*.42
    return (f'<path d="M{cx-r*.75},{cy+r*.66} A{r},{r} 0 1 1 {cx-r*.35},{cy+r*.93} L{x+s*.04},{y+s*.98} Z" fill="none" stroke="{c}" stroke-width="{k}" stroke-linejoin="round"/>'
            f'<path d="M{cx-r*.38},{cy-r*.42} q{r*.05},{r*.6} {r*.75},{r*.85}" fill="none" stroke="{c}" stroke-width="{k*1.6}" stroke-linecap="round"/>')

W, H = 1900, 1300
Y = 92; PH = 1120; LG, FR, RG = 112, 452, 1492
s = [f'<rect width="{W}" height="{H}" fill="#F2F2F2"/>']
s.append(T(LG, 50, 'تصميم ٤ – فخم Monogram', 22, '#333', 700, 'Cairo', anchor='start'))

def gusset(x):
    g = f'<rect x="{x}" y="{Y}" width="300" height="{PH}" fill="#fff"/>'
    g += brackets(x, Y, 300, PH, 38, 50)
    lw = 102; g += logo2(x+150-lw/2, Y+87, lw)
    cx, cy = x+150, Y+622
    g += f'<g transform="rotate(-90 {cx} {cy})">' + T(cx, cy+5, '974GROUP.NET', 15, GOLD, 500, 'Lexend Exa', ls=6) + '</g>'
    return g
s.append(gusset(LG)); s.append(gusset(RG))

# front
f = [f'<defs><clipPath id="fc"><rect x="{FR}" y="{Y}" width="1000" height="{PH}"/></clipPath></defs>',
     f'<rect x="{FR}" y="{Y}" width="1000" height="{PH}" fill="#fff"/>',
     f'<g clip-path="url(#fc)">' + logo(FR+121, Y+659, 1199, WM) + '</g>']
f.append(brackets(FR, Y, 1000, PH, 55, 72))
cx = FR+500
lw = 204; f.append(logo2(cx-lw/2, Y+122, lw))
f.append(T(cx, Y+527, '974GROUP.NET', 29, BUR, 700, 'Lexend Exa', ls=11))
f.append(f'<line x1="{cx-29}" y1="{Y+559}" x2="{cx+29}" y2="{Y+559}" stroke="{GOLD}" stroke-width="2.4"/>')
f.append(T(cx, Y+601, 'DOHA · QATAR', 19, BUR, 500, 'Lexend Exa', ls=8))
vx, vy = FR+62, Y+560
f.append(f'<g transform="rotate(-90 {vx} {vy})">' + T(vx, vy+5, 'BANDS · GOGGLES · SOCKS &amp; MORE', 15, GOLD, 500, 'Lexend Exa', ls=7.5) + '</g>')
yc = Y+1013; fs = 16
f.append(wa(FR+188, yc-15, 19, BUR) + T(FR+214, yc, '+974 5555 6278', fs, BUR, 600, 'Lexend Exa', anchor='start', ls=1))
f.append(igicon(FR+432, yc-14.5, 18, BUR) + T(FR+458, yc, '974.Group', fs, BUR, 600, 'Lexend Exa', anchor='start', ls=1))
f.append(globe(FR+624, yc-15, 19, BUR) + T(FR+650, yc, '974group.net', fs, BUR, 600, 'Lexend Exa', anchor='start', ls=1))
s += f
s.append(T(LG, 1252, '300mm جنب', 17, '#444', 700, 'Cairo', anchor='start'))
s.append(T(RG, 1252, '300mm جنب', 17, '#444', 700, 'Cairo', anchor='start'))
s.append(T(FR, 1252, '1000mm x 1120mm الوجه – نفس التصميم على الوجه الثاني', 17, '#444', 700, 'Cairo', anchor='start'))

svg = ''.join(s)
os.makedirs(D+'out', exist_ok=True)
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
@page{{size:{W}mm {H}mm;margin:0}} html,body{{margin:0}} svg{{display:block;width:{W}mm;height:{H}mm}}</style></head>
<body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{svg}</svg></body></html>'''
open(D+'out/src.html', 'w').write(html)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{D}out/src.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.pdf({{path:'{D}out/fonts.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});await b.close();}})()"""
subprocess.run(['node', '-e', js], check=True)
# outline all text: PDF -> SVG (cairo turns glyphs into paths) -> PDF
subprocess.run(['pdftocairo', '-svg', D+'out/fonts.pdf', D+'out/outlined.svg'], check=True)
js2 = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.setContent('<html><head><style>@page{{size:{W}mm {H}mm;margin:0}}html,body{{margin:0}}img{{display:block;width:{W}mm;height:{H}mm}}</style></head><body></body></html>');
const svg=require('fs').readFileSync('{D}out/outlined.svg','utf8').replace(/<\\?xml[^>]*>/,'');
await p.evaluate(s=>{{document.body.innerHTML=s;const e=document.body.firstElementChild;e.style.display='block';e.style.width='{W}mm';e.style.height='{H}mm'}},svg);
await p.pdf({{path:'{D}out/974-bag-monogram-white.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});
await p.setViewportSize({{width:1900,height:1300}});await p.evaluate(()=>{{const e=document.body.firstElementChild;e.style.width='1900px';e.style.height='1300px'}});
await p.screenshot({{path:'{D}out/preview.png'}});await b.close();}})()"""
subprocess.run(['node', '-e', js2], check=True)
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
r = PdfReader(D+'out/974-bag-monogram-white.pdf'); w = PdfWriter(); pg = r.pages[0]; top = float(pg.mediabox.top); k = 72/25.4
box = RectangleObject([0, top-H*k, W*k, top]); pg.mediabox = box; pg.cropbox = box; pg.trimbox = box
w.add_page(pg); w.add_metadata({'/Title': '974 Bag — Monogram (white)', '/Creator': '974Group'})
w.write(D+'out/974-bag-monogram-white.pdf')
import shutil; shutil.copy(D+'out/974-bag-monogram-white.pdf', D+'out/974-bag-monogram-white.ai')
for x in ('fonts.pdf', 'outlined.svg', 'src.html'): os.remove(D+'out/'+x)
