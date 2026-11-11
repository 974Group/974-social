# Maroon Whoop silicone — LIGHT version: warm off-white (#F4F1F2) with maroon type, maroon serration, band as hero.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
C = '/home/claude/974-social/posts/2026-11/maroon-qatar/cut/'
MAR = '#6A0B12'
INK = '#2A1013'
BG = 'radial-gradient(70% 45% at 50% 56%,#FFFFFF 0%,#F6F1F1 55%,#EDE3E4 100%)'

def g(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    bh = 720 if story else 570
    btop = o + (490 if story else 350)
    n = 9; st = 1080 / n; y0 = 14; d = 22
    pts = '0,0 1080,0 1080,%d ' % y0 + ' '.join(f'{1080-i*st:.0f},{y0} {1080-(i+.5)*st:.0f},{y0+d}' for i in range(n)) + f' 0,{y0}'
    body = f'''
<svg class="abs" style="left:0;top:0" width="1080" height="40"><polygon fill="{MAR}" points="{pts}"/></svg>
<div class="abs en" style="left:-10px;top:{o+(330 if story else 250)}px;font-weight:700;font-size:{250 if story else 230}px;line-height:.84;letter-spacing:-9px;color:rgba(106,11,18,.07);white-space:nowrap">MAROON</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(118 if story else 108)}px">
 <div style="font-weight:900;font-size:{88 if story else 76}px;line-height:1.08;color:{MAR}">لون علمنا..<br>على يدك</div>
 <div style="font-weight:700;font-size:{30 if story else 27}px;margin-top:12px;color:{INK};opacity:.8">سير سيليكون عنابي لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
<div class="abs" style="left:50%;transform:translateX(-50%);top:{btop + bh - 40}px;width:{bh*0.9:.0f}px;height:60px;border-radius:50%;background:radial-gradient(closest-side,rgba(60,10,15,.28),transparent)"></div>
<img class="abs band" src="file://{C}p49m-0.png" style="left:50%;transform:translateX(-50%);top:{btop}px;height:{bh}px">
<div class="abs ar" style="right:48px;left:48px;top:{btop + bh + (40 if story else 26)}px">
 <div class="pts"><span>عنابي برّا.. أبيض داخل</span><i></i><span>حديدة فضية لمّاعة</span><i></i><span>خفيف وما يتأثر بالعرق</span></div>
</div>'''
    extra = f'''.band{{filter:drop-shadow(0 26px 30px rgba(80,10,18,.22))}}
.pts{{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;direction:rtl;font-weight:800;font-size:{27 if story else 24}px;color:{INK}}} .pts i{{width:7px;height:7px;border-radius:50%;background:{MAR};opacity:.6}}
.pill{{background:{MAR};color:#fff;border:none!important}}'''
    cta = 'اطلبه من <em>974group.net</em> 🛒' if story else 'علّق <em>«سيليكون»</em> ونرسل لك الرابط'
    return page(H, BG, INK, body, story, LB, '974 BANDS', 99, cta, extra, pf_ink=INK)

if __name__ == '__main__':
    shot('974-maroon-silicone-light-post', g(), 1350)
    shot('974-maroon-silicone-light-story', g(True), 1920)
