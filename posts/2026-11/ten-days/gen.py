# 10 regular posts + stories for 24 Nov – 3 Dec 2026 (10:00 each). Full prices, in-stock colours only, a fresh layout per product.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
R = '/home/claude/974-social/'; P = R + 'posts/2026-11/'
LOGO_B, LOGO_W = G.LB, G.LW
BASE = G.CTA_CSS + '''.pill{display:inline-block;border-radius:30px;padding:3px 18px 7px;font-weight:800;font-size:22px}
.price{font-weight:900;font-size:30px;direction:rtl}.price .en{font-size:74px;font-weight:900}'''


def head(logo, tag, ink):
    return (f'<img class="abs" src="file://{logo}" style="left:48px;top:46px;height:46px">'
            f'<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:16px;letter-spacing:4px;color:{ink};opacity:.75">{tag}</div>')


def bottom(price, cta, ink, cbg, cfg, top=1150, pre=''):
    return (f'<div class="abs" style="left:48px;right:48px;top:{top}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">'
            f'<div class="price" style="color:{ink}">{pre}<span class="en">{price}</span> ر.ق</div>{G.cta(cta, cbg, cfg)}</div>')


# 1 ROLEX — white studio, quote led, four bands in a row
def rolex():
    C = R + 'refs/rolex/'; ink = '#13213F'
    row = ''.join(f'<img src="file://{C}{f}.png" style="height:250px;filter:drop-shadow(0 18px 18px rgba(0,0,0,.18))">' for f in ['r18', 'r19', 'r20', 'r21'])
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(180deg,#FFFFFF 0%,#EEF0F4 100%)"></div><!--/bk-->
{head(LOGO_B, 'WHOOP 5.0 · MG · SOFT FABRIC', ink)}
<div class="abs en" style="left:0;right:0;top:200px;text-align:center;font-weight:900;font-style:italic;font-size:64px;line-height:1.05;color:{ink}">"Who cares,<br>I'm already late"</div>
<div class="abs ar" style="left:48px;right:48px;top:390px;text-align:center;font-weight:800;font-size:32px;color:#3a4766">الجملة اللي الكل يسألنا عنها.. صارت على سيرك</div>
<div class="abs" style="left:0;right:0;top:540px;display:flex;justify-content:center;gap:10px">{row}</div>
<div class="abs" style="left:48px;right:48px;top:880px;display:flex;gap:12px;justify-content:center;direction:rtl">
 <span class="pill" style="background:{ink};color:#fff">طباعة <span class="en">3D</span> بارزة</span><span class="pill" style="background:#E3E7EF;color:{ink}">قماش ناعم</span><span class="pill" style="background:#E3E7EF;color:{ink}">سير فقط بدون الجهاز</span></div>
<div class="abs ar" style="left:48px;right:48px;top:960px;text-align:center;font-weight:800;font-size:24px;color:#59647d">الأكثر مبيعاً عندنا 🔥</div>
{bottom('159', 'اطلبه الحين', ink, ink, '#fff', 1080)}'''
    return G.doc('#EEF0F4', ink, body, extra=BASE)


# 2 الماسك — colour mosaic with a big "23"
def mask():
    C = P + 'face-mask/src/cut/'; ink = '#1C1C1C'
    cols = ['black', 'white', 'red', 'orange', 'grey', 'green', 'skyblue', 'royalblue', 'pink', 'lightgreen', 'navy', 'armygreen',
            'lightpurple', 'darkgrey', 'brightred', 'purple', 'cream', 'brown', 'khaki', 'beige', 'babyblue', 'lilac', 'hotpink']
    tiles = ''.join(f'<div class="t"><img src="file://{C}{c}.png"></div>' for c in cols[:15])
    css = BASE + '.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.t{background:#fff;border-radius:22px;height:150px;display:flex;align-items:center;justify-content:center}.t img{height:128px}'
    body = f'''<div class="abs" style="inset:0;background:#F2EFEA"></div><!--/bk-->
{head(LOGO_B, '974 GUARDS · FACE MASK', ink)}
<div class="abs ar" style="right:48px;top:40px;color:{ink}">
 <div style="font-weight:900;font-size:70px;line-height:1.08">الماسك اللي<br>الكل لابسه</div></div>
<div class="abs" style="left:48px;top:150px;display:flex;align-items:baseline;gap:10px;color:{ink}"><span class="en" style="font-weight:900;font-size:120px;line-height:1">23</span><span style="font-weight:900;font-size:34px">لون</span></div>
<div class="abs" style="left:48px;right:48px;top:300px"><div class="grid">{tiles}</div></div>
<div class="abs" style="left:48px;right:48px;top:830px;display:flex;gap:12px;justify-content:center;direction:rtl;flex-wrap:wrap">
 <span class="pill" style="background:{ink};color:#fff">شمس وغبار وهوا</span><span class="pill" style="background:#fff;color:{ink}">خفيف ويتنفس</span><span class="pill" style="background:#fff;color:{ink}">للبر والسيكل والطلعات</span></div>
<div class="abs ar" style="left:48px;right:48px;top:910px;text-align:center;font-weight:700;font-size:24px;color:#555">و٨ ألوان ثانية بالموقع</div>
{bottom('39', 'اختار لونك', ink, ink, '#fff', 1080)}'''
    return G.doc('#F2EFEA', ink, body, extra=css)


# 3 2 IN 1 goggles — staircase cascade on deep sea-to-sand split
def goggles():
    C = P + 'summer-goggles/cut/'; ink = '#fff'
    items = [('yellow', 'Yellow', '209'), ('pink', 'Pink', '209'), ('red', 'Red', '249'), ('blue', 'Blue', '249'), ('grey', 'Grey', '249'), ('black', 'Black', '249')]
    st = '<div class="abs" style="left:40px;right:40px;top:330px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px 14px">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:4px"><img src="file://{C}{k}.png" style="width:310px;filter:drop-shadow(0 14px 14px rgba(0,0,0,.35))"><span class="en" style="font-weight:700;font-size:20px;color:#fff">{n} · {p}</span></div>' for k, n, p in items) + '</div>'
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(160deg,#0B4F6C 0%,#0B4F6C 46%,#C99A5B 46.2%,#E2BE86 100%)"></div><!--/bk-->
{head(LOGO_W, '974 GUARDS · 2 IN 1', '#fff')}
<div class="abs ar" style="right:48px;top:40px;color:{ink}">
 <div style="font-weight:900;font-size:76px;line-height:1.05">بر وبحر 🌊🏜️</div>
 <div style="font-weight:800;font-size:30px;margin-top:6px;opacity:.95">بالستراب للبر.. وبدونه نظارة شمسية</div></div>
{st}
<div class="abs ar" style="left:48px;right:48px;top:960px;display:flex;gap:12px;direction:rtl;justify-content:center">
 <span class="pill" style="background:#0B4F6C;color:#fff">بولارايز + <span class="en">UV</span></span><span class="pill" style="background:#fff;color:#0B4F6C">عدستين بالعلبة</span></div>
{bottom('209', 'اطلبها الحين', '#2B1A06', '#0B4F6C', '#fff', 1080, pre='من ')}'''
    return G.doc('#E2BE86', ink, body, extra=BASE)


# 4 CIRQA fabric 3.0 — split: big orange hero left, colour list right
def cirqa3():
    C = R + 'products/garmin-cirqa-fabric3/cut/'; ink = '#1B1B1F'
    cols = [('orange', 'Orange', '#E9631F'), ('black', 'Black', '#1d1d1f'), ('green', 'Green', '#2F4A30'), ('pink', 'Pink', '#E79BB0'),
            ('purple', 'Purple', '#8E78C9'), ('light-pink', 'Light Pink', '#F1C9CF'), ('cement-gray', 'Cement Gray', '#9C978E'), ('navy', 'Navy', '#22305A')]
    lst = ''.join(f'<div style="display:flex;align-items:center;gap:14px;direction:ltr"><img src="file://{C}{k}.png" style="height:84px"><span class="en" style="font-weight:700;font-size:22px">{n}</span></div>' for k, n, c in cols[1:])
    body = f'''<div class="abs" style="inset:0;background:#F5F2EE"></div><div class="abs" style="left:0;top:0;bottom:0;width:560px;background:linear-gradient(180deg,#F07A35,#D9551A)"></div><!--/bk-->
{head(LOGO_W, 'GARMIN CIRQA · FABRIC 3.0', '#fff')}
<div class="abs ar" style="left:600px;right:48px;top:44px;color:{ink}"><div style="font-weight:900;font-size:56px;line-height:1.1">قماش يتنفس..<br>ويتسكر باللزقة</div></div>
<img class="abs" src="file://{C}orange.png" style="left:40px;top:260px;width:480px;filter:drop-shadow(0 26px 26px rgba(80,20,0,.35))">
<div class="abs en" style="left:48px;top:800px;color:#fff;font-weight:700;font-size:24px">Orange</div>
<div class="abs" style="left:620px;right:40px;top:250px;display:flex;flex-direction:column;gap:10px;color:{ink}">{lst}</div>
<div class="abs ar" style="left:48px;right:600px;top:880px;color:#fff;font-weight:800;font-size:26px;line-height:1.4">مقاسين: <span class="en">S/M</span> و <span class="en">L/XL</span></div>
<div class="abs ar" style="left:600px;right:48px;top:960px;font-weight:700;font-size:22px;color:#555">للمعصم.. ويتلبس على الذراع بعد</div>
{bottom('109', 'اختار لونك', ink, ink, '#fff', 1080)}'''
    return G.doc('#F5F2EE', ink, body, pf_ink=ink, extra=BASE)


# 5 Pilates Club socks — clothesline
def pilates():
    C = P + 'pilates-socks/src/'; ink = '#5B2333'
    ks = ['cherrybow', 'pinkbow', 'coffee', 'juice', 'lemonade', 'orange', 'peach', 'cherrystripe']
    line = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;transform:rotate({(-4 if i%2 else 4)}deg)"><div style="width:16px;height:34px;background:#C9A24B;border-radius:4px;margin-bottom:-8px;z-index:2"></div><img src="file://{C}{k}.png" style="height:250px"></div>' for i, k in enumerate(ks))
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 40%,#FFF4F4 0%,#FBE1E4 70%,#F6CDD3 100%)"></div><!--/bk-->
{head(LOGO_B, 'PILATES CLUB · GRIP SOCKS', ink)}
<div class="abs ar" style="right:48px;top:40px;color:{ink}"><div style="font-weight:900;font-size:66px;line-height:1.1">دلاغات بيلاتيس 🎀<br><span style="font-size:44px">ثابتة على الريفورمر</span></div></div>
<svg class="abs" style="left:0;top:322px" width="1080" height="60"><path d="M0 10 Q540 70 1080 10" stroke="#5B2333" stroke-width="3" fill="none"/></svg>
<div class="abs" style="left:10px;right:10px;top:330px;display:flex;justify-content:space-between">{line[:len(line)//2] if False else ''}</div>
<div class="abs" style="left:20px;right:20px;top:338px;display:grid;grid-template-columns:repeat(4,1fr);row-gap:40px;justify-items:center">{line}</div>
<div class="abs" style="left:48px;right:48px;top:960px;display:flex;gap:12px;justify-content:center;direction:rtl;flex-wrap:wrap">
 <span class="pill" style="background:{ink};color:#fff">تطريز مب طباعة</span><span class="pill" style="background:#fff;color:{ink}">نعل سيليكون ضد الزلق</span><span class="pill" style="background:#fff;color:{ink}"><span class="en">12</span> تصميم</span></div>
{bottom('49', 'اختاري تصميمك', ink, ink, '#fff', 1060, pre='')}
<div class="abs ar" style="right:48px;top:1140px;font-weight:800;font-size:24px;color:{ink}">أي ٣ بـ <span class="en">134</span> ر.ق</div>'''
    return G.doc('#FBE1E4', ink, body, extra=BASE)


# 6 Maroon Whoop silicone — cream, callout zooms
def maroon():
    C = P + 'maroon-qatar/cut/'; ink = '#5C0A1D'
    z = lambda f, l, t, lab: f'<div class="abs" style="left:{l}px;top:{t}px;display:flex;flex-direction:column;align-items:center;gap:6px"><img src="file://{C}{f}" style="width:190px;height:190px;border-radius:50%;border:6px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.18);object-fit:cover"><span style="font-weight:800;font-size:22px;color:{ink}">{lab}</span></div>'
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(70% 50% at 50% 45%,#FFFFFF 0%,#F4EEE8 70%,#EADFD5 100%)"></div><!--/bk-->
{head(LOGO_B, 'WHOOP 5.0 · MG · SILICONE', ink)}
<div class="abs ar" style="right:48px;top:40px;color:{ink}"><div style="font-weight:900;font-size:72px;line-height:1.08">العنابي 🇶🇦</div><div style="font-weight:800;font-size:30px;margin-top:4px">لون علمنا.. على معصمك</div></div>
<img class="abs" src="file://{C}p49m-0.png" style="left:315px;top:270px;height:560px;filter:drop-shadow(0 30px 30px rgba(60,0,10,.28))">
{z('zoom-maroon.png', 48, 300, 'عنابي من برا')}{z('zoom-white.png', 48, 610, 'أبيض من داخل')}{z('zoom-clasp.png', 850, 520, 'قفل فضي لمّاع')}
<div class="abs" style="left:48px;right:48px;top:920px;display:flex;gap:12px;justify-content:center;direction:rtl">
 <span class="pill" style="background:{ink};color:#fff">سيليكون ناعم</span><span class="pill" style="background:#fff;color:{ink}">للتمرين والنوم</span><span class="pill" style="background:#fff;color:{ink}"><span class="en">5.0</span> و <span class="en">MG</span></span></div>
{bottom('99', 'اطلبه الحين', ink, ink, '#fff', 1060)}'''
    return G.doc('#F4EEE8', ink, body, extra=BASE)


# 7 LUSAIL — magazine cover
def lusail():
    C = P + 'sunglasses/cut/'; ink = '#E8EEF6'
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(180deg,#2B3342 0%,#141820 100%)"></div><!--/bk-->
<img class="abs" src="file://{LOGO_W}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:52px;font-weight:700;font-size:18px;letter-spacing:5px;color:#B6C9DD">25.42° N · MADE TO LEAD</div>
<div class="abs en" style="left:0;right:0;top:120px;text-align:center;font-weight:900;font-size:210px;letter-spacing:-4px;line-height:1;color:{ink}">LUSAIL</div>
<img class="abs" src="file://{C}lusail-hero.png" style="left:150px;top:330px;width:780px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.55))">
<div class="abs ar" style="left:48px;right:48px;top:845px;text-align:center;color:#fff"><div style="font-weight:900;font-size:56px">جري وسيكل.. بدون إطار</div><div style="font-weight:700;font-size:26px;color:#B6C9DD;margin-top:4px">عدسة وحدة تعطيك رؤية واسعة وحماية ضد الصدمات</div></div>
<div class="abs" style="left:48px;right:48px;top:990px;display:flex;justify-content:center;gap:40px;direction:rtl">
 <div style="display:flex;align-items:center;gap:10px"><img src="file://{C}lusail-clear.png" style="height:60px"><span style="font-weight:800;font-size:22px;color:#fff">☁️ بالظل</span></div>
 <span style="font-family:Poppins;color:#B6C9DD;font-size:34px">←</span>
 <div style="display:flex;align-items:center;gap:10px"><img src="file://{C}lusail-dark.png" style="height:60px"><span style="font-weight:800;font-size:22px;color:#fff">☀️ بالشمس</span></div></div>
{bottom('319', 'اطلبها الحين', '#fff', '#B6C9DD', '#141820', 1100)}'''
    return G.doc('#141820', '#fff', body, pf_ink='#fff', extra=BASE)


# 8 Garmin CIRQA magnetic — tinted tiles 5x2 on navy
def gmag():
    C = P + 'garmin-magnetic/cut/'; ink = '#fff'
    cols = [('black', 'Black', '#3a3a3e'), ('white', 'White', '#d9dbe0'), ('starlight', 'Starlight', '#e6dccb'), ('grey', 'Grey', '#9a9ca2'), ('dark-blue', 'Dark Blue', '#27345c'),
            ('wine-red', 'Wine Red', '#6e2433'), ('pink', 'Pink', '#e9c3cc'), ('orange', 'Orange', '#f08a2c'), ('lime', 'Lime', '#cfe03a'), ('army-green', 'Army Green', '#6f7a55')]
    tiles = ''.join(f'<div style="background:{c};border-radius:24px;height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px"><img src="file://{C}{k}.png" style="height:170px;filter:drop-shadow(0 10px 10px rgba(0,0,0,.25))"><span class="en" style="font-weight:700;font-size:15px;color:{"#141414" if k in ("white","starlight","pink","lime","grey") else "#fff"}">{n}</span></div>' for k, n, c in cols)
    body = f'''<div class="abs" style="inset:0;background:#0F1730"></div><!--/bk-->
{head(LOGO_W, 'GARMIN CIRQA · MAGNETIC', '#fff')}
<div class="abs ar" style="right:48px;top:40px;color:{ink}"><div style="font-weight:900;font-size:68px;line-height:1.08">بدون قفل 🧲<br><span style="color:#CFE03A">يتسكر بالمغناطيس</span></div></div>
<div class="abs" style="left:48px;right:48px;top:290px;display:grid;grid-template-columns:repeat(5,1fr);gap:14px">{tiles}</div>
<div class="abs" style="left:48px;right:48px;top:850px;display:flex;gap:12px;justify-content:center;direction:rtl">
 <span class="pill" style="background:#CFE03A;color:#0F1730"><span class="en">10</span> ألوان</span><span class="pill" style="background:#1E2A4E;color:#fff">يتضبط على أي معصم بثانية</span><span class="pill" style="background:#1E2A4E;color:#fff">ضد العرق</span></div>
{bottom('99', 'اختار لونك', '#fff', '#CFE03A', '#0F1730', 1060)}'''
    return G.doc('#0F1730', '#fff', body, pf_ink='#fff', extra=BASE)


# 9 Fitbit Air magnetic woven — hero + strip
def fitair():
    C = R + 'products/fitbit-air-magnetic/'; ink = '#2A1B12'
    rest = ['black', 'dark-blue', 'green', 'dark-gray', 'light-gray', 'starlight', 'white']
    names = {'black': 'Black', 'dark-blue': 'Dark Blue', 'green': 'Green', 'dark-gray': 'Dark Gray', 'light-gray': 'Light Gray', 'starlight': 'Starlight', 'white': 'White'}
    strip = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><img src="file://{C}{k}-cut.png" style="height:130px"><span class="en" style="font-weight:700;font-size:14px;color:#6b5547">{names[k]}</span></div>' for k in rest)
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(180deg,#F7EDE6 0%,#EBD8CB 100%)"></div><div class="abs" style="left:290px;top:250px;width:500px;height:500px;border-radius:50%;background:#7A1F2B;opacity:.12"></div><!--/bk-->
{head(LOGO_B, 'FITBIT AIR · MAGNETIC WOVEN', ink)}
<div class="abs ar" style="right:48px;top:40px;color:{ink}"><div style="font-weight:900;font-size:66px;line-height:1.08">منسوج ويتمطط..<br><span style="color:#8E2232">ويتسكر بالمغناطيس</span></div></div>
<img class="abs" src="file://{C}wine-red-cut.png" style="left:340px;top:270px;height:470px;filter:drop-shadow(0 24px 24px rgba(60,10,10,.3))">
<div class="abs en" style="left:0;right:0;top:760px;text-align:center;font-weight:700;font-size:20px;letter-spacing:3px;color:#8E2232">WINE RED</div>
<div class="abs" style="left:30px;right:30px;top:820px;display:flex;justify-content:space-between">{strip}</div>
<div class="abs" style="left:48px;right:48px;top:1010px;display:flex;gap:12px;justify-content:center;direction:rtl">
 <span class="pill" style="background:{ink};color:#fff">خفيف ومريح</span><span class="pill" style="background:#fff;color:{ink}">يتضبط على أي معصم</span></div>
{bottom('89', 'اختار لونك', ink, '#8E2232', '#fff', 1090)}'''
    return G.doc('#EBD8CB', ink, body, extra=BASE)


# 10 Silver & Black goggles — light silver, lens duo
def silver():
    C = P + 'silver-black-goggles/cut/'; ink = '#16181C'
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(135deg,#F4F5F7 0%,#D6D9DE 55%,#B9BEC6 100%)"></div><!--/bk-->
{head(LOGO_B, 'SILVER & BLACK EDITION', ink)}
<div class="abs ar" style="right:48px;top:40px;color:{ink}"><div style="font-weight:900;font-size:70px;line-height:1.08">عدسة للنهار..<br>وعدسة لليل</div></div>
<img class="abs" src="file://{C}0c.png" style="left:150px;top:260px;width:780px;filter:drop-shadow(0 30px 30px rgba(0,0,0,.30))">
<div class="abs" style="left:48px;right:48px;top:790px;display:flex;gap:18px;direction:rtl">
 <div style="flex:1;background:#16181C;color:#fff;border-radius:26px;padding:20px 24px"><div style="font-weight:900;font-size:34px">مغناطيس</div><div style="font-weight:700;font-size:22px;opacity:.8">تبدّل العدسة بثواني</div></div>
 <div style="flex:1;background:#fff;color:{ink};border-radius:26px;padding:20px 24px"><div style="font-weight:900;font-size:34px">ضد الضباب</div><div style="font-weight:700;font-size:22px;opacity:.7">رؤية واضحة طول الطلعة</div></div>
 <div style="flex:1;background:#fff;color:{ink};border-radius:26px;padding:20px 24px"><div style="font-weight:900;font-size:34px">عدستين</div><div style="font-weight:700;font-size:22px;opacity:.7">شمس + شفافة بالعلبة</div></div></div>
<div class="abs ar" style="left:48px;right:48px;top:965px;text-align:center;font-weight:800;font-size:26px;color:#3b3f47">للبر والتزلج 🏔️</div>
{bottom('319', 'اطلبها الحين', ink, ink, '#fff', 1060)}'''
    return G.doc('#D6D9DE', ink, body, extra=BASE)


F = dict(rolex=rolex, mask=mask, goggles=goggles, cirqa3=cirqa3, pilates=pilates, maroon=maroon, lusail=lusail, gmag=gmag, fitair=fitair, silver=silver)
if __name__ == '__main__':
    for k in (sys.argv[1:] or F):
        G.STORY = False; G.shot(f'974-{k}-post', F[k]())
        G.STORY = True; G.shot(f'974-{k}-story', F[k](), 1920)
    print('ok')
