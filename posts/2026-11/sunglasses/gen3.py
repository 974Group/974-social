import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
HEAD=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''
G21=[('zubarah','ZUBARAH','#4A515C'),('fuwairit','FUWAIRIT','#C2401A'),('dukhan','DUKHAN','#2F8A80'),
     ('khor','KHOR AL ADAID','#7652AA'),('pearl','THE PEARL','#5E9A2A'),('sealine','SEALINE','#C9621A')]
G33=[('lusail','LUSAIL','#4D5566'),('halul','HALUL','#2149A6'),('ruwais','AL RUWAIS','#9E1F25'),('doha','DOHA','#B9507E')]
def foot(acc,dark,story):
    return f'''<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«شمسية»</em> ونرسل لك الرابط 📩</div><div class="price"><b>319</b> ر.ق</div></div>'''
def fcss(acc,ink,story,s):
    return f'''.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:56px;right:56px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:{acc};color:{ink};border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40*s}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26*s}px;color:#fff}} .cta em{{font-style:normal;color:{acc}}}'''

def d21(W,H,story):
    s=1.12 if story else 1; T=150 if story else 0
    rowh=228 if not story else 300
    cards=''.join(f'''<div class="cd" style="--c:{c}"><div class="im"><img src="file://{C}{k}-glass.png"></div><b>{n}</b></div>''' for k,n,c in G21)
    return f'''<style>{HEAD}
body{{width:{W}px;height:{H}px;background:radial-gradient(ellipse at 50% 0%,#3a3f47 0%,#121417 70%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.logo{{position:absolute;top:{50+T}px;left:56px;height:46px}}
.tg{{position:absolute;top:{62+T}px;right:56px;font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:4px;color:#C9A24B}}
.h{{position:absolute;top:{118+T}px;left:0;right:0;text-align:center;direction:rtl;font-weight:900;font-size:{62*s}px;line-height:1.15}}
.h em{{font-style:normal;font-family:Poppins;color:#C9A24B}}
.sub{{position:absolute;top:{200*s+T+8}px;left:0;right:0;text-align:center;direction:rtl;font-weight:700;font-size:{27*s}px;opacity:.85}}
.grid{{position:absolute;left:44px;right:44px;top:{270*s+T+(30 if story else 0)}px;display:grid;grid-template-columns:1fr 1fr;gap:{16*s}px;direction:ltr}}
.cd{{height:{rowh}px;border-radius:26px;background:linear-gradient(160deg,var(--c) 0%,rgba(0,0,0,.25) 120%);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px 18px 10px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.15)}}
.im{{flex:1;width:100%;display:flex;align-items:center;justify-content:center;min-height:0}}
.im img{{max-width:92%;max-height:100%;filter:drop-shadow(0 14px 14px rgba(0,0,0,.45))}}
.cd b{{font-family:Poppins;font-weight:800;font-size:{20*s}px;letter-spacing:3px;margin-top:6px}}
.chips{{position:absolute;left:30px;right:30px;top:{(270*s+T+(30 if story else 0))+3*rowh+2*16*s+(22 if not story else 50)}px;display:flex;gap:10px;direction:rtl;justify-content:center}}
.chips span{{border:2px solid #C9A24B;border-radius:40px;padding:3px 18px 7px;font-weight:800;font-size:{22*s}px;white-space:nowrap}}
.chips b{{font-family:Poppins}}
{fcss('#C9A24B','#121417',story,s)}
</style><body>
<img class="logo" src="file://{LOGO}"><div class="tg">974 GUARDS</div>
<div class="h">وزنها <em>21</em> جرام.. ما تحس فيها</div>
<div class="sub">6 ألوان · عدسة تغمق بروحها مع الشمس</div>
<div class="grid">{cards}</div>
<div class="chips"><span>☀️ فوتوكروميك</span><span>UV400</span><span>إطار TR90 مرن</span></div>
{foot('#C9A24B','#121417',story)}</body>'''

def d33(W,H,story):
    s=1.12 if story else 1; T=150 if story else 0
    if not story: hT,gT,ch,gap,eT,fT=118,222,312,18,893,1025
    else:         hT,gT,ch,gap,eT,fT=300,440,400,20,1290,1450
    cards=''.join(f'''<div class="cd" style="--c:{c}"><div class="im"><img src="file://{C}{k}-glass.png"></div><div class="nb"><b>{n}</b><i>{'عدسة وردية' if k=='doha' else 'فوتوكروميك'}</i></div></div>''' for k,n,c in G33)
    return f'''<style>{HEAD}
body{{width:{W}px;height:{H}px;background:linear-gradient(180deg,#720842 0%,#51022D 60%,#2E0119 100%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;top:{48+T-(0 if not story else 40)}px;left:44px;right:44px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}}
.top span{{font-family:Poppins;font-weight:700;font-size:{18*s}px;letter-spacing:5px;color:#F4C6DC}}
.h{{position:absolute;top:{hT}px;left:44px;right:44px;direction:rtl;font-weight:900;font-size:{50*s}px;line-height:1.2;text-align:center;white-space:nowrap}}
.h em{{font-style:normal;color:#F4C6DC}}
.grid{{position:absolute;left:44px;right:44px;top:{gT}px;display:grid;grid-template-columns:1fr 1fr;gap:{gap}px}}
.cd{{height:{ch}px;border-radius:26px;background:#F4F1F2;display:flex;flex-direction:column;overflow:hidden}}
.im{{flex:1;display:flex;align-items:center;justify-content:center;padding:14px 18px;min-height:0}}
.im img{{max-width:100%;max-height:100%;filter:drop-shadow(0 12px 12px rgba(0,0,0,.25))}}
.nb{{background:var(--c);height:{46*s}px;padding:0 18px;display:flex;justify-content:space-between;align-items:center}}
.nb b{{font-family:Poppins;font-weight:800;font-size:{20*s}px;letter-spacing:2px;white-space:nowrap}}
.nb i{{font-style:normal;font-weight:700;font-size:{18*s}px;opacity:.95}}
.exp{{position:absolute;left:44px;right:44px;top:{eT}px;height:{108*s}px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:24px;padding:0 22px;display:flex;align-items:center;gap:12px;direction:rtl}}
.exp .tx{{flex:1}}
.exp .tx b{{display:block;font-weight:900;font-size:{25*s}px;color:#F4C6DC;line-height:1.3}}
.exp .tx i{{display:block;font-style:normal;font-weight:600;font-size:{19*s}px;line-height:1.35}}
.exp .tl{{display:flex;flex-direction:column;align-items:center;gap:2px}}
.exp .tl img{{height:{54*s}px;background:#fff;border-radius:12px;padding:5px 8px}}
.exp .tl span{{font-weight:700;font-size:{15*s}px}}
.exp .ar{{font-size:{26*s}px;font-weight:900;color:#F4C6DC}}
.feat{{position:absolute;left:44px;right:44px;top:{fT}px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;direction:rtl}}
.feat span{{background:rgba(255,255,255,.12);border-radius:16px;height:{50*s}px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:{21*s}px;white-space:nowrap}}
.feat b{{font-family:Poppins;color:#F4C6DC;margin-left:6px}}
{fcss('#F4C6DC','#51022D',story,s)}
</style><body>
<div class="top"><span>974 GUARDS · F26</span><img src="file://{LOGO}"></div>
<div class="h">ذراع تتعدّل <em>4 وضعيات</em> وتثبت على راسك</div>
<div class="grid">{cards}</div>
<div class="exp"><div class="tx"><b>يعني شنو فوتوكروميك؟</b><i>العدسة تغمق بروحها تحت الشمس وترجع شفافة بالظل والليل</i></div><div class="tl"><img src="file://{C}halul-clear.png"><span>بالظل</span></div><div class="ar">←</div><div class="tl"><img src="file://{C}halul-dark.png"><span>بالشمس</span></div></div>
<div class="feat"><span><b>33</b> جرام</span><span>أطراف معدن تنثني</span><span>ضد الصدمات</span></div>
{foot('#F4C6DC','#51022D',story)}</body>'''
for nm,fn in (('21g',d21),('f26',d33)):
    for kind,W,H,st in (('post',1080,1350,False),('story',1080,1920,True)):
        name=f'974-sun-{nm}-{kind}'
        open(name+'.html','w').write('<!doctype html><html><head><meta charset="utf-8"></head>'+fn(W,H,st)+'</html>')
        js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{name}.html');await pg.waitForTimeout(700);await pg.screenshot({{path:'{name}.png'}});await b.close();}})()"
        subprocess.run(['node','-e',js],check=True)
