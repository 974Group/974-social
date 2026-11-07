# Design B: big staggered "wall" so each band reads large
import subprocess,re
src=open('gen.py').read()
exec(src.split('def page(story):')[0])          # shared constants, RING, NEW, fonts
def page(story):
    W,H=1080,(1920 if story else 1350)
    if story: top,bot,bh,sp=470,1570,212,204
    else:     top,bot,bh,sp=264,1122,180,202
    rows=[5,4,5,4,5]; pitch=(bot-top-bh)/4; items='';k=0
    for r,n in enumerate(rows):
        y=top+bh/2+r*pitch
        for c in range(n):
            x=540+(c-(n-1)/2)*sp; nm=RING[k]; k+=1
            badge=f'<span class="nw">NEW</span>' if nm in NEW else ''
            items+=f'<div class="b" style="left:{x:.0f}px;top:{y:.0f}px;height:{bh}px"><img src="file://{C}{nm}.png">{badge}</div>'
    pf=240 if story else 140; fb=124 if story else 38; t=200 if story else 48; ht=t+(100 if story else 82)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:linear-gradient(180deg,#F4F1F2 0%,#E9E4E1 100%);color:{INK};font-family:Cairo;position:relative;overflow:hidden}}
.abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}}
.b{{position:absolute;transform:translate(-50%,-50%)}} .b img{{height:100%;display:block}}
.nw{{position:absolute;right:-6px;top:-4px;background:#720842;color:#fff;font-family:Poppins;font-weight:700;font-size:{15 if story else 13}px;letter-spacing:1px;border-radius:20px;padding:3px 9px 2px}}
.hd{{position:absolute;left:48px;right:48px;top:{ht}px;display:flex;align-items:center;justify-content:space-between}}
.hd b{{font-family:Poppins;font-weight:700;font-size:{150 if story else 120}px;line-height:.8;letter-spacing:-5px;color:#720842}}
.hd div{{text-align:right;direction:rtl}} .hd i{{display:block;font-style:normal;font-weight:900;font-size:{50 if story else 44}px;line-height:1.15}}
.hd em{{display:block;font-style:normal;font-family:Poppins;font-weight:500;font-size:{19 if story else 17}px;letter-spacing:4px;opacity:.6;direction:ltr;margin-top:6px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
{payfoot.css(1.0 if not story else 1.12)}
.foot{{position:absolute;left:48px;right:48px;bottom:{fb}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:{INK};color:#fff;border-radius:40px;padding:2px 30px 8px;font-weight:900;font-size:36px;white-space:nowrap}} .price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;color:#720842}}
</style></head><body>
<img class="abs" src="file://{LOGO}" style="left:48px;top:{t}px;height:44px">
<div class="abs en" style="right:48px;top:{t+8}px;font-weight:700;font-size:17px;letter-spacing:4px">WHOOP 5.0 · MG</div>
<div class="hd"><b>23</b><div><i>لون سيليكون.. اختار لونك</i><em>SILICONE BANDS</em></div></div>
{items}
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«سيليكون»</em> ونرسل لك الرابط 📩</div><div class="price"><b>99</b> ر.ق</div></div>
</body></html>'''
for n,st,H in (('974-w5-silicone-wall-post',False,1350),('974-w5-silicone-wall-story',True,1920)):
    open(n+'.html','w').write(page(st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
