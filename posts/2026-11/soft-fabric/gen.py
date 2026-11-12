# Whoop soft fabric (plain colours) — post + story (12 Nov 2026). Light, airy, 11 colours.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
D = '/home/claude/974-social/posts/2026-11/soft-fabric/'
C = '/home/claude/974-social/products/whoop5-soft-fabric/cut/'
COLS = [('onyx', 'Onyx'), ('granite', 'Granite'), ('cloud', 'Cloud'), ('desert', 'Desert'), ('dune', 'Dune'), ('forest', 'Forest'),
        ('twilight', 'Twilight'), ('sky', 'Sky'), ('pink', 'Pink'), ('phoenix', 'Phoenix'), ('orange', 'Orange')]
ACC = '#720842'

def grid(top, rows, bh, cw, gap):
    h = ''; y = top
    for r in rows:
        x0 = (1080 - cw * len(r)) // 2
        for i, (f, n) in enumerate(r):
            h += f'<div class="b" style="left:{x0+i*cw}px;top:{y}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i class="en">{n}</i></div>'
        y += bh + gap
    return h

def soft(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#2B1E22'
    if story:
        rows = [COLS[0:4], COLS[4:8], COLS[8:11]]; bh = 205; cw = 240; gap = 70; top = o + 420
    else:
        rows = [COLS[0:6], COLS[6:11]]; bh = 168; cw = 172; gap = 66; top = 395
    body = f'''
<div class="abs en" style="left:0;right:0;top:{o+(300 if story else 250)}px;text-align:center;font-weight:700;font-size:{250 if story else 210}px;line-height:.8;letter-spacing:-6px;color:rgba(114,8,66,.045)">SOFT</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{82 if story else 72}px;line-height:1.05">11 لون.. <span style="color:{ACC}">سير لكل مود</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.75">سير قماش ناعم لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span> · خفيف ويتنفّس</div>
</div>
{grid(top, rows, bh, cw, gap)}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1275 if story else 912)}px;display:flex;gap:10px;flex-wrap:wrap;direction:rtl">
 <span class="fx">يلبس طول اليوم</span><span class="fx">ما يعرّق</span><span class="fx">بكلة فضي · ذهبي · أسود</span>
</div>'''
    extra = f'''.b{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 18px 20px rgba(60,20,30,.22))}}
.b i{{font-style:normal;font-weight:700;font-size:{18 if story else 16}px;letter-spacing:1px;margin-top:10px;opacity:.75}}
.fx{{font-weight:800;font-size:{23 if story else 21}px;color:{ACC};border:1.5px solid rgba(114,8,66,.35);border-radius:40px;padding:4px 18px 7px}}
.pill{{background:{ACC};color:#fff;border:none!important}}'''
    return page(H, 'radial-gradient(90% 60% at 50% 45%,#FBF8F6 0%,#F2ECE9 60%,#E9E0DC 100%)', INK, body, story, LB,
                'WHOOP 5.0 · MG · SOFT FABRIC', 89, 'اطلبه من <em>974group.net</em> 🛒', extra)

if __name__ == '__main__':
    os.chdir(D)
    shot('974-soft-fabric-post', soft(), 1350); shot('974-soft-fabric-story', soft(True), 1920)
