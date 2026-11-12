# Football club charms — post + story (12 Nov 2026). Night-pitch green, charms hanging from one line.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LW
D = '/home/claude/974-social/posts/2026-11/club-charms/'
C = '/home/claude/974-social/products/charms-clubs/cut/'
CL = [('alarabi', 'AL-ARABI'), ('algharafa', 'AL-GHARAFA'), ('alwakrah', 'AL-WAKRAH'), ('realmadrid', 'REAL MADRID'), ('psg', 'PSG'),
      ('arsenal', 'ARSENAL'), ('chelsea', 'CHELSEA'), ('liverpool', 'LIVERPOOL'), ('manutd', 'MAN UNITED')]
LIME = '#C8F25A'

def charms(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#F1F5EE'
    if story:
        rows = [CL[0:5], CL[5:9]]; ch = 330; cw = 196; top = o + 430; gap = 70
    else:
        rows = [CL]; ch = 410; cw = 116; top = 410; gap = 0
    h = ''; y = top
    for r in rows:
        x0 = (1080 - cw * len(r)) // 2
        h += f'<div class="abs" style="left:40px;right:40px;top:{y-6}px;height:3px;border-radius:3px;background:rgba(241,245,238,.35)"></div>'
        for i, (f, n) in enumerate(r):
            h += f'<div class="c" style="left:{x0+i*cw}px;top:{y}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{ch}px"><i class="en">{n}</i></div>'
        y += ch + 60 + gap
    body = f'''
<div class="abs" style="left:0;right:0;top:0;bottom:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 90px,rgba(255,255,255,0) 90px 180px)"></div>
<div class="abs" style="left:50%;top:{o+(1330 if story else 1010)}px;display:none;width:520px;height:520px;margin-left:-260px;border:3px solid rgba(255,255,255,.06);border-radius:50%"></div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 110)}px">
 <div class="en" style="font-weight:700;font-size:{18 if story else 16}px;letter-spacing:5px;color:{LIME}">FOOTBALL CLUB CHARMS</div>
 <div style="font-weight:900;font-size:{80 if story else 66}px;line-height:1.05;margin-top:6px">علّق شعار ناديك ⚽</div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.8">Charm جلد بشعار ناديك · على شنطتك أو مفاتيحك</div>
</div>
{h}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1310 if story else 940)}px;display:flex;gap:10px;flex-wrap:wrap;direction:rtl">
 <span class="fx">دوري نجوم قطر 🇶🇦</span><span class="fx">الدوري الإنجليزي</span><span class="fx">هدية حلوة لأي مشجّع 🎁</span>
</div>'''
    extra = f'''.c{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.c img{{filter:drop-shadow(0 18px 18px rgba(0,0,0,.5))}}
.c i{{font-style:normal;font-weight:700;font-size:{14 if story else 11}px;letter-spacing:1px;margin-top:12px;opacity:.75;white-space:nowrap}}
.fx{{font-weight:800;font-size:{23 if story else 21}px;color:{LIME};border:1.5px solid rgba(200,242,90,.5);border-radius:40px;padding:4px 18px 7px}}
.pill{{background:{LIME};color:#10220F;border:none!important}}'''
    return page(H, 'radial-gradient(110% 80% at 50% 30%,#1F4A2A 0%,#123220 55%,#0B2116 100%)', INK, body, story, LW,
                'CHARMS · 974GROUP', 75, 'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink=INK)

if __name__ == '__main__':
    os.chdir(D)
    shot('974-club-charms-post', charms(), 1350); shot('974-club-charms-story', charms(True), 1920)
