# Rolex customised Whoop soft fabric — 3D print, all 6 in-stock colours. Story for 23 Nov 20:00 (+ matching post). 159 QAR, full price.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
BG = '#14161C'; GOLD = '#C9A24B'
COLS = [('white-blue', 'White · Blue'), ('black-white', 'Black · White'), ('navy-white', 'Navy · White'),
        ('white-pink', 'White · Pink'), ('green-white', 'Green · White'), ('pink-white', 'Pink · White')]
CSS = G.CTA_CSS + f'''.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 10px;justify-items:center}}
.g div{{display:flex;flex-direction:column;align-items:center;gap:8px}}
.g img{{height:var(--h);filter:drop-shadow(0 16px 18px rgba(0,0,0,.55))}}
.g span{{font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:1px;color:#cfd3dc}}
.pill{{display:inline-block;border-radius:30px;padding:3px 18px 7px;font-weight:800;font-size:22px}}'''


def page(story):
    h = 300 if story else 255
    grid = ''.join(f'<div><img src="file://{S}{k}-cut.png"><span>{n}</span></div>' for k, n in COLS)
    gtop = 330 if story else 300
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(80% 55% at 50% 45%,#262A35 0%,{BG} 70%)"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:56px;font-weight:700;font-size:16px;letter-spacing:4px;color:{GOLD}">WHOOP 5.0 · MG · 3D PRINT</div>
<div class="abs en" style="left:0;right:0;top:120px;text-align:center;font-weight:900;font-style:italic;font-size:{58 if story else 54}px;line-height:1.05;color:#fff">"Who cares, I'm already late"</div>
<div class="abs ar" style="left:48px;right:48px;top:{200 if story else 190}px;text-align:center;font-weight:800;font-size:30px;color:{GOLD}">الجملة اللي الكل يسألنا عنها.. صارت على سيرك</div>
<div class="abs g" style="left:30px;right:30px;top:{gtop}px;--h:{h}px">{grid}</div>
<div class="abs" style="left:48px;right:48px;top:{1050 if story else 1000}px;display:flex;gap:12px;justify-content:center;direction:rtl">
 <span class="pill" style="background:{GOLD};color:{BG}">طباعة <span class="en">3D</span> بارزة</span><span class="pill" style="background:#262A35;color:#fff">قماش ناعم</span><span class="pill" style="background:#262A35;color:#fff"><span class="en">6</span> ألوان</span></div>
<div class="abs" style="left:48px;right:48px;top:{1140 if story else 1090}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:#fff"><span class="en" style="font-size:74px;font-weight:900">159</span> ر.ق</div>{G.cta('اختار لونك', GOLD, BG)}</div>'''
    return G.doc(BG, '#fff', body, pf_ink='#fff', extra=CSS)


if __name__ == '__main__':
    G.STORY = True; G.shot('974-rolex-3d-story', page(True), 1920)
    G.STORY = False; G.shot('974-rolex-3d-post', page(False))
    print('ok')
