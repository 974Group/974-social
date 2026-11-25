# SEALINE 24.85° N orange sunglasses (photochromic, 21g, 319 QAR) — 7-slide carousel (one feature per slide) + story, owner's photos.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
NV = '#1C1410'; BL = '#F26A1B'; N = 7
CSS = G.CTA_CSS + '''.sh{text-shadow:0 2px 18px rgba(0,0,0,.35)}
.num{font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:3px}
.ttl{font-weight:900;font-size:68px;line-height:1.12}.sub{font-weight:800;font-size:30px;margin-top:10px;line-height:1.35}'''
NOFOOT = '.pf{display:none}'


def photo(f, pos='center', fit='cover', bg='#000'):
    return f'<div class="abs" style="inset:0;background:{bg}"></div><img class="abs" src="file://{S}{f}" style="left:0;top:0;width:1080px;height:100%;object-fit:{fit};object-position:{pos}">'


def text_block(i, ttl, sub, ink, top=None, bottom=None, align='right'):
    where = f'top:{top}px' if top is not None else f'bottom:{bottom}px'
    return (f'<div class="abs ar" style="left:56px;right:56px;{where};color:{ink};text-align:{align}">'
            f'<div class="num en" style="opacity:.8;direction:ltr;text-align:{"left" if align=="left" else "right"}">0{i} / 0{N}</div>'
            f'<div class="ttl">{ttl}</div><div class="sub">{sub}</div></div>')


def slide(i, f, ttl, sub, ink, shade, pos='center', top=None, bottom=None, foot=False, logo=True):
    grad = (f'<div class="abs" style="left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,{shade} 0%,transparent 100%)"></div>' if top is not None
            else f'<div class="abs" style="left:0;right:0;bottom:0;height:640px;background:linear-gradient(0deg,{shade} 0%,{shade} 30%,transparent 100%)"></div>')
    lg = f'<img class="abs" src="file://{G.LW if ink=="#fff" else G.LB}" style="left:56px;{"bottom:60px" if top is not None else "top:50px"};height:40px">' if logo else ''
    body = f'{photo(f, pos)}{grad}<!--/bk-->{lg}' + text_block(i, ttl, sub, ink, top=top, bottom=bottom)
    return G.doc('#000', ink, body, pf_ink=ink, extra=CSS + ('' if foot else NOFOOT))


def s1():
    body = f'''<div class="abs" style="inset:0;background:#E9E7EA"></div><img class="abs" src="file://{S}s1.jpg" style="left:-60px;top:250px;width:1200px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 12%,#000 85%,transparent 100%)">
<div class="abs" style="left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(248,244,242,.95) 0%,rgba(248,244,242,0) 100%)"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,#F6F2F0 0%,#F6F2F0 45%,rgba(246,242,240,0) 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:44px">
<div class="abs en" style="right:56px;top:56px;font-weight:700;font-size:18px;letter-spacing:5px;color:{NV}">24.85° N · MADE TO WANDER</div>
<div class="abs en" style="left:0;right:0;top:110px;text-align:center;font-weight:900;font-size:170px;letter-spacing:-3px;line-height:1;color:{NV}">SEALINE</div>
<div class="abs ar" style="left:56px;right:56px;top:960px;text-align:center;color:{NV}"><div style="font-weight:900;font-size:50px">برتقالي.. وعدسة تفهم الشمس</div>
 <div style="font-weight:800;font-size:24px;margin-top:6px;opacity:.75">اسحب ← وشوف مميزاتها</div></div>
<div class="abs" style="left:56px;right:56px;top:1100px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{NV}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', NV, '#fff')}</div>'''
    return G.doc('#F6F2F0', NV, body, extra=CSS)


def s7():
    body = f'''<div class="abs" style="inset:0;background:#ECEAE8"></div><img class="abs" src="file://{S}s7.jpg" style="left:0;top:250px;width:1080px;height:860px;object-fit:cover;object-position:50% 50%;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 10%,#000 88%,transparent 100%)"><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:40px">
{text_block(7, 'تجيك مع علبتها', 'علبة 974 صلبة بسحاب وكلّاب.. تعلّقها على شنطتك', NV, top=60)}
<div class="abs" style="left:56px;right:56px;top:1100px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{NV}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', NV, '#fff')}</div>'''
    return G.doc('#ECEAE8', NV, body, extra=CSS)


SLIDES = [
    ('s1', s1),
    ('s2', lambda: slide(2, 's2.jpg', 'بالظل شفافة..<br>وبالشمس تغمق ☀️', 'عدسة فوتوكروميك تتغير لحالها مع الضو', '#fff', 'rgba(8,12,30,.80)', 'center 45%', top=60)),
    ('s3', lambda: slide(3, 's3.jpg', 'عدسة وحدة.. بدون إطار', 'رؤية أوسع، وحماية <span class="en">UV400</span> كاملة', NV, 'rgba(236,234,236,.97)', 'center 30%', bottom=70)),
    ('s4', lambda: slide(4, 's4.jpg', '<span class="en">21g</span> بس..<br>ما تحس فيها', 'خفيفة طول الجري والسيكل', NV, 'rgba(240,238,240,.97)', 'center 50%', top=60)),
    ('s5', lambda: slide(5, 's5.jpg', 'أنف سيليكون<br>ما يزلق مع العرق', 'ثابتة على وجهك وأنت تتحرك', NV, 'rgba(236,234,236,.97)', 'center 35%', top=60)),
    ('s6', lambda: slide(6, 's6.jpg', 'إطار <span class="en">TR90</span>..<br>مرن ما ينكسر', 'وشعار 974 على الذراعين', '#fff', 'rgba(8,12,30,.80)', 'center 50%', top=60)),
    ('s7', s7),
]


def story():
    body = f'''<img class="abs" src="file://{S}story.jpg" style="left:0;top:0;width:1080px;height:1920px;object-fit:cover;object-position:50% 60%">
<div class="abs" style="left:0;right:0;bottom:0;height:820px;background:linear-gradient(0deg,rgba(28,20,16,.96) 0%,rgba(28,20,16,.85) 45%,transparent 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:0;height:44px">
<div class="abs en" style="left:0;right:0;top:90px;text-align:center;font-weight:900;font-size:150px;letter-spacing:-3px;line-height:1;color:{NV}">SEALINE</div>
<div class="abs en" style="left:0;right:0;top:250px;text-align:center;font-weight:700;font-size:20px;letter-spacing:6px;color:{BL}">24.85° N · MADE TO WANDER</div>
<div class="abs ar" style="left:56px;right:56px;top:1060px;text-align:center;color:#fff"><div style="font-weight:900;font-size:56px">بالظل شفافة.. وبالشمس تغمق</div>
 <div style="font-weight:800;font-size:26px;margin-top:8px;color:#FFC79E">عدسة فوتوكروميك · <span class="en">21g</span> · <span class="en">UV400</span></div></div>
<div class="abs" style="left:56px;right:56px;top:1230px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:#fff"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', BL, '#fff')}</div>'''
    return G.doc('#1C1410', '#fff', body, pf_ink='#fff', extra=CSS)


if __name__ == '__main__':
    G.STORY = False
    for n, fn in SLIDES: G.shot(f'974-sealine-{n}', fn())
    G.STORY = True; G.shot('974-sealine-story', story(), 1920)
    print('ok')
