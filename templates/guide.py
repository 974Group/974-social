# Shared "band guide" carousel builder (hook + one slide per band type + CTA).
# Used by posts/2026-11/{fitbit,cirqa}-guide/gen.py. Whoop version: posts/2026-11/whoop5-guide/gen.py
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
from PIL import Image as _I
GOLD = '#C9A24B'
MAROON_BG = 'radial-gradient(120% 80% at 30% 15%,#7A0B47 0%,#51022D 50%,#2B0118 100%)'
BASE = '''.b{position:absolute;display:flex;flex-direction:column;align-items:center}
.b img{filter:drop-shadow(0 18px 22px rgba(0,0,0,.28))}
.b i{font-style:normal;font-family:Poppins;font-weight:700;font-size:15px;letter-spacing:1.5px;margin-top:12px;text-transform:uppercase;white-space:nowrap}
.cnt{left:48px;top:118px;font-weight:700;font-size:20px;letter-spacing:2px;opacity:.55}
.chips{display:flex;gap:12px;justify-content:center;direction:rtl}
.chips span{font-weight:800;font-size:28px;border-radius:40px;padding:4px 26px 9px}
.rl{position:absolute;left:48px;right:48px;font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:3px;text-align:left}'''

def row(bands, top, h, labcol, x0=40, width=1000):
    n = len(bands); cw = width // n; x0 = x0 + (width - cw*n)//2
    for p, _ in bands:  # same visual height: no image may be width-limited
        w0, h0 = _I.open(p).size
        h = min(h, int((cw-14) * h0 / w0))
    return ''.join(f'<div class="b" style="left:{x0+i*cw}px;top:{top}px;width:{cw}px"><div style="height:{h}px;width:{cw-14}px;display:flex;align-items:flex-end;justify-content:center"><img src="file://{p}" style="max-height:{h}px;max-width:{cw-14}px"></div><i style="color:{labcol}">{l}</i></div>'
                   for i, (p, l) in enumerate(bands))

def counter(i, N, ink):
    return f'<div class="abs en cnt" style="color:{ink}">{i}/{N}</div>'

def slide(s, i, N, tag):
    """s: dict ar, en, head, chips, line, price, frm, bands | rows=[(label, bands)], bg, ink, acc, h"""
    dark = s['ink'] == '#FFFFFF'
    lab = 'rgba(255,255,255,.75)' if dark else s['ink']
    chip_html = ''.join(f'<span style="background:{s["acc"]};color:{"#2B0118" if dark else "#fff"}">{c}</span>' for c in s['chips'])
    if 'rows' in s:
        bands = ''
        for k, (rlab, bs) in enumerate(s['rows']):
            y = 430 + k*230
            bands += f'<div class="rl" style="top:{y}px;color:{s["acc"]}">{rlab}</div>' + row(bs, y+28, 150, lab)
        chips_top = 900
    else:
        h = s.get('h', 300); top = s.get('top', 470)
        bands = row(s['bands'], top, h, lab)
        chips_top = s.get('chips_top', 870)
    body = f'''{counter(i, N, s['ink'])}
<div class="abs ar" style="right:48px;left:48px;top:150px">
 <div class="en" style="font-weight:700;font-size:22px;letter-spacing:6px;color:{s['acc']}">{s['en']}</div>
 <div style="font-weight:900;font-size:84px;line-height:1.05;margin-top:6px">{s['ar']}</div>
 <div style="font-weight:900;font-size:50px;line-height:1.15;color:{s['acc']}">{s['head']}</div>
</div>
{bands}
<div class="abs" style="left:48px;right:48px;top:{chips_top}px">
 <div class="chips">{chip_html}</div>
 <div class="ar" style="text-align:center;font-weight:800;font-size:30px;margin-top:22px">{s['line']}</div>
</div>'''
    extra = BASE + ('.pill::before{content:"من ";font-size:.7em}' if s.get('frm') else '') + (f'.pill{{border-color:{s["acc"]}!important;color:{s["acc"]}}}' if dark else '')
    return page(1350, s['bg'], s['ink'], body, False, LW if dark else LB, tag, s['price'],
                'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink='#fff' if dark else None)

def hook(N, title_html, sub, picks, tag, price, h=260):
    body = f'''{counter(1, N, '#fff')}
<div class="abs ar" style="right:48px;left:48px;top:170px;text-align:center">
 <div style="font-weight:900;font-size:92px;line-height:1.1">{title_html}</div>
 <div style="font-weight:800;font-size:36px;margin-top:22px;opacity:.9">{sub}</div>
</div>
{row(picks, 580, h, 'rgba(255,255,255,.75)')}
<div class="abs" style="left:0;right:0;top:880px;text-align:center"><span class="swipe">اسحب وشوف ←</span></div>'''
    extra = BASE + f'''.swipe{{display:inline-block;font-weight:900;font-size:32px;color:#2B0118;background:{GOLD};border-radius:40px;padding:6px 34px 12px}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}} .pill::before{{content:"من ";font-size:.7em}}'''
    return page(1350, MAROON_BG, '#fff', body, False, LW, tag, price, 'كلها على <em>974group.net</em> 🛒', extra, pf_ink='#fff')

def cta(N, items, tag, price, note, what='سير'):
    rows = ''.join(f'<div class="r"><b>{a}</b><span>{h}</span></div>' for a, h in items)
    body = f'''{counter(N, N, '#fff')}
<div class="abs ar" style="right:48px;left:48px;top:160px;text-align:center">
 <div style="font-weight:900;font-size:76px;line-height:1.1">محتار أي {what}<br><span style="color:{GOLD}">يناسبك؟</span></div>
 <div style="font-weight:800;font-size:32px;margin-top:16px;opacity:.9">راسلنا وقول لنا وش تسوي في يومك.. ونختار لك</div>
</div>
<div class="abs tbl" style="left:120px;right:120px;top:500px">{rows}</div>
<div class="abs ar" style="left:48px;right:48px;top:990px;text-align:center;font-weight:800;font-size:28px;color:{GOLD}">{note}</div>'''
    extra = BASE + f'''.tbl{{direction:rtl}} .r{{display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid rgba(255,255,255,.18);padding:10px 6px 14px}}
.r b{{font-weight:900;font-size:36px}} .r span{{font-weight:700;font-size:28px;color:{GOLD}}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}} .pill::before{{content:"من ";font-size:.7em}}'''
    return page(1350, MAROON_BG.replace('30% 15%', '70% 15%'), '#fff', body, False, LW, tag, price,
                'راسلنا في الخاص <em>أو</em> 974group.net', extra, pf_ink='#fff')

def build(name_slides, outdir):
    import os
    os.chdir(outdir)
    only = sys.argv[1:]
    for n, f in name_slides:
        if not only or any(o in n for o in only):
            shot(n, f(), 1350)
