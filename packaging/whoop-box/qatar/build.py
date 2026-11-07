# Qatar Edition box for Whoop silicone (maroon / Burgundy p49), same manufacturer die as final/tpl.html
import os,subprocess
S='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad/wpkg'
M='#420303'; M2='#360202'; M3='#2A0101'; W='#FFFFFF'
BC='97430007'
def serr(w,h,n=9,fill=W,down=True):
    # white band with n triangular points along the bottom edge (Qatar flag serration)
    step=w/n; pts=[f'0,0',f'{w},0']
    for i in range(n,0,-1):
        x1=i*step; xm=x1-step/2; x0=x1-step
        pts+= [f'{x1:.1f},{h-60}',f'{xm:.1f},{h}',f'{x0:.1f},{h-60}'] if down else []
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0;display:block"><polygon points="{" ".join(pts)}" fill="{fill}"/></svg>'
def skyline(w=791,h=760):
    sky="#5A0707"
    p=[]
    # generic towers
    for x,tw,th in [(18,46,250),(70,34,330),(250,40,300),(470,44,270),(520,30,380),(690,52,240),(745,40,330)]:
        p.append(f'<rect x="{x}" y="{h-th}" width="{tw}" height="{th}"/>')
    # Katara twin crescent towers (Lusail)
    p.append(f'<path d="M110 {h} C110 {h-260} 150 {h-420} 205 {h-480} C175 {h-380} 160 {h-250} 162 {h} Z"/>')
    p.append(f'<path d="M232 {h} C232 {h-250} 222 {h-380} 205 {h-480} C262 {h-420} 290 {h-260} 284 {h} Z" />')
    # Doha Tower (Burj Doha): cylinder, domed top, spire
    p.append(f'<path d="M318 {h} V{h-470} C318 {h-540} 386 {h-540} 386 {h-470} V{h} Z"/><rect x="349" y="{h-610}" width="6" height="90"/>')
    # Tornado Tower: hyperboloid
    p.append(f'<path d="M400 {h} C424 {h-180} 424 {h-260} 402 {h-430} H460 C438 {h-260} 438 {h-180} 462 {h} Z"/>')
    # Aspire Torch
    p.append(f'<path d="M585 {h} L596 {h-470} C578 {h-500} 580 {h-560} 600 {h-600} C620 {h-640} 640 {h-560} 618 {h-470} L630 {h} Z"/><rect x="606" y="{h-700}" width="4" height="110"/>')
    # Museum of Islamic Art (stepped)
    p.append(f'<path d="M640 {h} V{h-120} H655 V{h-170} H668 V{h-215} H690 V{h-170} H703 V{h-120} H718 V{h} Z"/>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;bottom:0"><g fill="{sky}" opacity=".9">{"".join(p)}</g></svg>'
def dunes(w=791,h=520):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;bottom:0" preserveAspectRatio="none">
<defs><linearGradient id="d1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6E0B0B"/><stop offset="1" stop-color="{M2}"/></linearGradient>
<linearGradient id="d2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#560606"/><stop offset="1" stop-color="{M3}"/></linearGradient></defs>
<path d="M0 140 C140 60 260 70 380 150 C470 210 600 120 791 90 V{h} H0 Z" fill="url(#d1)"/>
<path d="M0 300 C120 220 300 200 430 280 C540 350 660 260 791 240 V{h} H0 Z" fill="url(#d2)"/>
<path d="M380 150 C470 210 600 120 791 90" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="3"/>
<path d="M0 300 C120 220 300 200 430 280" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="3"/></svg>'''
def scene(sc=1.15,col=None): return f'<div class="abs" style="left:0;right:0;bottom:0;height:1250px"><div class="abs" style="left:0;right:0;bottom:330px;height:760px;transform:scale({sc});transform-origin:50% 100%">{skyline() if not col else skyline().replace("#5A0707",col)}</div><div class="abs" style="left:0;right:0;bottom:0;height:520px">{dunes()}</div></div>'

AR_T='قطر.. من هنا بدأنا'
AR_P='توحّدت قطر على يد المؤسس الشيخ جاسم بن محمد آل ثاني، ونحتفل بذكراه كل سنة في اليوم الوطني ١٨ ديسمبر. ونالت استقلالها في ٣ سبتمبر ١٩٧١. واليوم قطر من أكبر ٣ دول في العالم بمخزون الغاز الطبيعي، وأول دولة عربية تستضيف كأس العالم لكرة القدم في ٢٠٢٢. وهذا السير بلون العنابي.. لون علمنا.'
EN_P='Qatar was unified by its founder, Sheikh Jassim bin Mohammed Al Thani, honoured every 18 December on National Day, and became independent on 3 September 1971. Today it holds the world\'s third-largest natural gas reserves and was the first Arab country to host the FIFA World Cup, in 2022. This band wears maroon, the colour of our flag.'

html=f'''<!doctype html><html lang="ar"><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500 600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700 900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
body{{margin:0;background:#555;font-family:'Cairo'}}
.die{{position:relative;width:3530px;height:4072px;overflow:hidden;background:#fff}}
.p{{position:absolute;overflow:hidden;box-sizing:border-box;background:linear-gradient(180deg,{M} 0%,{M2} 100%);color:#fff}}
.glueL{{left:280px;width:273px;top:733px;height:2465px}} .front{{left:553px;width:791px;top:733px;height:2465px;background:linear-gradient(180deg,#4C0505 0%,#420303 55%,#350202 100%)!important}}
.side{{left:1344px;width:243px;top:733px;height:2465px;background:#fff!important;color:{M}}}
.back{{left:1587px;width:791px;top:733px;height:2465px}} .glueR{{left:2378px;width:224px;top:733px;height:2465px}}
.lidF{{left:553px;width:791px;top:327px;height:406px;background:#fff!important}} .lidB{{left:1587px;width:791px;top:209px;height:524px}}
.tabS1{{left:1344px;width:243px;top:512px;height:221px}} .tabS2{{left:1344px;width:243px;top:3198px;height:221px}}
.botF{{left:553px;width:791px;top:3198px;height:455px;background:{M3}!important}} .botB{{left:1587px;width:791px;top:3198px;height:227px;background:{M3}!important}}
.en{{font-family:'Poppins';direction:ltr}} .ar{{direction:rtl}} .abs{{position:absolute}}
.circ{{display:inline-block;width:34px;height:34px;border-radius:50%;vertical-align:middle;margin-left:8px;background:#fff}}
.vert{{writing-mode:vertical-rl}}
.rule{{position:absolute;height:3px;background:rgba(255,255,255,.55)}}
</style>
<div class="die" id="W8">
 <div class="p lidF"><img class="abs" src="../../pkg/logo-maroon.png" style="left:50%;top:150px;width:200px;transform:translateX(-50%)"></div>
 <div class="p lidB"></div><div class="p tabS1"></div><div class="p tabS2"></div><div class="p botF"></div><div class="p botB"></div><div class="p glueL"></div><div class="p glueR"></div>
 <div class="p front">
  <div class="abs" style="left:0;top:0;width:791px;height:400px">{serr(791,400)}</div>
  <img class="abs" src="../../pkg/logo-maroon.png" style="left:70px;top:80px;width:220px">
  <div class="abs en" style="right:70px;top:96px;text-align:right;font-weight:700;letter-spacing:6px;font-size:22px;color:{M};line-height:1.6">QATAR<br>EDITION</div>
  <div class="abs ar" style="left:70px;right:70px;top:230px;font-size:46px;font-weight:900;color:{M};white-space:nowrap">سير سيليكون لساعة Whoop</div>
  {scene(1.15,'#5C0808')}
  <img class="abs" src="../img/p49m-50.png" style="left:10px;top:470px;width:780px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
  <img class="abs" src="../img/p49m-0.png" style="left:-130px;top:1160px;width:780px;transform:rotate(14deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
  <div class="abs en" style="right:70px;top:520px;font-weight:700;font-size:22px;letter-spacing:4px;color:rgba(255,255,255,.7)">5.0</div>
  <div class="abs en" style="right:70px;top:1200px;font-weight:700;font-size:22px;letter-spacing:4px;color:rgba(255,255,255,.7)">MG</div>
  <div class="abs ar" style="right:70px;bottom:250px;font-size:84px;font-weight:900;line-height:1">عنابي</div>
  <div class="abs en" style="left:70px;bottom:262px;font-weight:700;font-size:40px;line-height:1">Maroon</div>
  <div class="abs en" style="left:70px;bottom:200px;font-weight:600;font-size:20px;letter-spacing:5px;color:rgba(255,255,255,.8)">SILICONE · QATAR EDITION</div>
  <div class="rule" style="left:70px;right:70px;bottom:150px"></div>
  <div class="abs en" style="left:70px;bottom:86px;font-weight:700;font-size:20px;letter-spacing:4px">974GROUP.NET</div>
  <div class="abs en" style="right:70px;bottom:78px;font-weight:700;font-size:30px;line-height:1;display:flex;gap:34px;align-items:center"><span>5.0 <span class="circ"></span></span><span>MG <span class="circ"></span></span></div>
 </div>
 <div class="p side">
  <img class="abs" src="../../pkg/logo-maroon.png" style="left:50%;top:80px;width:150px;transform:translateX(-50%)">
  <div class="abs en vert" style="left:50%;top:50%;transform:translate(-50%,-50%) rotate(180deg);font-weight:700;font-size:44px;letter-spacing:6px;white-space:nowrap">QATAR EDITION · MAROON SILICONE</div>
  <div class="abs" style="left:0;right:0;bottom:0;height:300px;background:{M}"></div>
 </div>
 <div class="p back">
  {scene(0.8)}
  <div class="abs" style="left:0;top:0;width:791px;height:330px">{serr(791,330)}</div>
  <img class="abs" src="../../pkg/logo-maroon.png" style="left:70px;top:80px;width:170px">
  <div class="abs en" style="left:70px;top:190px;font-weight:700;font-size:26px;letter-spacing:5px;color:{M}">QATAR EDITION</div>
  <div class="abs ar" style="left:70px;right:70px;top:420px;font-size:56px;font-weight:900;line-height:1.2">{AR_T}</div>
  <div class="abs ar" style="left:70px;right:70px;top:520px;font-size:31px;font-weight:600;line-height:1.75;color:rgba(255,255,255,.92)">{AR_P}</div>
  <div class="abs en" style="left:70px;right:70px;top:1010px;font-size:22px;font-weight:500;line-height:1.6;color:rgba(255,255,255,.75)">{EN_P}</div>
  <div class="abs" style="left:70px;top:1330px;width:250px;background:#fff;border-radius:14px;padding:12px 14px 8px"><img src="../bcw/{BC}.png" style="display:block;width:100%;height:80px"><div class="en" style="text-align:center;font-weight:600;font-size:18px;letter-spacing:4px;color:#111;margin-top:4px">{BC}</div></div>
  <div class="abs" style="left:350px;top:1330px;width:240px;background:#fff;border-radius:16px;padding:8px"><img src="../../pkg/qr.png" style="display:block;width:100%"></div>
  <div class="abs ar" style="right:70px;top:1340px;width:0"></div>
  <div class="abs en" style="left:70px;top:1470px;font-weight:700;font-size:22px;line-height:1.7">974GROUP.NET<br>+974 5555 6278<br>@974.Group</div>
  <div class="abs ar" style="left:350px;top:1600px;font-size:22px;font-weight:700;color:rgba(255,255,255,.85)">امسح وتسوّق مباشرة</div>
  <img class="abs" src="../../pkg/icons-white.png" style="left:70px;top:1600px;height:28px">
  <div class="abs en" style="left:0;right:0;bottom:30px;text-align:center;font-size:13px;letter-spacing:3px;color:rgba(255,255,255,.75)">MADE IN CHINA · DESIGNED IN QATAR</div>
 </div>
</div></html>'''
open(S+'/pages/wq49.html','w').write(html)
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:3600,height:4200}});await pg.goto('file://"+S+"/pages/wq49.html');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(400);await pg.locator('#W8').screenshot({path:'"+S+"/pages/dieq49.png'});await b.close();})()"
subprocess.run(['node','-e',js],check=True)
print('ok')
