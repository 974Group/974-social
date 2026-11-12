# Garmin Fenix 9 silicone strap (12 Nov 2026) — post + story.
# Dark graphite (rugged), orange accent from the strap. Hero = orange strap on the watch,
# row of 7 colours underneath, sizes 20/22 chips.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LW
D = '/home/claude/974-social/posts/2026-11/garmin-fenix9/'
C = '/home/claude/974-social/products/garmin-fenix9-silicone-nov26/cut/'
COLS = [('black', 'BLACK'), ('grey', 'GREY'), ('white-black', 'WHITE'), ('army-green', 'ARMY GREEN'),
        ('khaki-brown', 'KHAKI'), ('starlight', 'STARLIGHT'), ('orange', 'ORANGE')]
ORG = '#F07A2A'

def fenix(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#F1EEEA'
    hero = 600 if story else 520
    bh = 182 if story else 172; cw = 146
    x0 = (1080 - cw * len(COLS)) // 2
    row = ''.join(f'<div class="c" style="left:{x0+i*cw}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i>{n}</i></div>'
                  for i, (f, n) in enumerate(COLS))
    body = f'''
<div class="abs" style="left:-120px;top:{o+(170 if story else 110)}px;width:{hero+260}px;height:{hero+260}px;border-radius:50%;background:radial-gradient(circle,rgba(240,122,42,.20) 0%,rgba(240,122,42,0) 62%)"></div>
<div class="abs en" style="right:-20px;top:{o+(560 if story else 430)}px;font-weight:700;font-size:{300 if story else 260}px;line-height:.8;letter-spacing:-10px;color:rgba(255,255,255,.04)">FĒNIX</div>
<img class="abs" src="file://{C}hero-orange.png" style="left:{20 if story else 24}px;top:{o+(190 if story else 128)}px;height:{hero}px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))">
<div class="abs ar" style="right:48px;top:{o+(200 if story else 140)}px;width:{430 if story else 420}px">
 <div class="en" style="font-weight:700;font-size:{19 if story else 17}px;letter-spacing:5px;color:{ORG}">NEW · FENIX 9</div>
 <div style="font-weight:900;font-size:{82 if story else 72}px;line-height:1.05;margin-top:8px">جهازك<br>جديد؟<br><span style="color:{ORG}">سيرك وصل</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:16px;opacity:.8">سيليكون لونين · بكلة ستيل<br>يركب <span class="en">QuickFit</span> بدون أدوات</div>
 <div class="sz"><span>20mm</span><span>22mm</span></div>
 <div class="bo">سير فقط · بدون الجهاز</div>
</div>
<div class="abs" style="left:0;right:0;top:{o+(900 if story else 705)}px;height:{bh+60}px">{row}</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1200 if story else 965)}px;font-weight:800;font-size:{30 if story else 26}px">7 ألوان.. <span style="opacity:.65">لكل طلعة لون</span></div>'''
    extra = f'''.c{{position:absolute;top:0;display:flex;flex-direction:column;align-items:center}} .c img{{filter:drop-shadow(0 16px 18px rgba(0,0,0,.55))}}
.c i{{font-style:normal;font-family:Poppins;font-weight:700;font-size:{14 if story else 13}px;letter-spacing:1.5px;margin-top:12px;opacity:.7;white-space:nowrap}}
.sz{{display:flex;gap:10px;margin-top:22px;justify-content:flex-end;direction:ltr}} .sz span{{font-family:Poppins;font-weight:700;font-size:22px;border:2px solid {ORG};color:{ORG};border-radius:30px;padding:2px 18px}}
.pill{{background:{ORG};border-color:{ORG}!important;color:#fff}}'''
    return page(H, 'radial-gradient(120% 90% at 30% 25%,#2A2B2F 0%,#1B1C1F 55%,#121315 100%)', INK, body, story, LW,
                'GARMIN · FENIX 9 · SILICONE', 99, 'علّق <em>«قارمن»</em> ونرسل لك الرابط 📩', extra, pf_ink=INK)

if __name__ == '__main__':
    os.chdir(D)
    shot('974-garmin-fenix9-post', fenix(), 1350); shot('974-garmin-fenix9-story', fenix(True), 1920)
