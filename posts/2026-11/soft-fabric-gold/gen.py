# Whoop soft fabric — Shiny Gold buckle with 974 logo (16 Nov 2026). Champagne + gold, 9 in-stock colours.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
D = '/home/claude/974-social/posts/2026-11/soft-fabric-gold/'
C = '/home/claude/974-social/products/whoop5-soft-fabric/gold/cut/'
COLS = [('onyx', 'Onyx'), ('granite', 'Granite'), ('twilight', 'Twilight'), ('forest', 'Forest'), ('dune', 'Dune'),
        ('cloud', 'Cloud'), ('sky', 'Sky'), ('pink', 'Pink'), ('orange', 'Orange')]
GOLD = '#A97F2C'; INK = '#2A1E12'


def grid(top, rows, bh, cw, gap):
    h = ''; y = top
    for r in rows:
        x0 = (1080 - cw * len(r)) // 2
        for i, (f, n) in enumerate(r):
            h += f'<div class="b" style="left:{x0+i*cw}px;top:{y}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i class="en">{n}</i></div>'
        y += bh + gap
    return h


def gold(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    if story:
        rows = [COLS[0:3], COLS[3:6], COLS[6:9]]; bh = 226; cw = 320; gap = 58; top = o + 455
    else:
        rows = [COLS[0:5], COLS[5:9]]; bh = 196; cw = 200; gap = 62; top = 392
    body = f'''
<div class="abs" style="left:0;right:0;top:{o+(380 if story else 300)}px;height:{1100 if story else 640}px;background:radial-gradient(55% 50% at 50% 50%,rgba(255,236,190,.75),transparent 70%)"></div>
<div class="abs en" style="left:0;right:0;top:{o+(250 if story else 215)}px;text-align:center;font-weight:700;font-size:{250 if story else 215}px;line-height:.8;letter-spacing:-6px;color:rgba(169,127,44,.09)">GOLD</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 110)}px">
 <div style="font-weight:900;font-size:{72 if story else 70}px;line-height:1.08;white-space:nowrap">البكلة الذهبية.. <span class="gt">بتوقيع 974</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.75">سير قماش ناعم لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span> · حديدة ذهبي لمّاع عليها شعارنا</div>
</div>
{grid(top, rows, bh, cw, gap)}
<div class="abs ar" style="right:48px;left:48px;top:{o+(330 if story else 965)}px;display:flex;gap:10px;flex-wrap:wrap;direction:rtl">
 <span class="fx gd">9 ألوان</span><span class="fx">خفيف ويتنفّس</span><span class="fx">يلبس طول اليوم</span>
</div>'''
    extra = f'''.b{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 18px 20px rgba(70,45,10,.25))}}
.b i{{font-style:normal;font-weight:700;font-size:{19 if story else 16}px;letter-spacing:1.5px;margin-top:10px;color:{GOLD};text-transform:uppercase}}
.gt{{background:linear-gradient(180deg,#E6C477 0%,#B88A2E 55%,#8C6418 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.fx{{font-weight:800;font-size:{23 if story else 21}px;color:{INK};border:1.5px solid rgba(169,127,44,.55);border-radius:40px;padding:4px 18px 7px}}
.gd{{background:linear-gradient(180deg,#E6C477,#B88A2E);color:#fff;border:none}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}}'''
    return page(H, 'linear-gradient(175deg,#FCF8F0 0%,#F5ECDC 55%,#EBDDC3 100%)', INK, body, story, LB,
                'WHOOP 5.0 · MG · GOLD EDITION', 119, 'اطلبه من <em>974group.net</em> 🛒', extra)


if __name__ == '__main__':
    os.chdir(D)
    shot('974-soft-fabric-gold-post', gold(), 1350); shot('974-soft-fabric-gold-story', gold(True), 1920)
