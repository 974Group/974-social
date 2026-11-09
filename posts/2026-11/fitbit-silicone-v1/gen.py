import subprocess,sys,os
from PIL import Image
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
SRC='/home/claude/974-social/products/fitbit-silicone-v1/uni/'
os.makedirs('crop',exist_ok=True)
for f in os.listdir(SRC):
    im=Image.open(SRC+f); im.crop(im.getbbox()).save('crop/'+f)
C=os.getcwd()+'/crop/'
BG='#F3EFEA'; INK='#1C1A19'; MUTE='#7B746E'; ACC='#F26A1B'
TRIO=[('orange','Orange'),('tiffany','Tiffany'),('maroon','Maroon')]
REST=[('black','Black'),('white','White'),('red','Red'),('pink','Pink'),('light-pink','Light Pink'),('lavender','Lavender'),('navy','Navy'),('grey-blue','Grey Blue'),
      ('blue-grey','Blue Grey'),('green','Green'),('grey','Grey'),('dark-grey','Dark Grey'),('darker-grey','Darker Grey'),('beige','Beige'),('darker-beige','Darker Beige'),('brown','Brown')]
def page(story):
    W,H=(1080,1920) if story else (1080,1350)
    if story: tag_t,hd_t,h1,big_t,trio_t,trio_h,r1,rh,cta_b,pf=230,290,80,470,575,400,1065,120,440,300
    else:     tag_t,hd_t,h1,big_t,trio_t,trio_h,r1,rh,cta_b,pf=44,96,64,190,300,370,770,112,170,38
    trio=''.join(f'<div class="t"><img src="file://{C}{k}.png" style="height:{trio_h}px"><span>{n}</span></div>' for k,n in TRIO)
    rows=''.join(f'<div class="sw"><img src="file://{C}{k}.png" style="height:{rh}px"><span>{n}</span></div>' for k,n in REST)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;background:{BG};color:{INK}}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply;pointer-events:none}}
.tag{{position:absolute;top:{tag_t}px;left:56px;right:56px;display:flex;justify-content:space-between;font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:6px;color:{MUTE}}}
.tag b{{color:{ACC}}}
.big{{position:absolute;top:{big_t}px;left:30px;font-family:Poppins;font-weight:700;font-size:{560 if story else 440}px;line-height:.8;letter-spacing:-30px;color:transparent;-webkit-text-stroke:3px rgba(242,106,27,.35)}}
.hd{{position:absolute;top:{hd_t}px;right:56px;text-align:right;direction:rtl}}
.hd h1{{font-weight:900;font-size:{h1}px;line-height:1.1}} .hd h1 em{{font-style:normal;color:{ACC}}}
.hd h1 bdi{{font-family:Poppins;font-weight:700}}
.hd p{{margin-top:8px;font-weight:600;font-size:{30 if story else 25}px;color:{MUTE}}} .hd p bdi{{font-family:Poppins;font-weight:700;color:{INK}}}
.trio{{position:absolute;top:{trio_t}px;left:50px;right:50px;display:flex;justify-content:space-between;align-items:flex-end;direction:ltr}}
.t{{display:flex;flex-direction:column;align-items:center}} .t img{{filter:drop-shadow(0 26px 26px rgba(60,30,10,.22))}}
.t span{{font-family:Poppins;font-weight:700;font-size:{22 if story else 19}px;margin-top:8px;color:{INK}}}
.rows{{position:absolute;top:{r1}px;left:36px;right:36px;display:grid;grid-template-columns:repeat(8,1fr);row-gap:{22 if story else 16}px;direction:ltr}}
.sw{{display:flex;flex-direction:column;align-items:center}} .sw img{{filter:drop-shadow(0 8px 8px rgba(0,0,0,.14))}}
.sw span{{font-family:Poppins;font-weight:500;font-size:{15 if story else 13}px;color:{MUTE};margin-top:4px;white-space:nowrap}}
.foot{{position:absolute;left:56px;right:56px;bottom:{cta_b}px;display:flex;align-items:center;justify-content:space-between;direction:rtl}}
.cta{{font-weight:800;font-size:{32 if story else 27}px}} .cta em{{font-style:normal;color:{ACC}}}
.price{{background:{INK};color:#fff;border-radius:999px;padding:4px 28px 8px;font-weight:800;font-size:{28 if story else 24}px;display:flex;align-items:baseline;gap:8px}}
.price b{{font-family:Poppins;font-weight:700;font-size:{48 if story else 40}px;color:{ACC}}}
{payfoot.css(1.0 if not story else 1.12)}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
</style></head><body>
<svg class="grain" width="100%" height="100%"><filter id="g"><feTurbulence baseFrequency="0.9" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
<div class="big">19</div>
<div class="tag"><span>FITBIT · <b>SILICONE</b></span><span>19 COLOURS</span></div>
<div class="hd"><h1><bdi>19</bdi> لون..<br><em>وكلها بـ <bdi>69</bdi></em></h1><p>سيليكون <bdi dir="ltr">Fitbit</bdi> ناعم بخطوط بارزة</p></div>
<div class="trio">{trio}</div>
<div class="rows">{rows}</div>
<div class="foot"><div class="cta">علّق <em>«فت بت»</em> ونرسل لك الرابط 📩</div><div class="price"><b>69</b>ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''
for s in (0,1): open(f'p_{s}.html','w').write(page(bool(s)))
subprocess.run(['node','-e',"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const s of [0,1]){const p=await b.newPage({viewport:{width:1080,height:s?1920:1350}});await p.goto('file://'+process.cwd()+'/p_'+s+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.screenshot({path:'out/974-fitbit-silicone-'+(s?'story':'post')+'.png'});}
await b.close();})()"""],check=True)
for s in (0,1): os.remove(f'p_{s}.html')
