# 974 playing cards — card back (63x88 mm poker) + reverse-tuck box. Vector PDF output (opens editable in Illustrator).
import json, re, subprocess, os
from reportlab.graphics.barcode.qrencoder import QRCode, QRErrorCorrectLevel
D = os.path.dirname(os.path.abspath(__file__)) + '/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
BUR, DARK, CREAM, GOLD, GOLD2 = '#720842', '#51022D', '#F4F1F2', '#C9A24B', '#E3C67E'

# ---- 974 mark (vector paths from reels/brand/src/logo.html) ----
src = open('/home/claude/974-social/reels/brand/src/logo.html').read()
P = json.loads(re.search(r'const PATHS=(\{.*?\});', src).group(1))
LOGO_D = ' '.join(' '.join(x) for x in P['d'])
def logo(x, y, w, fill=GOLD):  # top-left x,y in mm, width w mm
    s = w / P['w']
    return f'<path transform="translate({x},{y}) scale({s})" d="{LOGO_D}" fill="{fill}" fill-rule="evenodd"/>'
LOGO_RATIO = P['h'] / P['w']

# ---- QR (vector modules) ----
def qr(x, y, size, data='https://974group.net', fg=DARK):
    q = QRCode(None, QRErrorCorrectLevel.Q); q.addData(data); q.make()
    n = q.getModuleCount(); m = size / n
    d = ''.join(f'M{x+c*m:.3f},{y+r*m:.3f}h{m:.3f}v{m:.3f}h-{m:.3f}z' for r in range(n) for c in range(n) if q.isDark(r, c))
    return f'<path d="{d}" fill="{fg}" shape-rendering="crispEdges"/>'

# ---- Qatar serration (9 points) ----
def serr(x, y, w, h, n=9, fill=CREAM, side='left'):
    """vertical serrated band: solid strip of width w with n triangular teeth of depth h pointing right"""
    step = 1.0 * (h) / n
    pts = [f'{x},{y}']
    for i in range(n):
        pts += [f'{x+w},{y+i*step}', f'{x+w+step*0.9},{y+(i+.5)*step}']
    pts += [f'{x+w},{y+h}', f'{x},{y+h}']
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'

def igicon(x, y, s, c):
    r = s * .28
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r}" fill="none" stroke="{c}" stroke-width="{s*.1}"/>'
            f'<circle cx="{x+s/2}" cy="{y+s/2}" r="{s*.23}" fill="none" stroke="{c}" stroke-width="{s*.1}"/>'
            f'<circle cx="{x+s*.76}" cy="{y+s*.24}" r="{s*.065}" fill="{c}"/>')
def globe(x, y, s, c):
    k = s * .09; cx, cy, r = x+s/2, y+s/2, s*.45
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="{k}"/>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{r*.45}" ry="{r}" fill="none" stroke="{c}" stroke-width="{k}"/>'
            f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{c}" stroke-width="{k}"/>')

FONTS = f'''@font-face{{font-family:Cairo;font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:Cairo;font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:Poppins;font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:Poppins;font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:Poppins;font-weight:300;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf)}}'''
def T(x, y, txt, size, fill=GOLD, w=700, fam='Poppins', anchor='middle', ls=0, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{txt}</text>'

def page(name, W, H, svg):
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
@page{{size:{W}mm {H}mm;margin:0}} html,body{{margin:0;padding:0}} svg{{display:block;width:{W}mm;height:{H}mm}}</style></head>
<body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{svg}</svg></body></html>'''
    os.makedirs(D + 'out', exist_ok=True); open(D + f'out/{name}.html', 'w').write(html)
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{D}out/{name}.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.pdf({{path:'{D}out/{name}.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});
await p.setViewportSize({{width:Math.round({W}*11.811),height:Math.round({H}*11.811)}});
await p.addStyleTag({{content:'svg{{width:100vw!important;height:100vh!important}}'}});
await p.screenshot({{path:'{D}out/{name}-preview.png'}});await b.close();}})()"""
    subprocess.run(['node', '-e', js], check=True)
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    r = PdfReader(D+f'out/{name}.pdf'); w = PdfWriter(); pg = r.pages[0]; top = float(pg.mediabox.top)
    k = 72/25.4; box = RectangleObject([0, top-H*k, W*k, top])
    pg.mediabox = box; pg.cropbox = box; pg.bleedbox = box
    pg.trimbox = RectangleObject([3*k, top-H*k+3*k, (W-3)*k, top-3*k])
    w.add_page(pg); w.write(D+f'out/{name}.pdf')

# ================= CARD BACK =================
def card_back():
    B = 3; TW, TH = 63, 88; W, H = TW+2*B, TH+2*B
    s = [f'<defs><pattern id="lat" width="4.2" height="4.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<path d="M0,0H4.2M0,0V4.2" stroke="{DARK}" stroke-width=".35"/></pattern>'
         f'<radialGradient id="glow" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#8a1252"/><stop offset="1" stop-color="{BUR}"/></radialGradient></defs>',
         f'<rect width="{W}" height="{H}" fill="url(#glow)"/>',
         f'<rect width="{W}" height="{H}" fill="url(#lat)" opacity=".55"/>']
    # frames (safe area 4 mm inside trim)
    fx, fy = B+3.6, B+3.6; fw, fh = TW-7.2, TH-7.2
    s.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="2.2" fill="none" stroke="{GOLD}" stroke-width=".45"/>')
    s.append(f'<rect x="{fx+1.3}" y="{fy+1.3}" width="{fw-2.6}" height="{fh-2.6}" rx="1.4" fill="none" stroke="{GOLD}" stroke-width=".18" opacity=".8"/>')
    # serrated bands top & bottom (180° symmetric) — 9 points, like the flag
    cx = W/2; bw = fw-2.6-4; n = 9; st = bw/n; yT = fy+5.2
    def teeth(y, down):
        pts = []
        for i in range(n+1):
            pts.append(f'{cx-bw/2+i*st},{y}')
            if i < n: pts.append(f'{cx-bw/2+(i+.5)*st},{y+(2.4 if down else -2.4)}')
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GOLD}" stroke-width=".35" stroke-linejoin="miter"/>'
    s += [teeth(yT, True), teeth(H-yT, False)]
    # tiny 974group.net top + rotated bottom
    s.append(T(cx, yT-1.6, '974GROUP.NET', 1.9, GOLD, 500, ls=.55))
    s.append(f'<g transform="rotate(180 {cx} {H/2})">{T(cx, yT-1.6, "974GROUP.NET", 1.9, GOLD, 500, ls=.55)}</g>')
    # centre medallion
    cy = H/2; R = 15.5
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R+1.6}" fill="none" stroke="{GOLD}" stroke-width=".2" opacity=".7"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{DARK}" stroke="{GOLD}" stroke-width=".5"/>')
    # 9-point star ring around medallion
    import math
    ring = []
    for i in range(36):
        a = i*math.pi*2/36; r = R+3.4 if i % 2 == 0 else R+2.2
        ring.append(f'{cx+r*math.cos(a):.3f},{cy+r*math.sin(a):.3f}')
    s.append(f'<polygon points="{" ".join(ring)}" fill="none" stroke="{GOLD}" stroke-width=".22" opacity=".85"/>')
    lw = 21; s.append(logo(cx-lw/2, cy-lw*LOGO_RATIO/2, lw))
    # corner diamonds
    for (x, y) in [(fx+3.2, fy+3.2), (fx+fw-3.2, fy+3.2), (fx+3.2, fy+fh-3.2), (fx+fw-3.2, fy+fh-3.2)]:
        s.append(f'<rect x="{x-.9}" y="{y-.9}" width="1.8" height="1.8" transform="rotate(45 {x} {y})" fill="{GOLD}"/>')
    page('974-card-back-63x88-bleed3', W, H, ''.join(s))
    # guide version (trim + safe lines) for the printer
    g = ''.join(s) + (f'<rect x="{B}" y="{B}" width="{TW}" height="{TH}" rx="3" fill="none" stroke="#00E5FF" stroke-width=".25"/>'
                      f'<rect x="{B+3}" y="{B+3}" width="{TW-6}" height="{TH-6}" rx="1" fill="none" stroke="#FF00AA" stroke-width=".2" stroke-dasharray="1 .8"/>')
    page('974-card-back-GUIDES', W, H, g)

# ================= TUCK BOX =================
def box():
    B = 3; Wd, Ht, Dp = 64.5, 89.5, 21  # inner panel width, height, depth (fits 54-card deck ~19 mm)
    tuck, glue = 14, 10
    # columns: glue | back | side | front | side
    X0 = B; xg = X0; xb = xg+glue; xs1 = xb+Wd; xf = xs1+Dp; xs2 = xf+Wd; xe = xs2+Dp
    Y0 = B + tuck + Dp; yb = Y0+Ht      # main panel top/bottom
    W = xe + B; H = yb + Dp + tuck + B
    s = [f'<defs><pattern id="lat" width="4.2" height="4.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<path d="M0,0H4.2M0,0V4.2" stroke="{DARK}" stroke-width=".35"/></pattern></defs>']
    # background flood on the whole sheet (bleed beyond the die)
    s.append(f'<rect width="{W}" height="{H}" fill="{BUR}"/><rect width="{W}" height="{H}" fill="url(#lat)" opacity=".45"/>')

    # ---- FRONT ----
    cx = xf+Wd/2
    s.append(f'<rect x="{xf+5}" y="{Y0+5}" width="{Wd-10}" height="{Ht-10}" rx="2.4" fill="none" stroke="{GOLD}" stroke-width=".45"/>')
    s.append(f'<rect x="{xf+6.3}" y="{Y0+6.3}" width="{Wd-12.6}" height="{Ht-12.6}" rx="1.6" fill="none" stroke="{GOLD}" stroke-width=".18" opacity=".8"/>')
    lw = 38; ly = Y0+24
    s.append(logo(cx-lw/2, ly, lw))
    s.append(T(cx, ly+lw*LOGO_RATIO+9, 'PLAYING CARDS', 4.1, CREAM, 500, ls=1.6))
    # serrated divider (9 points)
    n = 9; bw = 34; st = bw/n; yy = ly+lw*LOGO_RATIO+14.5
    pts = []
    for i in range(n+1):
        pts.append(f'{cx-bw/2+i*st},{yy}')
        if i < n: pts.append(f'{cx-bw/2+(i+.5)*st},{yy+2.2}')
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GOLD}" stroke-width=".4"/>')
    s.append(T(cx, yy+9.5, 'لعبة الورق.. بهوية قطرية', 3.5, GOLD2, 700, 'Cairo', extra='direction="rtl"'))
    s.append(T(cx, Y0+Ht-10.5, '52 CARDS · 2 JOKERS', 2.2, GOLD, 500, ls=.8))

    # ---- BACK (Instagram + site + QR) ----
    cb = xb+Wd/2
    s.append(f'<rect x="{xb}" y="{Y0}" width="{Wd}" height="{Ht}" fill="{DARK}"/>')
    s.append(f'<rect x="{xb+5}" y="{Y0+5}" width="{Wd-10}" height="{Ht-10}" rx="2.4" fill="none" stroke="{GOLD}" stroke-width=".3" opacity=".7"/>')
    s.append(logo(cb-8, Y0+9.5, 16))
    s.append(T(cb, Y0+25.5, 'امسح الكود.. وتسوّق', 4.1, CREAM, 800, 'Cairo', extra='direction="rtl"'))
    qs = 27; qx, qy = cb-qs/2, Y0+31
    s.append(f'<rect x="{qx-3}" y="{qy-3}" width="{qs+6}" height="{qs+6}" rx="3" fill="{CREAM}"/>')
    s.append(qr(qx, qy, qs))
    # contact lines
    y1 = qy+qs+10.5
    s.append(igicon(cb-20.5, y1-3.6, 4.4, GOLD) + T(cb-14, y1, '@974.group', 3.6, CREAM, 500, anchor='start'))
    s.append(globe(cb-20.5, y1+4.2, 4.4, GOLD) + T(cb-14, y1+7.8, '974group.net', 3.6, CREAM, 500, anchor='start'))
    s.append(T(cb, Y0+Ht-7.6, 'MADE FOR QATAR · 974', 1.9, GOLD, 500, ls=.7))

    # ---- SIDES ----
    for xs in (xs1, xs2):
        c = xs+Dp/2; m = Y0+Ht/2
        s.append(f'<g transform="rotate(-90 {c} {m})">'
                 + logo(c-26, m-4.2, 15) + T(c+12, m+1.6, '@974.group', 3.4, CREAM, 500)
                 + '</g>')
        s.append(f'<line x1="{c}" y1="{Y0+6}" x2="{c}" y2="{Y0+14}" stroke="{GOLD}" stroke-width=".3"/>'
                 f'<line x1="{c}" y1="{yb-14}" x2="{c}" y2="{yb-6}" stroke="{GOLD}" stroke-width=".3"/>')
    # ---- TOP lid (on back) + BOTTOM lid (on front) ----
    s.append(logo(xb+Wd/2-7, B+tuck+Dp/2-7*LOGO_RATIO/2, 14))
    s.append(T(xf+Wd/2, yb+Dp/2+1.3, '974group.net', 3.4, GOLD, 500))
    page('974-card-box-artwork-bleed3', W, H, ''.join(s))

    # ---- dieline (cut = red solid, fold = blue dashed) ----
    cut, fold = '#FF0000', '#0070FF'
    def L(x1, y1, x2, y2, c, dash=False):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width=".3"{" stroke-dasharray=\"2 1.2\"" if dash else ""}/>'
    die = []
    # main panel outline pieces
    die += [L(xg, Y0+4, xb, Y0, cut), L(xg, yb-4, xb, yb, cut), L(xg, Y0+4, xg, yb-4, cut)]  # glue flap (tapered)
    die += [L(xb, Y0, xb, yb, fold), L(xs1, Y0, xs1, yb, fold), L(xf, Y0, xf, yb, fold), L(xs2, Y0, xs2, yb, fold), L(xe, Y0, xe, yb, cut)]
    # top: lid + tuck on BACK panel
    yl = Y0-Dp; yt = yl-tuck
    die += [L(xb, Y0, xs1, Y0, fold), L(xb, yl, xs1, yl, fold), L(xb, Y0, xb, yl, cut), L(xs1, Y0, xs1, yl, cut)]
    die.append(f'<path d="M{xb},{yl} L{xb+2},{yt+4} Q{xb+3},{yt} {xb+8},{yt} L{xs1-8},{yt} Q{xs1-3},{yt} {xs1-2},{yt+4} L{xs1},{yl}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    # bottom: lid + tuck on FRONT panel
    yl2 = yb+Dp; yt2 = yl2+tuck
    die += [L(xf, yb, xs2, yb, fold), L(xf, yl2, xs2, yl2, fold), L(xf, yb, xf, yl2, cut), L(xs2, yb, xs2, yl2, cut)]
    die.append(f'<path d="M{xf},{yl2} L{xf+2},{yt2-4} Q{xf+3},{yt2} {xf+8},{yt2} L{xs2-8},{yt2} Q{xs2-3},{yt2} {xs2-2},{yt2-4} L{xs2},{yl2}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    # front top edge & back bottom edge = cut ; dust flaps on sides (top & bottom)
    die += [L(xf, Y0, xs2, Y0, cut), L(xb, yb, xs1, yb, cut)]
    for xs in (xs1, xs2):
        die += [L(xs, Y0, xs+Dp, Y0, fold), L(xs, yb, xs+Dp, yb, fold)]
        fh = Dp*0.85
        die.append(f'<path d="M{xs},{Y0} L{xs+1},{Y0-fh+3} Q{xs+1.5},{Y0-fh} {xs+5},{Y0-fh} L{xs+Dp-2},{Y0-fh+4} L{xs+Dp},{Y0}" fill="none" stroke="{cut}" stroke-width=".3"/>')
        die.append(f'<path d="M{xs},{yb} L{xs+1},{yb+fh-3} Q{xs+1.5},{yb+fh} {xs+5},{yb+fh} L{xs+Dp-2},{yb+fh-4} L{xs+Dp},{yb}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    legend = (T(B+1, H-1.2, 'CUT ──  red    FOLD - - blue    BLEED 3 mm    deck 63×88 mm · box inner 64.5×89.5×21 mm', 2, '#ffffff', 500, anchor='start'))
    page('974-card-box-DIELINE', W, H, ''.join(s) + f'<rect width="{W}" height="{H}" fill="#fff" opacity=".35"/>' + ''.join(die) + legend)
    page('974-card-box-dieline-only', W, H, f'<rect width="{W}" height="{H}" fill="#fff"/>' + ''.join(die))

card_back(); box()
