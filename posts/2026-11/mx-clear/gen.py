# MX Clear goggles (109 QAR, Black 281 / White 79 / Grey 87) - quick post + story, 21 Nov 2026.
# Layout: 3 goggles stacked in a column (same angle, same size), specs + price column beside them.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True); C=D+'/cut/'
INK='#17181A'

def page():
    rows=''.join(f'<div class="g"><img src="file://{C}{k}.png"><i class="en">{n}</i></div>' for k,n in [('black','BLACK'),('grey','GREY'),('white','WHITE')])
    body=f'''
<div class="abs" style="inset:0;background:linear-gradient(160deg,#ECECEA 0%,#D6D7D4 60%,#C4C5C1 100%)"></div>
<div class="abs en" style="right:-30px;top:330px;font-weight:900;font-size:300px;line-height:.8;color:rgba(23,24,26,.06);letter-spacing:-10px">MX</div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#55575B">MX CLEAR GOGGLES</div>
<div class="abs" style="right:48px;left:48px;top:118px;color:{INK};direction:rtl;text-align:right">
  <div style="font-weight:900;font-size:78px;line-height:1.05">للدباب والبقي..<br><span style="color:#720842">عدسة شفافة</span></div>
</div>
<div class="abs" style="left:40px;top:330px;width:480px;display:flex;flex-direction:column;gap:10px">{rows}</div>
<div class="abs" style="right:48px;top:390px;width:430px;direction:rtl;color:{INK}">
  <div class="sp"><b>👁️</b><span>تشوف فيها الصبح والليل</span></div>
  <div class="sp"><b>🌫️</b><span>ضد الضباب والخدش</span></div>
  <div class="sp"><b>☀️</b><span>حماية <span class="en">UV400</span></span></div>
  <div class="sp"><b>🛡️</b><span>إطار مرن يتحمّل الصدمات</span></div>
  <div class="sp"><b>🧽</b><span>فوم ثلاث طبقات مريح</span></div>
  <div class="sp"><b>〰️</b><span>ستراب سيليكون ما يزحلق</span></div>
</div>
<div class="abs" style="right:48px;top:1010px;direction:rtl;display:flex;align-items:center;gap:28px;color:{INK}">
  <div style="font-weight:900;font-size:32px"><span class="en" style="font-size:96px;color:#720842">109</span> ر.ق</div>
</div>
<div class="abs" style="right:48px;top:1135px">{G.cta('اختار لونك','#720842','#fff')}</div>'''
    extra=G.CTA_CSS+'''.g{display:flex;flex-direction:column;align-items:center}
.g img{width:410px;filter:drop-shadow(0 18px 20px rgba(0,0,0,.25))}
.g i{font-style:normal;font-weight:700;font-size:15px;letter-spacing:5px;color:#55575B;margin-top:2px}
.sp{display:flex;align-items:center;gap:14px;margin-bottom:16px}.sp b{font-size:30px;width:40px;text-align:center}.sp span{font-weight:800;font-size:29px}'''
    return G.doc('#D6D7D4',INK,body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.STORY=False; G.shot('974-mx-clear-post',page())
    G.STORY=True; G.shot('974-mx-clear-story',page(),1920)
