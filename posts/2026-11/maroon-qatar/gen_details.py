# Maroon Whoop 5.0/MG silicone — "details" design: big band + 3 zoom circles
# (maroon outside · white inside · shiny silver clasp). Light background like the approved light version.
import sys, os
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
D = '/home/claude/974-social/posts/2026-11/maroon-qatar/'
C = D + 'cut/'
MAR = '#6A0B12'; INK = '#2A1013'
BG = 'radial-gradient(70% 45% at 50% 52%,#FFFFFF 0%,#F6F1F1 55%,#EDE3E4 100%)'
SRC = C + 'p49m-0.png'            # 867x988 render, transparent
SW, SH = 867, 988
# zoom spots in source pixels: (name, centre x, centre y, crop size)
SPOTS = {'white': (205, 335, 210), 'clasp': (468, 330, 210), 'maroon': (742, 600, 230)}

def crops():
    src = Image.open(SRC).convert('RGBA')
    for k, (x, y, s) in SPOTS.items():
        bg = Image.new('RGBA', (s, s), (238, 232, 233, 255))
        bg.alpha_composite(src.crop((x - s // 2, y - s // 2, x + s // 2, y + s // 2)))
        im = bg.resize((520, 520), Image.LANCZOS)
        m = Image.new('L', (520, 520), 0); ImageDraw.Draw(m).ellipse((0, 0, 519, 519), fill=255)
        im.putalpha(m); im.save(C + f'zoom-{k}.png')

def g(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    bh = 640 if story else 660                 # band height
    s = bh / SH; bw = SW * s
    bx = (1080 - bw) / 2; by = o + (560 if story else 335)
    r = 104 if story else 100                  # zoom circle radius
    def P(k):                                  # spot -> canvas point
        x, y, _ = SPOTS[k]
        if k == 'maroon': x, y = 800, 470          # dot on plain maroon, not on the logo
        return bx + x * s, by + y * s
    # circle centres: white on the left, clasp top-right, maroon bottom-right
    cx_l = 30 + r; cx_r = 1080 - 30 - r
    circ = {'white': (cx_l, by + bh * 0.30), 'clasp': (cx_r, by + bh * 0.16), 'maroon': (cx_r, by + bh * 0.64)}
    lab = {'white': ('أبيض من داخل', 'ناعم على يدك'),
           'clasp': ('حديدة رصاصية', 'لمّاعة وثابتة'),
           'maroon': ('عنابي من برّا', 'لون علمنا')}
    svg = ''; html = ''
    for k, (cx, cy) in circ.items():
        px, py = P(k)
        # leader: from circle edge toward the point
        import math
        ang = math.atan2(py - cy, px - cx); ex, ey = cx + math.cos(ang) * (r + 6), cy + math.sin(ang) * (r + 6)
        svg += f'<line x1="{ex:.0f}" y1="{ey:.0f}" x2="{px:.0f}" y2="{py:.0f}" stroke="{MAR}" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/>'
        svg += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="11" fill="#fff" stroke="{MAR}" stroke-width="4"/><circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{MAR}"/>'
        html += f'<img class="abs zm" src="file://{C}zoom-{k}.png" style="left:{cx-r:.0f}px;top:{cy-r:.0f}px;width:{2*r}px;height:{2*r}px">'
        t1, t2 = lab[k]
        html += f'''<div class="abs lb" style="left:{cx-125:.0f}px;width:250px;top:{cy+r+14:.0f}px"><b>{t1}</b><span>{t2}</span></div>'''
    n = 9; st = 1080 / n; y0 = 14; d = 22
    pts = '0,0 1080,0 1080,%d ' % y0 + ' '.join(f'{1080-i*st:.0f},{y0} {1080-(i+.5)*st:.0f},{y0+d}' for i in range(n)) + f' 0,{y0}'
    body = f'''
<svg class="abs" style="left:0;top:0" width="1080" height="40"><polygon fill="{MAR}" points="{pts}"/></svg>
<div class="abs ar" style="right:48px;left:48px;top:{o+(118 if story else 108)}px">
 <div style="font-weight:900;font-size:{86 if story else 74}px;line-height:1.08;color:{MAR}">تفاصيل.. تفرق</div>
 <div style="font-weight:700;font-size:{30 if story else 27}px;margin-top:10px;color:{INK};opacity:.8">سير سيليكون عنابي لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
<div class="abs" style="left:50%;transform:translateX(-50%);top:{by+bh-40:.0f}px;width:{bw*0.9:.0f}px;height:60px;border-radius:50%;background:radial-gradient(closest-side,rgba(60,10,15,.26),transparent)"></div>
<img class="abs band" src="file://{SRC}" style="left:{bx:.0f}px;top:{by:.0f}px;height:{bh}px">
<svg class="abs" style="left:0;top:0;overflow:visible" width="1080" height="{H}">{svg}</svg>
{html}'''
    extra = f'''.band{{filter:drop-shadow(0 26px 30px rgba(80,10,18,.22))}}
.zm{{border-radius:50%;border:{7 if story else 6}px solid #fff;box-shadow:0 0 0 2px {MAR},0 18px 30px rgba(80,10,18,.25)}}
.lb{{text-align:center;direction:rtl;line-height:1.15}} .lb b{{display:block;font-weight:900;font-size:{31 if story else 29}px;color:{MAR}}} .lb span{{display:block;font-weight:700;font-size:{24 if story else 21}px;color:{INK};opacity:.75}}
.pill{{background:{MAR};color:#fff;border:none!important}}'''
    cta = 'اطلبه من <em>974group.net</em> 🛒' if story else 'علّق <em>«سيليكون»</em> ونرسل لك الرابط'
    return page(H, BG, INK, body, story, LB, '974 BANDS', 99, cta, extra, pf_ink=INK)

if __name__ == '__main__':
    crops()
    shot('974-maroon-details-post', g(), 1350)
    shot('974-maroon-details-story', g(True), 1920)
