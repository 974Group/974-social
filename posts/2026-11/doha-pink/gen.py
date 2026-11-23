# DOHA 25.28° N pink sunglasses (F26 model, 319 QAR) — post + story from the owner's studio photos (different photo each).
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
INK = '#521A37'; PK = '#B9507E'
CSS = G.CTA_CSS + f'''.sp{{background:#fff;box-shadow:0 8px 22px rgba(82,26,55,.10);border-radius:24px;padding:12px 10px 14px;text-align:center;flex:1}}
.sp b{{display:block;font-family:Poppins;font-weight:900;font-size:38px;color:{INK};line-height:1.05}}.sp i{{display:block;font-style:normal;font-weight:800;font-size:20px;color:#7a4a60}}'''


def specs():
    return (f'<div class="sp"><b>33g</b><i>خفيفة</i></div><div class="sp"><b>4</b><i>وضعيات تعديل</i></div>'
            f'<div class="sp"><b style="font-family:Cairo;font-size:34px">حماية</b><i>ضد الصدمات</i></div>')


def post():
    body = f'''<img class="abs" src="file://{S}post-photo.jpg" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">
<div class="abs" style="left:0;right:0;bottom:0;height:480px;background:linear-gradient(180deg,rgba(250,244,246,0) 0%,rgba(250,244,246,.95) 45%,#FAF4F6 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:16px;letter-spacing:4px;color:{INK}">DOHA · 25.28° N</div>
<div class="abs ar" style="right:48px;top:40px;color:{INK};text-align:right">
 <div style="font-weight:900;font-size:72px;line-height:1.08">وردية..</div>
 <div style="font-weight:900;font-size:50px;line-height:1.2;color:{PK}">وتركيز كامل</div></div>
<div class="abs" style="left:48px;right:48px;top:950px;display:flex;gap:12px;direction:rtl">{specs()}</div>
<div class="abs" style="left:48px;right:48px;top:1068px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{INK}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', INK, '#fff')}</div>'''
    return G.doc('#FAF4F6', INK, body, extra=CSS)


def story():
    body = f'''<img class="abs" src="file://{S}story-photo2.jpg" style="left:-600px;top:0;width:2880px;height:1920px;object-fit:cover;filter:blur(40px) brightness(1.05);transform:scale(1.1)">
<div class="abs" style="inset:0;background:rgba(246,240,244,.45)"></div>
<img class="abs" src="file://{S}story-photo2.jpg" style="left:-160px;top:520px;width:1400px;-webkit-mask-image:radial-gradient(closest-side at 50% 50%,#000 72%,transparent 100%)"><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:0;right:0;top:120px;text-align:center;font-weight:900;font-size:180px;letter-spacing:-3px;line-height:1;color:{INK}">DOHA</div>
<div class="abs en" style="left:0;right:0;top:300px;text-align:center;font-weight:700;font-size:20px;letter-spacing:6px;color:{PK}">25.28° N · MADE TO FOCUS</div>
<div class="abs" style="left:48px;right:48px;top:1000px;display:flex;gap:12px;direction:rtl">{specs()}</div>
<div class="abs ar" style="left:48px;right:48px;top:1110px;text-align:center;font-weight:900;font-size:40px;color:{INK}">وردية.. وتركيز كامل 🩷</div>
<div class="abs" style="left:48px;right:48px;top:1200px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{INK}"><span class="en" style="font-size:70px;font-weight:900">319</span> ر.ق</div>{G.cta('اطلبها الحين', INK, '#fff')}</div>'''
    return G.doc('#F3EDF1', INK, body, extra=CSS)


if __name__ == '__main__':
    G.STORY = False; G.shot('974-doha-pink-post', post())
    G.STORY = True; G.shot('974-doha-pink-story', story(), 1920)
    print('ok')
