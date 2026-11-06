import subprocess,sys
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R='/home/claude/974-social/'
G=R+'products/goggles/'; MK=R+'posts/2026-11/face-mask/src/cut/'
LOGO=R+'posts/2026-11/pilates-socks/src/logo-white.png'
GS=[('green','Green','#1F8F7A'),('iceblue','Ice Blue','#4BB3E6'),('maroon','Maroon','#8E1450'),('red','Red','#D7263D'),('silver','Silver & Black','#9AA3AD'),('uae','UAE','#2E9E4F')]
def page(story):
    W,H=1080,(1920 if story else 1350); s=1.1 if story else 1; T=150 if story else 0
    ch=230 if not story else 300
    cards=''.join(f'<div class="cd" style="--c:{c}"><div class="im"><img src="file://{G}{k}-edition-render.png"></div><div class="nm"><i></i>{n}</div></div>' for k,n,c in GS)
    gT=255+T; gEnd=gT+3*ch+2*14
    mT=gEnd+(22 if not story else 50)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:linear-gradient(180deg,#140F22 0%,#3B1D2E 40%,#8A4A2C 80%,#B66A35 100%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.stars{{position:absolute;inset:0;background-image:radial-gradient(1.5px 1.5px at 12% 8%,#fff8,transparent),radial-gradient(1.5px 1.5px at 30% 14%,#fff6,transparent),radial-gradient(2px 2px at 70% 6%,#fff9,transparent),radial-gradient(1.5px 1.5px at 85% 15%,#fff6,transparent),radial-gradient(1.5px 1.5px at 52% 10%,#fff5,transparent)}}
.top{{position:absolute;top:{46+T-(0 if not story else 40)}px;left:44px;right:44px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:{17*s}px;letter-spacing:5px;color:#FFD9A8}}
.h{{position:absolute;top:{112+T}px;left:0;right:0;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:{62*s}px;line-height:1.2}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:{25*s}px;color:#FFD9A8}}
.grid{{position:absolute;left:44px;right:44px;top:{gT}px;display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.cd{{height:{ch}px;border-radius:24px;background:linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.04));box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);display:flex;flex-direction:column;overflow:hidden}}
.im{{flex:1;display:flex;align-items:center;justify-content:center;padding:10px 20px 0;min-height:0}}
.im img{{max-width:100%;max-height:100%;filter:drop-shadow(0 14px 14px rgba(0,0,0,.45))}}
.nm{{height:{44*s}px;display:flex;align-items:center;justify-content:center;gap:8px;font-family:Poppins;font-weight:700;font-size:{20*s}px;letter-spacing:1px}}
.nm i{{width:12px;height:12px;border-radius:50%;background:var(--c);box-shadow:0 0 0 2px rgba(255,255,255,.5)}}
.mask{{position:absolute;left:44px;right:44px;top:{mT}px;height:{120*s}px;border-radius:24px;background:rgba(0,0,0,.3);display:flex;align-items:center;justify-content:space-between;padding:0 24px;direction:rtl}}
.mask .tx b{{display:block;font-weight:900;font-size:{28*s}px}}
.mask .tx i{{display:block;font-style:normal;font-weight:700;font-size:{20*s}px;color:#FFD9A8}}
.mask .im3{{display:flex;gap:10px;align-items:flex-end}}
.mask .im3 img{{height:{96*s}px;filter:drop-shadow(0 8px 8px rgba(0,0,0,.4))}}
.mask .pr{{background:#FFD9A8;color:#3B1D2E;border-radius:30px;padding:2px 20px 6px;font-weight:900;font-size:{28*s}px;white-space:nowrap}}
.mask .pr b{{font-family:Poppins}}
.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:44px;right:44px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#FFD9A8;color:#3B1D2E;border-radius:40px;padding:4px 30px 10px;font-weight:900;font-size:{36*s}px;white-space:nowrap}}
.price b{{font-family:Poppins}} .price small{{font-size:{20*s}px}}
.cta{{font-weight:700;font-size:{24*s}px}} .cta em{{font-style:normal;color:#FFD9A8}}
</style></head><body><div class="stars"></div>
<div class="top"><span>EDITION GOGGLES</span><img src="file://{LOGO}"></div>
<div class="h"><b>جاهز للبر؟ 🏜️</b><i>6 إصدارات · معاها عدسة شفافة لليل تتبدل بالمغناطيس</i></div>
<div class="grid">{cards}</div>
<div class="mask"><div class="tx"><b>وكمّلها بماسك 974</b><i>23 لون · يحميك من الغبار والهوا</i></div><div class="im3"><img src="file://{MK}beige.png"><img src="file://{MK}black.png"><img src="file://{MK}orange.png"></div><div class="pr"><b>39</b> ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«نظارة»</em> أو <em>«ماسك»</em> ونرسل لك الرابط 📩</div><div class="price"><small>النظارة </small><b>319</b> ر.ق</div></div>
</body></html>'''
for kind,st in (('post',False),('story',True)):
    n=f'974-goggles-editions-masks-{kind}'; H=1920 if st else 1350
    open(n+'.html','w').write(page(st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
