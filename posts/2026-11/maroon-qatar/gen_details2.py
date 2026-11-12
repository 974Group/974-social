# Maroon silicone — details v2, deliberately unlike the posted light post:
# near-black studio with a maroon glow, huge band bleeding off the left edge, numbered gold callouts 01/02/03 on the right.
import sys, math
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LW
D = '/home/claude/974-social/posts/2026-11/maroon-qatar/'
C = D + 'cut/'
GOLD = '#C9A24B'; INK = '#FFFFFF'
BG = 'radial-gradient(60% 42% at 30% 55%,#4A0A10 0%,#24080B 45%,#0F0C0D 100%)'
SRC = C + 'p49m-0.png'; SW, SH = 867, 988
# anchor points on the band (source px) and the zoom image made by gen_details.crops()
ANCH = {'clasp': (468, 330), 'maroon': (800, 470), 'white': (430, 870)}

def g(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    bh = 860 if story else 800
    s = bh / SH; bx = -170 if story else -150; by = o + (400 if story else 285)
    r = 104 if story else 92
    cx = 1080 - 36 - r
    ys = ([by + bh * f for f in (0.20, 0.47, 0.74)])
    items = [('clasp', '01', 'حديدة رصاصية', 'لمّاعة وثابتة'),
             ('maroon', '02', 'عنابي من برّا', 'لون علمنا'),
             ('white', '03', 'أبيض من داخل', 'ناعم على يدك')]
    svg = ''; html = ''
    for (k, n, t1, t2), cy in zip(items, ys):
        px, py = bx + ANCH[k][0] * s, by + ANCH[k][1] * s
        ang = math.atan2(py - cy, px - cx); ex, ey = cx + math.cos(ang) * (r + 8), cy + math.sin(ang) * (r + 8)
        svg += f'<line x1="{ex:.0f}" y1="{ey:.0f}" x2="{px:.0f}" y2="{py:.0f}" stroke="{GOLD}" stroke-width="2.5"/>'
        svg += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="10" fill="{GOLD}"/><circle cx="{px:.0f}" cy="{py:.0f}" r="20" fill="none" stroke="{GOLD}" stroke-width="2" opacity=".55"/>'
        html += f'<img class="abs zm" src="file://{C}zoom-{k}.png" style="left:{cx-r:.0f}px;top:{cy-r:.0f}px;width:{2*r}px;height:{2*r}px">'
        html += f'<div class="abs num en" style="left:{cx-r-6:.0f}px;top:{cy-r-12:.0f}px">{n}</div>'
        html += f'<div class="abs lb" style="right:{1080-(cx-r-22):.0f}px;top:{cy-r-4:.0f}px"><b>{t1}</b><span>{t2}</span></div>'
    body = f'''
<div class="abs en" style="left:-20px;bottom:{(300 if story else 170)}px;font-weight:700;font-size:{300 if story else 270}px;line-height:.8;letter-spacing:-12px;color:rgba(255,255,255,.035)">974</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(118 if story else 108)}px">
 <div style="font-weight:900;font-size:{92 if story else 80}px;line-height:1.02">من قريب..</div>
 <div style="font-weight:700;font-size:{30 if story else 27}px;margin-top:10px;opacity:.75">كل تفصيلة في السير العنابي <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
<img class="abs band" src="file://{SRC}" style="left:{bx:.0f}px;top:{by:.0f}px;height:{bh}px">
<svg class="abs" style="left:0;top:0;overflow:visible" width="1080" height="{H}">{svg}</svg>
{html}'''
    extra = f'''.band{{filter:drop-shadow(0 40px 50px rgba(0,0,0,.6))}}
.zm{{border-radius:50%;border:3px solid {GOLD};box-shadow:0 0 0 8px rgba(201,162,75,.12),0 20px 40px rgba(0,0,0,.5)}}
.num{{font-weight:700;font-size:{26 if story else 23}px;color:#0F0C0D;background:{GOLD};border-radius:30px;padding:2px 12px}}
.lb{{text-align:right;direction:rtl;line-height:1.15}} .lb b{{display:block;font-weight:900;font-size:{30 if story else 29}px;color:#fff;white-space:nowrap}} .lb span{{display:block;font-weight:700;font-size:{23 if story else 20}px;color:{GOLD}}}
.pill{{background:{GOLD};color:#0F0C0D;border:none!important}}'''
    cta = 'اطلبه من <em>974group.net</em> 🛒' if story else 'علّق <em>«سيليكون»</em> ونرسل لك الرابط'
    return page(H, BG, INK, body, story, LW, '974 BANDS', 99, cta, extra, pf_ink=INK)

if __name__ == '__main__':
    shot('974-maroon-details2-post', g(), 1350)
    shot('974-maroon-details2-story', g(True), 1920)
