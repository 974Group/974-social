# Garmin CIRQA silicone 2.0 v3 (for 22 Nov 10:30) - post + story. 89 QAR, all 10 colours ~100 each.
# Fresh layout: the 10 bands stacked as a pyramid 1-2-3-4 (same size, same angle, no overlap) on a light background.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True); C=D+'/cut/'; os.makedirs(C,exist_ok=True)
SRC='/home/claude/974-social/products/garmin-cirqa-silicone-v2/src/'
KS=['orange','lime','mousse-pink','sea-mist-blue','black','starlight','midnight-blue','green','white','light-gray']
for k in KS:
    if not os.path.exists(C+k+'.png'):
        im=Image.open(SRC+k+'-cut.png').convert('RGBA'); a=im.split()[3].point(lambda v:255 if v>20 else 0); im.crop(a.getbbox()).save(C+k+'.png')
INK='#1B1F2A'; ACC='#FF5A1F'

def page(story):
    w=116 if not story else 138
    rows=[KS[0:1],KS[1:3],KS[3:6],KS[6:10]]
    pyr=''.join('<div class="pr">'+''.join(f'<img src="file://{C}{k}.png" style="width:{w}px">' for k in r)+'</div>' for r in rows)
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(80% 55% at 50% 55%,#FFFFFF 0%,#F1F2EE 60%,#E4E6E0 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#6B7280">GARMIN CIRQA · SILICONE 2.0</div>
<div class="abs" style="right:48px;left:48px;top:112px;color:{INK};direction:rtl;text-align:right">
  <div style="font-weight:900;font-size:78px;line-height:1.05">فيه لون.. <span style="color:{ACC}">لكل مزاج</span> 😎</div>
  <div style="font-weight:700;font-size:28px;opacity:.75;margin-top:6px">سير سيليكون مثقّب لـ <span class="en">Garmin CIRQA</span> · خفيف ويتنفّس</div>
</div>
<div class="abs" style="left:0;right:0;top:{285 if not story else 300}px;display:flex;flex-direction:column;align-items:center;gap:{6 if not story else 10}px">{pyr}</div>
<div class="abs" style="left:0;right:0;top:{945 if not story else 1085}px;display:flex;justify-content:center;gap:12px;direction:rtl">
  <span class="tg">💧 ضد العرق والماي</span><span class="tg">🎨 <span class="en">10</span> ألوان</span><span class="tg">⌚ سير فقط بدون الجهاز</span>
</div>
<div class="abs" style="left:48px;right:48px;top:{1035 if not story else 1170}px;display:flex;align-items:center;justify-content:space-between;direction:rtl;color:{INK}">
  <div style="font-weight:900;font-size:32px"><span class="en" style="font-size:88px;color:{ACC}">89</span> ر.ق</div>
  {G.cta('اختار لونك',INK,'#fff')}
</div>'''
    extra=G.CTA_CSS+f'''.pr{{display:flex;gap:{14 if not story else 18}px;justify-content:center}}.pr img{{filter:drop-shadow(0 14px 14px rgba(27,31,42,.22))}}
.tg{{background:#fff;border:2px solid #E1E3DC;border-radius:30px;padding:5px 18px 8px;font-weight:800;font-size:23px;color:{INK}}}'''
    G.STORY=story
    return G.doc('#F1F2EE',INK,body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-cirqa-sil2-v3-post',page(False))
    G.shot('974-cirqa-sil2-v3-story',page(True),1920)
