import subprocess,sys,os
from PIL import Image
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
SRC='/home/claude/974-social/products/garmin-cirqa-fabric/cut/'
os.makedirs('crop',exist_ok=True)
import glob
for f in glob.glob(SRC+'*.png'):
    im=Image.open(f); im.crop(im.getbbox()).save('crop/'+os.path.basename(f))
C=os.getcwd()+'/crop/'
BG='#15171A'; LIME='#C9E64B'; TXT='#F2F2EF'; MUTE='#9A9D97'
V1=[('v1-navy','Navy'),('v1-black','Black'),('v1-army-green','Army Green'),('v1-grey','Grey'),('v1-blue','Blue'),('v1-lime','Lime'),('v1-pink','Pink')]
V2=[('v2-green','Green'),('v2-black-grey','Black & Grey'),('v2-white-grey','White & Grey'),('v2-blue','Blue'),('v2-black','Black')]
def col(items,ver,line1,line2,story):
    hero=items[0]; rest=items[1:]
    sw=''.join(f'<div class="sw"><img src="file://{C}{k}.png"><span>{n}</span></div>' for k,n in rest)
    return f'''<div class="col"><div class="ver">{ver}</div><div class="hero"><img src="file://{C}{hero[0]}.png"></div><div class="hn">{hero[1]}</div>
<div class="d"><b>{line1}</b><span>{line2}</span></div><div class="sws">{sw}</div></div>'''
def page(story):
    W,H=(1080,1920) if story else (1080,1350)
    k=1.25 if story else 1.0
    top_tag=230 if story else 44; hd=290 if story else 96; cols_t=470 if story else 268
    pf=300 if story else 38
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;background:{BG};color:{TXT}}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:overlay;pointer-events:none}}
.tag{{position:absolute;top:{top_tag}px;left:56px;right:56px;display:flex;justify-content:space-between;font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:6px;color:{MUTE}}}
.tag b{{color:{LIME};font-weight:700}}
.hd{{position:absolute;top:{hd}px;left:56px;right:56px;text-align:center;direction:rtl}}
.hd h1{{font-weight:900;font-size:{int(66*k)}px;line-height:1.1}} .hd h1 em{{font-style:normal;color:{LIME}}}
.hd p{{margin-top:8px;font-weight:600;font-size:{int(26*k)}px;color:{MUTE}}} .hd p bdi{{font-family:Poppins;font-weight:700;color:{TXT}}}
.cols{{position:absolute;top:{cols_t}px;left:40px;right:40px;display:flex;direction:rtl}}
.col{{flex:1;display:flex;flex-direction:column;align-items:center;position:relative}}
.col+.col{{border-right:1px solid rgba(255,255,255,.12)}}
.ver{{font-family:Poppins;font-weight:700;font-size:{int(26*k)}px;letter-spacing:4px;color:{LIME};border:2px solid {LIME};border-radius:999px;padding:2px 22px}}
.hero{{height:{int(330*k)}px;margin-top:{int(18*k)}px}} .hero img{{height:100%;filter:drop-shadow(0 26px 30px rgba(0,0,0,.5))}}
.hn{{font-family:Poppins;font-weight:500;font-size:{int(16*k)}px;color:{MUTE};margin-top:6px}}
.d{{text-align:center;margin-top:{int(14*k)}px;direction:rtl}} .d b{{display:block;font-weight:800;font-size:{int(28*k)}px}} .d span{{display:block;font-weight:600;font-size:{int(20*k)}px;color:{MUTE}}}
.sws{{margin-top:16px;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 14px;width:430px;direction:ltr}}
.sw{{display:flex;flex-direction:column;align-items:center;width:{90 if story else 84}px}}
.sw img{{height:{82 if story else 76}px;filter:drop-shadow(0 6px 8px rgba(0,0,0,.4))}}
.sw span{{font-family:Poppins;font-weight:500;font-size:{14 if story else 13}px;color:{MUTE};white-space:nowrap;margin-top:3px}}
.foot{{position:absolute;left:56px;right:56px;bottom:{pf+(135 if story else 128)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl}}
.cta{{font-weight:800;font-size:{int(27*k)}px}} .cta em{{font-style:normal;color:{LIME}}}
.price{{background:{LIME};color:{BG};border-radius:999px;padding:4px 26px 8px;font-weight:800;font-size:{int(24*k)}px;display:flex;align-items:baseline;gap:8px}}
.price b{{font-family:Poppins;font-weight:700;font-size:{int(40*k)}px}}
{payfoot.css(1.0 if not story else 1.12, text=TXT)}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
</style></head><body>
<svg class="grain" width="100%" height="100%"><filter id="g"><feTurbulence baseFrequency="0.9" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
<div class="tag"><span>GARMIN <b>CIRQA</b></span><span>FABRIC 1.0 · 2.0</span></div>
<div class="hd"><h1>نفس الراحة.. <em>بنسختين.</em></h1><p>سيور قماش لـ <bdi dir="ltr">Garmin CIRQA</bdi> · خفيفة وتتنفس</p></div>
<div class="cols">{col(V1,'1.0','ناعم وخفيف','للمعصم أو الذراع · 7 ألوان',story)}{col(V2,'2.0','حواف بلون مختلف','لمسة رياضية · 5 ألوان',story)}</div>
<div class="foot"><div class="cta">علّق <em>«قارمن»</em> ونرسل لك الرابط 📩</div><div class="price"><b>109</b>ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''
for s in (0,1): open(f'p_{s}.html','w').write(page(bool(s)))
subprocess.run(['node','-e',"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const s of [0,1]){const p=await b.newPage({viewport:{width:1080,height:s?1920:1350}});await p.goto('file://'+process.cwd()+'/p_'+s+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.screenshot({path:'out/974-cirqa-fabric-'+(s?'story':'post')+'.png'});}
await b.close();})()"""],check=True)
for s in (0,1): os.remove(f'p_{s}.html')
