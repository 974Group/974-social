# v2 — white-dominant: white stock, burgundy Qatar serration bands, burgundy 974 mark, gold accents only.
from gen import *
import math
WH = '#FFFFFF'

def hteeth(x0, x1, y, n, depth, down=True):
    """points of a 9-tooth serrated edge along y, from x0 to x1, teeth pointing down/up"""
    st = (x1-x0)/n; pts = []
    for i in range(n+1):
        pts.append((x0+i*st, y))
        if i < n: pts.append((x0+(i+.5)*st, y+(depth if down else -depth)))
    return pts
def vteeth(y0, y1, x, n, depth, right=True):
    st = (y1-y0)/n; pts = []
    for i in range(n+1):
        pts.append((x, y0+i*st))
        if i < n: pts.append((x+(depth if right else -depth), y0+(i+.5)*st))
    return pts
def poly(pts, fill, extra=''):
    return f'<polygon points="{" ".join(f"{a:.3f},{b:.3f}" for a,b in pts)}" fill="{fill}" {extra}/>'
def pline(pts, stroke, w=.3):
    return f'<polyline points="{" ".join(f"{a:.3f},{b:.3f}" for a,b in pts)}" fill="none" stroke="{stroke}" stroke-width="{w}"/>'

SUITS = {  # simple vector suits, unit box 0..10
 'spade': 'M5,0 C7,3 10,4.5 10,6.8 C10,8.6 8,9.4 6.2,8.2 L7,10 L3,10 L3.8,8.2 C2,9.4 0,8.6 0,6.8 C0,4.5 3,3 5,0Z',
 'heart': 'M5,10 C3,7.6 0,5.6 0,3 C0,1.2 1.4,0 3,0 C4,0 4.7,.6 5,1.4 C5.3,.6 6,0 7,0 C8.6,0 10,1.2 10,3 C10,5.6 7,7.6 5,10Z',
 'diamond': 'M5,0 L9,5 L5,10 L1,5Z',
 'club': 'M5,0 A2.4,2.4 0 1 1 4.99,0Z M5,0 C6.4,0 7.4,1 7.4,2.4 C7.4,3.4 6.8,4.2 6,4.6 C7,4 10,4 10,6.6 C10,8.2 8.6,9 7.2,8.8 C6.4,8.7 5.9,8.2 5.6,7.8 L6.6,10 L3.4,10 L4.4,7.8 C4.1,8.2 3.6,8.7 2.8,8.8 C1.4,9 0,8.2 0,6.6 C0,4 3,4 4,4.6 C3.2,4.2 2.6,3.4 2.6,2.4 C2.6,1 3.6,0 5,0Z'}
def suit(k, cx, cy, s, fill):
    return f'<path transform="translate({cx-s/2},{cy-s/2}) scale({s/10})" d="{SUITS[k]}" fill="{fill}"/>'

# ================= CARD BACK v2 =================
def card_back2():
    B = 3; TW, TH = 63, 88; W, H = TW+2*B, TH+2*B; cx, cy = W/2, H/2
    band = B+9.5; depth = 4.2; n = 9
    s = [f'<rect width="{W}" height="{H}" fill="{WH}"/>']
    top = [(0, 0), (W, 0), (W, band)] + [p for p in reversed(hteeth(B, W-B, band, n, depth))][0:] + [(0, band)]
    # build top band: full-bleed rect down to band, then teeth across the trim width
    t = hteeth(B, W-B, band, n, depth)
    topband = [(0, 0), (W, 0), (W, band)] + list(reversed(t)) + [(0, band)]
    s.append(poly(topband, BUR))
    s.append(pline([(a, b+1.6) for a, b in t], GOLD, .28))
    s.append(T(cx, B+5.6, '974GROUP.NET', 2.1, WH, 500, ls=.7))
    bot = f'<g transform="rotate(180 {cx} {cy})">' + poly(topband, BUR) + pline([(a, b+1.6) for a, b in t], GOLD, .28) + T(cx, B+5.6, '974GROUP.NET', 2.1, WH, 500, ls=.7) + '</g>'
    s.append(bot)
    # centre: mark + 4 suits (180° symmetric arrangement)
    lw = 34; s.append(logo(cx-lw/2, cy-lw*LOGO_RATIO/2, lw, BUR))
    dy = 15.5; ds = 3.6
    s.append(f'<line x1="{cx-16}" y1="{cy-dy}" x2="{cx-5}" y2="{cy-dy}" stroke="{GOLD}" stroke-width=".25"/><line x1="{cx+5}" y1="{cy-dy}" x2="{cx+16}" y2="{cy-dy}" stroke="{GOLD}" stroke-width=".25"/>')
    s.append(suit('spade', cx-2.3, cy-dy, ds, BUR) + suit('heart', cx+2.3, cy-dy, ds, GOLD))
    s.append(f'<g transform="rotate(180 {cx} {cy})"><line x1="{cx-16}" y1="{cy-dy}" x2="{cx-5}" y2="{cy-dy}" stroke="{GOLD}" stroke-width=".25"/><line x1="{cx+5}" y1="{cy-dy}" x2="{cx+16}" y2="{cy-dy}" stroke="{GOLD}" stroke-width=".25"/>'
             + suit('diamond', cx-2.3, cy-dy, ds, GOLD) + suit('club', cx+2.3, cy-dy, ds, BUR) + '</g>')
    page('974-card-back-v2-63x88-bleed3', W, H, ''.join(s))
    g = ''.join(s) + (f'<rect x="{B}" y="{B}" width="{TW}" height="{TH}" rx="3" fill="none" stroke="#00E5FF" stroke-width=".25"/>'
                      f'<rect x="{B+3}" y="{B+3}" width="{TW-6}" height="{TH-6}" rx="1" fill="none" stroke="#FF00AA" stroke-width=".2" stroke-dasharray="1 .8"/>')
    page('974-card-back-v2-GUIDES', W, H, g)

# ================= TUCK BOX v2 =================
def box2():
    B = 3; Wd, Ht, Dp = 64.5, 89.5, 21; tuck, glue = 14, 10
    xg = B; xb = xg+glue; xs1 = xb+Wd; xf = xs1+Dp; xs2 = xf+Wd; xe = xs2+Dp
    Y0 = B+tuck+Dp; yb = Y0+Ht; W = xe+B; H = yb+Dp+tuck+B
    bw, depth, n = 9, 4.4, 9   # serration band width on back/front next to the spine
    s = [f'<rect width="{W}" height="{H}" fill="{WH}"/>']
    # burgundy spine: side1 + teeth onto back (pointing left) and front (pointing right)
    lt = vteeth(Y0, yb, xs1-bw, n, depth, right=False); rt = vteeth(Y0, yb, xf+bw, n, depth, right=True)
    s.append(f'<rect x="{xs1}" y="{Y0-Dp}" width="{Dp}" height="{Ht+2*Dp}" fill="{BUR}"/>')
    s.append(poly([(xs1, Y0)] + lt + [(xs1, yb)], BUR) + poly([(xf, Y0)] + rt + [(xf, yb)], BUR))
    s.append(pline([(a+1.5, b) for a, b in rt], GOLD, .28) + pline([(a-1.5, b) for a, b in lt], GOLD, .28))
    # side 2 solid burgundy (incl. dust flaps + bleed)
    s.append(f'<rect x="{xs2}" y="{Y0-Dp}" width="{W-xs2}" height="{Ht+2*Dp}" fill="{BUR}"/>')
    # ---- FRONT ----
    fx0 = xf+bw+depth; cx = fx0+(xs2-fx0)/2
    lw = 34; ly = Y0+20
    s.append(logo(cx-lw/2, ly, lw, BUR))
    y = ly+lw*LOGO_RATIO
    s.append(T(cx, y+8.5, 'PLAYING CARDS', 3.5, BUR, 500, ls=1.3))
    s.append(f'<line x1="{cx-10}" y1="{y+13}" x2="{cx-3}" y2="{y+13}" stroke="{GOLD}" stroke-width=".3"/><line x1="{cx+3}" y1="{y+13}" x2="{cx+10}" y2="{y+13}" stroke="{GOLD}" stroke-width=".3"/>')
    s.append(suit('diamond', cx, y+13, 2.6, GOLD))
    s.append(T(cx, y+21, 'لعبة الورق.. بهوية قطرية', 3.6, BUR, 800, 'Cairo', extra='direction="rtl"'))
    s.append(T(cx, yb-8, '52 CARDS · 2 JOKERS', 2.1, GOLD, 500, ls=.7))
    # ---- BACK ----
    bx1 = xs1-bw-depth; cb = xb+(bx1-xb)/2+0.5
    s.append(logo(cb-7, Y0+9, 14, BUR))
    s.append(T(cb, Y0+23.5, 'امسح الكود.. وتسوّق', 3.9, BUR, 800, 'Cairo', extra='direction="rtl"'))
    qs = 27; qx, qy = cb-qs/2, Y0+28
    s.append(qr(qx, qy, qs, fg=BUR))
    y1 = qy+qs+10
    s.append(igicon(cb-19, y1-3.4, 4.2, GOLD) + T(cb-12.8, y1, '@974.group', 3.4, BUR, 500, anchor='start'))
    s.append(globe(cb-19, y1+4.2, 4.2, GOLD) + T(cb-12.8, y1+7.6, '974group.net', 3.4, BUR, 500, anchor='start'))
    # ---- SIDES ----
    for xs in (xs1, xs2):
        c = xs+Dp/2; m = Y0+Ht/2
        s.append(f'<g transform="rotate(-90 {c} {m})">' + logo(c-25, m-3.9, 14, WH) + T(c+12, m+1.5, '@974.group', 3.2, WH, 500) + '</g>')
        s.append(suit('diamond', c, Y0+9, 2.2, GOLD) + suit('diamond', c, yb-9, 2.2, GOLD))
    # ---- LIDS ----
    s.append(logo(xb+Wd/2-7, B+tuck+Dp/2-7*LOGO_RATIO/2, 14, BUR))
    s.append(T(xf+Wd/2, yb+Dp/2+1.2, '974group.net', 3.3, BUR, 500))
    art = ''.join(s)
    page('974-card-box-v2-artwork-bleed3', W, H, art)
    # dieline (same geometry as v1)
    cut, fold = '#FF0000', '#0070FF'
    def L(x1, y1, x2, y2, c, dash=False):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width=".3"{" stroke-dasharray=\"2 1.2\"" if dash else ""}/>'
    die = [L(xg, Y0+4, xb, Y0, cut), L(xg, yb-4, xb, yb, cut), L(xg, Y0+4, xg, yb-4, cut),
           L(xb, Y0, xb, yb, fold), L(xs1, Y0, xs1, yb, fold), L(xf, Y0, xf, yb, fold), L(xs2, Y0, xs2, yb, fold), L(xe, Y0, xe, yb, cut)]
    yl = Y0-Dp; yt = yl-tuck
    die += [L(xb, Y0, xs1, Y0, fold), L(xb, yl, xs1, yl, fold), L(xb, Y0, xb, yl, cut), L(xs1, Y0, xs1, yl, cut)]
    die.append(f'<path d="M{xb},{yl} L{xb+2},{yt+4} Q{xb+3},{yt} {xb+8},{yt} L{xs1-8},{yt} Q{xs1-3},{yt} {xs1-2},{yt+4} L{xs1},{yl}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    yl2 = yb+Dp; yt2 = yl2+tuck
    die += [L(xf, yb, xs2, yb, fold), L(xf, yl2, xs2, yl2, fold), L(xf, yb, xf, yl2, cut), L(xs2, yb, xs2, yl2, cut)]
    die.append(f'<path d="M{xf},{yl2} L{xf+2},{yt2-4} Q{xf+3},{yt2} {xf+8},{yt2} L{xs2-8},{yt2} Q{xs2-3},{yt2} {xs2-2},{yt2-4} L{xs2},{yl2}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    die += [L(xf, Y0, xs2, Y0, cut), L(xb, yb, xs1, yb, cut)]
    for xs in (xs1, xs2):
        die += [L(xs, Y0, xs+Dp, Y0, fold), L(xs, yb, xs+Dp, yb, fold)]
        fh = Dp*0.85
        die.append(f'<path d="M{xs},{Y0} L{xs+1},{Y0-fh+3} Q{xs+1.5},{Y0-fh} {xs+5},{Y0-fh} L{xs+Dp-2},{Y0-fh+4} L{xs+Dp},{Y0}" fill="none" stroke="{cut}" stroke-width=".3"/>')
        die.append(f'<path d="M{xs},{yb} L{xs+1},{yb+fh-3} Q{xs+1.5},{yb+fh} {xs+5},{yb+fh} L{xs+Dp-2},{yb+fh-4} L{xs+Dp},{yb}" fill="none" stroke="{cut}" stroke-width=".3"/>')
    legend = T(B+1, H-1.2, 'CUT — red   FOLD — blue   BLEED 3 mm   deck 63×88 mm · box inner 64.5×89.5×21 mm', 2, '#555', 500, anchor='start')
    page('974-card-box-v2-DIELINE', W, H, art + f'<rect width="{W}" height="{H}" fill="#fff" opacity=".3"/>' + ''.join(die) + legend)

card_back2(); box2()
