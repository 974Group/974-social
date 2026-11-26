# Thank-you story: why the 4-years discount, orders above expectations, please be patient.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); G.OUT = D + '/out'
M, DEEP, GOLD = '#720842', '#51022D', '#C9A24B'
CSS = '''
.t{font-family:Cairo;color:#fff;text-align:center;direction:rtl}
.P{font-family:Poppins;font-weight:900}
/* owner asked: no payfoot on this story */ .pf{display:none!important}
.ln{width:120px;height:4px;background:%s;margin:0 auto;border-radius:4px}
''' % GOLD
def page():
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(90% 55% at 50% 30%,#8A1550 0%,{M} 45%,{DEEP} 100%)"></div>
<div class="abs" style="inset:0;background-image:radial-gradient(rgba(232,200,120,.10) 1.6px,transparent 1.7px);background-size:30px 30px"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:50%;transform:translateX(-50%);top:0;height:54px">
<div class="abs t" style="left:70px;right:70px;top:200px">
  <div style="display:flex;justify-content:center;align-items:center;gap:22px;direction:ltr">
    <span class="P" style="font-size:190px;line-height:.9;color:transparent;-webkit-text-stroke:5px {GOLD}">4</span>
    <span class="P" style="font-size:54px;line-height:1.05;color:#fff;text-align:left">YEARS<br><span style="color:{GOLD};font-size:34px;letter-spacing:3px">THANK YOU</span></span>
  </div>
  <div style="font-weight:900;font-size:66px;margin-top:26px;line-height:1.25">شكراً من القلب</div>
  <div class="ln" style="margin-top:26px"></div>
  <div style="font-weight:700;font-size:38px;line-height:1.75;margin-top:30px">
    اللي يعرفنا يدري إن احنا نادر ما نسوي خصومات<br>
    خصم هالأسبوع مب عشان البيع..<br>
    الخصم هو <span style="color:{GOLD};font-weight:900">تقدير لكل واحد دعمنا</span><br>
    بمناسبة <span style="color:{GOLD};font-weight:900">٤ سنين</span> من الافتتاح<br>
    ووصلنا للي احنا فيه بفضل الله ثم فضلكم
  </div>
  <div class="ln" style="margin-top:34px;width:60px;opacity:.6"></div>
  <div style="font-weight:700;font-size:38px;line-height:1.75;margin-top:30px">
    والحمدلله الطلبات <span style="color:{GOLD};font-weight:900">فاقت توقعاتنا</span><br>
    نطلب منكم الصبر علينا،<br>
    وإن شاء الله كل الطلبات توصلكم اليوم<br>
    <span style="font-size:31px;color:#F4D9A0">وأي تأخير بيكون خارج عن إرادتنا</span>
  </div>
  <div style="font-weight:900;font-size:44px;margin-top:40px;display:flex;justify-content:center;align-items:center;gap:16px">فريق <img src="file://{G.LW}" style="height:40px"> 🤍</div>
</div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)
if __name__ == '__main__':
    G.STORY = True; G.shot('974-4years-thanks-story', page(), 1920); print('ok')
