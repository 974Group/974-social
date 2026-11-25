# Burgundy Friday product stories: one every 2 h, Thu 26 Nov 02:00 → Fri 27 Nov 22:00. 40% off, website only. Six rotating layouts.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
R = '/home/claude/974-social/'; P = R + 'posts/2026-11/'
BUR, DEEP, GOLD, CREAM = '#720842', '#51022D', '#C9A24B', '#F4F1F2'
def p(*a): return [R + x for x in a]
def off(v): return '%.2f' % round(v * 0.6, 2)

S = [  # time, key, Arabic title, English line, images, old price, template, prefix
 ('Thu 02:00', 'rolex', 'سير الروليكس', 'ROLEX · WHOOP 5.0 / MG', p('refs/rolex/r18.png', 'refs/rolex/r19.png', 'refs/rolex/r20.png'), 159, 'slash', ''),
 ('Thu 04:00', 'goggles2in1', 'نظارات <bdi dir="ltr">2 in 1</bdi>', 'بر وبحر · 974 GUARDS', p('posts/2026-11/summer-goggles/cut/yellow.png', 'posts/2026-11/summer-goggles/cut/pink.png', 'posts/2026-11/summer-goggles/cut/black.png'), 209, 'split', 'من '),
 ('Thu 06:00', 'softfabric', 'سيور Whoop القماش', 'WHOOP SOFT FABRIC · 11 COLOURS', p(*[f'products/whoop5-soft-fabric/cut/{c}.png' for c in ['desert', 'onyx', 'pink', 'sky', 'forest', 'orange']]), 89, 'grid', 'من '),
 ('Thu 08:00', 'fitbitfabric', 'سيور Fitbit القماش', 'FITBIT FABRIC · يتسكر باللزقة', p(*[f'posts/2026-11/ig-ads-best-sellers/fitbit-trim/{c}.png' for c in ['grey', 'navy', 'olive', 'light-pink']]), 74, 'tape', 'من '),
 ('Thu 10:00', 'cirqa2', 'سيور CIRQA سيليكون 2.0', 'GARMIN CIRQA · SILICONE 2.0', p(*[f'posts/2026-11/cirqa-silicone-2-v3/cut/{c}.png' for c in ['orange', 'lime', 'mousse-pink', 'midnight-blue']]), 89, 'receipt', ''),
 ('Thu 12:00', 'halul', 'نظارة HALUL', 'HALUL 25.67° N · فوتوكروميك', p('posts/2026-11/halul-carousel/src/story2.jpg'), 319, 'photo', ''),
 ('Thu 14:00', 'mask', 'الماسك', 'FACE MASK · 23 COLOURS', p(*[f'posts/2026-11/face-mask/src/cut/{c}.png' for c in ['red', 'black', 'royalblue', 'khaki', 'pink', 'green']]), 39, 'grid', ''),
 ('Thu 16:00', 'loops', 'سيور Trail و Alpine', 'APPLE WATCH LOOPS', p('products/apple-loops/cut/trail-orange.png', 'products/apple-loops/cut/alpine-black.png', 'products/apple-loops/cut/trail-navy-orange.png'), 79, 'slash', ''),
 ('Thu 18:00', 'photochromic', 'نظارة Photochromic', 'بالليل شفافة · بالشمس تغمق', p('posts/2026-11/photochromic-v2/src/front-dark.png'), 349, 'split', ''),
 ('Thu 20:00', 'waterproof', 'سيور Whoop الووتربروف', 'WATERPROOF · اسبح فيه', p(*[f'posts/2026-11/waterproof/src/cut/{c}.png' for c in ['maroon', 'black1', 'lime', 'orange']]), 99, 'tape', 'من '),
 ('Thu 22:00', 'fitair', 'سيور Fitbit Air المنسوجة', 'FITBIT AIR · MAGNETIC WOVEN', p('products/fitbit-air-magnetic/wine-red-cut.png', 'products/fitbit-air-magnetic/green-cut.png', 'products/fitbit-air-magnetic/dark-blue-cut.png'), 89, 'receipt', ''),
 ('Fri 00:00', 'maroon', 'سير Whoop العنابي', 'لون علمنا 🇶🇦', p('posts/2026-11/maroon-qatar/cut/p49m-0.png'), 99, 'spot', ''),
 ('Fri 02:00', 'cirqamag', 'سيور CIRQA المغناطيس', 'GARMIN CIRQA · MAGNETIC', p(*[f'posts/2026-11/garmin-magnetic/cut/{c}.png' for c in ['orange', 'lime', 'black', 'pink-clean', 'dark-blue', 'wine-red']]), 99, 'grid', ''),
 ('Fri 04:00', 'green', 'نظارة Green Edition', '974 GUARDS · GREEN', p('products/goggles/green-edition-render.png'), 319, 'slash', ''),
 ('Fri 06:00', 'pilates', 'دلاغات البيلاتيس', 'PILATES CLUB · GRIP SOCKS', p(*[f'posts/2026-11/pilates-socks/src/{c}.png' for c in ['cherrybow', 'coffee', 'lemonade']]), 49, 'split', ''),
 ('Fri 08:00', 'sealine', 'نظارة SEALINE', 'SEALINE 24.85° N · فوتوكروميك', p('posts/2026-11/sunglasses/cut/sealine-hero.png'), 319, 'tape', ''),
 ('Fri 10:00', 'pearl', 'نظارة THE PEARL', 'THE PEARL 25.37° N · فوتوكروميك', p('posts/2026-11/sunglasses/cut/pearl-hero.png'), 319, 'receipt', ''),
 ('Fri 12:00', 'cirqa3', 'سيور CIRQA القماش 3.0', 'GARMIN CIRQA · FABRIC 3.0', p(*[f'products/garmin-cirqa-fabric3/cut/{c}.png' for c in ['orange', 'pink', 'purple', 'navy']]), 109, 'spot', ''),
 ('Fri 14:00', 'doha', 'نظارة DOHA', 'DOHA 25.28° N · وردية', p('posts/2026-11/sunglasses/cut/doha-hero.png'), 319, 'slash', ''),
 ('Fri 16:00', 'mxclear', 'نظارة MX Clear', 'MX CLEAR · للبر', p('posts/2026-11/mx-clear/cut/black.png', 'posts/2026-11/mx-clear/cut/white.png'), 109, 'split', ''),
 ('Fri 18:00', 'quickfit', 'سيور Garmin QuickFit', 'QUICKFIT 20mm', p(*[f'products/garmin-20mm-quickfit/cut/{c}.png' for c in ['orange', 'turquoise', 'lightgreen', 'babyblue', 'white', 'green']]), 99, 'grid', ''),
 ('Fri 20:00', 'silver', 'نظارة Silver & Black', 'عدسة للنهار + عدسة لليل', p('posts/2026-11/silver-black-goggles/cut/0c.png'), 319, 'tape', ''),
 ('Fri 22:00', 'lastcall', '', '', [], 0, 'last', ''),
]

CSS = G.CTA_CSS + f'''.en{{font-family:Poppins}}.ar{{font-family:Cairo;direction:rtl}}
.tag{{font-family:Poppins;font-weight:800;font-size:17px;letter-spacing:4px}}
.old{{font-family:Poppins;font-weight:700;font-size:56px;text-decoration:line-through;text-decoration-thickness:5px;opacity:.65}}
.new{{font-family:Poppins;font-weight:900;font-size:128px;line-height:1}}
.qar{{font-family:Cairo;font-weight:900;font-size:34px}}
.badge{{direction:ltr;font-family:Poppins;font-weight:900;color:{DEEP};background:{GOLD};border-radius:50%;display:flex;align-items:center;justify-content:center}}
.note{{font-family:Cairo;font-weight:800;font-size:22px;direction:rtl;text-align:center}}
.row{{display:flex;justify-content:center;align-items:flex-end}}
.row img{{object-fit:contain;filter:drop-shadow(0 18px 20px rgba(0,0,0,.35))}}'''


def head(ink, logo):
    return (f'<img class="abs" src="file://{logo}" style="left:48px;top:20px;height:44px">'
            f'<div class="abs tag" style="right:48px;top:30px;color:{GOLD}">BURGUNDY FRIDAY · -40%</div>')


def imgs(L, H, W=980, gap=-30):
    n = len(L); w = min(W // n - 10, 820)
    return f'<div class="row" style="gap:0;width:{W}px;height:{H}px">' + ''.join(
        f'<img src="file://{x}" style="width:{w}px;max-height:{H}px;margin:0 5px">' for x in L) + '</div>'


def price(old, pre, ink, newc, align='center'):
    return (f'<div style="display:flex;flex-direction:column;align-items:{align};direction:rtl">'
            f'<div class="old" style="color:{ink}">{pre}{old} <span class="qar" style="text-decoration:none">ر.ق</span></div>'
            f'<div style="display:flex;align-items:baseline;gap:10px;direction:rtl"><span class="new" style="color:{newc}">{off(old)}</span><span class="qar" style="color:{newc}">ر.ق</span></div></div>')


NOTE = 'للطلبات من الموقع فقط · ما يجتمع مع عروض ثانية'


def slash(t, ar, en, L, old, pre):
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(85% 55% at 50% 42%,#8E1756 0%,{BUR} 45%,{DEEP} 100%)"></div><!--/bk-->{head('#fff', G.LW)}
<div class="abs ar" style="left:48px;right:48px;top:110px;text-align:center;color:#fff;font-weight:900;font-size:66px">{ar}</div>
<div class="abs en" style="left:0;right:0;top:205px;text-align:center;color:{GOLD};font-weight:700;font-size:22px;letter-spacing:3px">{en}</div>
<div class="abs" style="left:50px;top:270px">{imgs(L, 560)}</div>
<div class="abs badge" style="right:60px;top:280px;width:170px;height:170px;font-size:52px;transform:rotate(-10deg)">-40%</div>
<div class="abs" style="left:0;right:0;top:860px">{price(old, pre, '#fff', GOLD)}</div>
<div class="abs note" style="left:48px;right:48px;top:1110px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1170px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)


def split(t, ar, en, L, old, pre):
    body = f'''<div class="abs" style="inset:0;background:{CREAM}"></div><div class="abs" style="left:0;right:0;bottom:0;height:52%;background:{BUR};border-radius:70px 70px 0 0"></div><!--/bk-->{head(DEEP, G.LB)}
<div class="abs" style="left:50px;top:140px">{imgs(L, 520)}</div>
<div class="abs ar" style="left:48px;right:48px;top:690px;color:#fff;text-align:right"><div style="font-weight:900;font-size:64px;line-height:1.1">{ar}</div>
 <div class="en" style="font-weight:700;font-size:22px;letter-spacing:2px;color:{GOLD};direction:ltr;text-align:right">{en}</div></div>
<div class="abs" style="left:48px;right:48px;top:850px;display:flex;justify-content:space-between;align-items:center;direction:rtl">
 {price(old, pre, '#fff', GOLD, 'flex-start')}<div class="badge" style="width:200px;height:200px;font-size:60px">-40%</div></div>
<div class="abs note" style="left:48px;right:48px;top:1110px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1170px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc(BUR, '#fff', body, pf_ink='#fff', extra=CSS)


def grid(t, ar, en, L, old, pre):
    n = len(L); cols = 3 if n >= 6 else 2
    cells = ''.join(f'<div style="background:rgba(255,255,255,.07);border:1px solid rgba(201,162,75,.35);border-radius:28px;height:{250 if n >= 6 else 300}px;display:flex;align-items:center;justify-content:center"><img src="file://{x}" style="max-height:88%;max-width:88%;object-fit:contain;filter:drop-shadow(0 10px 12px rgba(0,0,0,.4))"></div>' for x in L)
    body = f'''<div class="abs" style="inset:0;background:{DEEP}"></div><div class="abs" style="inset:0;background-image:radial-gradient(rgba(201,162,75,.12) 1.5px,transparent 1.6px);background-size:28px 28px"></div><!--/bk-->{head('#fff', G.LW)}
<div class="abs ar" style="left:48px;right:48px;top:100px;color:#fff;text-align:center"><div style="font-weight:900;font-size:62px">{ar}</div><div class="en" style="font-weight:700;font-size:20px;letter-spacing:3px;color:{GOLD}">{en}</div></div>
<div class="abs" style="left:60px;right:60px;top:270px;display:grid;grid-template-columns:repeat({cols},1fr);gap:18px">{cells}</div>
<div class="abs" style="left:60px;right:60px;top:{830 if n >= 6 else 920}px;display:flex;justify-content:space-between;align-items:center;direction:rtl">
 {price(old, pre, '#fff', GOLD, 'flex-start')}<div class="badge" style="width:180px;height:180px;font-size:54px;transform:rotate(8deg)">-40%</div></div>
<div class="abs note" style="left:48px;right:48px;top:1120px;color:#F4D9A0">{NOTE} · كل الألوان</div>
<div class="abs" style="left:0;right:0;top:1180px;display:flex;justify-content:center">{G.cta('اختار لونك', GOLD, DEEP)}</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)


def tape(t, ar, en, L, old, pre):
    txt = ' ✦ BURGUNDY FRIDAY ✦ -40%' * 6
    tp = lambda y, r: f'<div class="abs en" style="left:-200px;right:-200px;top:{y}px;transform:rotate({r}deg);background:{GOLD};color:{DEEP};font-weight:900;font-size:34px;white-space:nowrap;padding:10px 0;letter-spacing:2px;box-shadow:0 8px 20px rgba(0,0,0,.35)">{txt}</div>'
    body = f'''<div class="abs" style="inset:0;background:linear-gradient(160deg,#16090F 0%,{DEEP} 60%,{BUR} 100%)"></div>{tp(520, -9)}{tp(720, 7)}<!--/bk-->{head('#fff', G.LW)}
<div class="abs ar" style="left:48px;right:48px;top:110px;color:#fff;text-align:center"><div style="font-weight:900;font-size:66px">{ar}</div><div class="en" style="font-weight:700;font-size:20px;letter-spacing:3px;color:{GOLD}">{en}</div></div>
<div class="abs" style="left:50px;top:300px">{imgs(L, 520)}</div>
<div class="abs" style="left:0;right:0;top:880px">{price(old, pre, '#fff', '#fff')}</div>
<div class="abs note" style="left:48px;right:48px;top:1120px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1180px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)


def receipt(t, ar, en, L, old, pre):
    zz = ''.join(f'{x},{0 if (x // 30) % 2 == 0 else 24} ' for x in range(0, 841, 30))
    line = lambda a, b, c='#333', w=700, s=34: f'<div style="display:flex;justify-content:space-between;direction:rtl;font-family:Cairo;font-weight:{w};font-size:{s}px;color:{c};margin:10px 0"><span>{a}</span><span class="en" style="font-family:Poppins">{b}</span></div>'
    body = f'''<div class="abs" style="inset:0;background:{BUR}"></div><div class="abs" style="inset:0;background-image:repeating-linear-gradient(135deg,rgba(255,255,255,.04) 0 18px,transparent 18px 36px)"></div><!--/bk-->{head('#fff', G.LW)}
<div class="abs" style="left:50px;top:90px">{imgs(L, 420)}</div>
<div class="abs" style="left:120px;right:120px;top:530px;background:#FFFDF8;border-radius:22px 22px 0 0;padding:34px 46px 20px;box-shadow:0 20px 40px rgba(0,0,0,.35)">
 <div class="en" style="text-align:center;font-weight:800;font-size:18px;letter-spacing:5px;color:#888">974 · RECEIPT · BURGUNDY FRIDAY</div>
 <div class="ar" style="text-align:center;font-weight:900;font-size:46px;color:{DEEP};margin:10px 0 6px">{ar}</div>
 <div style="border-top:3px dashed #ccc;margin:14px 0"></div>
 {line('السعر', f'{pre}{old}')}{line('خصم', '-40%', BUR, 900)}
 <div style="border-top:3px dashed #ccc;margin:14px 0"></div>
 {line('الحين', f'{off(old)} QAR', DEEP, 900, 52)}
</div>
<svg class="abs" style="left:120px;top:{530+430}px" width="840" height="26"><polygon points="0,0 {zz} 840,0" fill="#FFFDF8"/></svg>
<div class="abs note" style="left:48px;right:48px;top:1110px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1170px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc(BUR, '#fff', body, pf_ink='#fff', extra=CSS)


def spot(t, ar, en, L, old, pre):
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(48% 30% at 50% 40%,rgba(201,162,75,.45) 0%,rgba(114,8,66,.6) 45%,#0D0508 100%)"></div><!--/bk-->{head('#fff', G.LW)}
<div class="abs en" style="left:0;right:0;top:180px;text-align:center;font-weight:900;font-size:330px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(201,162,75,.55)">-40%</div>
<div class="abs" style="left:50px;top:290px">{imgs(L, 520)}</div>
<div class="abs ar" style="left:48px;right:48px;top:830px;color:#fff;text-align:center"><div style="font-weight:900;font-size:58px">{ar}</div><div class="en" style="font-weight:700;font-size:20px;letter-spacing:3px;color:{GOLD}">{en}</div></div>
<div class="abs" style="left:0;right:0;top:955px;display:flex;justify-content:center;align-items:baseline;gap:26px;direction:rtl">
 <span class="old" style="color:#fff;font-size:46px">{pre}{old}</span><span class="new" style="color:{GOLD};font-size:104px">{off(old)}</span><span class="qar" style="color:{GOLD}">ر.ق</span></div>
<div class="abs note" style="left:48px;right:48px;top:1110px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1170px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc('#0D0508', '#fff', body, pf_ink='#fff', extra=CSS)


def last(*_):
    picks = p('refs/rolex/r18.png', 'posts/2026-11/sunglasses/cut/sealine-hero.png', 'posts/2026-11/summer-goggles/cut/yellow.png', 'products/whoop5-soft-fabric/cut/desert.png', 'posts/2026-11/garmin-magnetic/cut/orange.png', 'posts/2026-11/pilates-socks/src/cherrybow.png')
    cells = ''.join(f'<div style="height:230px;display:flex;align-items:center;justify-content:center"><img src="file://{x}" style="max-height:90%;max-width:92%;object-fit:contain;filter:drop-shadow(0 10px 12px rgba(0,0,0,.4))"></div>' for x in picks)
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 40%,#8E1756 0%,{BUR} 45%,{DEEP} 100%)"></div><!--/bk-->{head('#fff', G.LW)}
<div class="abs ar" style="left:48px;right:48px;top:100px;text-align:center;color:#fff"><div style="font-weight:900;font-size:44px;color:{GOLD}">آخر ساعتين ⏳</div>
 <div class="en" style="font-weight:900;font-size:120px;line-height:1">-40%</div><div style="font-weight:900;font-size:46px">على كل الموقع</div></div>
<div class="abs" style="left:60px;right:60px;top:470px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px">{cells}</div>
<div class="abs ar" style="left:48px;right:48px;top:965px;text-align:center;color:#fff;font-weight:900;font-size:40px">الخصم يخلص الليلة ١١:٥٩</div>
<div class="abs note" style="left:48px;right:48px;top:1035px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1100px;display:flex;justify-content:center">{G.cta('الحق قبل لا يخلص', GOLD, DEEP)}</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)


def photo(t, ar, en, L, old, pre):
    body = f'''<img class="abs" src="file://{L[0]}" style="left:-300px;top:0;width:1680px;height:1920px;object-fit:cover;filter:blur(40px)"><div class="abs" style="inset:0;background:rgba(244,241,242,.35)"></div>
<img class="abs" src="file://{L[0]}" style="left:-120px;top:420px;width:1320px;-webkit-mask-image:radial-gradient(closest-side at 50% 50%,#000 78%,transparent 100%)">
<div class="abs" style="left:0;right:0;bottom:0;height:1060px;background:linear-gradient(0deg,{DEEP} 0%,{DEEP} 62%,rgba(81,2,45,0) 100%)"></div><!--/bk-->{head('#fff', G.LB)}
<div class="abs badge" style="right:60px;top:120px;width:180px;height:180px;font-size:54px;transform:rotate(-10deg)">-40%</div>
<div class="abs ar" style="left:48px;right:48px;top:800px;color:#fff;text-align:center"><div style="font-weight:900;font-size:66px">{ar}</div><div class="en" style="font-weight:700;font-size:20px;letter-spacing:3px;color:{GOLD}">{en}</div></div>
<div class="abs" style="left:0;right:0;top:930px">{price(old, pre, '#fff', GOLD)}</div>
<div class="abs note" style="left:48px;right:48px;top:1150px;color:#F4D9A0">{NOTE}</div>
<div class="abs" style="left:0;right:0;top:1205px;display:flex;justify-content:center">{G.cta('اطلب من الموقع', GOLD, DEEP)}</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)


T = dict(photo=photo, slash=slash, split=split, grid=grid, tape=tape, receipt=receipt, spot=spot, last=last)
if __name__ == '__main__':
    G.STORY = True
    only = sys.argv[1:]
    for i, (t, k, ar, en, L, old, tpl, pre) in enumerate(S):
        if only and k not in only: continue
        G.shot(f'{i+1:02d}-{k}', T[tpl](t, ar, en, L, old, pre), 1920)
    print('ok')
