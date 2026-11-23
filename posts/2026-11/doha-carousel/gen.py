# DOHA 25.28° N pink sunglasses (F26, 319 QAR) — 6-slide carousel, one feature per slide, owner's studio photos.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
INK = '#521A37'; PK = '#B9507E'; N = 6
CSS = G.CTA_CSS + '''.num{font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:3px}
.ttl{font-weight:900;font-size:66px;line-height:1.12}.sub{font-weight:800;font-size:30px;margin-top:10px;line-height:1.35}'''
NOFOOT = '.pf{display:none}'


def tb(i, ttl, sub, ink, top=None, bottom=None):
    w = f'top:{top}px' if top is not None else f'bottom:{bottom}px'
    return (f'<div class="abs ar" style="left:56px;right:56px;{w};color:{ink};text-align:right"><div class="num en" style="opacity:.8;text-align:right">0{i} / 0{N}</div>'
            f'<div class="ttl">{ttl}</div><div class="sub">{sub}</div></div>')


def price(ink, bg, fg, top=1100):
    return (f'<div class="abs" style="left:56px;right:56px;top:{top}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">'
            f'<div style="font-weight:900;font-size:30px;color:{ink}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta("اطلبها الحين", bg, fg)}</div>')


def cover_slide(i, f, ttl, sub, ink, shade, pos, top=None, bottom=None):
    grad = (f'<div class="abs" style="left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,{shade} 0%,transparent 100%)"></div>' if top is not None
            else f'<div class="abs" style="left:0;right:0;bottom:0;height:620px;background:linear-gradient(0deg,{shade} 0%,{shade} 30%,transparent 100%)"></div>')
    lg = f'<img class="abs" src="file://{G.LW if ink=="#fff" else G.LB}" style="left:56px;{"bottom:60px" if top is not None else "top:50px"};height:40px">'
    body = (f'<img class="abs" src="file://{S}{f}" style="left:0;top:0;width:1080px;height:100%;object-fit:cover;object-position:{pos}">{grad}<!--/bk-->{lg}'
            + tb(i, ttl, sub, ink, top=top, bottom=bottom))
    return G.doc('#000', ink, body, pf_ink=ink, extra=CSS + NOFOOT)


def float_slide(i, f, ttl, sub, bg, top_img=420, foot=False, extra_html='', w=1160, blur=False):
    back = (f'<img class="abs" src="file://{S}{f}" style="left:-500px;top:0;width:2080px;height:1350px;object-fit:cover;filter:blur(36px)">'
            f'<div class="abs" style="inset:0;background:rgba(240,236,242,.30)"></div>') if blur else f'<div class="abs" style="inset:0;background:{bg}"></div>'
    body = (back + f'<img class="abs" src="file://{S}{f}" style="left:{-(w-1080)//2}px;top:{top_img}px;width:{w}px;'
            f'-webkit-mask-image:radial-gradient(closest-side at 50% 50%,#000 {85 if blur else 75}%,transparent 100%)"><!--/bk-->'
            f'<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:40px">' + tb(i, ttl, sub, INK, top=60) + extra_html)
    return G.doc(bg, INK, body, extra=CSS + ('' if foot else NOFOOT))


def s1():
    body = f'''<img class="abs" src="file://{S}s1.jpg" style="left:0;top:0;width:1080px;height:100%;object-fit:cover">
<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,#FAF4F6 0%,#FAF4F6 45%,rgba(250,244,246,0) 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:56px;top:50px;height:44px">
<div class="abs en" style="right:56px;top:56px;font-weight:700;font-size:18px;letter-spacing:5px;color:{INK}">25.28° N · MADE TO FOCUS</div>
<div class="abs en" style="left:56px;top:110px;font-weight:900;font-size:170px;letter-spacing:-3px;line-height:1;color:{INK}">DOHA</div>
<div class="abs ar" style="left:56px;right:56px;top:960px;text-align:center;color:{INK}"><div style="font-weight:900;font-size:52px">وردية.. وتركيز كامل 🩷</div>
 <div style="font-weight:800;font-size:24px;margin-top:6px;opacity:.75">اسحبي ← وشوفي مميزاتها</div></div>{price(INK, INK, '#fff')}'''
    return G.doc('#FAF4F6', INK, body, extra=CSS)


SLIDES = [
    ('s1', s1),
    ('s2', lambda: cover_slide(2, 's2.jpg', 'عدسة وحدة.. بدون إطار', 'رؤية أوسع لين الأطراف', '#fff', 'rgba(82,26,55,.72)', 'center 30%', top=60)),
    ('s3', lambda: float_slide(3, 's3.jpg', 'حماية ضد الصدمات', 'تتحمّل الطيحات والضربات وهي عليك', '#C9C4CE', top_img=330, w=1300, blur=True)),
    ('s4', lambda: float_slide(4, 's4.jpg', '<span class="en">33g</span> بس..<br>ما تحس فيها', 'خفيفة طول الجري والسيكل', '#EBE8F1', top_img=340, w=1320)),
    ('s5', lambda: float_slide(5, 's5.jpg', 'تتعدّل على وجهك', 'أنف وأذرع تتضبط.. ٤ وضعيات تعديل', '#F1EEF5', top_img=290, w=1500)),
    ('s6', lambda: float_slide(6, 's6.jpg', 'تجيك مع علبتها', 'علبة 974 صلبة بسحاب وكلّاب', '#E8E5E4', top_img=330, foot=True, extra_html=price(INK, INK, '#fff'))),
]

if __name__ == '__main__':
    G.STORY = False
    for n, fn in SLIDES: G.shot(f'974-doha-{n}', fn())
    print('ok')
