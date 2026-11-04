import subprocess,sys
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'; P='/home/claude/974-social/products/fitbit-air-magnetic/'
PRICE=sys.argv[1] if len(sys.argv)>1 else '89'
cols=[('Black','black'),('Dark Blue','dark-blue'),('Wine Red','wine-red'),('Green','green'),('Dark Gray','dark-gray'),('Light Gray','light-gray'),('Starlight','starlight'),('White','white')]
def page(W,H,story):
    tw=226 if not story else 228; th=340 if not story else 470
    top=70 if not story else 150
    cards=''.join(f'<div class="c"><div class="t"><img src="file://{P}{f}-cut.png"></div><span>{n}</span></div>' for n,f in cols)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:linear-gradient(160deg,#2B2D31,#17181B);font-family:Cairo;color:#F1EFEA;position:relative;overflow:hidden}}
.head{{position:absolute;top:{top}px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center}}
.head img{{height:52px}} .head span{{font-family:Poppins;font-weight:500;letter-spacing:4px;font-size:20px;color:#B9B4AA}}
h1{{position:absolute;top:{top+80}px;right:56px;left:56px;text-align:right;direction:rtl;font-weight:900;font-size:{66 if story else 62}px;line-height:1.15}}
h1 i{{font-style:normal;color:#C9A24B}}
.sub{{position:absolute;top:{top+(185 if story else 170)}px;right:56px;left:56px;direction:rtl;text-align:right;font-weight:700;font-size:{32 if story else 28}px;color:#C9C4BA}}
.sub b{{font-family:Poppins;font-weight:700}}
.grid{{position:absolute;top:{top+(270 if story else 240)}px;left:50%;transform:translateX(-50%);display:grid;grid-template-columns:repeat(4,{tw}px);gap:{20 if story else 16}px}}
.c{{display:flex;flex-direction:column;align-items:center}}
.t{{width:{tw}px;height:{th}px;background:radial-gradient(circle at 50% 40%,#3A3C42,#26272B);border-radius:24px;display:flex;align-items:center;justify-content:center}}
.t img{{max-width:{tw-30}px;max-height:{th-40}px;filter:drop-shadow(0 14px 16px rgba(0,0,0,.45))}}
.c span{{font-family:Poppins;font-weight:500;font-size:{24 if story else 21}px;margin-top:8px;color:#E7E3DA}}
.pf{{position:absolute;left:28px;right:28px;bottom:{150 if not story else 240}px}}
{payfoot.css(1.0 if not story else 1.12, text='#F1EFEA', label='#C9C4BA')}
.foot{{position:absolute;left:56px;right:56px;bottom:{110 if story else 48}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#C9A24B;color:#17181B;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{48 if story else 40}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{30 if story else 26}px}}
.cta em{{font-style:normal;color:#C9A24B}}
</style></head><body>
<div class="head"><img src="file:///home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png"><span>FITBIT AIR · MAGNETIC</span></div>
<h1>بدون قفل<i>..</i> يتسكّر بالمغناطيس</h1>
<div class="sub">منسوج مطاطي خفيف · يتضبط على أي معصم · سير <b>Fitbit Air</b></div>
<div class="grid">{cards}</div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«فت بت»</em> ونرسل لك الرابط 📩</div><div class="price"><b>{PRICE}</b> ر.ق</div></div>
</body></html>'''
for name,W,H,st in (('974-fitbit-air-magnetic-post',1080,1350,False),('974-fitbit-air-magnetic-story',1080,1920,True)):
    open(name+'.html','w').write(page(W,H,st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(800);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print('ok')
