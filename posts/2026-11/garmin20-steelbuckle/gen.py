# Two designs (12 Nov 2026): Garmin 20mm QuickFit silicone + silicone band with steel butterfly buckle.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
D = '/home/claude/974-social/posts/2026-11/garmin20-steelbuckle/'
G = '/home/claude/974-social/products/garmin-20mm-quickfit/cut/'
S = '/home/claude/974-social/products/steel-buckle-silicone/cut/'

def row(path, items, top, bh, cw, label_size):
    x0 = (1080 - cw * len(items)) // 2
    return ''.join(f'<div class="b" style="left:{x0+i*cw}px;top:{top}px;width:{cw}px"><img src="file://{path}{f}.png" style="height:{bh}px"><i class="en" style="font-size:{label_size}px">{n}</i></div>'
                   for i, (f, n) in enumerate(items))

def garmin20(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#1E2328'; ACC = '#F2672A'
    items = [('white', 'WHITE'), ('babyblue', 'BABY BLUE'), ('lightgreen', 'LIGHT GREEN'), ('orange', 'ORANGE')]
    if story:
        r = row(G, items[:2], o + 470, 340, 360, 18) + row(G, items[2:], o + 900, 340, 360, 18)
    else:
        r = row(G, items, 420, 275, 255, 16)
    body = f'''
<div class="abs en" style="left:0;right:0;top:{o+(330 if story else 270)}px;text-align:center;font-weight:700;font-size:{300 if story else 260}px;line-height:.8;letter-spacing:-8px;color:rgba(30,35,40,.04)">20mm</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div class="en" style="font-weight:700;font-size:{18 if story else 16}px;letter-spacing:5px;color:{ACC}">GARMIN · QUICKFIT 20mm</div>
 <div style="font-weight:900;font-size:{84 if story else 72}px;line-height:1.05;margin-top:6px">خفيف.. <span style="color:{ACC}">وألوانه تفرّح</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.75">سير سيليكون لساعات <span class="en">Garmin</span> بمقاس <span class="en">20mm</span> · يركب بثانية بدون أدوات</div>
</div>
{r}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1310 if story else 850)}px;display:flex;gap:10px;flex-wrap:wrap;direction:rtl">
 <span class="fx">ما يعرّق</span><span class="fx">للجيم والجري</span><span class="fx">بكلة معدن</span>
</div>'''
    extra = f'''.b{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 20px 22px rgba(20,30,40,.22))}}
.b i{{font-style:normal;font-weight:700;letter-spacing:1.5px;margin-top:14px;opacity:.7}}
.fx{{font-weight:800;font-size:{23 if story else 21}px;color:{ACC};border:1.5px solid rgba(242,103,42,.45);border-radius:40px;padding:4px 18px 7px}}
.pill{{background:{ACC};color:#fff;border:none!important}}'''
    return page(H, 'radial-gradient(90% 60% at 50% 45%,#FFFFFF 0%,#F1F3F5 60%,#E4E8EC 100%)', INK, body, story, LB,
                'GARMIN · 20mm · SILICONE', 99, 'اطلبه من <em>974group.net</em> 🛒', extra)

def steel(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#F2F2F0'; SIL = '#C9CDD3'
    items = [('black', 'BLACK'), ('white', 'WHITE'), ('orange', 'ORANGE')]
    if story:
        r = row(S, items, o + 470, 360, 330, 18)
    else:
        r = row(S, items, 410, 300, 330, 16)
    clasp_top = o + (1000 if story else 800)
    body = f'''
<div class="abs" style="left:-100px;right:-100px;top:{o+(380 if story else 300)}px;height:520px;background:radial-gradient(50% 50% at 50% 50%,rgba(255,255,255,.08),rgba(255,255,255,0) 70%)"></div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div class="en" style="font-weight:700;font-size:{18 if story else 16}px;letter-spacing:5px;color:{SIL}">STAINLESS STEEL BUTTERFLY BUCKLE</div>
 <div style="font-weight:900;font-size:{84 if story else 72}px;line-height:1.05;margin-top:6px">سيليكون.. <span style="color:{SIL}">ببكلة ستيل</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.78">لـ <span class="en">Apple Watch</span> و <span class="en">MoonSwatch</span> · قفل فراشة يسكّر بضغطة</div>
</div>
{r}
<img class="abs" src="file://{S}extra.png" style="left:{60 if story else 70}px;top:{clasp_top}px;height:{240 if story else 210}px;filter:drop-shadow(0 18px 20px rgba(0,0,0,.6)) brightness(1.15)">
<div class="abs ar" style="right:48px;top:{clasp_top+(30 if story else 20)}px;width:{600 if story else 560}px">
 <div style="font-weight:900;font-size:{36 if story else 31}px">قفل فراشة ستيل</div>
 <div style="font-weight:700;font-size:{24 if story else 21}px;opacity:.75;margin-top:6px;line-height:1.45">ما يطيح ولا يرتخي.. ومريح طول اليوم<br>3 ألوان · لكل مقاسات <span class="en">Apple Watch</span> و <span class="en">MoonSwatch</span></div>
</div>'''
    extra = f'''.b{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 22px 26px rgba(0,0,0,.55)) drop-shadow(0 0 1px rgba(255,255,255,.35))}}
.b i{{font-style:normal;font-weight:700;letter-spacing:1.5px;margin-top:10px;opacity:.7}}
.pill{{background:{INK};color:#151618;border:none!important}}'''
    return page(H, 'radial-gradient(120% 90% at 50% 35%,#2A2C31 0%,#1A1B1E 60%,#111214 100%)', INK, body, story, LW,
                'APPLE WATCH · MOONSWATCH', 149, 'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink=INK)

if __name__ == '__main__':
    os.chdir(D)
    shot('974-garmin20-post', garmin20(), 1350); shot('974-garmin20-story', garmin20(True), 1920)
    shot('974-steel-buckle-post', steel(), 1350); shot('974-steel-buckle-story', steel(True), 1920)
