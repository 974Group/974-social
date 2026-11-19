# Instagram ad creatives (feed 1080x1350) for the 4 best sellers by revenue, last 60 days (19 Nov 2026).
# Ads only, not posted as stories. Full prices (no discounts). Fresh layout per product.
#  rolex   - Rolex customised Whoop soft fabric (3D print 159) - photo-led, dark
#  goggles - Summer Edition goggles = "2 in 1" (from 209)        - sand, diagonal hero
#  fitbit  - Fitbit Fabric bands (74)                            - fog, big-number + arc
#  cirqa3  - Garmin CIRQA fabric 3.0 (109)                       - navy, tile grid
import sys, os, math, subprocess
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R='/home/claude/974-social/'
LW=R+'posts/2026-11/pilates-socks/src/logo-white.png'
LB=R+'posts/2026-11/pilates-socks/src/logo-black.png'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'out'); os.makedirs(OUT,exist_ok=True)
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr;unicode-bidi:isolate}} .ar{{direction:rtl;text-align:right}}
body{{width:1080px;height:1350px;font-family:Cairo;position:relative;overflow:hidden}}
.pf{{position:absolute;left:28px;right:28px;bottom:30px}}'''

def doc(bg,ink,body,pf_ink=None,extra=''):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{background:{bg};color:{ink}}}
{payfoot.css(1.0,text=pf_ink or ink,label=pf_ink or ink)}
{extra}</style></head><body>{body}<div class="pf">{payfoot.html()}</div></body></html>'''

def cta(txt,bg,fg):
    return f'<div class="cta" style="background:{bg};color:{fg}">{txt} <span style="font-family:Poppins">←</span></div>'
CTA_CSS='.cta{display:inline-flex;align-items:center;gap:12px;border-radius:40px;padding:8px 30px 12px;font-weight:900;font-size:30px;direction:rtl;white-space:nowrap}'

# ---------- Rolex ----------
def rolex():
    ph=R+'reels/2026-11/rolex-src/s204.png'; C=R+'refs/rolex/'
    body=f'''
<div class="abs" style="inset:0 0 auto 0;height:900px;background:url(file://{ph}) center 42%/1080px auto no-repeat"></div>
<div class="abs" style="left:0;right:0;top:420px;height:500px;background:linear-gradient(180deg,rgba(20,12,8,0) 0%,rgba(20,12,8,.85) 70%,#140C08 100%)"></div>
<div class="abs" style="left:0;right:0;top:900px;bottom:0;background:#140C08"></div>
<img class="abs" src="file://{LW}" style="left:48px;top:46px;height:46px">
<div class="abs" style="right:48px;top:44px;background:#C9A24B;color:#140C08;border-radius:30px;padding:4px 22px 8px;font-weight:900;font-size:26px">الأكثر مبيعاً 🔥</div>
<div class="abs ar" style="right:48px;left:48px;top:640px;color:#fff">
  <div style="font-weight:900;font-size:76px;line-height:1.1">متأخر؟ <span style="color:#C9A24B">عادي..</span></div>
  <div style="font-weight:800;font-size:34px;opacity:.92;margin-top:6px">سيرك يقولها عنك: <span class="en" style="font-weight:700;font-style:italic">Who cares, I'm already late</span></div>
</div>
<div class="abs ar" style="right:48px;top:870px;color:#fff">
  <div style="font-weight:700;font-size:26px;opacity:.8">سير <span class="en">Rolex</span> قماش ناعم لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
  <div style="font-weight:700;font-size:26px;opacity:.8">طباعة <span class="en">3D</span> بارزة · سير فقط بدون الجهاز</div>
  <div style="margin-top:22px;display:flex;align-items:center;gap:26px;direction:rtl">
    <div style="font-weight:900;font-size:30px"><span class="en" style="font-size:78px;font-weight:900;color:#C9A24B">159</span> ر.ق</div>
    {cta('اطلبه الحين','#fff','#140C08')}
  </div>
</div>
<div class="abs" style="left:40px;top:930px;display:flex;gap:6px">
  <img src="file://{C}r18.png" style="height:130px"><img src="file://{C}r19.png" style="height:130px"><img src="file://{C}r20.png" style="height:130px">
</div>'''
    return doc('#140C08','#fff',body,pf_ink='#fff',extra=CTA_CSS)

# ---------- 2 in 1 goggles ----------
G=R+'posts/2026-11/summer-goggles/cut/'
def goggles():
    cols=[('yellow','Yellow','209'),('pink','Pink','209'),('black','Black','249'),('grey','Grey','249'),('red','Red','249'),('blue','Blue','249')]
    row=''.join(f'<div class="g"><img src="file://{G}{k}.png"><i class="en">{n}</i></div>' for k,n,p in cols)
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(120% 80% at 70% 30%,#F7E7C6 0%,#EBCF9B 55%,#D9B477 100%)"></div>
<div class="abs en" style="left:-20px;top:300px;font-weight:900;font-size:360px;line-height:.8;color:rgba(110,70,20,.10);letter-spacing:-12px">2 IN 1</div>
<img class="abs" src="file://{LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#5A3A12">974 GUARDS · 2 IN 1</div>
<div class="abs ar" style="right:48px;left:48px;top:120px;color:#2B1A06">
  <div style="font-weight:900;font-size:80px;line-height:1.08">بالستراب للبر..<br><span style="color:#A8670E">وبدونه نظارة شمسية</span></div>
</div>
<img class="abs" src="file://{G}yellow.png" style="left:90px;top:380px;width:900px;transform:rotate(-7deg);filter:drop-shadow(0 34px 34px rgba(90,55,10,.35))">
<div class="abs ar" style="right:48px;top:900px;display:flex;gap:12px;direction:rtl">
  <span class="tg">بولارايز + <span class="en">UV</span></span><span class="tg">عدستين بالعلبة</span><span class="tg">خفيفة <span class="en">TR90</span></span>
</div>
<div class="abs" style="left:30px;right:30px;top:975px;display:flex;justify-content:space-between">{row}</div>
<div class="abs" style="right:48px;left:48px;top:1100px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <div style="font-weight:900;font-size:30px;color:#2B1A06">من <span class="en" style="font-size:70px">209</span> ر.ق</div>
  {cta('اختار لونك','#2B1A06','#F7E7C6')}
</div>'''
    extra=CTA_CSS+'''.tg{background:rgba(255,255,255,.7);border-radius:30px;padding:4px 18px 7px;font-weight:800;font-size:22px;color:#2B1A06}
.g{width:165px;display:flex;flex-direction:column;align-items:center}.g img{width:160px;filter:drop-shadow(0 8px 8px rgba(90,55,10,.25))}
.g i{font-style:normal;font-weight:700;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:#5A3A12;margin-top:2px}'''
    return doc('#EBCF9B','#2B1A06',body,extra=extra)

# ---------- Fitbit fabric ----------
def fitbit():
    F=os.path.dirname(os.path.abspath(__file__))+'/fitbit-trim/'
    cols=['black','grey','navy','blue','fog','olive','lime','beige','light-pink','pinky-red','purple']
    r1=''.join(f'<img src="file://{F}{c}.png">' for c in cols[:6]); r2=''.join(f'<img src="file://{F}{c}.png">' for c in cols[6:])
    body=f'''
<div class="abs" style="inset:0;background:linear-gradient(180deg,#EEF3F3 0%,#DCE7E8 100%)"></div>
<img class="abs" src="file://{LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#355">FITBIT AIR · FABRIC</div>
<div class="abs ar" style="left:48px;right:48px;top:130px;text-align:center;color:#17302F">
  <div style="font-weight:900;font-size:58px;line-height:1.15">سير لـ <span class="en">Fitbit Air</span> بكل لون تبيه</div>
  <div style="font-weight:700;font-size:28px;opacity:.75;margin-top:6px">قماش مطاطي ناعم · يتنفّس · خفيف على اليد</div>
</div>
<div class="abs rw" style="top:330px">{r1}</div>
<div class="abs" style="left:0;right:0;top:560px;text-align:center;color:#17302F;direction:rtl">
  <span class="en" style="font-weight:900;font-size:220px;line-height:1;letter-spacing:-6px">74</span>
  <span style="font-weight:900;font-size:44px">ريال بس</span>
</div>
<div class="abs rw" style="top:830px">{r2}</div>
<div class="abs" style="left:0;right:0;top:1060px;text-align:center;font-weight:800;font-size:28px;color:#17302F"><span class="en">11</span> لون متوفر · سير فقط بدون الجهاز</div>
<div class="abs" style="left:0;right:0;top:1120px;text-align:center">{cta('اختار لونك','#17302F','#fff')}</div>'''
    return doc('#E3ECEC','#17302F',body,extra=CTA_CSS+'.pf{bottom:24px} .rw{left:0;right:0;display:flex;justify-content:center;gap:4px} .rw img{width:170px;height:200px;object-fit:contain;padding:12px 6px;filter:drop-shadow(0 10px 10px rgba(20,50,50,.18))}')

# ---------- Garmin CIRQA fabric 3.0 ----------
def cirqa3():
    C=R+'products/garmin-cirqa-fabric3/cut/'
    cols=[('pink','Pink','#F3B8C8'),('purple','Purple','#C8B8EC'),('navy','Navy','#AEB8D6'),('green','Green','#B9CDB0'),('orange','Orange','#F6C49C'),('light-pink','Light pink','#F6DADF'),('cement-gray','Cement Gray','#D2D2CE'),('black','Black','#B8B8B8')]
    tiles=''.join(f'<div class="t" style="background:{bg}"><img src="file://{C}{k}.png"><i class="en">{n}</i></div>' for k,n,bg in cols)
    body=f'''
<div class="abs" style="inset:0;background:#141A2E"></div>
<img class="abs" src="file://{LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#9FA8C8">GARMIN CIRQA · FABRIC 3.0</div>
<div class="abs ar" style="right:48px;left:48px;top:120px;color:#fff">
  <div style="font-weight:900;font-size:74px;line-height:1.1">قارمن واحد..<br><span style="color:#C9A24B">8 ستايلات</span></div>
  <div style="font-weight:700;font-size:27px;opacity:.75;margin-top:8px">سير نسيج <span class="en">3.0</span> لـ <span class="en">Garmin CIRQA</span> · يقفل بالفلكرو · <span class="en">S/M</span> و <span class="en">L/XL</span></div>
</div>
<div class="abs" style="left:40px;right:40px;top:400px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{tiles}</div>
<div class="abs" style="right:48px;left:48px;top:1105px;display:flex;align-items:center;justify-content:space-between;direction:rtl;color:#fff">
  <div style="font-weight:900;font-size:30px"><span class="en" style="font-size:72px;color:#C9A24B">109</span> ر.ق</div>
  {cta('اطلبه الحين','#C9A24B','#141A2E')}
</div>'''
    extra=CTA_CSS+'''.t{height:320px;border-radius:26px;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
.t img{height:230px;filter:drop-shadow(0 12px 12px rgba(0,0,0,.25))}.t i{font-style:normal;font-weight:700;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:#141A2E;margin-top:8px;opacity:.75}'''
    return doc('#141A2E','#fff',body,pf_ink='#fff',extra=extra)

def shot(name,html):
    p=os.path.join(OUT,name+'.html'); open(p,'w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1350}}}});await pg.goto('file://{p}');await pg.waitForTimeout(900);await pg.screenshot({{path:'{OUT}/{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True,env={**os.environ,'PLAYWRIGHT_BROWSERS_PATH':'/opt/pw-browsers','NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})

if __name__=='__main__':
    F={'rolex':rolex,'goggles':goggles,'fitbit':fitbit,'cirqa3':cirqa3}
    for k in (sys.argv[1:] or F): shot(f'974-ad-{k}',F[k]())
