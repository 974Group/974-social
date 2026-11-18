# Universal Fitbit Air FABRIC band box: tuck-end carton with a vertical window so the band colour shows.
# One design for every colour; colour is marked with a small sticker in the "COLOUR" box.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import FONTS
from playwright.sync_api import sync_playwright
LW = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
BAND = '/home/claude/974-social/products/fitbit-fabric-blush/src/'
W, D, H = 60, 22, 150          # box: width, depth, height (mm)
GL, TU, DU = 12, 12, 18        # glue flap, tuck tongue, dust flap height
WIN_W, WIN_H, WIN_T = 26, 94, 32   # window size and distance from top of front panel
M = 12                          # page margin
X_GLUE = M; X_BACK = X_GLUE + GL; X_S1 = X_BACK + W; X_FRONT = X_S1 + D; X_S2 = X_FRONT + W
Y_BODY = M + D + TU; Y_BOT = Y_BODY + H
PW = X_S2 + D + M; PH = Y_BOT + D + TU + M
GOLD = '#C9A24B'; BG = 'linear-gradient(170deg,#8A0C52 0%,#720842 45%,#51022D 100%)'

def panel(x, y, w, h, inner='', bg=BG, extra=''):
    return f'<div class="p" style="left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;background:{bg};{extra}">{inner}</div>'

def front(band=None):
    win = (f'<div class="win" style="left:{(W-WIN_W)/2}mm;top:{WIN_T}mm;width:{WIN_W}mm;height:{WIN_H}mm">'
           + (f'<img src="file://{band}" style="height:118%;position:absolute;left:50%;top:50%;transform:translate(-38%,-50%)">' if band else '<span>WINDOW<br>{0}×{1} mm</span>'.format(WIN_W, WIN_H))
           + '</div>')
    return f'''<img class="logo" src="file://{LW}" style="left:{(W-17)/2}mm;top:8mm;width:17mm">
<div class="tag" style="top:23mm">FOR GOOGLE FITBIT AIR</div>
{win}
<div class="ttl" style="top:{WIN_T+WIN_H+5}mm">FABRIC BAND</div>
<div class="ar" style="top:{WIN_T+WIN_H+11}mm">سير فابريك · يتسكر باللزقة</div>
<div class="col" style="top:{WIN_T+WIN_H+17}mm"><span>COLOUR</span><i></i></div>'''

def back():
    return f'''<img class="logo" src="file://{LW}" style="left:{(W-18)/2}mm;top:8mm;width:18mm">
<div class="ar big" style="top:20mm">سير فابريك لـ<br><b class="en">Google Fitbit Air</b></div>
<div class="list ar" style="top:38mm">✓ خفيف ويتنفس<br>✓ يتسكر باللزقة<br>✓ يتعدّل على مقاسك<br>✓ مريح وقت النوم</div>
<div class="list en" style="top:66mm">✓ Lightweight &amp; breathable<br>✓ Hook-and-loop closure<br>✓ Adjustable fit<br>✓ Comfortable for sleep</div>
<div class="note" style="top:92mm">سير فقط · الجهاز غير مشمول<br><span class="en">Band only · device not included</span></div>
<div class="bar" style="top:106mm"><span>BARCODE</span></div>
<div class="web" style="top:134mm"><b>974group.net</b> · @974.group</div>'''

def side(label):
    return f'<div class="side"><img src="file://{LW}" style="width:12mm"><span>{label}</span></div>'

def lines():
    cut, fold = '#E3001B', '#0077CC'
    L = []
    def c(x1, y1, x2, y2): L.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cut}" stroke-width="0.25"/>')
    def f(x1, y1, x2, y2): L.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{fold}" stroke-width="0.25" stroke-dasharray="2 1.2"/>')
    # body outline pieces
    c(X_GLUE, Y_BODY+3, X_GLUE, Y_BOT-3); c(X_GLUE, Y_BODY+3, X_BACK, Y_BODY); c(X_GLUE, Y_BOT-3, X_BACK, Y_BOT)
    for x in (X_BACK, X_S1, X_FRONT, X_S2): f(x, Y_BODY, x, Y_BOT)
    c(X_S2+D, Y_BODY, X_S2+D, Y_BOT)
    # top: lid + tongue on front, dust flaps on sides
    f(X_FRONT, Y_BODY, X_S2, Y_BODY); c(X_FRONT, Y_BODY, X_FRONT, Y_BODY-D); c(X_S2, Y_BODY, X_S2, Y_BODY-D)
    f(X_FRONT, Y_BODY-D, X_S2, Y_BODY-D)
    L.append(f'<path d="M{X_FRONT},{Y_BODY-D} L{X_FRONT+3},{Y_BODY-D-TU} L{X_S2-3},{Y_BODY-D-TU} L{X_S2},{Y_BODY-D}" fill="none" stroke="{cut}" stroke-width="0.25"/>')
    for xs in (X_S1, X_S2):
        f(xs, Y_BODY, xs+D, Y_BODY)
        L.append(f'<path d="M{xs},{Y_BODY} L{xs+2},{Y_BODY-DU} L{xs+D-6},{Y_BODY-DU} L{xs+D},{Y_BODY-4} L{xs+D},{Y_BODY}" fill="none" stroke="{cut}" stroke-width="0.25"/>')
    c(X_BACK, Y_BODY, X_S1, Y_BODY)
    # bottom: lid + tongue on back, dust flaps on sides
    f(X_BACK, Y_BOT, X_S1, Y_BOT); c(X_BACK, Y_BOT, X_BACK, Y_BOT+D); c(X_S1, Y_BOT, X_S1, Y_BOT+D); f(X_BACK, Y_BOT+D, X_S1, Y_BOT+D)
    L.append(f'<path d="M{X_BACK},{Y_BOT+D} L{X_BACK+3},{Y_BOT+D+TU} L{X_S1-3},{Y_BOT+D+TU} L{X_S1},{Y_BOT+D}" fill="none" stroke="{cut}" stroke-width="0.25"/>')
    for xs in (X_S1, X_S2):
        f(xs, Y_BOT, xs+D, Y_BOT)
        L.append(f'<path d="M{xs},{Y_BOT} L{xs+2},{Y_BOT+DU} L{xs+D-6},{Y_BOT+DU} L{xs+D},{Y_BOT+4} L{xs+D},{Y_BOT}" fill="none" stroke="{cut}" stroke-width="0.25"/>')
    c(X_FRONT, Y_BOT, X_S2, Y_BOT)
    # window
    wx = X_FRONT + (W-WIN_W)/2; wy = Y_BODY + WIN_T
    L.append(f'<rect x="{wx}" y="{wy}" width="{WIN_W}" height="{WIN_H}" rx="4" fill="none" stroke="{cut}" stroke-width="0.25"/>')
    return f'<svg class="lines" width="{PW}mm" height="{PH}mm" viewBox="0 0 {PW} {PH}">{"".join(L)}</svg>'

CSS = f'''{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{PW}mm;height:{PH}mm;position:relative;background:#fff;font-family:Cairo}}
.p{{position:absolute;overflow:hidden;color:#fff}}
.p > *{{position:absolute}}
.logo{{filter:none}}
.tag,.ttl,.ar,.col,.list,.note,.web,.bar,.big{{left:0;right:0;text-align:center}}
.tag{{font-family:Poppins;font-weight:600;font-size:2.4mm;letter-spacing:.6mm;color:{GOLD}}}
.ttl{{font-family:Poppins;font-weight:700;font-size:4.6mm;letter-spacing:.9mm}}
.ar{{direction:rtl;font-weight:700;font-size:3mm}}
.big{{font-size:3.6mm;line-height:1.35}} .big b{{font-family:Poppins;color:{GOLD}}}
.col{{display:flex;justify-content:center;align-items:center;gap:1.5mm}} .col span{{font-family:Poppins;font-weight:600;font-size:2.2mm;letter-spacing:.5mm;color:{GOLD}}}
.col i{{display:block;width:16mm;height:5mm;border:.3mm solid {GOLD};border-radius:2.5mm}}
.win{{position:absolute;border-radius:4mm;overflow:hidden;background:#F4F1F2;display:flex;align-items:center;justify-content:center;outline:.5mm solid {GOLD};outline-offset:1.2mm}}
.win span{{color:#999;font-family:Poppins;font-size:2.4mm;text-align:center}}
.list{{font-size:2.9mm;line-height:1.55}} .list.en{{font-family:Poppins;font-size:2.4mm}} .list.ar{{direction:rtl}}
.note{{direction:rtl;font-size:2.4mm;opacity:.8;line-height:1.4}} .note .en{{font-family:Poppins;font-size:2.1mm}}
.bar{{left:10mm;right:10mm;height:22mm;background:#fff;border-radius:1.5mm;display:flex;align-items:center;justify-content:center}} .bar span{{color:#bbb;font-family:Poppins;font-size:2.2mm;letter-spacing:.5mm}}
.web{{font-family:Poppins;font-size:2.4mm}} .web b{{color:{GOLD}}}
.side{{left:0;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6mm}}
.side span{{writing-mode:vertical-rl;font-family:Poppins;font-weight:700;font-size:3.2mm;letter-spacing:1.2mm}}
.lines{{position:absolute;left:0;top:0;pointer-events:none}}
.legend{{position:absolute;left:{M}mm;bottom:3mm;font-family:Poppins;font-size:2.4mm;color:#333}}'''

def dieline():
    body = ''
    body += panel(X_BACK, Y_BODY, W, H, back())
    body += panel(X_S1, Y_BODY, D, H, side('FABRIC BAND'))
    body += panel(X_FRONT, Y_BODY, W, H, front())
    body += panel(X_S2, Y_BODY, D, H, side('974 GROUP'))
    body += panel(X_GLUE, Y_BODY, GL, H, bg='#f2f2f2')
    body += panel(X_FRONT, Y_BODY-D, W, D, bg=BG)                      # top lid
    body += panel(X_FRONT+3, Y_BODY-D-TU, W-6, TU, bg=BG)              # top tongue
    body += panel(X_BACK, Y_BOT, W, D, bg=BG); body += panel(X_BACK+3, Y_BOT+D, W-6, TU, bg=BG)
    for xs in (X_S1, X_S2):
        body += panel(xs, Y_BODY-DU, D, DU, bg=BG); body += panel(xs, Y_BOT, D, DU, bg=BG)
    legend = f'<div class="legend">974Group · Fitbit Air FABRIC band box · {W}×{D}×{H} mm (W×D×H) · window {WIN_W}×{WIN_H} mm with clear PET film · <span style="color:#E3001B">— cut</span> · <span style="color:#0077CC">- - fold</span></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}{lines()}{legend}</body></html>'

def mockup(colors):
    # flat front panels at 7 px/mm, one per colour, to show the same box works for every colour
    cards = ''.join(f'<div class="card">{panel(0,0,W,H,front(BAND+c+"-cut.png"))}</div>' for c in colors)
    css = CSS + f'''body{{width:{len(colors)*W+ (len(colors)+1)*10}mm;height:{H+20}mm;background:#EFE9E4;display:flex;gap:10mm;padding:10mm}}
.card{{position:relative;width:{W}mm;height:{H}mm;box-shadow:0 3mm 6mm rgba(0,0,0,.25)}}'''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{cards}</body></html>'

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    html = dieline(); open('dieline.html', 'w').write(html)
    pg.goto('file:///home/claude/974-social/packaging/fitbit-fabric/dieline.html'); pg.wait_for_timeout(500)
    pg.pdf(path='974-fitbit-fabric-box-dieline.pdf', width=f'{PW}mm', height=f'{PH}mm', print_background=True)
    pg2 = b.new_page(device_scale_factor=2, viewport={'width': int(PW*3.78), 'height': int(PH*3.78)})
    pg2.goto('file:///home/claude/974-social/packaging/fitbit-fabric/dieline.html'); pg2.wait_for_timeout(500)
    pg2.screenshot(path='974-fitbit-fabric-box-dieline.png', full_page=True)
    cols = ['grey', 'blush', 'fog', 'olive']
    open('mockup.html', 'w').write(mockup(cols))
    n = len(cols)
    pg3 = b.new_page(device_scale_factor=2, viewport={'width': int((n*W+(n+1)*10)*3.78), 'height': int((H+20)*3.78)})
    pg3.goto('file:///home/claude/974-social/packaging/fitbit-fabric/mockup.html'); pg3.wait_for_timeout(500)
    pg3.screenshot(path='974-fitbit-fabric-box-mockup.png', full_page=True)
    b.close()
print(PW, PH)
