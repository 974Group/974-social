import subprocess,sys
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
A='/home/claude/974-social/products/garmin-cirqa-silicone-v2/src/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
cols=[('Black','black'),('Starlight','starlight'),('Lime','lime'),('Midnight Blue','midnight-blue'),('Army Green','green'),('Sea Mist Blue','sea-mist-blue'),('Mousse Pink','mousse-pink'),('Orange','orange'),('White','white'),('Light Gray','light-gray')]
def page(W,H,story,price):
    T=0 if not story else 110
    bh=228 if not story else 232
    rows=[cols[:5],cols[5:]]
    def row(r,top):
        out=''
        for i,(n,f) in enumerate(r):
            dy=0 if i%2==0 else (34 if not story else 44)
            out+=f'<div class="b" style="left:{40+i*200}px;top:{top+dy}px"><img src="file://{A}{f}-crop.png"><span>{n}</span></div>'
        return out
    r1=310+T+(10 if not story else 170); r2=r1+bh+(110 if not story else 200)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;font-family:Cairo;color:#fff;position:relative;overflow:hidden;
background:radial-gradient(circle,rgba(255,255,255,.07) 3px,transparent 4px) 0 0/34px 34px,linear-gradient(170deg,#1C2C52 0%,#101A33 60%,#0A1124 100%)}}
.logo{{position:absolute;top:{50+T}px;left:56px;height:46px}}
.tag{{position:absolute;top:{58+T}px;right:56px;font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:3px;border:2px solid #D9E33A;color:#D9E33A;padding:6px 16px;border-radius:30px}}
h1{{position:absolute;top:{120+T}px;left:0;right:0;text-align:center;direction:rtl;font-weight:900;font-size:{74 if not story else 76}px;white-space:nowrap;line-height:1.1}}
h1 em{{font-style:normal;color:#D9E33A}}
.feat{{position:absolute;top:{215+T+(0 if not story else 20)}px;left:0;right:0;display:flex;justify-content:center;gap:12px;direction:rtl}}
.feat span{{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:30px;padding:4px 18px 6px;font-weight:700;font-size:{22 if not story else 26}px}}
.b{{position:absolute;width:200px;display:flex;flex-direction:column;align-items:center}}
.b img{{height:{bh}px;max-width:174px;object-fit:contain;filter:drop-shadow(0 18px 18px rgba(0,0,0,.5))}}
.b span{{font-family:Poppins;font-weight:500;font-size:{17 if not story else 20}px;color:#C9D3EA;margin-top:6px;white-space:nowrap}}
.pf{{position:absolute;left:28px;right:28px;bottom:{142 if not story else 236}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#C9D3EA')}
.foot{{position:absolute;left:56px;right:56px;bottom:{36 if not story else 120}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{background:#D9E33A;color:#101A33;border-radius:40px;padding:4px 34px 10px;font-weight:900;font-size:{40 if not story else 48}px}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{26 if not story else 30}px}}
.cta em{{font-style:normal;color:#D9E33A}}
</style></head><body>
<img class="logo" src="file://{LOGO}"><div class="tag">GARMIN CIRQA 2.0</div>
<h1><em>يتنفّس</em> معك.. في كل تمرين</h1>
<div class="feat"><span>💨 فتحات تهوية</span><span>🪶 خفيف</span><span>💧 ضد العرق</span><span>🎨 10 ألوان</span></div>
{row(rows[0],r1)}{row(rows[1],r2)}
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«قارمن»</em> ونرسل لك الرابط 📩</div><div class="price"><b>{price}</b> ر.ق</div></div>
</body></html>'''
for name,W,H,st in (('974-cirqa-silicone-2-v2-post',1080,1350,False),('974-cirqa-silicone-2-v2-story',1080,1920,True)):
    open(name+'.html','w').write(page(W,H,st,'89'))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print('ok')
