# Timeline design (option C) as an 8 s animated story for Friday 27 Nov 00:00 — LAST DAY.
import sys, os, asyncio, subprocess
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); OUT = D + '/out'; os.makedirs(OUT, exist_ok=True)
M, DEEP, GOLD, PAPER = '#720842', '#51022D', '#C9A24B', '#F4F1F2'
CSS = G.CTA_CSS + f'''
.P{{font-family:Poppins;font-weight:900}}
.chip{{display:inline-block;background:{GOLD};color:{DEEP};font-family:Cairo;font-weight:900;font-size:40px;border-radius:44px;padding:6px 36px 12px}}
#cv{{position:fixed;inset:0;width:1080px;height:1920px;pointer-events:none}}
#ring{{position:fixed;left:540px;width:10px;height:10px;border:8px solid {GOLD};border-radius:50%;transform:translate(-50%,-50%)}}
.dot{{opacity:0}}
'''
YRS = [('2022','البداية'),('2023',''),('2024',''),('2025',''),('2026','٤ سنين')]
def dots():
    out=''
    for i,(y,t) in enumerate(YRS):
        big=i==4; s=44 if big else 24
        out+=f'''<div class="dot" id="d{i}" style="text-align:center;width:160px"><div id="b{i}" style="width:{s}px;height:{s}px;border-radius:50%;background:{GOLD if big else M};margin:0 auto;border:5px solid {PAPER};box-shadow:0 0 0 3px {M}"></div>
<div class="P" style="font-size:{38 if big else 28}px;color:{M};margin-top:12px">{y}</div><div style="font-family:Cairo;font-weight:800;font-size:24px;color:{DEEP}">{t}</div></div>'''
    return out
SCRIPT = r'''<script>
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3), seg=(t,a,b)=>ease((t-a)/(b-a)), lin=(t,a,b)=>Math.max(0,Math.min(1,(t-a)/(b-a)));
const back=t=>{t=Math.max(0,Math.min(1,t));const c=1.70158;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)};
const q=id=>document.getElementById(id); function rnd(s){let x=Math.sin(s*12.9898)*43758.5453;return x-Math.floor(x)}
const cv=q('cv'), cx=cv.getContext('2d'); cv.width=1080; cv.height=1920; let CY=0;
window.R=function(t){
 if(!CY){const r=q('pct').getBoundingClientRect(); CY=r.top+r.height/2;}
 cx.clearRect(0,0,1080,1920);
 for(let i=0;i<90;i++){const x=rnd(i)*1080,y=((rnd(i+500)*1920-t*(25+rnd(i+900)*50))%1920+1920)%1920,a=.12+.35*rnd(i+77)*(.5+.5*Math.sin(t*3+i));
   cx.fillStyle=`rgba(201,162,75,${a})`; cx.beginPath(); cx.arc(x,y,1+rnd(i+3)*2.4,0,7); cx.fill();}
 const tb=0.72; if(t>tb){const k=t-tb; for(let i=0;i<200;i++){const ang=rnd(i+11)*6.283, sp=500+rnd(i+31)*1300;
   const x=540+Math.cos(ang)*sp*k*(1-0.35*k), y=CY+Math.sin(ang)*sp*k*(1-0.35*k)+520*k*k, al=Math.max(0,1-k/2.4); if(al<=0) continue;
   cx.save(); cx.translate(x,y); cx.rotate(k*8*rnd(i+5)+i); cx.fillStyle=(i%3==0)?`rgba(114,8,66,${al})`:(i%3==1)?`rgba(201,162,75,${al})`:`rgba(81,2,45,${al})`;
   cx.fillRect(-7,-3,14+rnd(i)*10,6); cx.restore();}}
 // card + counter hook
 const cs=0.82+0.18*back(lin(t,0,0.45)); q('card').style.transform=`scale(${cs})`; q('card').style.opacity=seg(t,0,.15);
 q('cnt').textContent=Math.min(40,Math.floor(41*lin(t,0.05,0.7)))+'%';
 q('pct').style.transform=`scale(${t<0.7?1:0.92+0.08*back(lin(t,0.7,1.0))})`;
 q('ring').style.top=CY+'px'; const rk=lin(t,0.72,1.45); q('ring').style.opacity=(rk>0&&rk<1)?1-rk:0; q('ring').style.width=q('ring').style.height=(40+1300*ease(rk))+'px';
 document.body.style.transform=`translate(${t>0.72&&t<1.0?Math.sin(t*120)*9*(1.0-t)/0.28:0}px,0)`;
 q('blk').style.opacity=seg(t,0.85,1.1); q('ln').style.strokeDashoffset=600*(1-seg(t,1.05,1.3));
 q('bur').style.opacity=seg(t,1.2,1.5);
 q('off').style.opacity=seg(t,1.35,1.65); q('off').style.transform=`translateY(${(1-seg(t,1.35,1.65))*24}px)`;
 q('chip').style.opacity=seg(t,1.6,1.9); q('chip').style.transform=`scale(${0.6+0.4*back(lin(t,1.6,2.0))})`;
 // title + timeline
 q('ttl').style.opacity=seg(t,2.0,2.4); q('ttl').style.transform=`translateY(${(1-seg(t,2.0,2.4))*-30}px)`;
 q('line').style.transform=`scaleX(${seg(t,2.4,4.0)})`;
 for(let i=0;i<5;i++){const a=2.45+i*0.38; const k=lin(t,a,a+0.3); q('d'+i).style.opacity=k>0?1:0; q('b'+i).style.transform=`scale(${back(k)})`;}
 const pl=lin(t,4.3,8); q('b4').style.boxShadow=`0 0 0 3px #720842, 0 0 0 ${8+14*Math.abs(Math.sin(pl*Math.PI*3))}px rgba(201,162,75,${.45-.3*Math.abs(Math.sin(pl*Math.PI*3))})`;
 q('terms').style.opacity=seg(t,4.4,4.8);
 const f=document.querySelector('.pf'); if(f) f.style.opacity=seg(t,4.7,5.1);
 const g2=Math.sin(Math.PI*lin(t,5.2,7.8)); q('cnt').style.textShadow=`0 0 ${60*g2}px rgba(244,217,160,${.8*g2})`;
};
document.fonts.ready.then(()=>{R(location.hash?parseFloat(location.hash.slice(1)):99); window.READY=1;});
</script>'''
def page():
    body = f'''<div class="abs" style="inset:0;background:{PAPER}"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:52px;top:10px;height:52px">
<div id="ttl" class="abs" dir="rtl" style="right:52px;top:0;text-align:right;color:{DEEP}">
  <div style="font-family:Cairo;font-weight:900;font-size:74px;line-height:1.15">شكراً على ٤ سنين</div>
  <div style="font-family:Cairo;font-weight:700;font-size:32px;color:{M}">من ٢٠٢٢ لين اليوم.. وانتوا معانا</div></div>
<div id="line" class="abs" style="left:110px;right:110px;top:268px;height:5px;background:{M};transform-origin:0 50%"></div>
<div class="abs" style="left:60px;right:60px;top:248px;display:flex;justify-content:space-between">{dots()}</div>
<div id="card" class="abs" style="left:90px;right:90px;top:470px;height:640px;border-radius:48px;background:{M};box-shadow:0 30px 60px rgba(81,2,45,.35)">
 <div style="position:absolute;left:0;right:0;top:44px;text-align:center">
  <div class="P" style="font-size:46px;line-height:1.1"><span id="blk" style="position:relative;color:rgba(255,255,255,.55)">BLACK<svg style="position:absolute;left:-6px;top:22px" width="190" height="20" viewBox="0 0 190 20"><path id="ln" d="M4 12 C 60 4, 130 16, 186 6" stroke="{GOLD}" stroke-width="8" stroke-linecap="round" fill="none" stroke-dasharray="600" stroke-dashoffset="600"/></svg></span><span style="display:inline-block;width:22px"></span><span id="bur" style="color:#fff">BURGUNDY FRIDAY</span></div>
  <div id="pct" class="P" style="font-size:250px;color:#fff;line-height:1.05;margin-top:6px"><span id="cnt">0%</span></div>
  <div id="off" dir="rtl" style="font-family:Cairo;font-weight:900;font-size:48px;color:{GOLD}">خصم على كل الموقع</div>
  <div id="chip" dir="rtl" style="margin-top:30px"><span class="chip">اليوم الجمعة آخر يوم لين الساعة <bdi dir="ltr" style="font-family:Poppins;font-weight:800">11:59</bdi></span></div>
 </div></div>
<div id="terms" class="abs" dir="rtl" style="left:0;right:0;top:1150px;text-align:center;font-family:Cairo;font-weight:800;font-size:30px;line-height:1.6;color:{DEEP}">للطلبات من الموقع فقط <span class="P" style="font-weight:700">974group.net</span><br>ما يجتمع مع أي خصم أو عرض ثاني</div>
<div id="ring"></div><canvas id="cv"></canvas>
{SCRIPT}'''
    return G.doc(PAPER, DEEP, body, extra=CSS)

async def main(stills=None):
    from playwright.async_api import async_playwright
    G.STORY = True; p = OUT + '/cstory.html'; open(p, 'w').write(page())
    fr = OUT + '/cframes'; os.makedirs(fr, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + p); await pg.wait_for_function('window.READY===1'); await pg.wait_for_timeout(600)
        if stills:
            for s in stills:
                await pg.evaluate(f'R({s})'); await pg.screenshot(path=f'{OUT}/cstill-{s}.jpg', type='jpeg', quality=85)
        else:
            for i in range(240):
                await pg.evaluate(f'R({i/30})'); await pg.screenshot(path=f'{fr}/{i:03d}.jpg', type='jpeg', quality=92)
        await b.close()
    if not stills:
        tmp = OUT + '/974-lastday-story.tmp.mp4'
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',fr+'/%03d.jpg','-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
            '-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-shortest','-movflags','+faststart',tmp],check=True)
        os.replace(tmp, OUT + '/974-lastday-story.mp4')
    print('ok')
if __name__ == '__main__':
    st=[float(x) for x in sys.argv[1:]] or None; asyncio.run(main(st))
