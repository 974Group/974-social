# 4 YEARS + Burgundy Friday — animated story (8 s, 1080x1920, frame-driven R(t)).
import sys, os, asyncio, subprocess
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); OUT = D + '/out'; os.makedirs(OUT, exist_ok=True)
M, DEEP, GOLD = '#720842', '#51022D', '#C9A24B'
CSS = G.CTA_CSS + f'''
.P{{font-family:Poppins;font-weight:900}}
#bgB{{position:fixed;inset:0;background:radial-gradient(90% 60% at 50% 42%,#8A1550 0%,{M} 45%,{DEEP} 100%);clip-path:circle(var(--r,0%) at 50% 45%)}}
#cv{{position:fixed;inset:0;width:1080px;height:1920px;pointer-events:none}}
#big4{{position:absolute;left:0;top:0;transform-origin:0 0;overflow:visible}}
#big4 text{{font-family:Poppins;font-weight:900;font-size:560px}}
.chip{{display:inline-block;background:{GOLD};color:{DEEP};font-family:Cairo;font-weight:900;font-size:40px;border-radius:40px;padding:6px 34px 12px}}
#shim{{position:absolute;inset:0;background:linear-gradient(105deg,transparent 35%,rgba(255,255,255,.75) 50%,transparent 65%);mix-blend-mode:overlay;background-size:300% 100%}}
#ring{{position:fixed;left:540px;top:0;width:10px;height:10px;border:8px solid {GOLD};border-radius:50%;transform:translate(-50%,-50%)}}
'''
SCRIPT = r'''<script>
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3), seg=(t,a,b)=>ease((t-a)/(b-a)), lin=(t,a,b)=>Math.max(0,Math.min(1,(t-a)/(b-a)));
const back=t=>{t=Math.max(0,Math.min(1,t));const c=1.70158;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)};
const q=id=>document.getElementById(id);
function rnd(s){let x=Math.sin(s*12.9898)*43758.5453;return x-Math.floor(x)}
const cv=q('cv'), cx=cv.getContext('2d'); cv.width=1080; cv.height=1920;
let A=null;
function setup(){ // start & end rects for the morphing 4
  const b=q('big4'); b.style.transform='none'; const g=q('st').getBoundingClientRect(); const r1=q('f4').getBoundingClientRect();
  A={cx0:g.left+g.width/2,cy0:g.top+g.height*0.53,h0:g.height,cx1:r1.left+r1.width/2,cy1:r1.top+r1.height*0.52,s:0.6};
  const p=q('pct').getBoundingClientRect(); A.cy=p.top+p.height/2;
}
window.R=function(t){
 if(!A) setup();
 // dust + confetti
 cx.clearRect(0,0,1080,1920);
 for(let i=0;i<140;i++){const x=rnd(i)*1080, y=(rnd(i+500)*1920 - t*(30+rnd(i+900)*60))%1920, a=0.15+0.5*rnd(i+77)*(0.5+0.5*Math.sin(t*3+i));
   cx.fillStyle=`rgba(232,200,120,${a*seg(t,0,.6)})`; cx.beginPath(); cx.arc(x,(y+1920)%1920,1+rnd(i+3)*2.6,0,7); cx.fill();}
 const tb=4.75; if(t>tb){const k=t-tb; for(let i=0;i<220;i++){const ang=rnd(i+11)*6.283, sp=500+rnd(i+31)*1300;
   const x=540+Math.cos(ang)*sp*k*(1-0.35*k), y=A.cy+Math.sin(ang)*sp*k*(1-0.35*k)+520*k*k, al=Math.max(0,1-k/2.6);
   cx.save(); cx.translate(x,y); cx.rotate(k*8*rnd(i+5)+i); cx.fillStyle=(i%3==0)?`rgba(255,255,255,${al})`:(i%3==1)?`rgba(201,162,75,${al})`:`rgba(244,217,160,${al})`;
   cx.fillRect(-7,-3,14+rnd(i)*10,6); cx.restore();}}
 // big 4: draw outline, then morph into the 4 of 40%
 const d=seg(t,.25,1.5); q('st').style.strokeDashoffset=2600*(1-d); q('st').style.opacity=seg(t,.2,.4);
 q('st').style.filter=`drop-shadow(0 0 ${30*seg(t,.8,1.5)}px rgba(201,162,75,.9))`;
 const m=seg(t,2.7,3.5), sc=1+(A.s-1)*m;
 const bx=q('big4'); bx.style.transformOrigin=`${A.cx0-parseFloat(bx.style.left)}px ${A.cy0-parseFloat(bx.style.top)-230}px`;
 bx.style.transform=`translate(${(A.cx1-A.cx0)*m}px,${(A.cy1-A.cy0)*m}px) scale(${sc})`;
 q('st').style.fill=`rgba(201,162,75,${seg(t,3.2,3.5)})`; const xf=seg(t,3.5,3.7); bx.style.opacity=1-xf; q('f4').style.color=`rgba(201,162,75,${xf})`;
 // scene 1 texts
 const s1=1-seg(t,2.4,2.8);
 q('yrs').style.opacity=seg(t,1.0,1.5)*s1; q('yrs').style.transform=`translateX(${(1-seg(t,1.0,1.5))*120}px)`;
 q('cnt').textContent=2022+Math.min(4,Math.floor(5*lin(t,1.2,2.2))); q('cnt').style.opacity=seg(t,1.1,1.4)*s1;
 q('ar1').style.opacity=seg(t,1.6,2.1)*s1; q('ar1').style.transform=`translateY(${(1-seg(t,1.6,2.1))*30}px)`;
 // burgundy wipe
 document.documentElement.style.setProperty('--r',(seg(t,2.5,3.3)*140)+'%');
 // scene 2
 q('blk').style.opacity=seg(t,3.4,3.75); q('ln').style.strokeDashoffset=1000*(1-seg(t,3.7,4.0));
 q('bur').style.opacity=seg(t,3.95,4.3); q('bur').style.transform=`scale(${0.7+0.3*back(lin(t,3.95,4.4))})`;
 const z=lin(t,4.4,4.75); q('f0').style.opacity=z>0?1:0; q('f0').style.transform=`scale(${2.4-1.4*back(z)})`;
 q('ring').style.top=A.cy+'px'; const rk=lin(t,4.75,5.5); q('ring').style.opacity=rk>0?1-rk:0; q('ring').style.width=q('ring').style.height=(40+1400*ease(rk))+'px';
 const sh=1-Math.exp(-((t-4.85)**2)/0.004)*0; document.body.style.transform=`translate(${t>4.75&&t<5.05?Math.sin(t*120)*10*(5.05-t)/0.3:0}px,0)`;
 q('off').style.opacity=seg(t,5.0,5.4); q('off').style.transform=`translateY(${(1-seg(t,5.0,5.4))*30}px)`;
 q('chip').style.opacity=seg(t,5.3,5.7); q('chip').style.transform=`scale(${0.6+0.4*back(lin(t,5.3,5.75))})`;
 q('terms').style.opacity=seg(t,5.6,6.0);
 const f=document.querySelector('.pf'); if(f) f.style.opacity=seg(t,5.9,6.3);
 const gl=Math.sin(Math.PI*lin(t,5.9,7.6)); q('pct').style.textShadow=`0 0 ${70*gl}px rgba(244,217,160,${0.85*gl})`;
 q('logo').style.opacity=seg(t,0,.5);
};
document.fonts.ready.then(()=>{setup(); R(location.hash?parseFloat(location.hash.slice(1)):99); window.READY=1;});
</script>'''

def page():
    body = f'''<div class="abs" style="inset:0;background:#0B0B0D"></div><div id="bgB"></div><!--/bk-->
<img id="logo" class="abs" src="file://{G.LW}" style="left:50%;transform:translateX(-50%);top:0;height:52px">
<svg id="big4" class="abs" width="360" height="430" style="left:190px;top:260px" viewBox="0 0 360 430"><text id="st" x="0" y="405" stroke="{GOLD}" stroke-width="7" fill="transparent" stroke-dasharray="2600" stroke-dashoffset="2600">4</text></svg>
<div id="yrs" class="abs P" style="left:580px;top:400px;color:#fff;font-size:92px;line-height:1">YEARS<br><span style="color:{GOLD};font-size:52px;letter-spacing:3px">OF 974</span></div>
<div id="cnt" class="abs P" style="left:580px;top:620px;font-size:44px;color:rgba(255,255,255,.5);letter-spacing:4px">2022</div>
<div id="ar1" class="abs" dir="rtl" style="left:0;right:0;top:790px;text-align:center;font-family:Cairo;font-weight:900;font-size:60px;color:#fff">٤ سنين معاكم.. والهدية منّا</div>
<div id="blk" class="abs P" style="left:0;right:0;top:150px;text-align:center;font-size:110px;color:rgba(255,255,255,.55);letter-spacing:-2px">BLACK
 <svg style="position:absolute;left:300px;top:52px" width="480" height="40" viewBox="0 0 480 40"><path id="ln" d="M6 28 C 150 6, 320 36, 474 10" stroke="{GOLD}" stroke-width="16" stroke-linecap="round" fill="none" stroke-dasharray="1000" stroke-dashoffset="1000"/></svg></div>
<div id="bur" class="abs P" style="left:0;right:0;top:290px;text-align:center;font-size:100px;color:#fff;line-height:1.05">BURGUNDY<br><span style="color:{GOLD}">FRIDAY</span></div>
<div id="pct" class="abs P" style="left:0;right:0;top:560px;text-align:center;font-size:330px;line-height:1;letter-spacing:-8px"><span id="f4" style="color:transparent">4</span><span id="f0" style="display:inline-block;color:#fff;transform-origin:30% 60%">0%</span></div>
<div id="off" class="abs" dir="rtl" style="left:0;right:0;top:930px;text-align:center;font-family:Cairo;font-weight:900;font-size:56px;color:#fff">خصم على كل الموقع</div>
<div id="chip" class="abs" dir="rtl" style="left:0;right:0;top:1040px;text-align:center"><span class="chip">الخميس والجمعة ٢٦ و ٢٧ نوفمبر</span></div>
<div id="terms" class="abs" dir="rtl" style="left:0;right:0;top:1140px;text-align:center;font-family:Cairo;font-weight:800;font-size:28px;color:#F4D9A0;line-height:1.55">للطلبات من الموقع فقط <span class="P" style="font-weight:700">974group.net</span><br>ما يجتمع مع أي خصم أو عرض ثاني</div>
<div id="ring"></div><canvas id="cv"></canvas>
{SCRIPT}'''
    return G.doc('#0B0B0D', '#fff', body, pf_ink='#fff', extra=CSS)

async def main(stills=None):
    from playwright.async_api import async_playwright
    G.STORY = True; p = OUT + '/story.html'; open(p, 'w').write(page())
    fr = OUT + '/frames'; os.makedirs(fr, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + p); await pg.wait_for_function('window.READY===1'); await pg.wait_for_timeout(600)
        if stills:
            for s in stills:
                await pg.evaluate(f'R({s})'); await pg.screenshot(path=f'{OUT}/still-{s}.jpg', type='jpeg', quality=85)
        else:
            for i in range(240):
                await pg.evaluate(f'R({i/30})'); await pg.screenshot(path=f'{fr}/{i:03d}.jpg', type='jpeg', quality=92)
            await pg.evaluate('R(99)'); await pg.screenshot(path=OUT + '/974-4years-story.jpg', type='jpeg', quality=92)
        await b.close()
    if not stills:
        tmp = OUT + '/974-4years-story.tmp.mp4'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', fr + '/%03d.jpg', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', tmp], check=True)
        os.replace(tmp, OUT + '/974-4years-story.mp4')
    print('ok')

if __name__ == '__main__':
    st = [float(x) for x in sys.argv[1:]] or None
    asyncio.run(main(st))
