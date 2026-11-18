# Maroon Whoop silicone — "flag" layout (18 Nov 2026): white hoist with 9 serrations, maroon field, band across the edge.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
C = '/home/claude/974-social/posts/2026-11/maroon-qatar/cut/'
GOLD = '#C9A24B'

def flag(H, x=300, depth=70):
    n = 9; st = H / n
    pts = [(0, 0), (x, 0)]
    for i in range(n):
        pts += [(x + depth, st*(i+0.5)), (x, st*(i+1))]
    pts += [(0, H)]
    return ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts)

def build(story=False):
    H = 1920 if story else 1350
    top = 250 if story else 120
    band_top = 560 if story else 330
    bh = 760 if story else 640
    body = f'''<svg class="abs" style="left:0;top:0" width="1080" height="{H}"><polygon points="{flag(H)}" fill="#F4F1F2"/></svg>
<div class="abs ar" style="right:56px;left:420px;top:{top}px;text-align:right;color:#fff">
 <div class="en" style="font-weight:700;font-size:20px;letter-spacing:6px;color:{GOLD}">QATAR MAROON · SILICONE</div>
 <div style="font-weight:900;font-size:96px;line-height:1.05;margin-top:10px">عنابي..<br>وبكل فخر</div>
 <div style="font-weight:700;font-size:30px;margin-top:14px;opacity:.9">سير سيليكون لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
<img class="abs hero" src="file://{C}p49m-0.png" style="left:90px;top:{band_top}px;height:{bh}px">
<div class="abs ar feats" style="right:56px;top:{band_top + (230 if story else 170)}px">
 <div><b>خفيف</b><span>تنساه وانت لابسه</span></div>
 <div><b>ما يتأثر بالعرق</b><span>ينغسل بثواني</span></div>
 <div><b>حديدة فضية</b><span>لمّاعة وثابتة</span></div>
</div>'''
    extra = f'''.hero{{filter:drop-shadow(0 40px 50px rgba(0,0,0,.45))}}
.feats{{display:flex;flex-direction:column;gap:22px;width:330px}}
.feats div{{border-right:4px solid {GOLD};padding:2px 18px 6px 0;color:#fff}}
.feats b{{display:block;font-weight:900;font-size:34px;line-height:1.2}} .feats span{{font-weight:600;font-size:22px;opacity:.75}}
.pill{{border-color:#720842!important;color:#720842;background:#fff}} .top .tag{{color:#720842!important}}'''
    return page(H, 'radial-gradient(120% 90% at 75% 30%,#8A0C52 0%,#720842 35%,#51022D 75%,#3A011F 100%)', '#fff', body, story, LB,
                'QATAR EDITION', 99, 'علّق <em>«سيليكون»</em> ونرسل لك الرابط 📩', extra, pf_ink='#51022D')

if __name__ == '__main__':
    shot('974-maroon-flag-post', build(False), 1350)
    shot('974-maroon-flag-story', build(True), 1920)
