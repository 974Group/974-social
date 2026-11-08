import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
P='/home/claude/974-social/products/fitbit-air-magnetic/'
WINE='#8E1E2A'; DEEP='#3A0B12'; BG='#F3EEEC'; INK='#1E1214'
OTHERS=[('black','Black'),('dark-blue','Dark Blue'),('green','Green'),('dark-gray','Dark Gray'),('light-gray','Light Gray'),('starlight','Starlight'),('white','White')]
def page(story):
    W,H=(1080,1920) if story else (1080,1350)
    if story:
        tag_t,hd_t,hd_w,h1,sub=230,290,960,84,30
        hero_t,hero_h,hero_l=600,700,30
        name_t=860; row_t=1320; sw=100; pf=300; slab_h=1290; slab_t=610
    else:
        tag_t,hd_t,hd_w,h1,sub=44,100,450,62,26
        hero_t,hero_h,hero_l=150,690,24
        name_t=520; row_t=890; sw=96; pf=40; slab_h=840; slab_t=0
    chips=''.join(f'<div class="sw"><img src="file://{P}{k}-cut.png"><span>{n}</span></div>' for k,n in OTHERS)
    cta='' if story else '<div class="foot"><div class="cta">علّق <em>«فت بت»</em> ونرسل لك الرابط على الخاص 📩</div></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;background:{BG};color:{INK}}}
.slab{{position:absolute;left:0;top:{slab_t}px;width:44%;height:{slab_h-slab_t}px;background:linear-gradient(165deg,{WINE},{DEEP})}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply;pointer-events:none}}
.tag{{position:absolute;top:{tag_t}px;right:56px;font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:6px;color:{WINE}}}
.tagl{{position:absolute;top:{tag_t}px;left:56px;font-family:Poppins;font-weight:700;font-size:20px;letter-spacing:6px;color:#F3D9DC}}
.hd{{position:absolute;top:{hd_t}px;right:56px;width:{hd_w}px;text-align:right;direction:rtl}}
.hd h1{{font-weight:900;font-size:{h1}px;line-height:1.1;color:{INK}}}
.hd h1 em{{font-style:normal;color:{WINE}}}
.hd p{{margin-top:12px;font-weight:600;font-size:{sub}px;color:#5B4446;line-height:1.45}}
.hd p bdi{{font-family:Poppins;font-weight:700}}
.hero{{position:absolute;top:{hero_t}px;left:{hero_l}px;height:{hero_h}px;transform:rotate(-7deg);filter:drop-shadow(0 40px 50px rgba(58,11,18,.35))}}
.hero img{{height:100%}}
.name{{position:absolute;top:{name_t}px;right:56px;text-align:right;direction:rtl}}
.name > b{{display:block;font-family:Poppins;font-weight:700;font-size:{62 if story else 50}px;color:{WINE};letter-spacing:-1px;direction:ltr;line-height:1.1}}
.name span{{display:block;font-weight:700;font-size:{28 if story else 23}px;color:#5B4446;margin-top:4px}}
.price{{display:inline-flex;margin-top:18px;background:{WINE};color:#fff;border-radius:999px;padding:4px 28px 8px;font-weight:800;font-size:{30 if story else 26}px;align-items:baseline;gap:8px;direction:rtl}}
.price b{{font-family:Poppins;font-weight:700;font-size:{50 if story else 42}px}}
.swr{{position:absolute;top:{row_t}px;left:44px;right:44px;display:flex;justify-content:space-between;align-items:flex-end;direction:ltr}}
.lbl{{position:absolute;top:{row_t-44}px;right:56px;font-weight:800;font-size:{28 if story else 23}px;direction:rtl;color:{INK}}}
.sw{{display:flex;flex-direction:column;align-items:center;gap:6px;width:{sw+18}px}}
.sw img{{height:{int(sw*1.29)}px;filter:drop-shadow(0 8px 10px rgba(0,0,0,.16))}}
.sw span{{font-family:Poppins;font-weight:500;font-size:{17 if story else 15}px;color:#5B4446;white-space:nowrap}}
.foot{{position:absolute;left:56px;right:56px;top:{row_t+int(sw*1.29)+52}px;text-align:center;direction:rtl}}
.cta{{font-weight:800;font-size:28px;color:{INK}}} .cta em{{font-style:normal;color:{WINE}}}
{payfoot.css(1.0 if not story else 1.12)}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
</style></head><body>
<div class="slab"></div>
<svg class="grain" width="100%" height="100%"><filter id="g"><feTurbulence baseFrequency="0.85" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
<div class="tagl" style="color:{'#8E1E2A' if story else '#F3D9DC'}">FITBIT AIR</div><div class="tag">MAGNETIC</div>
<div class="hd"><h1>بدون قفل..<br><em>يتسكّر بالمغناطيس.</em></h1><p>سير <bdi dir="ltr">Fitbit Air</bdi> منسوج مطاطي خفيف، يتضبط على أي معصم بثانية</p></div>
<div class="hero"><img src="file://{P}wine-red-cut.png"></div>
<div class="name"><b>Wine Red</b><span>العنابي.. الأقرب لقلبنا</span><div class="price"><b>89</b>ر.ق</div></div>
<div class="lbl">و 7 ألوان ثانية</div>
<div class="swr">{chips}</div>
{cta}
<div class="pf">{payfoot.html()}</div>
</body></html>'''
for s in (0,1): open(f'p_{s}.html','w').write(page(bool(s)))
subprocess.run(['node','-e',"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const s of [0,1]){const p=await b.newPage({viewport:{width:1080,height:s?1920:1350}});await p.goto('file://'+process.cwd()+'/p_'+s+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.screenshot({path:'out/974-fitbit-magnetic-v2-'+(s?'story':'post')+'.png'});}
await b.close();})()"""],check=True)
for s in (0,1): os.remove(f'p_{s}.html')
