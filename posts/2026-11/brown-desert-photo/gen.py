# Brown Edition goggles - owner's desert lifestyle photo (20 Nov 2026). Post 1080x1350 + story 1080x1920.
# Photo-led: headline in the dune area left of the face, price block on a dark gradient at the bottom.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
PH=D+'/src/photo.jpg'

def page(story):
    # photo 1536x2752 -> width 1080 = 1935 tall. Story shows y 0..1920; post shows y 215..1565 (focus on goggles+face).
    py=0 if story else -280
    top=760 if story else 430          # headline block (dune area, left of the face)
    bot=1215 if story else 880        # price block
    body=f'''
<div class="abs" style="left:0;top:{py}px;width:1080px;height:1935px;background:url(file://{PH}) center top/1080px auto no-repeat"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:{760 if story else 470}px;background:linear-gradient(180deg,rgba(38,22,12,0) 0%,rgba(38,22,12,.78) 45%,#26160C 100%)"></div>
<div class="abs" style="left:0;top:0;bottom:0;width:560px;background:linear-gradient(90deg,rgba(60,36,18,.55),rgba(60,36,18,0))"></div>
<!--/bk-->
<div class="abs" style="left:0;right:0;top:0;bottom:0">
<img class="abs" src="file://{G.LW}" style="left:48px;top:{200 if story else 46}px;height:46px">
<div class="abs" style="left:48px;top:{top}px;width:420px;color:#fff;direction:rtl;text-align:left">
  <div style="font-weight:900;font-size:96px;line-height:1.02;text-shadow:0 4px 18px rgba(0,0,0,.35)">الطعس<br><span style="color:#E8C99A">ينادي..</span></div>
  <div style="font-weight:700;font-size:28px;margin-top:14px;text-shadow:0 2px 10px rgba(0,0,0,.4)">والنظارة جاهزة 😎</div>
</div>
<div class="abs" style="left:48px;right:48px;top:{bot}px;color:#fff;direction:rtl">
  <div class="en" style="font-weight:700;font-size:17px;letter-spacing:5px;color:#E8C99A;text-align:right">BROWN EDITION · 974 GUARDS</div>
  <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:10px">
    <div>
      <div style="font-weight:800;font-size:30px">عدستين مغناطيس · ضد الضباب · تحمي من الغبار</div>
      <div style="font-weight:700;font-size:26px;opacity:.85;margin-top:4px">كمّل اللوك بالماسك البني بـ <span class="en" style="font-weight:700">39</span> ر.ق</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px">
    <div style="font-weight:900;font-size:32px"><span class="en" style="font-size:88px;color:#E8C99A">319</span> ر.ق</div>
    {G.cta('اطلبها الحين','#E8C99A','#26160C')}
  </div>
</div>
</div>'''
    G.STORY=story
    return G.doc('#26160C','#fff',body.replace('<div class="abs" style="left:0;right:0;top:0;bottom:0">','',1).rsplit('</div>',1)[0],pf_ink='#fff',extra=G.CTA_CSS + ('' if story else ''))

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-brown-desert-post',page(False))
    # story: content wrapper is shifted by G.O in doc(); undo by using O=0 for this photo layout
    G.O=0; G.shot('974-brown-desert-story',page(True),1920)
