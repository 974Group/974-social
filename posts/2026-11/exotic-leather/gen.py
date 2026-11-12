# Exotic leather drop (12 Nov 2026) — three designs, post + story each:
#  new      : the 5 new bands, each labelled with its leather (light, soft blush-ivory)
#  restock  : the 5 bands back in stock + Edition X box (dark charcoal / silver)
#  himalayan: Himalayan alone — 15 unique pieces, pick your own (warm studio, open-box render)
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
D = '/home/claude/974-social/posts/2026-11/exotic-leather/'
C = D + 'cut/'
PK = '/home/claude/974-social/products/packaging-edition-x/'

NEW = [('white-python', 'بايثون أبيض', 'جلد بايثون طبيعي', 299, True),
       ('black-python', 'بايثون أسود', 'جلد بايثون طبيعي', 299, True),
       ('pink-lizard', 'سحلية وردي', 'جلد سحلية طبيعي', 299, True),
       ('ivory-ostrich', 'نعام عاجي', 'جلد طبيعي بنقشة نعام', 199, False),
       ('holographic-croc', 'هولوغرافيك', 'جلد طبيعي بنقشة كروك', 199, False)]
BACK = [('pink-python', 'بايثون وردي', 'جلد بايثون طبيعي', 299),
        ('grey-python', 'بايثون رصاصي', 'جلد بايثون طبيعي', 299),
        ('natural-python', 'بايثون طبيعي', 'جلد بايثون طبيعي', 299),
        ('natural-lizard', 'سحلية طبيعي', 'جلد سحلية طبيعي', 299),
        ('himalayan', 'هيمالايا', 'جلد تمساح طبيعي', 849)]

def row(items, top, bh, ink, sub_op, story, cw=200):
    x0 = (1080 - cw * len(items)) // 2; h = ''
    for i, it in enumerate(items):
        f, nm, lt, pr = it[:4]
        h += f'''<div class="it" style="left:{x0+i*cw}px;top:{top}px;width:{cw}px">
 <img src="file://{C}{f}.png" style="height:{bh}px">
 <b>{nm}</b><span>{lt}</span><em class="en">{pr} <small>QAR</small></em></div>'''
    return h

ITCSS = lambda ink, shadow, sz: f'''.it{{position:absolute;display:flex;flex-direction:column;align-items:center;text-align:center}}
.it img{{filter:drop-shadow({shadow})}}
.it b{{font-weight:900;font-size:{sz}px;margin-top:22px;line-height:1.1;white-space:nowrap}}
.it span{{font-weight:700;font-size:{sz-9}px;opacity:.68;margin-top:4px;width:180px;line-height:1.25}}
.it em{{font-style:normal;font-weight:700;font-size:{sz-6}px;margin-top:8px;letter-spacing:.5px}} .it em small{{font-size:.62em;letter-spacing:2px;opacity:.7}}'''

def new(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#2A1A1E'; ACC = '#720842'
    bh = 505 if story else 470
    body = f'''
<div class="abs en" style="left:0;right:0;top:{o+(330 if story else 250)}px;text-align:center;font-weight:700;font-size:{300 if story else 270}px;line-height:.8;letter-spacing:-6px;color:rgba(114,8,66,.05)">EXOTIC</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 112)}px">
 <div style="font-weight:900;font-size:{80 if story else 70}px;line-height:1.05">وصلت.. <span style="color:{ACC}">5 جلود جديدة</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:10px;opacity:.75">سيور جلد لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
{row(NEW, o+(440 if story else 285), bh, INK, .7, story)}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1260 if story else 990)}px;display:flex;align-items:center;gap:14px;direction:rtl">
 <div class="box">✦ الجلد الطبيعي يوصلك في بوكس <span class="en">EDITION X</span></div>
</div>'''
    extra = ITCSS(INK, '0 22px 26px rgba(60,20,30,.22)', 28 if story else 24) + f'''
.box{{font-weight:800;font-size:{24 if story else 21}px;color:{ACC};border:1.5px solid rgba(114,8,66,.35);border-radius:40px;padding:6px 20px 8px}}
.pill{{background:{ACC};color:#fff;border:none!important}}'''
    return page(H, 'radial-gradient(90% 60% at 50% 45%,#FBF7F5 0%,#F3ECE9 60%,#EADFDB 100%)', INK, body, story, LB,
                'WHOOP 5.0 · MG · EXOTIC LEATHER', 'من 199', 'اطلبه من <em>974group.net</em> 🛒', extra)

def restock(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#F2EFEA'; SIL = '#C9CDD3'
    bh = 505 if story else 430
    body = f'''
<div class="abs" style="left:0;right:0;top:{o+(520 if story else 330)}px;height:{bh+40}px;background:radial-gradient(60% 55% at 50% 50%,rgba(255,255,255,.07),transparent 70%)"></div>
<img class="abs" src="file://{D}cut/box-closed.png" style="left:{40 if story else 36}px;top:{o+(160 if story else 118)}px;width:{290 if story else 240}px;transform:rotate(-8deg);filter:drop-shadow(0 22px 26px rgba(0,0,0,.55))">
<div class="abs ar" style="right:48px;left:{360 if story else 310}px;top:{o+(140 if story else 112)}px">
 <div style="font-weight:900;font-size:{78 if story else 68}px;line-height:1.05">رجعت<br><span style="color:{SIL}">متوفرة</span></div>
 <div style="font-weight:700;font-size:{27 if story else 24}px;margin-top:12px;opacity:.75">الكمية محدودة.. وكلها جلد طبيعي<br>توصلك في بوكس <span class="en">EDITION X</span></div>
</div>
{row(BACK, o+(600 if story else 375), bh, INK, .7, story)}'''
    extra = ITCSS(INK, '0 24px 30px rgba(0,0,0,.6)', 28 if story else 24) + f'''
.it em{{color:{SIL}}} .pill{{background:{INK};color:#151618;border:none!important}}'''
    return page(H, 'radial-gradient(120% 90% at 50% 35%,#24262B 0%,#17181B 60%,#101113 100%)', INK, body, story, LW,
                'WHOOP 5.0 · MG · BACK IN STOCK', 'من 299', 'علّق <em>«جلد»</em> ونرسل لك الرابط 📩', extra, pf_ink=INK)

def himalayan(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#2B2420'; ACC = '#7A5C48'
    hero = 640 if story else 560
    bh = 800 if story else 600
    body = f'''
<img class="abs" src="file://{C}box-open-band.png" style="left:{24 if story else 30}px;top:{o+(470 if story else 360)}px;width:{hero}px;filter:drop-shadow(0 24px 28px rgba(60,40,30,.25))">
<img class="abs" src="file://{C}himalayan.png" style="right:{40 if story else 60}px;top:{o+(400 if story else 360)}px;height:{bh}px;filter:drop-shadow(0 28px 32px rgba(60,40,30,.32))">
<div class="abs ar" style="right:48px;left:48px;top:{o+(130 if story else 108)}px">
 <div class="en" style="font-weight:700;font-size:{19 if story else 17}px;letter-spacing:6px;color:{ACC}">HIMALAYAN CROCODILE</div>
 <div style="font-weight:900;font-size:{84 if story else 72}px;line-height:1.05;margin-top:6px">15 قطعة..<br><span style="color:{ACC}">ولا وحدة تشبه الثانية</span></div>
 <div style="font-weight:700;font-size:{28 if story else 25}px;margin-top:12px;opacity:.78">جلد تمساح هيمالايا طبيعي · كل قطعة نقشتها ودرجتها غير</div>
</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1255 if story else 985)}px">
 <div class="pick"><b>اختار قطعتك بنفسك</b><span>نرسل لك صور الـ15 قطعة وتختار النقشة واللون اللي يعجبك</span></div>
</div>'''
    extra = f'''.pick{{display:flex;flex-direction:column;gap:4px;border-right:4px solid {ACC};padding-right:18px}}
.pick b{{font-weight:900;font-size:{36 if story else 31}px}} .pick span{{font-weight:700;font-size:{24 if story else 21}px;opacity:.75}}
.pill{{background:{INK};color:#F1E7DF;border:none!important}}'''
    return page(H, 'radial-gradient(90% 70% at 50% 50%,#F1E6DF 0%,#ECE0D8 60%,#E3D5CB 100%)', INK, body, story, LB,
                'WHOOP 5.0 · MG · LIMITED 15', 849, 'علّق <em>«هيمالايا»</em> ونرسل لك القطع 📩', extra)

if __name__ == '__main__':
    os.chdir(D)
    F = {'new': new, 'restock': restock, 'himalayan': himalayan}
    for k in (sys.argv[1:] or F):
        shot(f'974-exotic-{k}-post', F[k](), 1350); shot(f'974-exotic-{k}-story', F[k](True), 1920)
