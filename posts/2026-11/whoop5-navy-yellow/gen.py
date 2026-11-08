import subprocess,sys
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
NAVY='#1C2757'; YEL='#F4DE3C'; INK='#0E1330'
def page(story):
    W,H=(1080,1920) if story else (1080,1350)
    top = 330 if story else 130          # headline top
    band_y = 720 if story else 360        # band block top
    bh = 640 if story else 600            # band height
    pf = 300 if story else 60
    price_b = pf+110
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;background:{NAVY}}}
.half{{position:absolute;top:0;bottom:0;width:50%}}
.l{{left:0;background:{NAVY}}} .r{{right:0;background:{YEL}}}
.grain{{position:absolute;inset:0;opacity:.12;mix-blend-mode:overlay;pointer-events:none}}
.tag{{position:absolute;top:{64 if story else 40}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:6px}}
.tag span{{display:inline-block;width:50%}} .tag .a{{color:{YEL};text-align:center}} .tag .b{{color:{NAVY}}}
.hd{{position:absolute;top:{top}px;left:0;right:0;display:flex;direction:rtl}}
.hd div{{width:50%;text-align:center;font-weight:900;font-size:{74 if story else 64}px;line-height:1.1;padding:0 36px}}
.hd .y{{color:{NAVY}}} .hd .n{{color:{YEL}}}
.hd small{{display:block;font-weight:600;font-size:{34 if story else 30}px;opacity:.85;margin-top:10px}}
.band{{position:absolute;top:{band_y}px;height:{bh}px}}
.band img{{height:100%;filter:drop-shadow(0 30px 40px rgba(0,0,0,.28))}}
.b1{{left:25%;transform:translateX(-50%)}}
.b2{{left:75%;transform:translateX(-50%)}}
.ol{{position:absolute;top:{band_y+bh-40}px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:700;font-size:{150 if story else 120}px;letter-spacing:-4px;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.55);opacity:.9}}
.price{{position:absolute;bottom:{price_b}px;left:50%;transform:translateX(-50%);background:{INK};color:#fff;border-radius:999px;padding:10px 12px 10px 34px;display:flex;align-items:center;gap:22px;direction:rtl;white-space:nowrap}}
.price .nm{{font-weight:800;font-size:34px}}
.price .nm bdi{{font-family:Poppins;font-weight:700;font-size:30px;margin-right:8px}}
.price .pr{{background:{YEL};color:{INK};border-radius:999px;padding:4px 26px;font-weight:800;font-size:30px;display:flex;align-items:baseline;gap:8px}}
.price .pr b{{font-family:Poppins;font-weight:700;font-size:44px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF')}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
</style></head><body>
<div class="half l"></div><div class="half r"></div>
<svg class="grain" width="100%" height="100%"><filter id="g"><feTurbulence baseFrequency="0.9" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
<div class="tag"><span class="a">YELLOW · NAVY</span><span class="b">NAVY · YELLOW</span></div>
<div class="hd"><div class="y">برّا كحلي<small>وجوّا أصفر</small></div><div class="n">برّا أصفر<small>وجوّا كحلي</small></div></div>
<div class="band b1"><img src="file://{__import__('os').getcwd()}/yellownavy.png"></div>
<div class="band b2"><img src="file://{__import__('os').getcwd()}/navyyellow.png"></div>
<div class="price"><span class="nm">سيليكون<bdi dir="ltr">Whoop 5.0 · MG</bdi></span><span class="pr"><b>99</b>ر.ق</span></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''
import os
os.makedirs('out',exist_ok=True)
for story in (False,True):
    open(f'p_{int(story)}.html','w').write(page(story))
subprocess.run(['node','-e',"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const s of [0,1]){const p=await b.newPage({viewport:{width:1080,height:s?1920:1350}});await p.goto('file://'+process.cwd()+'/p_'+s+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:'out/974-w5-navy-yellow-'+(s?'story':'post')+'.png'});}
await b.close();})()"""],check=True)
