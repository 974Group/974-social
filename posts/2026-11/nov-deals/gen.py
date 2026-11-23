# November daily deals — announcement + day 1 (iPhone 18 cases 40%), post + story each. 14 Nov 2026 18:00
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/nov-deals/'
S = D + 'src/'
LOGOW = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
M = '#720842'; DK = '#3A0222'; GOLD = '#D4AF55'; LIME = GOLD  # owner: all neon → gold
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'PoppinsB';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}'''


def tape(top, rot, txt, bg=LIME, fg=DK, H=None):
    s = (txt + '  ✦  ') * 12
    return f'<div class="tape" style="top:{top}px;transform:rotate({rot}deg);background:{bg};color:{fg}"><span>{s}</span></div>'


def base(story, body):
    H = 1920 if story else 1350
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;font-family:Cairo;color:#fff;position:relative;overflow:hidden;
background:radial-gradient(900px 700px at 80% 20%,#9C0B5A 0%,transparent 60%),radial-gradient(800px 700px at 0% 100%,#4A022B 0%,transparent 60%),{M}}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.10) 2.2px,transparent 2.6px);background-size:22px 22px;-webkit-mask-image:linear-gradient(160deg,#000 0%,transparent 55%);mask-image:linear-gradient(160deg,#000 0%,transparent 55%)}}
.tape{{position:absolute;left:-120px;width:1320px;height:58px;display:flex;align-items:center;overflow:hidden;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.tape span{{white-space:nowrap;font-family:PoppinsB;font-weight:900;font-size:26px;letter-spacing:2px}}
.logo{{position:absolute;height:46px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12, text='#fff', label='#fff')}
.big{{font-family:PoppinsB;font-weight:900;line-height:.8;letter-spacing:-6px;direction:ltr}}
.out{{color:transparent;-webkit-text-stroke:4px {LIME}}}
.khasm{{display:inline-block;background:{LIME};color:{DK};font-weight:900;border-radius:26px;transform:rotate(-6deg);box-shadow:8px 8px 0 {DK}}}
.sticker{{position:absolute;width:190px;height:190px;border-radius:50%;background:{GOLD};color:{DK};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(12deg);box-shadow:6px 6px 0 {DK};font-weight:900;line-height:1.1}}
</style></head><body><div class="dots"></div>{body}<div class="pf">{payfoot.html()}</div></body></html>'''


def announce(story):
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS</div>
<div style="position:absolute;left:0;right:0;top:{o+(120 if not story else 150)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(46*k)}px;color:{LIME}">موسم الخصومات بدأ 🔥</div>
  <div style="font-weight:900;font-size:{int(104*k)}px;line-height:1.1;margin-top:6px">كل يوم..<br><span class="khasm" style="font-size:{int(96*k)}px;padding:0 34px 12px">خصم جديد</span></div>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(520 if not story else 640)}px;text-align:center">
  <div style="font-weight:800;font-size:{int(34*k)}px;direction:rtl">لين</div>
  <div class="big out" style="font-size:{int(300*k)}px">40%</div>
</div>
{tape(o+(905 if not story else 1000), -4, 'DAILY DEAL  ✦  عرض اليوم')}
<div style="position:absolute;left:60px;right:60px;top:{o+(1000 if not story else 1100)}px;direction:rtl;text-align:center;font-weight:800;font-size:{int(28*k)}px;line-height:1.55">
  كل يوم منتج مختلف بخصم <b style="color:{LIME}">35% لين 40%</b><br>العرض ٢٤ ساعة بس.. <b style="color:{LIME}">تابعنا</b> عشان ما يفوتك</div>'''
    return base(story, body)


def day1(story):
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    ph = int(300 * k)
    cases = [('cloudy-gray', 'Cloudy'), ('solid-black', 'Solid'), ('fading-blue', 'Fading')]
    imgs = ''
    cw = int(300 * k); gap = 20
    x0 = (1080 - (3 * cw + 2 * gap)) // 2
    for i, (f, nm) in enumerate(cases):
        imgs += f'<img src="file://{S}{f}-c.png" style="position:absolute;left:{x0+i*(cw+gap)}px;top:{o+(560 if not story else 665)}px;width:{cw}px;height:{int(cw*1.18)}px;object-fit:contain;filter:drop-shadow(0 18px 20px rgba(0,0,0,.45))">'
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS · DAY 1</div>
<div style="position:absolute;left:40px;right:40px;top:{o+(110 if not story else 140)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <span class="khasm" style="font-size:{int(118*k)}px;padding:0 30px 14px;background:{GOLD}">خصم</span>
  <span class="big" style="font-size:{int(250*k)}px;color:{GOLD};text-shadow:8px 8px 0 {DK}">40%</span>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(400 if not story else 470)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(52*k)}px">كفرات <span style="font-family:Poppins">iPhone 18</span></div>
  <div style="font-weight:800;font-size:{int(26*k)}px;color:{LIME};margin-top:2px">تركب على <span style="font-family:Poppins">iPhone 17</span> و <span style="font-family:Poppins">18</span> · Pro و Pro Max</div>
</div>
{imgs}
<div class="sticker" style="left:{36 if not story else 30}px;top:{o+(470 if not story else 620)}px"><span style="font-size:22px">بس</span><span style="font-family:PoppinsB;font-size:52px">24</span><span style="font-size:22px">ساعة</span></div>
{tape(o+(935 if not story else 1060), 3, 'عرض اليوم  ✦  DAY 1  ✦  NOVEMBER DEALS', bg=GOLD)}
<div style="position:absolute;left:48px;right:48px;top:{o+(1025 if not story else 1140)}px;display:flex;justify-content:center;gap:16px;direction:rtl">
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px">Solid · Cloudy</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">69</s> 41.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px">Fading</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">79</s> 47.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(1140 if not story else 1262)}px;text-align:center;direction:rtl;font-weight:800;font-size:{int(22*k)}px;opacity:.9">الخصم ينزل تلقائي في الموقع · ينتهي بكرة الساعة ٦ المغرب ⏳</div>'''
    return base(story, body)


V1 = '/home/claude/974-social/products/garmin-cirqa-silicone-v1/cut/'
V2 = '/home/claude/974-social/products/garmin-cirqa-silicone-v2/src/'


def day2(story):
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    rows = [(V2, ['black', 'lime', 'midnight-blue', 'mousse-pink', 'orange'], '-crop.png', 'CIRQA 2.0', '89', '53.40'),
            (V1, ['army-green', 'white', 'navy', 'dusty-pink', 'lemon'], '.png', 'CIRQA', '99', '59.40')]
    cw = 180 if not story else 190; gap = 14
    x0 = (1080 - (5 * cw + 4 * gap)) // 2
    imgs = ''
    for r, (d, cols, suf, nm, was, now) in enumerate(rows):
        y = o + (548 if not story else 640) + r * (198 if not story else 212)
        for i, c in enumerate(cols):
            imgs += f'<img src="file://{d}{c}{suf}" style="position:absolute;left:{x0+i*(cw+gap)}px;top:{y}px;width:{cw}px;height:{int(cw*0.95)}px;object-fit:contain;filter:drop-shadow(0 12px 14px rgba(0,0,0,.45))">'
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS · DAY 2</div>
<div style="position:absolute;left:40px;right:40px;top:{o+(110 if not story else 140)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <span class="khasm" style="font-size:{int(118*k)}px;padding:0 30px 14px;background:{GOLD}">خصم</span>
  <span class="big" style="font-size:{int(250*k)}px;color:{GOLD};text-shadow:8px 8px 0 {DK}">40%</span>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(400 if not story else 470)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(50*k)}px">سيور سيليكون <span style="font-family:Poppins">Garmin CIRQA</span></div>
  <div style="font-weight:800;font-size:{int(26*k)}px;color:{LIME};margin-top:2px">٢٠ لون · CIRQA و CIRQA 2.0</div>
</div>
{imgs}
<div class="sticker" style="left:{30}px;top:{o+(470 if not story else 545)}px;width:150px;height:150px"><span style="font-size:19px">بس</span><span style="font-family:PoppinsB;font-size:44px">24</span><span style="font-size:19px">ساعة</span></div>
{tape(o+(965 if not story else 1045), 3, 'عرض اليوم  ✦  DAY 2  ✦  NOVEMBER DEALS', bg=GOLD)}
<div style="position:absolute;left:48px;right:48px;top:{o+(1050 if not story else 1125)}px;display:flex;justify-content:center;gap:16px;direction:rtl">
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px;font-family:Poppins">CIRQA 2.0</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">89</s> 53.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px;font-family:Poppins">CIRQA</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">99</s> 59.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(1160 if not story else 1243)}px;text-align:center;direction:rtl;font-weight:800;font-size:{int(22*k)}px;opacity:.9">الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳</div>'''
    return base(story, body)


FB = '/home/claude/974-social/products/fitbit-silicone-v1/uni/'
DR = '/home/claude/974-social/posts/2026-11/whoop5-silicone-all/cut/'


def deal(story, day, title, sub, rows, cw, ch, rowgap, prices, note, extra='', pct='40%', ps=1.0, tmin=None, dy=0):
    """Generic daily-deal layout (same look as day 1/2). rows: list of lists of image paths."""
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    imgs = ''
    gap = 14
    top0 = o + (548 if not story else 640) + dy
    for r, row in enumerate(rows):
        n = len(row); x0 = (1080 - (n * cw + (n - 1) * gap)) // 2
        y = top0 + r * rowgap
        for i, f in enumerate(row):
            imgs += f'<img src="file://{f}" style="position:absolute;left:{x0+i*(cw+gap)}px;top:{y}px;width:{cw}px;height:{ch}px;object-fit:contain;filter:drop-shadow(0 12px 14px rgba(0,0,0,.45))">'
    after = top0 + len(rows) * rowgap
    tape_y = max(after + 10, o + (965 if not story else 1045)) if tmin is None else max(after + 10, tmin)
    chips = ''.join(f'<div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px">{lab}</div><div style="font-family:{'PoppinsB' if ps>1 else 'Poppins'};font-weight:{900 if ps>1 else 700};font-size:{int(34*k*ps)}px;line-height:1.15;direction:ltr"><s style="opacity:.45;font-size:{'.38em' if ps>1 else '.6em'};text-decoration-thickness:3px">{was}</s> {now} <small style="font-family:Cairo;font-size:{'.38em' if ps>1 else '.55em'}">ر.ق</small></div></div>' for lab, was, now in prices)
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS · DAY {day}</div>
<div style="position:absolute;left:40px;right:40px;top:{o+(110 if not story else 140)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <span class="khasm" style="font-size:{int(118*k)}px;padding:0 30px 14px;background:{GOLD}">خصم</span>
  <span class="big" style="font-size:{int(250*k)}px;color:{GOLD};text-shadow:8px 8px 0 {DK}">{pct}</span>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(400 if not story else 470)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(50*k)}px">{title}</div>
  <div style="font-weight:800;font-size:{int(26*k)}px;color:{LIME};margin-top:2px">{sub}</div>
</div>
{imgs}{extra}
<div class="sticker" style="left:30px;top:{o+(470 if not story else 545)}px;width:150px;height:150px"><span style="font-size:19px">بس</span><span style="font-family:PoppinsB;font-size:44px">24</span><span style="font-size:19px">ساعة</span></div>
{tape(tape_y, 3, f'عرض اليوم  ✦  DAY {day}  ✦  NOVEMBER DEALS', bg=GOLD)}
<div style="position:absolute;left:48px;right:48px;top:{tape_y+(85 if not story else 80)}px;display:flex;justify-content:center;gap:16px;direction:rtl">{chips}</div>
<div style="position:absolute;left:0;right:0;top:{tape_y+int((195 if not story else 198)+(ps-1)*42*k)}px;text-align:center;direction:rtl;font-weight:800;font-size:{int(22*k)}px;opacity:.9">{note}</div>'''
    return base(story, body)


def day3(story):
    order = ['black', 'white', 'grey', 'navy', 'maroon', 'pink', 'tiffany', 'orange', 'lavender', 'green',
             'red', 'brown', 'beige', 'blue-grey', 'light-pink', 'grey-blue', 'dark-grey', 'darker-grey', 'darker-beige']
    pics = [FB + c + '.png' for c in order[:12]]
    rows = [pics[:6], pics[6:12]]
    cw = 140 if not story else 150
    return deal(story, 3, 'سيور سيليكون <span style="font-family:Poppins">Fitbit</span>', '١٩ لون · كلها متوفرة', rows, cw, int(cw * 1.34),
                200 if not story else 225, [('Fitbit سيليكون', '69', '41.40')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳')


def day4(story):
    pics = [DR + 'drenched.png', DR + 'drenched-green.png', DR + 'drenched-orange.png']
    cw = 300 if not story else 310
    return deal(story, 4, 'سيور <span style="font-family:Poppins">Drenched</span> سيليكون', 'لـ <span style="font-family:Poppins">Whoop 5.0 و MG</span> · سير فقط بدون الجهاز', [pics], cw, int(cw * 1.14),
                380 if not story else 410, [('Drenched', '99', '59.40')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳')


GG = '/home/claude/974-social/posts/2026-11/goggles-guide/cut/'


def day5(story):
    cw = 560 if not story else 600
    return deal(story, 5, 'نظارة <span style="font-family:Poppins">Photochromic</span>', 'عدسة ذكية تغمق في الشمس وترجع شفافة بالليل', [[GG + 'photochromic.png']], cw, int(cw * 0.55),
                320 if not story else 345, [('Photochromic', '349', '226.85')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='35%', ps=2.3, tmin=0)


SFC = '/home/claude/974-social/products/whoop5-soft-fabric/cut/'


def day6(story):
    order = ['onyx', 'cloud', 'forest', 'phoenix', 'twilight', 'desert', 'granite', 'orange', 'pink', 'sky', 'dune']
    pics = [SFC + c + '.png' for c in order]
    rows = [pics[:6], pics[6:]]
    cw = 130 if not story else 136
    return deal(story, 6, 'سيور <span style="font-family:Poppins">Soft Fabric</span> لـ <span style="font-family:Poppins">Whoop</span>', '١١ لون · كلها عليها الخصم', rows, cw, int(cw * 1.15),
                160 if not story else 160, [('Soft Fabric · يبدأ من', '89', '57.85')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='35%', ps=2.1, tmin=0, dy=(100 if not story else 62))


AL = '/home/claude/974-social/products/apple-loops/cut/'


def day7(story):
    rows = [[AL + f + '.png' for f in ('alpine-black', 'alpine-starlight', 'ocean-orange', 'ocean-white')],
            [AL + f + '.png' for f in ('trail-blue-grey', 'trail-navy-orange', 'trail-orange', 'trail-yellow-beige')]]
    cw = 180 if not story else 178
    return deal(story, 7, 'سيور <span style="font-family:Poppins">Apple Watch</span>', '<span style="font-family:Poppins">Alpine · Ocean · Trail Loop</span>', rows, cw, cw,
                cw + 18, [('Alpine', '79', '47.40'), ('Ocean', '59', '35.40'), ('Trail', '79', '47.40')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='40%', ps=1.3, tmin=0, dy=(40 if not story else 20))


FT = '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers/fitbit-trim/'


def day8(story):
    order = ['black-L', 'grey', 'navy', 'blue', 'fog', 'olive', 'lime', 'beige', 'light-pink', 'pinky-red', 'purple', 'orange']
    import os
    pics = [FT + c + '.png' for c in order if os.path.exists(FT + c + '.png')]
    rows = [pics[:6], pics[6:]]
    cw = 130 if not story else 136
    return deal(story, 8, 'سيور قماش <span style="font-family:Poppins">Fitbit Air</span>', 'كل الألوان عليها الخصم · سير فقط بدون الجهاز', rows, cw, int(cw * 1.2),
                cw * 1.2 + 16, [('Fitbit Fabric', '74', '48.10')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='35%', ps=2.1, tmin=0, dy=(70 if not story else 30))


WPC = '/home/claude/974-social/posts/2026-11/waterproof/src/cut/'


def day9(story):
    pics = [WPC + c + '.png' for c in ('black1', 'blue', 'grey', 'lime', 'maroon', 'orange', 'rust')]
    rows = [pics[:4], pics[4:]]
    cw = 165 if not story else 175
    return deal(story, 9, 'سيور <span style="font-family:Poppins">Waterproof</span> لـ <span style="font-family:Poppins">Whoop</span>', 'اسبح فيه · ٧ ألوان · سير فقط بدون الجهاز', rows, cw, int(cw * 1.13),
                int(cw * 1.13) + 16, [('مطفي', '99', '59.40'), ('لمّاع', '109', '65.40')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='40%', ps=1.4, tmin=0, dy=(40 if not story else 0))



def day10(story):
    GM = '/home/claude/974-social/posts/2026-11/garmin-magnetic/cut/'
    pics = [GM + c + '.png' for c in ('black', 'white-clean', 'starlight-clean', 'grey', 'dark-blue', 'wine-red', 'pink-clean', 'orange', 'lime', 'army-green')]
    rows = [pics[:5], pics[5:]]
    cw = 150 if not story else 128
    return deal(story, 10, 'سيور <span style="font-family:Poppins">Garmin CIRQA</span> المغناطيس', 'بدون قفل · يتسكر بالمغناطيس · ١٠ ألوان', rows, cw, int(cw * 1.15),
                int(cw * 1.15) + 16, [('كل الألوان', '99', '64.35')], 'الخصم ينزل تلقائي في الموقع · ينتهي بعد ٢٤ ساعة ⏳', pct='35%', ps=2.1, tmin=0, dy=(40 if not story else 10))

def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('all', 'day1'):
        shot(announce(False), D + 'out/974-nov-deals-announce-post.png', 1350)
        shot(announce(True), D + 'out/974-nov-deals-announce-story.png', 1920)
        shot(day1(False), D + 'out/974-nov-deals-day1-cases-post.png', 1350)
        shot(day1(True), D + 'out/974-nov-deals-day1-cases-story.png', 1920)
    if which in ('all', 'day2'):
        shot(day2(False), D + 'out/974-nov-deals-day2-cirqa-post.png', 1350)
        shot(day2(True), D + 'out/974-nov-deals-day2-cirqa-story.png', 1920)
    if which in ('all', 'day3'):
        shot(day3(False), D + 'out/974-nov-deals-day3-fitbit-post.png', 1350)
        shot(day3(True), D + 'out/974-nov-deals-day3-fitbit-story.png', 1920)
    if which in ('all', 'day4'):
        shot(day4(False), D + 'out/974-nov-deals-day4-drenched-post.png', 1350)
        shot(day4(True), D + 'out/974-nov-deals-day4-drenched-story.png', 1920)
    if which in ('all', 'day5'):
        shot(day5(False), D + 'out/974-nov-deals-day5-photochromic-post.png', 1350)
        shot(day5(True), D + 'out/974-nov-deals-day5-photochromic-story.png', 1920)
    if which in ('all', 'day6'):
        shot(day6(False), D + 'out/974-nov-deals-day6-softfabric-post.png', 1350)
        shot(day6(True), D + 'out/974-nov-deals-day6-softfabric-story.png', 1920)
    if which in ('all', 'day7'):
        shot(day7(False), D + 'out/974-nov-deals-day7-apple-loops-post.png', 1350)
        shot(day7(True), D + 'out/974-nov-deals-day7-apple-loops-story.png', 1920)
    print('ok')
    if which in ('all', 'day8'):
        shot(day8(False), D + 'out/974-nov-deals-day8-fitbit-fabric-post.png', 1350)
        shot(day8(True), D + 'out/974-nov-deals-day8-fitbit-fabric-story.png', 1920)
    if which in ('all', 'day9'):
        shot(day9(False), D + 'out/974-nov-deals-day9-waterproof-post.png', 1350)
        shot(day9(True), D + 'out/974-nov-deals-day9-waterproof-story.png', 1920)
    if which in ('all', 'day10'):
        shot(day10(False), D + 'out/974-nov-deals-day10-cirqa-magnetic-post.png', 1350)
        shot(day10(True), D + 'out/974-nov-deals-day10-cirqa-magnetic-story.png', 1920)
