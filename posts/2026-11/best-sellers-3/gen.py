# Three best-sellers without an IG design (9 Nov 2026), three different layouts:
#  A) Garmin CIRQA fabric 3.0  — hero band + wave of colours (light lavender)
#  B) Garmin CIRQA silicone    — ring of 9 colours around the price (dark)
#  C) Whoop 5 fabric (99)      — staggered two-row colour line-up (cream)
import sys, os, math, subprocess
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
P='/home/claude/974-social/products/'
LW='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
LB='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
GRAIN="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}} .ar{{direction:rtl;text-align:right}}
.grain{{position:absolute;inset:0;background:{GRAIN};opacity:.14;mix-blend-mode:soft-light;pointer-events:none}}
.ol{{-webkit-text-stroke:2px currentColor;color:transparent}}'''

def page(H,bg,ink,body,story,logo,tag,price,cta,extra='',pf_ink=None):
    pf_b=250 if story else 130; ft_b=124 if story else 36; t=200 if story else 48
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:1080px;height:{H}px;background:{bg};color:{ink};font-family:Cairo;position:relative;overflow:hidden}}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf_b}px}}
{payfoot.css(1.0 if not story else 1.12, text=pf_ink or ink, label=pf_ink or ink)}
.foot{{position:absolute;left:48px;right:48px;bottom:{ft_b}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.pill{{border:2px solid {ink};border-radius:40px;padding:4px 26px 8px;font-weight:900;font-size:32px;white-space:nowrap}} .pill b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;text-decoration:underline;text-underline-offset:6px}}
.top{{position:absolute;left:48px;right:48px;top:{t}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .bo{{display:inline-block;margin-top:14px;font-weight:800;font-size:20px;border:1.5px dashed currentColor;border-radius:30px;padding:2px 16px 4px;opacity:.75}} .top span{{font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px}}
{extra}</style></head><body>
{body}<div class="grain"></div>
<div class="top"><img src="file://{logo}"><span>{tag}</span></div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">{cta}</div><div class="pill"><b>{price}</b> ر.ق</div></div>
</body></html>'''

# ---------- A: CIRQA fabric 3.0 ----------
A_COL=[('pink','Pink'),('light-pink','Light pink'),('purple','Purple'),('navy','Navy'),('green','Green'),('cement-gray','Cement Gray'),('orange','Orange'),('black','Black')]
def cirqa3(story=False):
    o=150 if story else 0; H=1920 if story else 1350; INK='#2A1F3D'; C=P+'garmin-cirqa-fabric3/cut/'
    n=len(A_COL); bh=150 if not story else 158; step=124
    x0=(1080-step*(n-1))//2
    wave=''
    for i,(f,name) in enumerate(A_COL):
        y=math.sin(i/(n-1)*math.pi*1.6)*26
        wave+=f'<div class="wv" style="left:{x0+i*step-60}px;top:{y:.0f}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i>{name}</i></div>'
    body=f'''
<div class="abs en ol" style="left:-30px;top:{o+(170 if story else 110)}px;font-weight:700;font-size:{430 if story else 400}px;line-height:.8;letter-spacing:-18px;color:rgba(42,31,61,.13)">3.0</div>
<img class="abs" src="file://{C}purple.png" style="left:{70 if story else 70}px;top:{o+(250 if story else 170)}px;height:{520 if story else 470}px;filter:drop-shadow(0 30px 40px rgba(60,40,90,.28))">
<div class="abs ar" style="right:48px;top:{o+(270 if story else 160)}px;width:{470 if story else 460}px">
 <div style="font-weight:900;font-size:{80 if story else 72}px;line-height:1.08">نسيج<br>ينسيك<br><span style="color:#7B5CC4">إنك لابسه</span></div>
 <div style="font-weight:700;font-size:{27 if story else 25}px;margin-top:18px;opacity:.8">Garmin CIRQA fabric 3.0<br>خفيف · يتنفّس · يقفل بالفلكرو</div>
 <div class="sz"><span>S/M</span><span>L/XL</span></div>
 <div class="bo">سير فقط · بدون الجهاز</div>
</div>
<div class="abs" style="left:0;right:0;top:{o+(900 if story else 730)}px;height:230px">{wave}</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1140 if story else 945)}px;font-weight:800;font-size:{30 if story else 27}px">8 ألوان.. <span style="opacity:.7">ولكل يوم مزاج</span></div>'''
    extra=f'''.wv{{position:absolute;width:120px;display:flex;flex-direction:column;align-items:center}} .wv img{{filter:drop-shadow(0 12px 14px rgba(60,40,90,.22))}}
.wv i{{font-style:normal;font-family:Poppins;font-weight:700;font-size:13px;letter-spacing:1px;margin-top:8px;opacity:.7;white-space:nowrap;text-transform:uppercase}}
.sz{{display:flex;gap:10px;margin-top:20px;justify-content:flex-end;direction:ltr}} .sz span{{font-family:Poppins;font-weight:700;font-size:22px;border:2px solid {INK};border-radius:30px;padding:2px 18px}}'''
    return page(H,'linear-gradient(170deg,#F4EFF7 0%,#E9E1F2 55%,#F6EEF1 100%)',INK,body,story,LB,'GARMIN CIRQA · FABRIC 3.0',109,'علّق <em>«قارمن»</em> ونرسل لك الرابط 📩',extra)

# ---------- B: CIRQA silicone (ring) ----------
B_COL=['black','white','orange','army-green','grey','dusty-pink','navy','beige','lemon']
def cirqa_sil(story=False):
    o=150 if story else 0; H=1920 if story else 1350; C=P+'garmin-cirqa-silicone-v1/cut/'
    cx=540; cy=o+(720 if story else 580); R=318 if story else 292; bh=175 if story else 165
    ring=''
    for i,f in enumerate(B_COL):
        a=-math.pi/2+i*2*math.pi/len(B_COL)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        ring+=f'<img class="abs" src="file://{C}{f}.png" style="height:{bh}px;left:{x:.0f}px;top:{y:.0f}px;transform:translate(-50%,-50%);filter:drop-shadow(0 14px 18px rgba(0,0,0,.5))">'
    body=f'''
<div class="abs" style="left:{cx-(R+150)}px;top:{cy-(R+150)}px;width:{2*(R+150)}px;height:{2*(R+150)}px;border-radius:50%;background:radial-gradient(circle,rgba(215,230,74,.10) 0%,rgba(215,230,74,0) 62%)"></div>
<div class="abs" style="left:{cx-R}px;top:{cy-R}px;width:{2*R}px;height:{2*R}px;border-radius:50%;border:1.5px dashed rgba(255,255,255,.14)"></div>
{ring}
<div class="abs" style="left:{cx-170}px;top:{cy-150}px;width:340px;text-align:center">
 <div class="en" style="font-weight:700;font-size:150px;line-height:.9;color:#D7E64A">9</div>
 <div style="font-weight:900;font-size:40px;line-height:1.1;margin-top:4px">ألوان سيليكون</div>
 <div class="en" style="font-weight:700;font-size:16px;letter-spacing:4px;opacity:.6;margin-top:10px">GARMIN CIRQA</div>
</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1170 if story else 935)}px">
 <div style="font-weight:900;font-size:{56 if story else 50}px;line-height:1.1">نوم، تمرين، دوام..<br><span style="color:#D7E64A">لون لكل وقت</span></div>
 <div class="bo">سير فقط · بدون الجهاز</div>
</div>'''
    return page(H,'radial-gradient(120% 90% at 50% 40%,#23262B 0%,#141518 100%)','#FFFFFF',body,story,LW,'GARMIN CIRQA · SILICONE',99,'علّق <em>«قارمن»</em> ونرسل لك الرابط 📩','')

# ---------- C: Whoop 5 fabric (staggered line-up) ----------
C_COL=[('alpine-green','Alpine Green'),('pine-green','Pine Green'),('green','Green'),('matcha','Matcha'),('light-blue','Light Blue'),
       ('purple','Purple'),('wine-red','Wine Red'),('copper','Copper'),('espresso','Espresso'),('dark-grey','Dark Grey')]
def w5fabric(story=False):
    o=150 if story else 0; H=1920 if story else 1350; INK='#2B2420'; C=P+'whoop5-fabric/cut/'
    bh=168 if not story else 180; cw=176
    rows=''
    for r in range(2):
        items=C_COL[r*5:(r+1)*5]; x0=(1080-cw*5)//2+(cw//2 if r else 0)-(cw//4)
        top=o+(490 if story else 400)+r*(bh+95)
        for i,(f,name) in enumerate(items):
            rows+=f'<div class="it" style="left:{x0+i*cw}px;top:{top}px;width:{cw}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i>{name}</i></div>'
    body=f'''
<div class="abs" style="left:0;right:0;top:{o+(450 if story else 362)}px;height:{2*bh+200}px;background:repeating-linear-gradient(-55deg,rgba(43,36,32,.035) 0 14px,transparent 14px 34px)"></div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(150 if story else 120)}px">
 <div style="font-weight:900;font-size:{78 if story else 70}px;line-height:1.08">10 ألوان fabric<br><span style="color:#9E1B2C">لـ Whoop 5.0</span></div>
 <div style="font-weight:700;font-size:{27 if story else 25}px;margin-top:10px;opacity:.75">نسيج ناعم · يتنفّس · خفيف على اليد</div>
</div>
{rows}
<div class="abs ar" style="right:48px;left:48px;top:{o+(1130 if story else 925)}px;font-weight:800;font-size:{30 if story else 27}px">أي لون يشبهك؟ <span style="opacity:.65">قول لنا بالتعليقات 👇</span></div>'''
    extra='''.it{position:absolute;display:flex;flex-direction:column;align-items:center} .it img{filter:drop-shadow(0 14px 16px rgba(43,36,32,.25))}
.it i{font-style:normal;font-family:Poppins;font-weight:700;font-size:13px;letter-spacing:1.5px;margin-top:10px;opacity:.65;text-transform:uppercase;white-space:nowrap}'''
    return page(H,'linear-gradient(180deg,#F3EEE6 0%,#ECE4D8 100%)',INK,body,story,LB,'WHOOP 5.0 · FABRIC',99,'اطلبه من <em>974group.net</em> 🛒',extra)

def shot(n,html,H):
    os.makedirs('out',exist_ok=True); open(f'out/{n}.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/out/{n}.html');await pg.waitForTimeout(900);await pg.screenshot({{path:'out/{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
if __name__=='__main__':
    F={'cirqa3':cirqa3,'cirqasil':cirqa_sil,'w5fabric':w5fabric}
    for k in (sys.argv[1:] or F):
        shot(f'974-{k}-post',F[k](),1350); shot(f'974-{k}-story',F[k](True),1920)
