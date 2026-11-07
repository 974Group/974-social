# Qatar Edition — option B: flag layout (white hoist band with 9 points on the front), ghost skyline, inverted white back
import subprocess
from build import S,M,M2,M3,W,BC,skyline,dunes,AR_T,AR_P,EN_P
def hoist(w,h,n=9,fill=W,side='left',depth=70):
    step=h/n
    if side=='left':
        pts=['0,0',f'{w-depth},0']
        for i in range(n): y0=i*step; pts+= [f'{w},{y0+step/2:.1f}',f'{w-depth},{y0+step:.1f}']
        pts+= ['0,'+str(h)]
    else:
        pts=[f'{w},0',f'{depth},0']
        for i in range(n): y0=i*step; pts+= [f'0,{y0+step/2:.1f}',f'{depth},{y0+step:.1f}']
        pts+= [f'{w},{h}']
    return f'<svg width="{w}" height="{h}" style="position:absolute;top:0;{side}:0"><polygon points="{" ".join(pts)}" fill="{fill}"/></svg>'
def ghost(col,op,sc=1.0,dcol=None):
    sk=skyline().replace('fill="#4A0819" opacity=".9"',f'fill="{col}" opacity="{op}"')
    d=dunes()
    if dcol: d=d.replace('#A3264E',dcol[0]).replace('#7E1233',dcol[1]).replace(M2,dcol[2]).replace(M3,dcol[3])
    return f'<div class="abs" style="left:0;right:0;bottom:0;height:1250px"><div class="abs" style="left:0;right:0;bottom:330px;height:760px;transform:scale({sc});transform-origin:50% 100%">{sk}</div><div class="abs" style="left:0;right:0;bottom:0;height:520px">{d}</div></div>'
HW=200
html=f'''<!doctype html><html lang="ar"><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500 600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700 900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
body{{margin:0;background:#555;font-family:'Cairo'}}
.die{{position:relative;width:3530px;height:4072px;overflow:hidden;background:#fff}}
.p{{position:absolute;overflow:hidden;box-sizing:border-box;background:{M};color:#fff}}
.glueL{{left:280px;width:273px;top:733px;height:2465px;background:#fff}} .front{{left:553px;width:791px;top:733px;height:2465px;background:radial-gradient(120% 60% at 70% 35%,#9E1C45 0%,{M} 55%,{M2} 100%)}}
.side{{left:1344px;width:243px;top:733px;height:2465px}}
.back{{left:1587px;width:791px;top:733px;height:2465px;background:#fff;color:{M}}} .glueR{{left:2378px;width:224px;top:733px;height:2465px;background:#fff}}
.lidF{{left:553px;width:791px;top:327px;height:406px}} .lidB{{left:1587px;width:791px;top:209px;height:524px;background:#fff}}
.tabS1{{left:1344px;width:243px;top:512px;height:221px}} .tabS2{{left:1344px;width:243px;top:3198px;height:221px}}
.botF{{left:553px;width:791px;top:3198px;height:455px;background:{M2}}} .botB{{left:1587px;width:791px;top:3198px;height:227px;background:{M2}}}
.en{{font-family:'Poppins';direction:ltr}} .ar{{direction:rtl}} .abs{{position:absolute}}
.circ{{display:inline-block;width:34px;height:34px;border-radius:50%;vertical-align:middle;margin-left:8px;background:currentColor}}
.vert{{writing-mode:vertical-rl}}
</style>
<div class="die" id="W8">
 <div class="p lidF"><img class="abs" src="../../pkg/logo-white.png" style="left:50%;top:150px;width:200px;transform:translateX(-50%)"></div>
 <div class="p lidB"></div><div class="p tabS1"></div><div class="p tabS2"></div><div class="p botF"></div><div class="p botB"></div><div class="p glueL"></div><div class="p glueR"></div>
 <div class="p front">
  {ghost('#FFFFFF','.13',1.15,('#B0305A','#8E1A40',M2,M3))}
  <div class="abs ar" style="right:50px;top:250px;font-weight:900;font-size:300px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.18)">قطر</div>
  {hoist(HW,2465)}
  <img class="abs" src="../../pkg/logo-maroon.png" style="left:18px;top:70px;width:96px">
  <div class="abs en vert" style="left:58px;top:330px;font-weight:700;font-size:26px;letter-spacing:10px;color:{M};white-space:nowrap">QATAR EDITION · 974</div>
  <div class="abs en vert" style="left:58px;bottom:120px;font-weight:700;font-size:22px;letter-spacing:6px;color:{M};white-space:nowrap">974GROUP.NET</div>
  <div class="abs ar" style="left:{HW+50}px;right:60px;top:90px;font-size:40px;font-weight:900;white-space:nowrap">سير سيليكون لساعة Whoop</div>
  <div class="abs ar" style="left:{HW+50}px;right:60px;top:150px;font-size:26px;font-weight:600;color:rgba(255,255,255,.75)">ناعم · مقاوم للماء والعرق · يناسب 5.0 و MG</div>
  <img class="abs" src="../img/p49-50.png" style="left:{HW-20}px;top:560px;width:640px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
  <img class="abs" src="../img/p49-0.png" style="left:{HW-60}px;top:1160px;width:640px;transform:rotate(12deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
  <div class="abs en" style="right:60px;top:600px;font-weight:700;font-size:22px;letter-spacing:4px;color:rgba(255,255,255,.75)">5.0</div>
  <div class="abs en" style="right:60px;top:1200px;font-weight:700;font-size:22px;letter-spacing:4px;color:rgba(255,255,255,.75)">MG</div>
  <div class="abs ar" style="right:60px;bottom:200px;text-align:right;line-height:1"><div style="font-size:96px;font-weight:900">عنابي</div><div class="en" style="font-weight:700;font-size:24px;letter-spacing:8px;margin-top:40px">QATAR MAROON</div></div>
  <div class="abs en" style="right:60px;bottom:90px;font-weight:700;font-size:28px;line-height:1;display:flex;gap:30px;align-items:center;color:#fff"><span>5.0 <span class="circ"></span></span><span>MG <span class="circ"></span></span></div>
 </div>
 <div class="p side">
  <img class="abs" src="../../pkg/logo-white.png" style="left:50%;top:80px;width:150px;transform:translateX(-50%)">
  <div class="abs en vert" style="left:50%;top:50%;transform:translate(-50%,-50%) rotate(180deg);font-weight:700;font-size:44px;letter-spacing:6px;white-space:nowrap">QATAR EDITION · MAROON SILICONE</div>
 </div>
 <div class="p back">
  {ghost(M,'.16',0.8,('#F1E3E8','#E6CFD7','#F4EBEE','#EDDDE3'))}
  {hoist(HW-60,2465,fill=M,side='right',depth=60)}
  <img class="abs" src="../../pkg/logo-maroon.png" style="left:70px;top:80px;width:170px">
  <div class="abs en" style="left:70px;top:190px;font-weight:700;font-size:24px;letter-spacing:6px">QATAR EDITION</div>
  <div class="abs ar" style="left:70px;right:{HW}px;top:330px;font-size:54px;font-weight:900;line-height:1.2">{AR_T}</div>
  <div class="abs ar" style="left:70px;right:{HW}px;top:430px;font-size:29px;font-weight:600;line-height:1.75;color:#3A1424">{AR_P}</div>
  <div class="abs en" style="left:70px;right:{HW}px;top:960px;font-size:21px;font-weight:500;line-height:1.6;color:#6B4A57">{EN_P}</div>
  <div class="abs" style="left:70px;top:1330px;width:250px;background:#fff;border:2px solid {M};border-radius:14px;padding:12px 14px 8px"><img src="../bcw/{BC}.png" style="display:block;width:100%;height:80px"><div class="en" style="text-align:center;font-weight:600;font-size:18px;letter-spacing:4px;color:#111;margin-top:4px">{BC}</div></div>
  <div class="abs" style="left:350px;top:1330px;width:220px;background:#fff;border:2px solid {M};border-radius:16px;padding:8px"><img src="../../pkg/qr.png" style="display:block;width:100%"></div>
  <div class="abs en" style="left:70px;top:1470px;font-weight:700;font-size:22px;line-height:1.7">974GROUP.NET<br>+974 5555 6278<br>@974.Group</div>
  <div class="abs ar" style="left:350px;top:1580px;font-size:22px;font-weight:700">امسح وتسوّق مباشرة</div>
  <img class="abs" src="../../pkg/icons-dark.png" style="left:70px;top:1600px;height:28px">
  <div class="abs en" style="left:0;right:{HW-60}px;bottom:30px;text-align:center;font-size:13px;letter-spacing:3px;color:{M}">MADE IN CHINA · DESIGNED IN QATAR</div>
 </div>
</div></html>'''
open(S+'/pages/wqb49.html','w').write(html)
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:3600,height:4200}});await pg.goto('file://"+S+"/pages/wqb49.html');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(400);await pg.locator('#W8').screenshot({path:'"+S+"/pages/dieqb49.png'});await b.close();})()"
subprocess.run(['node','-e',js],check=True)
print('ok')
