# DOHA 25.28° N pink sunglasses (F26 model, 319 QAR) — post + story from the owner's studio photos (different photo each).
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
INK = '#521A37'; PK = '#B9507E'
CSS = G.CTA_CSS + f'''.sp{{background:rgba(255,255,255,.78);backdrop-filter:blur(6px);border-radius:24px;padding:12px 10px 14px;text-align:center;flex:1}}
.sp b{{display:block;font-family:Poppins;font-weight:900;font-size:38px;color:{INK};line-height:1.05}}.sp i{{display:block;font-style:normal;font-weight:800;font-size:20px;color:#7a4a60}}'''


def specs():
    return (f'<div class="sp"><b>33g</b><i>خفيفة</i></div><div class="sp"><b>4</b><i>وضعيات تعديل</i></div>'
            f'<div class="sp"><b style="font-family:Cairo;font-size:34px">حماية</b><i>ضد الصدمات</i></div>')


def post():
    body = f'''<img class="abs" src="file://{S}post-photo.jpg" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">
<div class="abs" style="left:0;right:0;bottom:0;height:420px;background:linear-gradient(180deg,rgba(250,244,246,0) 0%,rgba(250,244,246,.92) 55%,#FAF4F6 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:16px;letter-spacing:4px;color:{INK}">DOHA · 25.28° N</div>
<div class="abs ar" style="right:48px;top:40px;color:{INK};text-align:right">
 <div style="font-weight:900;font-size:72px;line-height:1.08">وردية..</div>
 <div style="font-weight:900;font-size:50px;line-height:1.2;color:{PK}">وتركيز كامل</div></div>
<div class="abs" style="left:48px;right:48px;top:1000px;display:flex;gap:12px;direction:rtl">{specs()}</div>
<div class="abs" style="left:48px;right:48px;top:1135px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{INK}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', INK, '#fff')}</div>'''
    return G.doc('#FAF4F6', INK, body, extra=CSS)


def story():
    body = f'''<div class="abs" style="inset:0;background:#E8E6F2"></div>
<img class="abs" src="file://{S}story-photo.jpg" style="left:0;top:490px;width:1080px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 14%,#000 86%,transparent 100%)"><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:0;right:0;top:130px;text-align:center;font-weight:900;font-size:180px;letter-spacing:-3px;line-height:1;color:{INK}">DOHA</div>
<div class="abs en" style="left:0;right:0;top:310px;text-align:center;font-weight:700;font-size:20px;letter-spacing:6px;color:{PK}">25.28° N · MADE TO FOCUS</div>
<div class="abs" style="left:48px;right:48px;top:985px;display:flex;gap:12px;direction:rtl">{specs()}</div>
<div class="abs ar" style="left:48px;right:48px;top:1095px;text-align:center;font-weight:900;font-size:40px;color:{INK}">عدسة وردية.. وجري وسيكل بتركيز 🩷</div>
<div class="abs ar" style="left:48px;right:48px;top:1162px;text-align:center;font-weight:700;font-size:24px;color:#7a4a60">مع علبة 974 بسحاب وكلّاب</div>
<div class="abs" style="left:48px;right:48px;top:1215px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{INK}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', INK, '#fff')}</div>'''
    return G.doc('#E9E6F2', INK, body, extra=CSS)


if __name__ == '__main__':
    G.STORY = False; G.shot('974-doha-pink-post', post())
    G.STORY = True; G.shot('974-doha-pink-story', story(), 1920)
    print('ok')
