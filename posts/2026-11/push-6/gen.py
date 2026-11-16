# Six "push the best-sellers" designs (16 Nov 2026) — each a different layout.
#  mask     Plain face mask        — #1 best-seller mosaic (maroon, gold #1)
#  fitfab   Fitbit Fabric bands    — colour arc around the price (warm peach)
#  magnet   CIRQA magnetic         — dark, lime "magnet" axis, two rows
#  water    Whoop 5.0 waterproof   — deep blue, ripples, rising staircase
#  goggles  974 Guards goggles     — desert dunes, hero + line-up
#  islamic  Islamic charms         — (waiting for photos)
import sys, os, math
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
R = '/home/claude/974-social/'
D = R + 'posts/2026-11/push-6/'
GOLD = '#C9A24B'


def tiles(items, x0, y0, cw, ch, cols, img_h, label_css='', gapy=0):
    h = ''
    for i, (src, name) in enumerate(items):
        r, c = divmod(i, cols)
        h += (f'<div class="t" style="left:{x0+c*cw}px;top:{y0+r*(ch+gapy)}px;width:{cw}px">'
              f'<img src="file://{src}" style="height:{img_h}px"><i {label_css}>{name}</i></div>')
    return h


# ---------- 1. Plain face mask: best-seller mosaic ----------
MASKS = ['white', 'black', 'grey', 'darkgrey', 'navy', 'royalblue', 'skyblue', 'babyblue', 'lilac', 'lightpurple', 'purple', 'hotpink',
         'pink', 'red', 'brightred', 'orange', 'khaki', 'beige', 'cream', 'brown', 'armygreen', 'green', 'lightgreen']
MN = {'darkgrey': 'Dark grey', 'royalblue': 'Royal blue', 'skyblue': 'Sky blue', 'babyblue': 'Baby blue', 'lightpurple': 'Light purple',
      'hotpink': 'Hot pink', 'brightred': 'Bright red', 'armygreen': 'Army green', 'lightgreen': 'Light green'}


def mask(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    C = R + 'posts/2026-11/face-mask/src/cut/'
    items = [(C + m + '.png', MN.get(m, m.title())) for m in MASKS]
    if story:
        cols, cw, ch, ih, x0, y0 = 5, 196, 168, 146, 50, o + 470
    else:
        cols, cw, ch, ih, x0, y0 = 6, 164, 150, 124, 48, 420
    body = f'''
<div class="abs en" style="left:30px;top:{o+(110 if story else 90)}px;font-weight:700;font-size:{300 if story else 250}px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(201,162,75,.55)">#1</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(150 if story else 130)}px">
 <div class="badge">الأكثر مبيعاً في 974</div>
 <div style="font-weight:900;font-size:{78 if story else 70}px;line-height:1.08;margin-top:14px">الماسك<br><span style="color:{GOLD}">اللي الكل لابسه</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:10px;opacity:.8">للبر · السيكل · الجري · البايك — خفيف ويتنفّس</div>
</div>
<div class="abs" style="left:0;right:0;top:{y0-20}px;height:{(ch)*math.ceil(23/cols)+40}px;background:radial-gradient(60% 55% at 50% 50%,rgba(255,255,255,.07),transparent 70%)"></div>
{tiles(items, x0, y0, cw, ch, cols, ih)}
<div class="abs ar" style="right:48px;left:48px;top:{y0+math.ceil(23/cols)*ch+(14 if story else 8)}px;font-weight:800;font-size:{27 if story else 24}px;color:{GOLD}">23 لون · اختار لونك ولون فريقك 🔥</div>'''
    extra = f'''.t{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.t img{{filter:drop-shadow(0 10px 12px rgba(0,0,0,.45))}}
.t i{{font-style:normal;font-family:Poppins;font-weight:600;font-size:{14 if story else 12}px;letter-spacing:1px;margin-top:2px;color:rgba(255,255,255,.7);white-space:nowrap}}
.badge{{display:inline-block;background:linear-gradient(180deg,#E6C477,#B88A2E);color:#2E0119;font-weight:900;font-size:{26 if story else 23}px;border-radius:40px;padding:3px 22px 7px}}
.pill{{border-color:{GOLD}!important;color:{GOLD}}}'''
    return page(H, 'radial-gradient(120% 80% at 30% 20%,#7A0B47 0%,#51022D 45%,#2B0118 100%)', '#fff', body, story, LW,
                'PLAIN FACE MASK · 974 GUARDS', 39, 'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink='#fff')


# ---------- 2. Fitbit Fabric bands: colour arc ----------
FF = [('black', 'Black'), ('navy', 'Navy'), ('blue', 'Blue'), ('fog', 'Fog'), ('grey', 'Grey'), ('olive', 'Olive green'), ('lime', 'Lime green'),
      ('beige', 'Beige'), ('brown', 'Brown'), ('orange', 'Orange'), ('pinky-red', 'Pinky Red'), ('light-pink', 'Light pink'), ('purple', 'Purple')]


def fitfab(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#3B2320'; ACC = '#C2563A'
    C = R + 'products/fitbit-fabric-blush/src/'
    n = len(FF)
    cx = 540; cy = o + (1190 if story else 960); rx = 440 if story else 430; ry = 520 if story else 470; ih = 128 if story else 112
    arc = ''
    for i, (f, name) in enumerate(FF):
        a = math.pi * (1 - i / (n - 1))
        x = cx + rx * math.cos(a); y = cy - ry * math.sin(a)
        arc += f'<div class="ab" style="left:{x-60:.0f}px;top:{y-ih/2:.0f}px"><img src="file://{C}{f}-crop.png" style="height:{ih}px"></div>'
    body = f'''
<div class="abs" style="left:{cx-rx-90}px;top:{cy-ry-90}px;width:{2*rx+180}px;height:{2*ry+180}px;border-radius:50%;border:2px dashed rgba(194,86,58,.22)"></div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{78 if story else 68}px;line-height:1.08">الكل يسأل عنه.. <span style="color:{ACC}">جربته؟</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:10px;opacity:.75">سير قماش لـ <span class="en">Fitbit Air</span> · الأكثر طلباً هالشهر</div>
</div>
{arc}
<div class="abs" style="left:0;right:0;top:{cy-(250 if story else 230)}px;text-align:center;direction:rtl">
 <div style="font-weight:800;font-size:{30 if story else 27}px;opacity:.7">13 لون</div>
 <div class="en" style="font-weight:700;font-size:{170 if story else 150}px;line-height:1;color:{ACC}">74</div>
 <div style="font-weight:800;font-size:{30 if story else 27}px;margin-top:-6px">ريال بس</div>
 <div style="display:flex;gap:10px;justify-content:center;margin-top:18px">
  <span class="fx">ناعم على اليد</span><span class="fx">يتسكر باللزقة</span><span class="fx">للشباب والبنات</span>
 </div>
</div>'''
    extra = f'''.ab{{position:absolute;width:120px;display:flex;justify-content:center}} .ab img{{filter:drop-shadow(0 12px 14px rgba(90,40,25,.25))}}
.fx{{font-weight:800;font-size:{22 if story else 20}px;color:{ACC};border:1.5px solid rgba(194,86,58,.4);border-radius:40px;padding:3px 16px 6px;background:rgba(255,255,255,.5)}}'''
    return page(H, 'linear-gradient(170deg,#FFF6EF 0%,#FBE6DA 55%,#F6D9CB 100%)', INK, body, story, LB,
                'FITBIT AIR · FABRIC BAND', 74, 'اطلبه من <em>974group.net</em> 🛒', extra)


# ---------- 3. CIRQA magnetic: dark + lime magnet axis ----------
MG = [('black', 'Black'), ('grey', 'Grey'), ('white', 'White'), ('starlight', 'Starlight'), ('dark-blue', 'Dark Blue'),
      ('army-green', 'Army Green'), ('lime', 'Lime'), ('orange', 'Orange'), ('pink', 'Pink'), ('wine-red', 'Wine Red')]


def magnet(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; LIME = '#D7F23A'
    C = R + 'products/garmin-cirqa-magnetic/src/'
    ih = 220 if story else 178; cw = 196 if story else 196; x0 = (1080 - cw * 5) // 2
    y1 = o + (470 if story else 380); y2 = y1 + ih + (150 if story else 112)
    row = lambda items, y: ''.join(f'<div class="t" style="left:{x0+i*cw}px;top:{y}px;width:{cw}px"><img src="file://{C}{f}-crop.png" style="height:{ih}px"><i>{n}</i></div>' for i, (f, n) in enumerate(items))
    axis = y1 + ih + (62 if story else 46)
    body = f'''
<div class="abs" style="left:0;right:0;top:{axis}px;height:2px;background:linear-gradient(90deg,transparent,{LIME},transparent);box-shadow:0 0 24px {LIME}"></div>
<div class="abs en mg" style="left:46px;top:{axis-22}px">N</div><div class="abs en mg" style="right:46px;top:{axis-22}px">S</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{76 if story else 66}px;line-height:1.08">يتسكر بالمغناطيس..<br><span style="color:{LIME}">ثانية وخلاص</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:10px;opacity:.75">سير سيليكون مغناطيسي لـ <span class="en">Garmin CIRQA</span> · 10 ألوان</div>
</div>
{row(MG[:5], y1)}{row(MG[5:], y2)}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1330 if story else 1010)}px;display:flex;gap:10px;direction:rtl">
 <span class="fx">بدون قفل</span><span class="fx">ضد العرق والماء</span><span class="fx">مقاس واحد يركب الكل</span>
</div>'''
    extra = f'''.t{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.t img{{filter:drop-shadow(0 16px 18px rgba(0,0,0,.55))}}
.t i{{font-style:normal;font-family:Poppins;font-weight:600;font-size:{15 if story else 13}px;letter-spacing:1.5px;margin-top:10px;color:rgba(255,255,255,.65);text-transform:uppercase;white-space:nowrap}}
.mg{{font-weight:700;font-size:34px;color:{LIME};width:44px;height:44px;border:2px solid {LIME};border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1}}
.fx{{font-weight:800;font-size:{22 if story else 20}px;color:{LIME};border:1.5px solid rgba(215,242,58,.45);border-radius:40px;padding:3px 16px 6px}}
.pill{{border-color:{LIME}!important;color:{LIME}}}'''
    return page(H, 'radial-gradient(110% 70% at 50% 40%,#2A2C30 0%,#17181B 60%,#0E0F11 100%)', '#fff', body, story, LW,
                'GARMIN CIRQA · MAGNETIC', 99, 'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink='#fff')


# ---------- 4. Whoop 5.0 waterproof: water + rising staircase ----------
WP = [('black', 'Black'), ('grey', 'Grey'), ('blue', 'Blue'), ('orange', 'Orange'), ('maroon', 'Maroon')]


def water(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; AQ = '#7FE0FF'
    C = R + 'products/waterproof-logo/'
    ih = 250 if story else 215; step = 196; x0 = 32
    base = o + (1180 if story else 860); rise = 92 if story else 70
    stair = ''.join(f'<div class="t" style="left:{x0+i*step}px;top:{base-i*rise-ih}px;width:{ih}px"><img src="file://{C}{f}-engraved.png" style="height:{ih}px"><i>{n}</i></div>' for i, (f, n) in enumerate(WP))
    rip = ''.join(f'<div class="abs" style="left:{540-r}px;top:{base+40-r*0.28:.0f}px;width:{2*r}px;height:{r*0.56:.0f}px;border-radius:50%;border:1.5px solid rgba(127,224,255,{0.35-k*0.06:.2f})"></div>' for k, r in enumerate([160, 280, 400, 520, 640]))
    bub = ''.join(f'<div class="abs" style="left:{x}px;top:{o+y}px;width:{s}px;height:{s}px;border-radius:50%;border:1.5px solid rgba(255,255,255,.35)"></div>' for x, y, s in [(110, 300, 18), (930, 360, 26), (980, 520, 12), (60, 560, 14), (860, 260, 10), (180, 420, 9)])
    body = f'''{rip}{bub}
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{80 if story else 72}px;line-height:1.08">اسبح فيه.. <span style="color:{AQ}">عادي</span> 💧</div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:10px;opacity:.8">سير <span class="en">Whoop 5.0</span> و <span class="en">MG</span> ضد الماء · عليه شعار 974 محفور</div>
 <div style="display:flex;gap:10px;margin-top:18px;direction:rtl"><span class="fx">سباحة</span><span class="fx">جيم</span><span class="fx">شاور</span></div>
</div>
{stair}
<div class="abs ar" style="right:48px;left:48px;top:{base+(70 if story else 52)}px;font-weight:800;font-size:{27 if story else 24}px">مطفي بـ <b class="en">99</b> · لمّاع بـ <b class="en">109</b> <span style="opacity:.7">ر.ق</span></div>'''
    extra = f'''.t{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.t img{{filter:drop-shadow(0 18px 20px rgba(0,10,40,.5))}}
.t i{{font-style:normal;font-family:Poppins;font-weight:600;font-size:{15 if story else 13}px;letter-spacing:1.5px;margin-top:4px;color:rgba(255,255,255,.75);text-transform:uppercase}}
.fx{{font-weight:800;font-size:{22 if story else 20}px;color:#fff;background:rgba(127,224,255,.16);border:1.5px solid rgba(127,224,255,.5);border-radius:40px;padding:3px 16px 6px}}
.pill{{border-color:{AQ}!important;color:{AQ}}} .pill::before{{content:"من ";font-size:.7em}}'''
    return page(H, 'linear-gradient(180deg,#0B3A66 0%,#0A2A4D 55%,#06192F 100%)', '#fff', body, story, LW,
                'WHOOP 5.0 · MG · WATERPROOF', 99, 'اطلبه من <em>974group.net</em> 🛒', extra, pf_ink='#fff')


# ---------- 5. Goggles: desert dunes, hero + line-up ----------
GG = [('red', 'Red'), ('black', 'Black'), ('grey', 'Grey'), ('blue', 'Blue'), ('pink', 'Pink'), ('yellow', 'Yellow')]


def goggles(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#3A1E0E'; ACC = '#B5471B'
    C = R + 'posts/2026-11/summer-goggles/cut/'
    hero_w = 760 if story else 640
    hero_top = o + (330 if story else 290)
    rest = GG[1:]
    rw = 196 if story else 196
    ry = o + (960 if story else 760)
    x0 = (1080 - rw * 5) // 2
    line = ''.join(f'<div class="t" style="left:{x0+i*rw}px;top:{ry}px;width:{rw}px"><img src="file://{C}{f}.png" style="width:{rw-14}px"><i>{n}</i></div>' for i, (f, n) in enumerate(rest))
    dunes = f'''<svg class="abs" style="left:0;top:{o+(620 if story else 520)}px" width="1080" height="1500" viewBox="0 0 1080 1500"><path d="M0 220 C220 120 380 260 560 190 S900 90 1080 170 L1080 1500 L0 1500Z" fill="rgba(214,140,80,.22)"/><path d="M0 330 C200 260 420 380 640 300 S960 240 1080 300 L1080 1500 L0 1500Z" fill="rgba(190,105,55,.18)"/></svg>'''
    body = f'''{dunes}
<div class="abs" style="left:{540-260}px;top:{o+(200 if story else 170)}px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(255,196,120,.55),rgba(255,196,120,0) 70%)"></div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{80 if story else 70}px;line-height:1.08">جهّز طلعة <span style="color:{ACC}">البر</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:8px;opacity:.75">نظارات <span class="en">974 Guards</span> · عدسة تحمي من الشمس والغبار</div>
</div>
<img class="abs" src="file://{C}red.png" style="left:{(1080-hero_w)//2}px;top:{hero_top}px;width:{hero_w}px;filter:drop-shadow(0 30px 34px rgba(80,30,5,.35))">
{line}
<div class="abs ar" style="right:48px;left:48px;top:{ry+(205 if story else 175)}px;display:flex;gap:10px;direction:rtl">
 <span class="fx">بايك</span><span class="fx">بقي</span><span class="fx">ساند بورد</span><span class="fx">6 ألوان</span>
</div>'''
    extra = f'''.t{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.t img{{filter:drop-shadow(0 12px 14px rgba(80,30,5,.3))}}
.t i{{font-style:normal;font-family:Poppins;font-weight:700;font-size:{15 if story else 13}px;letter-spacing:1.5px;margin-top:6px;color:{ACC};text-transform:uppercase}}
.fx{{font-weight:800;font-size:{22 if story else 20}px;color:{INK};border:1.5px solid rgba(58,30,14,.3);border-radius:40px;padding:3px 16px 6px;background:rgba(255,255,255,.35)}}
.pill::before{{content:"من ";font-size:.7em}}'''
    return page(H, 'linear-gradient(180deg,#FFE7C4 0%,#F8CC96 50%,#EDB07A 100%)', INK, body, story, LB,
                '974 GUARDS · GOGGLES', 209, 'اطلبه من <em>974group.net</em> 🛒', extra)


# ---------- 6. CIRQA fabric 3.0: editorial lookbook (colour panel + swatch strip) ----------
C3 = [('purple', 'Purple'), ('pink', 'Pink'), ('light-pink', 'Light pink'), ('navy', 'Navy'), ('green', 'Green'), ('orange', 'Orange'), ('black', 'Black'), ('cement-gray', 'Cement Gray')]


def cirqa3(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#2A1F3D'; ACC = '#6E4FC2'
    C = R + 'products/garmin-cirqa-fabric3/cut/'
    pw, ph = (500, 640) if story else (470, 620)
    py = o + (150 if story else 120)
    panel = f'''<div class="abs" style="left:48px;top:{py}px;width:{pw}px;height:{ph}px;border-radius:36px;background:linear-gradient(160deg,#DCD3F7 0%,#C2B4EE 100%)"></div>
<div class="abs en" style="left:{48+pw-190}px;top:{py+ph-110}px;width:170px;text-align:right;font-weight:700;font-size:88px;line-height:1;color:rgba(255,255,255,.7);letter-spacing:-3px">3.0</div>
<img class="abs" src="file://{C}purple.png" style="left:{48+(pw-int((ph-120)*0.764))//2}px;top:{py+40}px;height:{ph-130}px;filter:drop-shadow(0 26px 30px rgba(60,40,110,.35))">
<div class="abs en" style="left:70px;top:{py+ph-48}px;font-weight:700;font-size:15px;letter-spacing:3px;color:#fff">PURPLE</div>'''
    tx = 48 + pw + 36
    text = f'''<div class="abs ar" style="right:48px;left:{tx}px;top:{py+20}px">
 <div style="font-weight:800;font-size:{24 if story else 22}px;color:{ACC}">الأكثر مبيعاً من CIRQA</div>
 <div style="font-weight:900;font-size:{74 if story else 66}px;line-height:1.1;margin-top:8px">خفيف..<br>ويتسكر<br><span style="color:{ACC}">باللزقة</span></div>
 <div style="font-weight:700;font-size:{25 if story else 22}px;margin-top:14px;opacity:.8;line-height:1.5">سير قماش لـ<br><span class="en">Garmin CIRQA fabric 3.0</span></div>
 <div class="sz"><span>S/M</span><span>L/XL</span></div>
 <div class="bo">سير فقط · بدون الجهاز</div>
</div>'''
    if story:
        cols, cw, ih, y0, gy = 4, 230, 170, py + ph + 56, 228
    else:
        cols, cw, ih, y0, gy = 8, 124, 118, py + ph + 42, 0
    x0 = (1080 - cw * cols) // 2
    strip = ''.join(f'<div class="t" style="left:{x0+(i%cols)*cw}px;top:{y0+(i//cols)*gy}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{ih}px"><i>{n}</i></div>' for i, (f, n) in enumerate(C3))
    body = panel + text + strip + f'''
<div class="abs ar" style="right:48px;left:48px;top:{y0+(gy+ih+48 if story else ih+50)}px;font-weight:800;font-size:{27 if story else 23}px">8 ألوان · مقاسين · <span style="color:{ACC}">109 ر.ق</span></div>'''
    extra = f'''.t{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.t img{{filter:drop-shadow(0 10px 12px rgba(60,40,110,.22))}}
.t i{{font-style:normal;font-family:Poppins;font-weight:700;font-size:{15 if story else 12}px;letter-spacing:1px;margin-top:8px;opacity:.7;white-space:nowrap;text-transform:uppercase}}
.sz{{display:flex;gap:10px;margin-top:18px;justify-content:flex-end;direction:ltr}} .sz span{{font-family:Poppins;font-weight:700;font-size:22px;border:2px solid {INK};border-radius:30px;padding:2px 18px}}
.bo{{display:inline-block;margin-top:16px;font-weight:800;font-size:{21 if story else 19}px;border:1.5px dashed currentColor;border-radius:30px;padding:2px 16px 4px;opacity:.75}}'''
    return page(H, 'linear-gradient(180deg,#FBF9FE 0%,#F1ECFA 100%)', INK, body, story, LB,
                'GARMIN CIRQA · FABRIC 3.0', 109, 'اطلبه من <em>974group.net</em> 🛒', extra)


F = {'mask': mask, 'fitfab': fitfab, 'magnet': magnet, 'water': water, 'goggles': goggles, 'cirqa3': cirqa3}
if __name__ == '__main__':
    os.chdir(D)
    for k in (sys.argv[1:] or F):
        shot(f'974-{k}-post', F[k](), 1350); shot(f'974-{k}-story', F[k](True), 1920)
