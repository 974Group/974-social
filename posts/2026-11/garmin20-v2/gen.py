# Garmin 20mm QuickFit silicone v2 (21 Nov 2026) - quick post + story. 99 QAR.
# Only the 4 colours with the same (C-shaped) photo angle: White 32, Baby blue 28, Light green 21, Orange 20.
# Layout: dark "track" background with curved lane lines, 4 bands in one row on the track.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
C='/home/claude/974-social/products/garmin-20mm-quickfit/cut/'
ACC='#FF7A2F'
LANES='''<svg class="abs" style="left:0;top:calc(380px + var(--o));width:1080px;height:760px" viewBox="0 0 1080 760">
<g fill="none" stroke="rgba(255,255,255,.10)" stroke-width="4">
<path d="M-60 700 C 260 420 820 420 1140 700"/><path d="M-60 600 C 260 320 820 320 1140 600"/>
<path d="M-60 500 C 260 220 820 220 1140 500"/><path d="M-60 400 C 260 120 820 120 1140 400"/></g>
<path d="M-60 650 C 260 370 820 370 1140 650" fill="none" stroke="rgba(255,122,47,.45)" stroke-width="6" stroke-dasharray="26 18"/></svg>'''

def page():
    cols=[('white','White'),('babyblue','Baby blue'),('lightgreen','Light green'),('orange','Orange')]
    row=''.join(f'<div class="b"><img src="file://{C}{k}.png"><i class="en">{n}</i></div>' for k,n in cols)
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 45%,#262B33 0%,#16191E 70%,#0F1114 100%)"></div>
{LANES}<!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#9AA3AE">GARMIN · QUICKFIT 20MM</div>
<div class="abs" style="right:48px;left:48px;top:118px;color:#fff;direction:rtl;text-align:right">
  <div style="font-weight:900;font-size:80px;line-height:1.05">غيّر لون قارمنك..<br><span style="color:{ACC}">بكبسة وحدة</span></div>
  <div style="font-weight:700;font-size:28px;opacity:.85;margin-top:8px">سير سيليكون لساعات <span class="en">Garmin</span> بمقاس <span class="en">QuickFit 20mm</span></div>
</div>
<div class="abs" style="left:30px;right:30px;top:490px;display:flex;justify-content:space-between">{row}</div>
<div class="abs" style="left:0;right:0;top:900px;display:flex;justify-content:center;gap:12px;direction:rtl">
  <span class="tg">ضد العرق والماي</span><span class="tg">قفل ستيل</span><span class="tg">يركب بدون أدوات</span>
</div>
<div class="abs" style="left:48px;right:48px;top:1010px;display:flex;align-items:center;justify-content:space-between;direction:rtl;color:#fff">
  <div style="font-weight:900;font-size:32px"><span class="en" style="font-size:90px;color:{ACC}">99</span> ر.ق</div>
  {G.cta('اختار لونك',ACC,'#16191E')}
</div>'''
    extra=G.CTA_CSS+'''.b{width:250px;display:flex;flex-direction:column;align-items:center}
.b img{height:290px;filter:drop-shadow(0 20px 22px rgba(0,0,0,.5))}
.b i{font-style:normal;font-weight:700;font-size:15px;letter-spacing:3px;text-transform:uppercase;color:#9AA3AE;margin-top:14px}
.tg{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.22);border-radius:30px;padding:5px 20px 8px;font-weight:800;font-size:24px;color:#fff}'''
    return G.doc('#16191E','#fff',body,pf_ink='#fff',extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.STORY=False; G.shot('974-garmin20-v2-post',page())
    G.STORY=True; G.shot('974-garmin20-v2-story',page(),1920)
