import subprocess,os
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'; D=os.path.abspath('designy')+'/'
LB='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
F=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .en{{font-family:Poppins;direction:ltr}}'''
SH=[('navy-back','Summer Breeze · Navy'),('blue-back','Summer Breeze · Sky Blue'),('white-back','Falling With Grace'),('beige-back','Citraz Vibes')]
INK='#1D1B1A'; BLUE='#2560a4'
def desktop():
    cells=''.join(f'<div class="c"><img src="file://{C}{n}.png"><span class="en">{t}</span></div>' for n,t in SH)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{F}
body{{width:2400px;height:1000px;background:linear-gradient(180deg,#EEF4F3 0%,#E4ECEA 100%);color:{INK};font-family:Cairo;position:relative;overflow:hidden}}
.hd{{position:absolute;left:0;right:0;top:70px;display:flex;align-items:center;justify-content:center;gap:56px}}
.hd .t{{font-family:Poppins;font-weight:700;font-size:150px;line-height:.9;letter-spacing:-5px}}
.hd .lg{{height:130px}}
.hd i{{width:2px;height:120px;background:rgba(0,0,0,.18)}}
.sub{{position:absolute;left:0;right:0;top:250px;text-align:center;direction:rtl;font-weight:700;font-size:38px}}
.sub b{{font-family:Poppins;font-weight:700}} .sub bdi{{font-weight:700}} .sub em{{font-style:normal;opacity:.55;margin:0 18px}}
.row{{position:absolute;left:110px;right:110px;top:345px;height:600px;display:grid;grid-template-columns:repeat(4,1fr);gap:40px}}
.c{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-height:0}}
.c img{{flex:0 1 auto;min-height:0;max-width:100%;max-height:100%;object-fit:contain}}
.c span{{margin-top:14px;font-weight:500;font-size:22px;letter-spacing:1px;opacity:.7}}
</style></head><body>
<div class="hd"><img class="lg" src="file://{D}designy-logo-blue-hd.png"><i></i><div class="t en">T-SHIRTS</div></div>
<div class="sub">تيشيرتات <bdi class="en">Designy Studios × 974</bdi><em>·</em><bdi class="en">S · M · L · XL</bdi><em>·</em><b>139</b> ر.ق</div>
<div class="row">{cells}</div></body></html>'''
def mobile():
    cells=''.join(f'<div class="c"><img src="file://{C}{n}.png"><span class="en">{t}</span></div>' for n,t in SH)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{F}
body{{width:1080px;height:1350px;background:linear-gradient(180deg,#EEF4F3 0%,#E4ECEA 100%);color:{INK};font-family:Cairo;position:relative;overflow:hidden}}
.lg{{position:absolute;left:50%;transform:translateX(-50%);top:62px;height:110px}}
.t{{position:absolute;left:0;right:0;top:190px;text-align:center;font-weight:700;font-size:130px;line-height:.9;letter-spacing:-4px}}
.sub{{position:absolute;left:0;right:0;top:330px;text-align:center;direction:rtl;font-weight:700;font-size:34px}}
.sub b{{font-family:Poppins}} .sz{{position:absolute;left:0;right:0;top:390px;text-align:center;font-weight:500;font-size:24px;letter-spacing:3px;opacity:.7}}
.row{{position:absolute;left:50px;right:50px;top:470px;bottom:50px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:28px 30px}}
.c{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-height:0}}
.c img{{flex:0 1 auto;min-height:0;max-width:100%;max-height:100%;object-fit:contain}}
.c span{{margin-top:8px;font-weight:500;font-size:17px;letter-spacing:1px;opacity:.7}}
</style></head><body>
<img class="lg" src="file://{D}designy-logo-blue-hd.png"><div class="t en">T-SHIRTS</div>
<div class="sub">تيشيرتات <bdi class="en">Designy Studios × 974</bdi> · <b>139</b> ر.ق</div>
<div class="sz en">S · M · L · XL</div>
<div class="row">{cells}</div></body></html>'''
def designy():  # Designy collection image
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{F}
body{{width:2400px;height:1000px;background:#edf7f6;font-family:Cairo;position:relative;overflow:hidden;color:{BLUE}}}
.lg{{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:1000px}}
.x{{position:absolute;left:0;right:0;top:760px;text-align:center;font-weight:700;font-size:40px;letter-spacing:10px;color:#434053}}
</style></head><body><img class="lg" src="file://{D}designy-logo-blue-hd.png"><div class="x en">DESIGNY STUDIOS × 974</div></body></html>'''
def shot(n,html,W,H):
    os.makedirs('out',exist_ok=True); open(f'out/{n}.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await pg.goto('file://'+process.cwd()+'/out/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'out/{n}.jpg',type:'jpeg',quality:92}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
shot('974-tshirts-banner-desktop',desktop(),2400,1000)
shot('974-tshirts-banner-mobile',mobile(),1080,1350)
shot('designy-collection',designy(),2400,1000)

def hero(W,H,mobile=False):
    tees=SH if not mobile else SH[:3]
    cells=''.join(f'<img src="file://{C}{n}.png">' for n,t in tees)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{F}
body{{width:{W}px;height:{H}px;background:linear-gradient(135deg,#F2F6F5 0%,#E2EAE8 100%);color:{INK};font-family:Cairo;position:relative;overflow:hidden}}
.l{{position:absolute;left:{70 if mobile else 110}px;top:50%;transform:translateY(-50%);width:{430 if mobile else 760}px}}
.lg{{height:{74 if mobile else 96}px;display:block}}
.t{{font-family:Poppins;font-weight:700;font-size:{96 if mobile else 128}px;line-height:.95;letter-spacing:-4px;margin-top:{14 if mobile else 18}px}}
.s{{direction:rtl;text-align:left;font-weight:700;font-size:{26 if mobile else 32}px;margin-top:{12 if mobile else 16}px}} .s b{{font-family:Poppins}}
.sz{{font-family:Poppins;font-weight:700;font-size:{17 if mobile else 20}px;letter-spacing:4px;opacity:.6;margin-top:8px}}
.r{{position:absolute;left:{520 if mobile else 900}px;right:{30 if mobile else 60}px;top:{40 if mobile else 50}px;bottom:{40 if mobile else 50}px;display:flex;align-items:flex-end;justify-content:space-between;gap:{10 if mobile else 20}px}}
.r img{{height:100%;max-width:{210 if mobile else 340}px;object-fit:contain}}
</style></head><body>
<div class="l"><img class="lg" src="file://{D}designy-logo-blue-hd.png"><div class="t">T-SHIRTS</div><div class="s">تيشيرتات <bdi class="en">Designy Studios × 974</bdi>{'<br>' if mobile else ' · '}<b>139</b> ر.ق</div><div class="sz">S · M · L · XL</div></div>
<div class="r">{cells}</div></body></html>'''
shot('designy-tshirts-desktop',hero(2400,630),2400,630)
shot('designy-tshirts-mobile',hero(1200,630,True),1200,630)
# square tile for the category chooser
def tile():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{F}
body{{width:800px;height:800px;background:linear-gradient(135deg,#F2F6F5 0%,#E2EAE8 100%);position:relative;overflow:hidden}}
img{{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);height:700px}}
</style></head><body><img src="file://{C}white-back.png"></body></html>'''
shot('designy-tshirts-tile',tile(),800,800)
