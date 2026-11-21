# UAE Edition goggles + flag-colour masks "كمّل اللوك" (22 Nov 2026). Post 1080x1350 + story 1080x1920.
# Goggle 319 (compare-at 379, 23 in stock). Masks 39: Red 126, Green 88, White 170, Black 146.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
GOG='/home/claude/974-social/products/goggles/uae-edition-render.png'
MK='/home/claude/974-social/posts/2026-11/face-mask/src/cut/'
INK='#1A1A1A'; RED='#C8102E'; GRN='#00732F'

def page(story):
    masks=''.join(f'<div class="m"><img src="file://{MK}{k}.png"><i class="en">{n}</i></div>' for k,n in [('red','RED'),('green','GREEN'),('white','WHITE'),('black','BLACK')])
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(80% 55% at 55% 40%,#FFFFFF 0%,#ECECEA 55%,#D9DAD6 100%)"></div>
<div class="abs" style="left:0;top:0;bottom:0;width:34px;background:{RED}"></div>
<div class="abs" style="left:34px;right:0;top:0;height:14px;background:{GRN}"></div>
<div class="abs" style="left:34px;right:0;bottom:0;height:14px;background:#111"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:72px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#6b6b6b">974 GUARDS · UAE EDITION 🇦🇪</div>
<div class="abs" style="right:48px;left:72px;top:112px;color:{INK};direction:rtl;text-align:right">
  <div style="font-weight:900;font-size:76px;line-height:1.05">نظارة <span class="en" style="font-weight:900">UAE Edition</span><br><span style="color:{RED}">بألوان العلم</span></div>
</div>
<img class="abs" src="file://{GOG}" style="left:{150 if story else 190}px;top:{300 if story else 290}px;width:{820 if story else 760}px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.28))">
<div class="abs" style="right:48px;top:{830 if story else 790}px;direction:rtl;display:flex;align-items:baseline;gap:14px;color:{INK}">
  <span style="font-weight:900;font-size:30px"><span class="en" style="font-size:78px;color:{RED}">319</span> ر.ق</span>
  <span class="en" style="font-size:30px;font-weight:700;opacity:.45;text-decoration:line-through">379</span>
</div>
<div class="abs" style="left:72px;top:{850 if story else 810}px;direction:rtl;display:flex;gap:10px">
  <span class="tg">عدستين مغناطيس</span><span class="tg">ضد الضباب</span>
</div>
<div class="abs" style="left:72px;right:48px;top:{950 if story else 900}px;border-top:2px dashed #BDBDB8"></div>
<div class="abs" style="right:48px;top:{968 if story else 915}px;direction:rtl;color:{INK};font-weight:900;font-size:34px">وكمّل اللوك 👌 <span style="font-weight:700;font-size:26px;opacity:.75">بماسك من ألوان العلم بـ <span class="en">39</span> ر.ق</span></div>
<div class="abs" style="left:72px;right:48px;top:{1030 if story else 975}px;display:flex;justify-content:space-between">{masks}</div>'''
    extra=G.CTA_CSS+f'''.m{{width:205px;display:flex;flex-direction:column;align-items:center}}.m img{{height:{150 if not story else 210}px;filter:drop-shadow(0 10px 12px rgba(0,0,0,.2))}}
.m i{{font-style:normal;font-weight:700;font-size:13px;letter-spacing:3px;color:#6b6b6b;margin-top:4px}}
.tg{{background:#fff;border:2px solid #DDDDD8;border-radius:30px;padding:4px 16px 7px;font-weight:800;font-size:22px;color:{INK}}}
{'.pf{bottom:22px}' if not story else ''}'''
    G.STORY=story
    return G.doc('#ECECEA',INK,body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-uae-goggles-post',page(False))
    G.shot('974-uae-goggles-story',page(True),1920)
