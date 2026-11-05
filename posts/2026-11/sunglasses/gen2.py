import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
A=dict(w='21',a='UV400',b='TR90 مرن',ph=True)
F=dict(w='33',a='ضد الصدمات',b='4 وضعيات',ph=True)
# key,name,coord,tag,c1,c2,acc,spec,layout,headline
P=[('zubarah','ZUBARAH','25.97° N','Made to last','#4A515C','#16191E','#D5DAE2',A,'A','خفيفة.. وتعيش معك'),
   ('lusail','LUSAIL','25.42° N','Made to lead','#4D5566','#1A1E26','#B6C9DD',F,'B','تتعدّل على راسك'),
   ('fuwairit','FUWAIRIT','26.04° N','Made to brave','#2A2526','#0D0C0D','#FF6A2E',A,'C','عدسة نارية للشمس القوية'),
   ('halul','HALUL','25.67° N','Made to explore','#2149A6','#0A1840','#7CC0FF',F,'A','زرقة البحر على عيونك'),
   ('dukhan','DUKHAN','25.42° N','Made to endure','#2F8A80','#0F3A35','#A4F0E2',A,'B','لون منعش.. وعدسة فضية'),
   ('ruwais','AL RUWAIS','26.14° N','Made to defy','#9E1F25','#3A070A','#FF8A75',F,'C','الأحمر اللي يتحدّى الشمس'),
   ('khor','KHOR AL ADAID','24.63° N','Made to discover','#7652AA','#2A1942','#E2CCFF',A,'A','بنفسجي يلفت الأنظار'),
   ('doha','DOHA','25.28° N','Made to focus','#B9507E','#4E1734','#FFC8DD',dict(F,ph=False),'C','ناعمة.. وتركيز كامل'),
   ('pearl','THE PEARL','25.37° N','Made to protect','#4E8A24','#152E08','#E8F55A',A,'B','لمعة لؤلؤية بعدسة زرقا'),
   ('sealine','SEALINE','24.85° N','Made to wander','#C9621A','#4A2005','#FFC066',A,'A','لون الغروب على الرمال')]
HEAD=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''
def lenses(k,sp,acc,s,tile=86):
    if sp['ph']:
        return f'''<div class="lp"><div class="lens"><img src="file://{C}{k}-clear.png" style="height:{tile*s}px"><span>☁️ بالظل</span></div><div class="arr">←</div><div class="lens"><img src="file://{C}{k}-dark.png" style="height:{tile*s}px"><span>☀️ بالشمس</span></div></div>'''
    return ''

def phtxt(sp):
    return ('<b>عدسة فوتوكروميك</b><i>تغمق بروحها مع الشمس</i>' if sp['ph'] else '<b>عدسة وردية</b><i>رؤية واضحة وناعمة</i>')
def common(acc,c2,s,story,dark_text=False):
    return f'''.lens{{display:flex;flex-direction:column;align-items:center;gap:4px}}
.lens img{{background:#fff;border-radius:16px;padding:8px 12px;display:block}}
.lens span{{font-weight:700;font-size:{17*s}px}}
.lp{{display:flex;align-items:center;gap:12px;direction:rtl}}
.arr{{font-size:{34*s}px;color:{acc};font-weight:900}}
.chips span{{border:2px solid {acc};border-radius:40px;padding:3px 20px 7px;font-weight:800;font-size:{23*s}px;white-space:nowrap;display:inline-block}}
.chips b{{font-family:Poppins}}
.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:56px;right:56px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:{acc};color:{c2};border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40*s}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26*s}px;color:#fff}}
.cta em{{font-style:normal;color:{acc}}}
.logo{{position:absolute;height:46px}}'''
FOOT='''<div class="pf">{pf}</div>
<div class="foot"><div class="cta">علّق <em>«شمسية»</em> ونرسل لك الرابط 📩</div><div class="price"><b>319</b> ر.ق</div></div>'''
def chips(sp): return f'''<span><b>{sp['w']}</b> جرام بس</span><span>{sp['a']}</span><span>{sp['b']}</span>'''

def layA(p,W,H,story):
    k,name,coord,tag,c1,c2,acc,sp,_,hl=p; s=1.15 if story else 1; T=150 if story else 0
    big=118 if len(name)<9 else (100 if len(name)<12 else 84)
    hw=840 if not story else 980
    return f'''<style>{HEAD}
body{{width:{W}px;height:{H}px;background:radial-gradient(ellipse at 50% 45%,{c1} 0%,{c2} 78%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
{common(acc,c2,s,story)}
.bgc{{position:absolute;left:-30px;right:-30px;top:{440+T}px;text-align:center;font-family:Poppins;font-weight:900;font-size:250px;letter-spacing:-6px;color:rgba(255,255,255,.05);white-space:nowrap}}
.tg{{position:absolute;top:{62+T}px;right:56px;font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:4px;color:{acc}}}
.nm{{position:absolute;top:{110+T}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:900;font-size:{big*s}px;line-height:1;letter-spacing:2px;white-space:nowrap}}
.co{{position:absolute;top:{110+T+big*s+14}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:500;font-size:{24*s}px;letter-spacing:6px;color:{acc}}}
.ar{{position:absolute;top:{110+T+big*s+52*s}px;left:0;right:0;text-align:center;direction:rtl;font-weight:800;font-size:{32*s}px}}
.hero{{position:absolute;left:60px;right:60px;top:{340+T+(40 if story else 0)}px;height:{470 if not story else 560}px;display:flex;align-items:center;justify-content:center}}
.hero img{{max-width:100%;max-height:100%;filter:drop-shadow(0 30px 34px rgba(0,0,0,.5))}}
.ph{{position:absolute;left:56px;right:56px;top:{850+T+(170 if story else 0)}px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:26px;padding:14px 22px;display:flex;align-items:center;gap:16px;direction:rtl}}
.phx{{margin-right:auto}}
.phx b{{display:block;font-weight:900;font-size:{28*s}px;color:{acc}}}
.phx i{{display:block;font-style:normal;font-weight:600;font-size:{21*s}px;opacity:.9}}
.chips{{position:absolute;left:40px;right:40px;top:{1012+T+(230 if story else 0)}px;display:flex;gap:12px;direction:rtl;justify-content:center}}
</style><body>
<div class="bgc">{coord.replace(' ','')}</div>
<img class="logo" style="top:{50+T}px;left:56px" src="file://{LOGO}"><div class="tg">974 GUARDS</div>
<div class="nm">{name}</div><div class="co">{coord} · {tag.upper()}</div>
<div class="ar">{hl}</div>
<div class="hero"><img src="file://{C}{k}-mirror.png"></div>
<div class="ph">{lenses(k,sp,acc,s)}<div class="phx">{phtxt(sp)}</div></div>
<div class="chips">{chips(sp)}</div>
{FOOT.format(pf=payfoot.html())}</body>'''

def layB(p,W,H,story):
    k,name,coord,tag,c1,c2,acc,sp,_,hl=p; s=1.15 if story else 1; T=150 if story else 0
    return f'''<style>{HEAD}
body{{width:{W}px;height:{H}px;background:linear-gradient(155deg,{c1} 0%,{c2} 70%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
{common(acc,c2,s,story)}
.ring{{position:absolute;width:{820*s}px;height:{820*s}px;border-radius:50%;left:50%;top:{250+T}px;transform:translateX(-50%);border:{26*s}px solid {acc};opacity:.16}}
.nm{{position:absolute;top:{150+T}px;left:56px;font-family:Poppins;font-weight:900;font-size:{(104 if len(name)<9 else 92)*s}px;line-height:.95;letter-spacing:1px;white-space:nowrap}}
.co{{position:absolute;top:{110+T}px;left:60px;font-family:Poppins;font-weight:700;font-size:{22*s}px;letter-spacing:5px;color:{acc}}}
.tl{{position:absolute;top:{(262 if len(name)<9 else 250)*s+T+(0 if not story else -20)}px;left:60px;font-family:Poppins;font-weight:500;font-size:{24*s}px;letter-spacing:4px;opacity:.85}}
.ar{{position:absolute;top:{300*s+T}px;right:56px;direction:rtl;font-weight:900;font-size:{40*s}px;color:{acc};text-align:right}}
.hero{{position:absolute;left:40px;right:40px;top:{390*s+T}px;height:{500*s}px;display:flex;align-items:center;justify-content:center;transform:rotate(-6deg)}}
.hero img{{max-width:100%;max-height:100%;filter:drop-shadow(0 34px 30px rgba(0,0,0,.5))}}
.low{{position:absolute;left:56px;right:56px;top:{930*s+T+(60 if story else 0)}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.chips{{display:flex;flex-direction:column;gap:10px;align-items:flex-start}}
.lpw{{background:rgba(0,0,0,.25);border-radius:24px;padding:14px 18px;text-align:center}}
.lpw b{{display:block;font-weight:900;font-size:{24*s}px;color:{acc};margin-bottom:6px}}
</style><body>
<img class="logo" style="top:{50+T}px;right:56px" src="file://{LOGO}">
<div class="ring"></div>
<div class="co">{coord}</div><div class="nm">{name}</div><div class="tl">{tag.upper()}</div>
<div class="ar">{hl}</div>
<div class="hero"><img src="file://{C}{k}-mirror.png"></div>
<div class="low"><div class="chips">{chips(sp)}</div><div class="lpw"><b>{'تغمق بروحها مع الشمس' if sp['ph'] else 'عدسة وردية'}</b>{lenses(k,sp,acc,s,80)}</div></div>
{FOOT.format(pf=payfoot.html())}</body>'''

def layC(p,W,H,story):
    k,name,coord,tag,c1,c2,acc,sp,_,hl=p; s=1.15 if story else 1; T=150 if story else 0
    split=(640 if not story else 980)
    return f'''<style>{HEAD}
body{{width:{W}px;height:{H}px;background:{c2};font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
{common(acc,c2,s,story)}
.top{{position:absolute;left:0;right:0;top:0;height:{split}px;background:linear-gradient(180deg,#F4F1F2 0%,{acc} 160%);border-radius:0 0 60px 60px}}
.bigc{{position:absolute;left:0;right:0;top:{150+T}px;text-align:center;font-family:Poppins;font-weight:900;font-size:{(150 if len(name)<9 else 112)*s}px;color:{c1};opacity:.18;white-space:nowrap;letter-spacing:-2px}}
.nm{{position:absolute;top:{90+T}px;left:56px;font-family:Poppins;font-weight:900;font-size:{(64 if len(name)<9 else 54)*s}px;color:{c2};line-height:1;white-space:nowrap}}
.co{{position:absolute;top:{(165 if len(name)<9 else 152)*s+T-(0)}px;left:58px;font-family:Poppins;font-weight:700;font-size:{20*s}px;letter-spacing:4px;color:{c1}}}
.hero{{position:absolute;left:60px;right:60px;top:{200*s+T}px;height:{split-200*s-T+90}px;display:flex;align-items:center;justify-content:center}}
.hero img{{max-width:100%;max-height:100%;filter:drop-shadow(0 26px 24px rgba(0,0,0,.35))}}
.ar{{position:absolute;top:{split+30}px;left:56px;right:56px;direction:rtl;font-weight:900;font-size:{40*s}px;text-align:right;white-space:nowrap}}
.ar small{{display:block;font-family:Poppins;font-weight:500;font-size:{20*s}px;letter-spacing:4px;color:{acc};direction:ltr;text-align:right}}
.mid{{position:absolute;left:56px;right:56px;top:{split+(150 if not story else 175)}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.mid .phx b{{display:block;font-weight:900;font-size:{26*s}px;color:{acc}}}
.mid .phx i{{display:block;font-style:normal;font-weight:600;font-size:{20*s}px;opacity:.9}}
.chips{{position:absolute;left:40px;right:40px;top:{split+(310 if not story else 380)}px;display:flex;gap:12px;direction:rtl;justify-content:center}}
</style><body>
<div class="top"></div>
<img class="logo" style="top:{50+T}px;right:56px;filter:invert(1) brightness(.2)" src="file://{LOGO}">
<div class="bigc">{coord.replace(' ','')}</div>
<div class="nm">{name}</div><div class="co">{coord}</div>
<div class="hero"><img src="file://{C}{k}-mirror.png"></div>
<div class="ar">{hl}<small>{tag.upper()}</small></div>
<div class="mid"><div class="phx">{phtxt(sp)}</div>{lenses(k,sp,acc,s,82)}</div>
<div class="chips">{chips(sp)}</div>
{FOOT.format(pf=payfoot.html())}</body>'''
L=dict(A=layA,B=layB,C=layC)
only=sys.argv[1:]
for p in P:
    if only and p[0] not in only: continue
    for kind,W,H,st in (('post',1080,1350,False),('story',1080,1920,True)):
        name=f'974-sun-{p[0]}-{kind}'
        open(name+'.html','w').write('<!doctype html><html><head><meta charset="utf-8"></head>'+L[p[8]](p,W,H,st)+'</html>')
        js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{name}.html');await pg.waitForTimeout(700);await pg.screenshot({{path:'{name}.png'}});await b.close();}})()"
        subprocess.run(['node','-e',js],check=True)
print('ok')
