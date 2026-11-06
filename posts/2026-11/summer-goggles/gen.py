import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
GS=[('yellow','Yellow','#E8C21A'),('black','Black','#2A2A2A'),('red','Red','#D7262B'),('pink','Pink','#D6337E'),('blue','Blue','#2441C9'),('grey','Grey','#8E9399')]
STRAP='''<svg viewBox="0 0 120 60" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 30 C8 14 112 14 112 30"/><rect x="22" y="22" width="76" height="28" rx="12"/><path d="M60 30v12"/></svg>'''
ARMS='''<svg viewBox="0 0 120 60" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><rect x="22" y="22" width="76" height="28" rx="12"/><path d="M22 30 L6 22"/><path d="M98 30 L114 22"/><path d="M60 30v12"/></svg>'''
def page(story):
    W,H=1080,(1920 if story else 1350); s=1.1 if story else 1; T=150 if story else 0
    ch=290 if not story else 360
    cards=''.join(f'<div class="cd" style="--c:{c}"><div class="im"><img src="file://{C}{k}.png"></div><div class="nm"><i></i>{n}</div></div>' for k,n,c in GS)
    if not story: hT,gT,mT,fT=112,240,240+2*ch+16+20,0
    else: hT,gT=300,470; mT=gT+2*ch+16+40
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:linear-gradient(180deg,#14161A 0%,#1E2228 55%,#2B2620 100%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;top:{46+T-(0 if not story else 40)}px;left:44px;right:44px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:{17*s}px;letter-spacing:5px;color:#F2C14E}}
.h{{position:absolute;top:{hT}px;left:44px;right:44px;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:{56*s}px;line-height:1.2}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:{25*s}px;color:#F2C14E;margin-top:2px}}
.grid{{position:absolute;left:44px;right:44px;top:{gT}px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.cd{{height:{ch}px;border-radius:22px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1);display:flex;flex-direction:column;overflow:hidden}}
.im{{flex:1;display:flex;align-items:center;justify-content:center;padding:12px 14px 0;min-height:0}}
.im img{{max-width:100%;max-height:100%;filter:drop-shadow(0 12px 12px rgba(0,0,0,.5))}}
.nm{{height:{38*s}px;display:flex;align-items:center;justify-content:center;gap:8px;font-family:Poppins;font-weight:500;font-size:{18*s}px}}
.nm i{{width:11px;height:11px;border-radius:50%;background:var(--c);box-shadow:0 0 0 2px rgba(255,255,255,.4)}}
.feat{{position:absolute;left:44px;right:44px;top:{mT}px;display:grid;grid-template-columns:1fr 1fr;gap:16px;direction:rtl}}
.f{{border-radius:22px;background:rgba(242,193,78,.1);box-shadow:inset 0 0 0 1px rgba(242,193,78,.35);padding:{18*s}px 18px;display:flex;align-items:center;gap:14px}}
.f svg{{width:{70*s}px;height:{35*s}px;color:#F2C14E;flex:none}}
.f b{{display:block;font-weight:900;font-size:{24*s}px;line-height:1.25}}
.f em{{display:block;font-style:normal;font-weight:600;font-size:{18*s}px;opacity:.85;line-height:1.35}}
.sw{{display:flex;align-items:center;gap:6px;flex:none}}
.ln{{width:{30*s}px;height:{30*s}px;border-radius:50%;}}
.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:44px;right:44px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:#F2C14E;color:#14161A;border-radius:40px;padding:4px 30px 10px;font-weight:900;font-size:{36*s}px;white-space:nowrap}}
.price b{{font-family:Poppins}} .price s{{font-family:Poppins;font-size:{22*s}px;opacity:.55;margin-right:10px}}
.cta{{font-weight:700;font-size:{24*s}px}} .cta em{{font-style:normal;color:#F2C14E}}
</style></head><body>
<div class="top"><span>974 GUARDS · 2 IN 1</span><img src="file://{LOGO}"></div>
<div class="h"><b>نظارة وحدة.. لكل طلعة</b><i>البر · الدراجات · سيلين · وحتى المشاوير</i></div>
<div class="grid">{cards}</div>
<div class="feat">
<div class="f">{STRAP}<div><b>نظارة بستراب</b><em>للدراجات والبر.. ثابتة على راسك</em></div></div>
<div class="f">{ARMS}<div><b>تتحول لنظارة عادية</b><em>القطع الجانبية بالعلبة.. تركبها بثواني</em></div></div>
<div class="f"><div class="sw"><span class="ln" style="background:linear-gradient(135deg,#F2C14E,#D7262B)"></span><span class="ln" style="background:rgba(255,255,255,.18);box-shadow:inset 0 0 0 2px rgba(255,255,255,.6)"></span></div><div><b>عدستين بالعلبة</b><em>ملونة للنهار.. وشفافة لليل</em></div></div>
<div class="f"><div class="sw" style="font-family:Poppins;font-weight:700;color:#F2C14E;font-size:{24*s}px">UV</div><div><b>بولرايزد + حماية UV</b><em>إطار TR90 خفيف ومرن</em></div></div>
</div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«نظارة»</em> ونرسل لك الرابط 📩</div><div class="price"><b>209</b> ر.ق <s>249</s></div></div>
</body></html>'''
for kind,st in (('post',False),('story',True)):
    n=f'974-goggles-2in1-{kind}'; H=1920 if st else 1350
    open(n+'.html','w').write(page(st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
