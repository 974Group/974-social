import subprocess,sys,os,math
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
# colour-wheel order (21 in stock)
RING=['black','black-ed','darkgrey','greyblack','whitegrey','creamy','creamyblue','splash','babyblue','iceblue','turquoise',
      'blue','navyyellow','drenched','greenarmy','yellownavy','yellow','orange','scarlet','red','pink']
NEW={'yellow','pink','babyblue','iceblue'}
BG='#ECE8E3'; INK='#1E1C1B'
def page(story):
    W,H=1080,(1920 if story else 1350)
    cx=540; cy=(960 if story else 640); R=(420 if story else 392); bh=(142 if story else 126)
    items='';badges=''
    for i,n in enumerate(RING):
        a=-math.pi/2+2*math.pi*i/len(RING)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        items+=f'<div class="b" style="left:{x:.0f}px;top:{y:.0f}px;height:{bh}px"><img src="file://{C}{n}.png"></div>'
        if n in NEW: badges+=f'<div class="b" style="left:{x:.0f}px;top:{y:.0f}px;height:{bh}px;width:{bh*0.83:.0f}px;z-index:5"><span class="nw">NEW</span></div>'
    pf=240 if story else 140; fb=124 if story else 38; t=200 if story else 48
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:radial-gradient(60% 45% at 50% {cy/H*100:.0f}%,#F7F5F2 0%,{BG} 100%);color:{INK};font-family:Cairo;position:relative;overflow:hidden}}
.abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}}
.b{{position:absolute;transform:translate(-50%,-50%)}} .b img{{height:100%;display:block}}
.nw{{position:absolute;right:-10px;top:-6px;background:#720842;color:#fff;font-family:Poppins;font-weight:700;font-size:12px;letter-spacing:1px;border-radius:20px;padding:3px 8px 2px}}
.mid{{position:absolute;left:{cx}px;top:{cy}px;transform:translate(-50%,-50%);text-align:center}}
.mid b{{display:block;font-family:Poppins;font-weight:700;font-size:{200 if story else 180}px;line-height:.85;letter-spacing:-6px}}
.mid i{{display:block;font-style:normal;font-weight:900;font-size:{50 if story else 44}px;line-height:1.1;margin-top:6px}}
.mid em{{display:block;font-style:normal;font-family:Poppins;font-weight:500;font-size:{20 if story else 18}px;letter-spacing:4px;opacity:.6;margin-top:12px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf}px}}
{payfoot.css(1.0 if not story else 1.12)}
.foot{{position:absolute;left:48px;right:48px;bottom:{fb}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:{INK};color:#fff;border-radius:40px;padding:2px 30px 8px;font-weight:900;font-size:36px;white-space:nowrap}} .price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;color:#720842}}
</style></head><body>
<img class="abs" src="file://{LOGO}" style="left:48px;top:{t}px;height:44px">
<div class="abs en" style="right:48px;top:{t+8}px;font-weight:700;font-size:17px;letter-spacing:4px">WHOOP 5.0 · MG</div>
{items}{badges}
<div class="mid"><b>21</b><i>لون سيليكون<br>اختار لونك</i><em>SILICONE BANDS</em></div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«سيليكون»</em> ونرسل لك الرابط 📩</div><div class="price"><b>99</b> ر.ق</div></div>
</body></html>'''
for n,st,H in (('974-w5-silicone-all-post',False,1350),('974-w5-silicone-all-story',True,1920)):
    open(n+'.html','w').write(page(st))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
