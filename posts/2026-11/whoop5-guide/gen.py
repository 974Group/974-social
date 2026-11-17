# Whoop 5.0 / MG band guide carousel (17 Nov 2026): hook + one slide per band type + CTA.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
R = '/home/claude/974-social/'
P = R + 'products/'; PO = R + 'posts/2026-11/'
GOLD = '#C9A24B'

SIL = PO + 'whoop5-silicone-restock/cut/'
SF = P + 'whoop5-soft-fabric/cut/'
WP = '/home/claude/974-social/posts/2026-11/whoop5-guide/cut/waterproof-matte-'
FB = P + 'whoop5-fabric/cut/'
WL = '/home/claude/974-social/posts/2026-11/whoop5-guide/cut/wool-logo-'
LT = PO + 'exotic-leather/cut/'
NV = '/home/claude/974-social/posts/2026-11/whoop5-guide/cut/'

# key: (ar name, en name, headline, chips, lines, price, from?, bands[(path,label)], bg, ink, accent)
T = {
 'silicone': ('السيليكون', 'SILICONE', 'للاستخدام اليومي', ['يومي', 'رياضة', 'سباحة', 'شاور'],
              'ما يتأثر بالعرق ولا الماي.. وينغسل بسهولة', 99, False,
              [(SIL+'black.png','Black'),(SIL+'iceblue.png','Ice blue'),(SIL+'babyblue.png','Baby blue'),(SIL+'yellow.png','Yellow'),(SIL+'pink.png','Pink')],
              'linear-gradient(170deg,#EAF6FB 0%,#CFEAF5 100%)', '#12324A', '#1E88B8'),
 'navigator': ('النافيقيتور', 'NAVIGATOR', 'لليومي والرياضة والكاجوال', ['يومي', 'رياضة', 'كاجوال', 'مشاوير'],
              'سيليكون ونايلون.. قوة الرياضة وشكل الكاجوال في سير واحد', 99, False,
              [(NV+'navigator-green.png','Green'),(NV+'navigator-white.png','White'),(NV+'navigator-navy.png','Navy')],
              'linear-gradient(170deg,#EEF1F6 0%,#D9DFEA 100%)', '#1B2540', '#D9601E'),
 'softfabric': ('الفابريك', 'SOFT FABRIC · FABRIC', 'للكاجوال ووقت النوم', ['كاجوال', 'دوام', 'مشاوير', 'نوم'],
              'السوفت ناعم وما يضايق.. والفابريك نفسه بس أقوى ويتحمل أكثر', 89, True,
              [(SF+'onyx.png','Soft · Onyx'),(SF+'cloud.png','Soft · Cloud'),(SF+'forest.png','Soft · Forest'),(FB+'matcha.png','Fabric · Matcha'),(FB+'alpine-green.png','Fabric · Alpine')],
              'linear-gradient(170deg,#F5F1EA 0%,#E8E0D2 100%)', '#2E2A22', '#6B7B4A'),
 'waterproof': ('الووتر بروف', 'WATERPROOF', 'اسبح فيه وانت مرتاح', ['سباحة', 'بحر', 'شاور', 'رياضة'],
              'خفيف وما يمتص العرق ولا الماي.. وينشف بسرعة', 99, False,
              [(WP+'black-1.png','Black'),(WP+'maroon-1.png','Maroon'),(WP+'blue-1.png','Blue'),(WP+'orange-1.png','Orange'),(WP+'grey-1.png','Grey')],
              'linear-gradient(180deg,#0B3A66 0%,#06192F 100%)', '#FFFFFF', '#7FE0FF'),
 'fabric': ('الفابريك', 'FABRIC', 'للجري والجيم', ['جري', 'جيم', 'مشي', 'يومي'],
              'مطاطي ويتنفس.. يثبت على يدك وانت تتحرك', 99, False,
              [(FB+'matcha.png','Matcha'),(FB+'alpine-green.png','Alpine green')],
              'linear-gradient(170deg,#F1F7E6 0%,#DCEBC4 100%)', '#1F3311', '#4E8A1E'),
 'wool': ('الصوف', 'WOOL', 'ستايل كاجوال للشتا', ['شتا', 'كاجوال', 'طلعات', 'دوام'],
              'ناعم ودافي على اليد.. بنقشة تفرق عن غيره', 99, False,
              [(WL+'black-1.png','Black'),(WL+'sky-1.png','Sky'),(WL+'rose-1.png','Rose'),(WL+'grass-2.png','Grass')],
              'linear-gradient(170deg,#F7EFEF 0%,#EADADB 100%)', '#3A1E24', '#B0475A'),
 'leather': ('الجلد', 'LEATHER', 'للمناسبات والدوام', ['مناسبات', 'دوام', 'مع الثوب', 'مع البدلة'],
              'بايثون وتمساح وسحلية + جلد منقوش.. فخامة على يدك', 199, True,
              [(LT+'pink-python.png','Pink python'),(LT+'white-python.png','White python'),(LT+'himalayan.png','Himalayan croc')],
              'radial-gradient(120% 80% at 30% 20%,#7A0B47 0%,#51022D 50%,#2B0118 100%)', '#FFFFFF', GOLD),
}
ORDER = ['silicone', 'navigator', 'softfabric', 'waterproof', 'wool', 'leather']
N = len(ORDER) + 2

from PIL import Image as _I
def row(bands, top, h, labcol):
    n = len(bands); cw = 1000 // n; x0 = 40 + (1000 - cw*n)//2
    # same visual height for every band: shrink h so no image is width-limited
    for p, _ in bands:
        w0, h0 = _I.open(p).size
        h = min(h, int((cw-14) * h0 / w0))
    return ''.join(f'<div class="b" style="left:{x0+i*cw}px;top:{top}px;width:{cw}px"><img src="file://{p}" style="height:{h}px;max-width:{cw-14}px;object-fit:contain"><i style="color:{labcol}">{l}</i></div>'
                   for i, (p, l) in enumerate(bands))

def counter(i, ink):
    return f'<div class="abs en cnt" style="color:{ink}">{i}/{N}</div>'

BASE = '''.b{position:absolute;display:flex;flex-direction:column;align-items:center}
.b img{filter:drop-shadow(0 18px 22px rgba(0,0,0,.28))}
.b i{font-style:normal;font-family:Poppins;font-weight:700;font-size:15px;letter-spacing:1.5px;margin-top:12px;text-transform:uppercase;white-space:nowrap}
.cnt{left:48px;top:118px;font-weight:700;font-size:20px;letter-spacing:2px;opacity:.55}
.chips{display:flex;gap:12px;justify-content:center;direction:rtl}
.chips span{font-weight:800;font-size:28px;border-radius:40px;padding:4px 26px 9px}'''

def slide(k, i):
    ar, en, head, chips, line, price, frm, bands, bg, ink, acc = T[k]
    dark = ink == '#FFFFFF'
    h = 340 if len(bands) <= 3 else (300 if len(bands) == 4 else 250)
    if k == 'leather': h = 470
    if k == 'fabric': h = 380
    chip_html = ''.join(f'<span style="background:{acc};color:{"#2B0118" if dark else "#fff"}">{c}</span>' for c in chips)
    body = f'''{counter(i, ink)}
<div class="abs ar" style="right:48px;left:48px;top:150px">
 <div class="en" style="font-weight:700;font-size:22px;letter-spacing:6px;color:{acc}">{en}</div>
 <div style="font-weight:900;font-size:84px;line-height:1.05;margin-top:6px">{ar}</div>
 <div style="font-weight:900;font-size:50px;line-height:1.15;color:{acc}">{head}</div>
</div>
{row(bands, 470 if k!='leather' else 440, h, ink if not dark else 'rgba(255,255,255,.75)')}
<div class="abs" style="left:48px;right:48px;top:{(840 if len(bands)>=5 else 900) if k!='leather' else 960}px">
 <div class="chips">{chip_html}</div>
 <div class="ar" style="text-align:center;font-weight:800;font-size:30px;margin-top:22px">{line}</div>
</div>'''
    extra = BASE + (f'.pill::before{{content:"من ";font-size:.7em}}' if frm else '') + (f'.pill{{border-color:{acc}!important;color:{acc}}}' if dark else '')
    return page(1350, bg, ink, body, False, LW if dark else LB, 'WHOOP 5.0 · MG', price,
                'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink='#fff' if dark else None)

def hook():
    C = '/home/claude/974-social/posts/2026-11/whoop5-guide/cut/'
    picks = [(C+'silicone-iceblue-r.png','Silicone'),(C+'navigator-navy.png','Navigator'),(C+'softfabric-forest.png','Fabric'),(C+'waterproof-maroon.png','Waterproof'),(C+'wool-rose.png','Wool'),(C+'leather-pinkpython.png','Leather')]
    body = f'''{counter(1, '#fff')}
<div class="abs ar" style="right:48px;left:48px;top:170px;text-align:center">
 <div style="font-weight:900;font-size:92px;line-height:1.1">عندك <span class="en" style="font-weight:700">Whoop 5.0</span><br>أو <span class="en" style="font-weight:700;color:{GOLD}">MG</span>؟</div>
 <div style="font-weight:800;font-size:36px;margin-top:22px;opacity:.9">كل سير له استخدامه.. اختار اللي يناسب يومك</div>
</div>
{row(picks, 580, 260, 'rgba(255,255,255,.75)')}
<div class="abs" style="left:0;right:0;top:880px;text-align:center"><span class="swipe">اسحب وشوف ←</span></div>'''
    extra = BASE + f'''.swipe{{display:inline-block;font-weight:900;font-size:32px;color:#2B0118;background:{GOLD};border-radius:40px;padding:6px 34px 12px}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}} .pill::before{{content:"من ";font-size:.7em}}'''
    return page(1350, 'radial-gradient(120% 80% at 30% 15%,#7A0B47 0%,#51022D 50%,#2B0118 100%)', '#fff', body, False, LW,
                'WHOOP 5.0 · MG', 89, 'كلها على <em>974group.net</em> 🛒', extra, pf_ink='#fff')

def cta():
    rows = ''.join(f'<div class="r"><b>{T[k][0]}</b><span>{T[k][2]}</span></div>' for k in ORDER)
    body = f'''{counter(N, '#fff')}
<div class="abs ar" style="right:48px;left:48px;top:160px;text-align:center">
 <div style="font-weight:900;font-size:76px;line-height:1.1">محتار أي سير<br><span style="color:{GOLD}">يناسبك؟</span></div>
 <div style="font-weight:800;font-size:32px;margin-top:16px;opacity:.9">راسلنا وقول لنا وش تسوي في يومك.. ونختار لك</div>
</div>
<div class="abs tbl" style="left:120px;right:120px;top:470px">{rows}</div>
<div class="abs ar" style="left:48px;right:48px;top:990px;text-align:center;font-weight:800;font-size:28px;color:{GOLD}">كل السيور تركب على <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>'''
    extra = BASE + f'''.tbl{{direction:rtl}} .r{{display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid rgba(255,255,255,.18);padding:6px 6px 10px}}
.r b{{font-weight:900;font-size:36px}} .r span{{font-weight:700;font-size:28px;color:{GOLD}}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}} .pill::before{{content:"من ";font-size:.7em}}'''
    return page(1350, 'radial-gradient(120% 80% at 70% 15%,#7A0B47 0%,#51022D 50%,#2B0118 100%)', '#fff', body, False, LW,
                'WHOOP 5.0 · MG', 89, 'راسلنا في الخاص <em>أو</em> 974group.net', extra, pf_ink='#fff')

if __name__ == '__main__':
    only = sys.argv[1:]
    S = [('01-hook', hook)] + [(f'{i+2:02d}-{k}', (lambda k=k, i=i: slide(k, i+2))) for i, k in enumerate(ORDER)] + [(f'{N:02d}-cta', cta)]
    for n, f in S:
        if not only or any(o in n for o in only):
            shot(n, f(), 1350)
