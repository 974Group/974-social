# Green Edition goggles (نظارة البر الخضرا), owner 20 Nov 2026. Post 1080x1350 + story 1080x1920.
# Site price 319 (compare-at 379). 32 in stock. Colours from the product: teal strap, green/blue mirror lens.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
HERO='/home/claude/974-social/products/goggles/green-edition-render.png'
DUNES='''<svg class="abs" style="left:0;right:0;bottom:0;width:1080px;height:calc(420px + var(--o))" viewBox="0 0 1080 420" preserveAspectRatio="none">
<path d="M0 170 C180 90 330 120 470 175 C610 230 760 120 900 110 C980 105 1040 130 1080 150 L1080 420 L0 420Z" fill="#0E3A33"/>
<path d="M0 250 C160 200 300 215 450 255 C620 300 780 220 1080 235 L1080 420 L0 420Z" fill="#0A2C27"/></svg>'''

def page():
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 38%,#1F6B5A 0%,#124A40 45%,#0A2C27 100%)"></div>
{DUNES}<!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#8FD9B0">974 GUARDS · GREEN EDITION</div>
<div class="abs ar" style="right:48px;left:48px;top:118px;color:#fff;text-align:center">
  <div style="font-weight:900;font-size:84px;line-height:1.05">البر.. <span style="color:#6BE38C">بعدسة خضرا</span></div>
  <div style="font-weight:700;font-size:30px;opacity:.88;margin-top:10px">عدستين مغناطيس · وحدة للشمس ووحدة لليل والغبار</div>
</div>
<img class="abs" src="file://{HERO}" style="left:60px;top:330px;width:960px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.45))">
<div class="abs" style="left:0;right:0;top:1000px;display:flex;justify-content:center;gap:12px;direction:rtl">
  <span class="tg">ضد الضباب</span><span class="tg">تحمي من الغبار والرمل</span><span class="tg">تبدّل العدسة بثواني</span>
</div>
<div class="abs" style="left:48px;right:48px;top:1090px;display:flex;align-items:center;justify-content:space-between;direction:rtl;color:#fff">
  <div style="font-weight:900;font-size:32px;display:flex;align-items:baseline;gap:14px;direction:rtl">
    <span><span class="en" style="font-size:84px;color:#6BE38C">319</span> ر.ق</span>
    <span class="en" style="font-size:34px;font-weight:700;opacity:.55;text-decoration:line-through">379</span>
  </div>
  {G.cta('اطلبها الحين','#6BE38C','#0A2C27')}
</div>'''
    extra=G.CTA_CSS+'.tg{background:rgba(255,255,255,.12);border:1.5px solid rgba(143,217,176,.45);border-radius:30px;padding:5px 20px 8px;font-weight:800;font-size:24px;color:#fff}'
    return G.doc('#0A2C27','#fff',body,pf_ink='#fff',extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.STORY=False; G.shot('974-green-goggles-post',page())
    G.STORY=True; G.shot('974-green-goggles-story',page(),1920)
