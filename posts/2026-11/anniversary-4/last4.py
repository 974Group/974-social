# "Last 4 hours" story — Fri 27 Nov ~19:30, sale ends 23:59.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); G.OUT = D + '/out'
M, DEEP, GOLD = '#720842', '#51022D', '#C9A24B'
CSS = G.CTA_CSS + '''.P{font-family:Poppins;font-weight:900}.t{font-family:Cairo;text-align:center;direction:rtl;color:#fff}
.chip{display:inline-block;background:%s;color:%s;font-family:Cairo;font-weight:900;font-size:42px;border-radius:44px;padding:6px 38px 12px}''' % (GOLD, DEEP)
def page():
    ticks=''.join(f'<div style="position:absolute;left:50%;top:0;width:6px;height:{26 if i%3==0 else 14}px;background:{GOLD if i%3==0 else "rgba(255,255,255,.35)"};transform-origin:3px 182px;transform:translateX(-3px) rotate({i*30}deg)"></div>' for i in range(12))
    body=f'''<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 38%,#8A1550 0%,{M} 45%,{DEEP} 100%)"></div>
<div class="abs" style="inset:0;background-image:radial-gradient(rgba(232,200,120,.09) 1.6px,transparent 1.7px);background-size:30px 30px"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:50%;transform:translateX(-50%);top:0;height:54px">
<div class="abs t" style="left:0;right:0;top:90px;font-weight:900;font-size:60px">آخر فرصة ⏳</div>
<div class="abs" style="left:350px;top:190px;width:380px;height:380px;border-radius:50%;border:8px solid {GOLD};box-shadow:0 0 60px rgba(201,162,75,.45)">
  <div style="position:absolute;inset:0">{ticks}</div>
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="P" style="font-size:200px;line-height:.9;color:#fff">4</div>
    <div class="P" style="font-size:44px;color:{GOLD};letter-spacing:6px">HOURS</div></div></div>
<div class="abs t" style="left:0;right:0;top:600px">
  <div style="font-weight:900;font-size:70px;line-height:1.2">باقي <span style="color:{GOLD}">٤ ساعات</span> بس</div>
  <div style="font-weight:700;font-size:40px;margin-top:10px;color:#F4D9A0">والخصم يخلص الليلة</div>
  <div style="margin-top:18px;line-height:1"><span class="P" style="font-size:180px">40%</span></div>
  <div style="font-weight:900;font-size:46px;color:{GOLD};margin-top:-4px">خصم على كل الموقع</div>
  <div style="margin-top:22px"><span class="chip">لين الساعة <bdi dir="ltr" style="font-family:Poppins;font-weight:800">11:59</bdi> الليلة</span></div>
  <div style="font-weight:800;font-size:27px;margin-top:18px;color:#F4D9A0;line-height:1.5">للطلبات من الموقع فقط <span class="P" style="font-weight:700">974group.net</span><br>ما يجتمع مع أي خصم أو عرض ثاني</div>
</div>'''
    return G.doc(DEEP,'#fff',body,pf_ink='#fff',extra=CSS)
G.STORY=True; G.shot('974-last4hours-story', page(), 1920); print('ok')
