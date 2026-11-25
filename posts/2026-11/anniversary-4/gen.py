# 974 turns 4 + Burgundy Friday: 3 options for the 00:00 reveal post (40% sitewide, Thu-Fri 26-27 Nov).
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
M, DEEP, GOLD, PAPER = '#720842', '#51022D', '#C9A24B', '#F4F1F2'
CSS = G.CTA_CSS + f'''
.P{{font-family:Poppins;font-weight:900}}
.chip{{display:inline-block;background:{GOLD};color:{DEEP};font-family:Cairo;font-weight:900;font-size:34px;border-radius:40px;padding:4px 30px 10px}}
.fine{{font-family:Cairo;font-weight:800;font-size:25px;line-height:1.55}}
'''
TERMS = 'للطلبات من الموقع فقط <span class="P" style="font-weight:700">974group.net</span><br>ما يجتمع مع أي خصم أو عرض ثاني'

def opt_a():  # Big gold "4" — anniversary first, Burgundy Friday underneath
    body = f'''<div class="abs" style="inset:0;background:radial-gradient(85% 60% at 50% 35%,#8A1550 0%,{M} 45%,{DEEP} 100%)"></div>
<div class="abs" style="inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 1.5px,transparent 1.6px);background-size:26px 26px"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs P" style="right:48px;top:52px;font-size:22px;letter-spacing:5px;color:{GOLD};font-weight:700">2022 — 2026</div>
<div class="abs" style="left:0;right:0;top:110px;display:flex;justify-content:center;align-items:center;gap:26px">
  <div class="P" style="font-size:400px;line-height:.9;color:transparent;-webkit-text-stroke:6px {GOLD}">4</div>
  <div class="P" style="font-size:78px;line-height:1;color:#fff;text-align:left">YEARS<br><span style="color:{GOLD};font-size:46px;letter-spacing:3px">OF 974</span></div></div>
<div class="abs" dir="rtl" style="left:0;right:0;top:500px;text-align:center;font-family:Cairo;font-weight:900;font-size:50px;color:#fff">٤ سنين معاكم.. والهدية منّا</div>
<div class="abs" style="left:0;right:0;top:640px;text-align:center">
  <div class="P" style="font-size:44px;color:rgba(255,255,255,.55);letter-spacing:2px"><s style="text-decoration-color:{GOLD};text-decoration-thickness:6px">BLACK</s> <span style="color:#fff">BURGUNDY FRIDAY</span></div>
  <div style="margin-top:6px"><span class="P" style="font-size:190px;color:#fff;line-height:1">40%</span><span style="font-family:Cairo;font-weight:900;font-size:56px;color:{GOLD};vertical-align:top;margin-left:12px">خصم</span></div>
  <div style="font-family:Cairo;font-weight:900;font-size:38px;color:#fff;margin-top:-4px">على كل الموقع</div></div>
<div class="abs" style="left:0;right:0;top:1040px;text-align:center;direction:rtl"><span class="chip">الخميس والجمعة ٢٦ و ٢٧ نوفمبر</span>
  <div class="fine" style="color:#F4D9A0;margin-top:12px">{TERMS}</div></div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)

def opt_b():  # "4 + 0% = 40%" — black half / burgundy half
    body = f'''<div class="abs" style="left:0;right:0;top:0;height:560px;background:#0B0B0D"></div>
<div class="abs" style="left:0;right:0;top:560px;bottom:0;background:linear-gradient(180deg,{M} 0%,{DEEP} 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs" style="left:0;right:0;top:120px;text-align:center">
  <div class="P" style="font-size:40px;color:#777;letter-spacing:4px"><s style="text-decoration-color:{GOLD};text-decoration-thickness:6px">BLACK FRIDAY</s></div>
  <div dir="rtl" style="text-align:center;font-family:Cairo;font-weight:900;font-size:62px;color:#fff;margin-top:14px;line-height:1.25">هالسنة غير..<br>نكمّل <span style="color:{GOLD}">٤ سنين</span></div></div>
<div class="abs" style="left:0;right:0;top:430px;text-align:center;line-height:1">
  <span class="P" style="font-size:300px;color:{GOLD};letter-spacing:-8px">4</span><span class="P" style="font-size:300px;color:#fff;letter-spacing:-8px">0%</span></div>
<div class="abs P" style="left:0;right:0;top:760px;text-align:center;font-size:56px;color:#fff;letter-spacing:3px">BURGUNDY FRIDAY</div>
<div class="abs" style="left:0;right:0;top:840px;text-align:center;font-family:Cairo;font-weight:900;font-size:40px;color:#fff">خصم على كل الموقع بمناسبة ٤ سنين</div>
<div class="abs" style="left:0;right:0;top:960px;text-align:center;direction:rtl"><span class="chip">الخميس والجمعة ٢٦ و ٢٧ نوفمبر</span>
  <div class="fine" style="color:#F4D9A0;margin-top:12px">{TERMS}</div></div>'''
    return G.doc(DEEP, '#fff', body, pf_ink='#fff', extra=CSS)

def opt_c():  # Timeline 2022 → 2026 on paper, 40% stamp
    yrs = [('2022','البداية'),('2023',''),('2024',''),('2025',''),('2026','٤ سنين')]
    dots = ''.join(f'<div style="text-align:center;width:150px"><div style="width:{40 if i==4 else 22}px;height:{40 if i==4 else 22}px;border-radius:50%;background:{GOLD if i==4 else M};margin:0 auto;border:5px solid {PAPER};box-shadow:0 0 0 3px {M}"></div><div class="P" style="font-size:{34 if i==4 else 26}px;color:{M};margin-top:12px">{y}</div><div style="font-family:Cairo;font-weight:800;font-size:22px;color:{DEEP}">{t}</div></div>' for i,(y,t) in enumerate(yrs))
    body = f'''<div class="abs" style="inset:0;background:{PAPER}"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs ar" style="right:48px;top:36px;text-align:right;color:{DEEP}">
  <div style="font-family:Cairo;font-weight:900;font-size:68px;line-height:1.15">شكراً على ٤ سنين</div>
  <div style="font-family:Cairo;font-weight:700;font-size:30px;color:{M}">من ٢٠٢٢ لين اليوم.. وانتوا معانا</div></div>
<div class="abs" style="left:90px;right:90px;top:300px;height:4px;background:{M};top:318px"></div>
<div class="abs" style="left:65px;right:65px;top:300px;display:flex;justify-content:space-between">{dots}</div>
<div class="abs" style="left:110px;right:110px;top:470px;height:500px;border-radius:44px;background:{M};box-shadow:0 30px 50px rgba(81,2,45,.3)"></div>
<div class="abs" style="left:110px;right:110px;top:500px;text-align:center">
  <div class="P" style="font-size:40px;color:rgba(255,255,255,.6)"><s style="text-decoration-color:{GOLD};text-decoration-thickness:6px">BLACK</s> <span style="color:#fff">BURGUNDY FRIDAY</span></div>
  <div><span class="P" style="font-size:210px;color:#fff;line-height:1.05">40%</span></div>
  <div style="font-family:Cairo;font-weight:900;font-size:40px;color:{GOLD};margin-top:-6px">خصم على كل الموقع</div>
  <div style="margin-top:22px;direction:rtl"><span class="chip">الخميس والجمعة ٢٦ و ٢٧ نوفمبر</span></div></div>
<div class="abs fine" style="left:0;right:0;top:1000px;text-align:center;color:{DEEP};direction:rtl">{TERMS}</div>'''
    return G.doc(PAPER, DEEP, body, extra=CSS)

if __name__ == '__main__':
    G.STORY = False
    for k, f in [('a', opt_a), ('b', opt_b), ('c', opt_c)]: G.shot(f'974-4years-option-{k}', f())
    print('ok')
