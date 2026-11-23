# HALUL 25.67° N blue sunglasses (F26, photochromic, 319 QAR) — 7-slide carousel (one feature per slide) + story, owner's photos.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
NV = '#0C1B45'; BL = '#2E6BFF'; N = 7
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
    body = f'''{photo('s1.jpg', 'center 45%')}
<div class="abs" style="left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(248,244,242,.95) 0%,rgba(248,244,242,0) 100%)"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,#F6F2F0 0%,#F6F2F0 45%,rgba(246,242,240,0) 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:44px">
<div class="abs en" style="right:56px;top:56px;font-weight:700;font-size:18px;letter-spacing:5px;color:{NV}">25.67° N · MADE TO EXPLORE</div>
<div class="abs en" style="left:0;right:0;top:110px;text-align:center;font-weight:900;font-size:170px;letter-spacing:-3px;line-height:1;color:{NV}">HALUL</div>
<div class="abs ar" style="left:56px;right:56px;top:960px;text-align:center;color:{NV}"><div style="font-weight:900;font-size:50px">جري وسيكل.. بعدسة تفهم الشمس</div>
 <div style="font-weight:800;font-size:24px;margin-top:6px;opacity:.75">اسحب ← وشوف مميزاتها</div></div>
<div class="abs" style="left:56px;right:56px;top:1100px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{NV}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', NV, '#fff')}</div>'''
    return G.doc('#F6F2F0', NV, body, extra=CSS)


def s7():
    body = f'''<div class="abs" style="inset:0;background:#ECEAE8"></div><img class="abs" src="file://{S}s7.jpg" style="left:0;top:310px;width:1080px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 8%,#000 90%,transparent 100%)"><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:40px">
{text_block(7, 'تجيك مع علبتها', 'علبة 974 صلبة بسحاب وكلّاب.. تعلّقها على شنطتك', NV, top=60)}
<div class="abs" style="left:56px;right:56px;top:1100px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{NV}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', NV, '#fff')}</div>'''
    return G.doc('#ECEAE8', NV, body, extra=CSS)


SLIDES = [
    ('s1', s1),
    ('s2', lambda: slide(2, 's2.jpg', 'بالظل شفافة..<br>وبالشمس تغمق ☀️', 'عدسة فوتوكروميك تتغير لحالها مع الضو', '#fff', 'rgba(20,40,30,.75)', 'center 40%', top=60)),
    ('s3', lambda: slide(3, 's3.jpg', 'عدسة وحدة.. بدون إطار', 'رؤية أوسع، وحماية ضد الصدمات', '#fff', 'rgba(20,40,70,.70)', 'center 45%', top=60)),
    ('s4', lambda: slide(4, 's4.jpg', '<span class="en">33g</span> بس..<br>ما تحس فيها', 'خفيفة طول الجري والسيكل', '#fff', 'rgba(15,30,20,.70)', 'center 52%', top=60)),
    ('s5', lambda: slide(5, 's5.jpg', 'تتعدّل على وجهك', 'أنف وأذرع تتضبط.. ٤ وضعيات تعديل', NV, 'rgba(238,236,240,.97)', 'center 30%', bottom=70)),
    ('s6', lambda: slide(6, 's6.jpg', 'اسمها محفور عليها', 'كل نظارة باسم مكان من قطر وإحداثياته', NV, 'rgba(250,250,250,.97)', '48% 30%', bottom=70)),
    ('s7', s7),
]


def story():
    body = f'''<img class="abs" src="file://{S}story.jpg" style="left:0;top:0;width:1080px;height:1920px;object-fit:cover;object-position:35% 50%">
<div class="abs" style="left:0;right:0;top:0;height:700px;background:linear-gradient(180deg,rgba(12,27,69,.75) 0%,transparent 100%)"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:900px;background:linear-gradient(0deg,rgba(12,27,69,.95) 0%,rgba(12,27,69,.85) 45%,transparent 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:56px;top:0;height:44px">
<div class="abs en" style="left:0;right:0;top:90px;text-align:center;font-weight:900;font-size:170px;letter-spacing:-3px;line-height:1;color:#fff">HALUL</div>
<div class="abs en" style="left:0;right:0;top:265px;text-align:center;font-weight:700;font-size:20px;letter-spacing:6px;color:#BFD3FF">25.67° N · MADE TO EXPLORE</div>
<div class="abs ar" style="left:56px;right:56px;top:1010px;text-align:center;color:#fff"><div style="font-weight:900;font-size:56px">بالظل شفافة.. وبالشمس تغمق</div>
 <div style="font-weight:800;font-size:26px;margin-top:8px;color:#BFD3FF">عدسة فوتوكروميك · <span class="en">33g</span> · ضد الصدمات</div></div>
<div class="abs" style="left:56px;right:56px;top:1190px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:#fff"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', '#fff', NV)}</div>'''
    return G.doc('#0C1B45', '#fff', body, pf_ink='#fff', extra=CSS)


if __name__ == '__main__':
    G.STORY = False
    for n, fn in SLIDES: G.shot(f'974-halul-{n}', fn())
    G.STORY = True; G.shot('974-halul-story', story(), 1920)
    print('ok')
