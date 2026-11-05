import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
A=dict(w='21',a='UV400',b='TR90 مرن',ph=True)   # 21g model
F=dict(w='33',a='ضد الصدمات',b='4 وضعيات',ph=True)  # F26
P=[('zubarah','ZUBARAH','25.97° N','Made to last','#454B55','#1A1D22','#D5DAE2',A),
   ('lusail','LUSAIL','25.42° N','Made to lead','#4D5566','#1E222B','#B6C9DD',F),
   ('fuwairit','FUWAIRIT','26.04° N','Made to brave','#2A2526','#0D0C0D','#FF6A2E',A),
   ('halul','HALUL','25.67° N','Made to explore','#2149A6','#0C1B45','#6FB7FF',F),
   ('dukhan','DUKHAN','25.42° N','Made to endure','#2F8A80','#123E3A','#9BEADD',A),
   ('ruwais','AL RUWAIS','26.14° N','Made to defy','#9E1F25','#3E080B','#FF7A66',F),
   ('khor','KHOR AL ADAID','24.63° N','Made to discover','#7652AA','#2E1C47','#DCC4FF',A),
   ('doha','DOHA','25.28° N','Made to focus','#B9507E','#521A37','#FFC8DD',dict(F,ph=False)),
   ('pearl','THE PEARL','25.37° N','Made to protect','#4E8A24','#18330A','#E8F55A',A),
   ('sealine','SEALINE','24.85° N','Made to wander','#C9621A','#4E2306','#FFC066',A)]
def page(p,W,H,story):
    k,name,coord,tag,c1,c2,acc,sp=p
    T=0 if not story else 150
    hero_w=900 if not story else 960
    big=118 if len(name)<9 else (92 if len(name)<12 else 80)
    if story: big=int(big*1.08)
    if sp['ph']:
        mid=f'''<div class="ph"><div class="lens"><img src="file://{C}{k}-clear.png"><span>☁️ بالظل</span></div>
<div class="arr">←</div><div class="lens"><img src="file://{C}{k}-dark.png"><span>☀️ بالشمس</span></div>
<div class="phx"><b>عدسة فوتوكروميك</b><i>تغمق بروحها مع الشمس</i></div></div>'''
    else:
        mid=f'''<div class="ph"><div class="lens wide"><img src="file://{C}{k}-b.png"></div><div class="phx"><b>عدسة وردية</b><i>رؤية واضحة وناعمة</i></div></div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:radial-gradient(ellipse at 50% 42%,{c1} 0%,{c2} 78%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.bgc{{position:absolute;left:-30px;right:-30px;top:{430+T}px;text-align:center;font-family:Poppins;font-weight:900;font-size:{250 if not story else 270}px;letter-spacing:-6px;color:rgba(255,255,255,.06);white-space:nowrap}}
.logo{{position:absolute;top:{50+T}px;left:56px;height:46px}}
.tg{{position:absolute;top:{62+T}px;right:56px;font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:4px;color:{acc}}}
.nm{{position:absolute;top:{120+T}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:900;font-size:{big}px;line-height:1;letter-spacing:2px}}
.co{{position:absolute;top:{120+T+big+12}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:500;font-size:{26 if not story else 30}px;letter-spacing:6px;color:{acc}}}
.ar{{position:absolute;top:{120+T+big+58}px;left:0;right:0;text-align:center;direction:rtl;font-weight:800;font-size:{30 if not story else 36}px;opacity:.92}}
.hero{{position:absolute;left:50%;top:{350+T+(0 if not story else 60)}px;width:{hero_w}px;transform:translateX(-50%);filter:drop-shadow(0 30px 34px rgba(0,0,0,.45))}}
.ph{{position:absolute;left:56px;right:56px;top:{800+T+(0 if not story else 160)}px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:26px;padding:16px 22px;display:flex;align-items:center;gap:16px;direction:rtl}}
.lens{{display:flex;flex-direction:column;align-items:center;gap:4px}}
.lens img{{height:{86 if not story else 110}px;background:#fff;border-radius:16px;padding:8px 12px}}
.lens.wide img{{height:{120 if not story else 150}px}}
.lens span{{font-weight:700;font-size:{17 if not story else 21}px}}
.arr{{font-size:36px;color:{acc};font-weight:900}}
.phx{{margin-right:auto;text-align:left;direction:rtl}}
.phx b{{display:block;font-weight:900;font-size:{28 if not story else 34}px;color:{acc};text-align:right}}
.phx i{{display:block;font-style:normal;font-weight:600;font-size:{21 if not story else 25}px;opacity:.9;text-align:right}}
.chips{{position:absolute;left:56px;right:56px;top:{970+T+(0 if not story else 230)}px;display:flex;gap:12px;direction:rtl;justify-content:center}}
.chips span{{border:2px solid {acc};border-radius:40px;padding:4px 22px 7px;font-weight:800;font-size:{23 if not story else 28}px;white-space:nowrap}}
.chips b{{font-family:Poppins}}
.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:56px;right:56px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:{acc};color:{c2};border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;color:{acc}}}
</style></head><body>
<div class="bgc">{coord.replace(' ','')}</div>
<img class="logo" src="file://{LOGO}"><div class="tg">974 GUARDS</div>
<div class="nm">{name}</div><div class="co">{coord} · {tag.upper()}</div>
<div class="ar">نظارة شمسية رياضية</div>
<img class="hero" src="file://{C}{k}-hero.png">
{mid}
<div class="chips"><span><b>{sp['w']}</b> جرام بس</span><span>{sp['a']}</span><span>{sp['b']}</span></div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«شمسية»</em> ونرسل لك الرابط 📩</div><div class="price"><b>319</b> ر.ق</div></div>
</body></html>'''
only=sys.argv[1:] 
for p in P:
    if only and p[0] not in only: continue
    for kind,W,H,st in (('post',1080,1350,False),('story',1080,1920,True)):
        name=f'974-sun-{p[0]}-{kind}'
        open(name+'.html','w').write(page(p,W,H,st))
        js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{name}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{name}.png'}});await b.close();}})()"
        subprocess.run(['node','-e',js],check=True)
print('ok')
