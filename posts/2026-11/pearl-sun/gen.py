# THE PEARL 25.37° N sunglasses (319 QAR, yellow frame, photochromic) — post + story for 23 Nov 10:00.
# Fresh layout: lime field from the frame, vertical name watermark, stat trio, clear->dark lens bar.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); C = '/home/claude/974-social/posts/2026-11/sunglasses/cut/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
INK = '#0B1A3C'; LIME = '#E4F255'; AQ = '#2FB8E0'
CSS = G.CTA_CSS + f'''
.stat{{flex:1;background:rgba(255,255,255,.55);border-radius:26px;padding:14px 10px 16px;text-align:center}}
.stat b{{display:block;font-family:Poppins;font-weight:900;font-size:50px;line-height:1.05;color:{INK}}}
.stat i{{display:block;font-style:normal;font-weight:800;font-size:22px;color:#33415e;margin-top:2px}}
.bar{{background:{INK};border-radius:40px;display:flex;align-items:center;justify-content:space-between;padding:14px 34px;direction:rtl;color:#fff}}
.bar .l{{display:flex;flex-direction:column;align-items:center;gap:2px}}
.bar img{{height:96px}} .bar span{{font-weight:800;font-size:22px}}
'''


def page():
    body = f'''
<div class="abs" style="inset:0;background:radial-gradient(80% 55% at 55% 38%,#F6FBB8 0%,{LIME} 55%,#C9DA2C 100%)"></div><!--/bk-->
<div class="abs en" style="left:22px;top:150px;writing-mode:vertical-rl;transform:rotate(180deg);font-weight:900;font-size:120px;letter-spacing:6px;color:rgba(11,26,60,.08);line-height:1">THE PEARL</div>
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:17px;letter-spacing:4px;color:{INK}">THE PEARL · 25.37° N</div>
<div class="abs ar" style="right:48px;top:36px;color:{INK}">
  <div style="font-weight:900;font-size:70px;line-height:1.1">جري وسيكل..</div>
  <div style="font-weight:900;font-size:48px;line-height:1.2;margin-top:30px">بعدسة <span style="background:{INK};color:{LIME};border-radius:16px;padding:2px 16px 8px">تغمق بروحها</span></div>
</div>
<img class="abs" src="file://{C}pearl-hero.png" style="left:110px;top:262px;width:860px;transform:rotate(-6deg);filter:drop-shadow(0 30px 30px rgba(40,60,0,.30))">
<div class="abs" style="left:48px;right:48px;top:820px">
  <div class="bar"><div class="l"><img src="file://{C}pearl-clear.png"><span>☁️ بالظل</span></div>
    <div style="font-family:Poppins;font-size:46px;color:{LIME}">←</div>
    <div class="l"><img src="file://{C}pearl-dark.png"><span>☀️ بالشمس</span></div></div>
</div>
<div class="abs" style="left:48px;right:48px;top:1000px;display:flex;gap:16px;direction:rtl">
  <div class="stat"><b>21g</b><i>خفيفة</i></div>
  <div class="stat"><b>UV400</b><i>حماية كاملة</i></div>
  <div class="stat"><b>TR90</b><i>مرنة ما تنكسر</i></div>
</div>
<div class="abs" style="left:48px;right:48px;top:1140px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <div style="font-weight:900;font-size:30px;color:{INK}"><span class="en" style="font-size:72px;font-weight:900">319</span> ر.ق</div>
  {G.cta('اطلبها الحين', INK, LIME)}
</div>'''
    return G.doc(LIME, INK, body, extra=CSS)


if __name__ == '__main__':
    G.STORY = False; G.shot('974-pearl-sun-post', page())
    G.STORY = True; G.shot('974-pearl-sun-story', page(), 1920)
    print('ok')
