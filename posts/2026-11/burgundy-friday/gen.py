# Burgundy Friday teaser story: BLACK gets struck through and becomes BURGUNDY. 40% off, Friday 27 Nov.
import sys, os, asyncio, subprocess
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); OUT = D + '/out'; os.makedirs(OUT, exist_ok=True)
BUR = '#720842'; DEEP = '#51022D'; GOLD = '#C9A24B'
CSS = G.CTA_CSS + f'''
#bgB{{position:fixed;inset:0;background:radial-gradient(90% 60% at 50% 40%,#8A1550 0%,{BUR} 45%,{DEEP} 100%);clip-path:circle(var(--r,0%) at 50% 38%)}}
.dots{{position:fixed;inset:0;background-image:radial-gradient(rgba(255,255,255,.08) 1.5px,transparent 1.6px);background-size:26px 26px}}
.w{{font-family:Poppins;font-weight:900;letter-spacing:-4px;line-height:.9}}
#black{{position:absolute;left:0;right:0;top:330px;text-align:center;font-size:200px;color:#fff}}
#strike{{position:absolute;left:90px;top:405px;width:900px;height:60px;overflow:visible}}
#bur{{position:absolute;left:0;right:0;top:550px;text-align:center;font-size:160px;color:#fff;text-shadow:0 0 40px rgba(201,162,75,.35)}}
#fri{{position:absolute;left:0;right:0;top:715px;text-align:center;font-size:150px;color:{GOLD}}}
#pct{{position:absolute;left:0;right:0;top:900px;text-align:center}}
#pct b{{font-family:Poppins;font-weight:900;font-size:230px;color:#fff;line-height:1}}
#pct span{{font-family:Cairo;font-weight:900;font-size:64px;color:{GOLD};vertical-align:top;margin-left:10px}}
#date{{position:absolute;left:0;right:0;top:1170px;text-align:center;direction:rtl}}
.chip{{display:inline-block;background:{GOLD};color:{DEEP};font-family:Cairo;font-weight:900;font-size:40px;border-radius:40px;padding:6px 34px 12px}}
#soon{{font-family:Cairo;font-weight:900;font-size:36px;color:#fff;margin-top:18px}}
'''
SCRIPT = '''<script>
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3), seg=(t,a,b)=>ease((t-a)/(b-a));
window.R=function(t){
 const q=id=>document.getElementById(id);
 q('black').style.opacity=seg(t,.1,.7); q('black').style.transform=`translateY(${(1-seg(t,.1,.7))*40}px)`;
 q('line').style.strokeDashoffset=1000*(1-seg(t,1.3,2.0));
 const r=seg(t,2.3,3.2); document.documentElement.style.setProperty('--r',(r*140)+'%');
 q('black').style.color=`rgba(255,255,255,${1-0.55*r})`;
 q('bur').style.opacity=seg(t,2.7,3.4); q('bur').style.transform=`scale(${0.8+0.2*seg(t,2.7,3.5)})`;
 q('fri').style.opacity=seg(t,3.2,3.8); q('fri').style.transform=`translateY(${(1-seg(t,3.2,3.8))*30}px)`;
 const p=seg(t,3.9,5.0); q('pct').style.opacity=seg(t,3.9,4.2); q('n').textContent=Math.round(40*p);
 q('pct').style.transform=`scale(${1+0.12*Math.sin(Math.PI*seg(t,4.9,5.4))})`;
 q('date').style.opacity=seg(t,5.3,5.9); q('date').style.transform=`translateY(${(1-seg(t,5.3,5.9))*30}px)`;
 const f=document.querySelector('.pf'); if(f) f.style.opacity=seg(t,5.8,6.4);
 q('logo').style.opacity=seg(t,0,.5);
};
R(location.hash?parseFloat(location.hash.slice(1)):99); window.READY=1;
</script>'''


def page():
    body = f'''<div class="abs" style="inset:0;background:#0B0B0D"></div><div id="bgB"></div><div class="dots"></div><!--/bk-->
<img id="logo" class="abs" src="file://{G.LW}" style="left:48px;top:20px;height:46px">
<div id="black" class="w">BLACK</div>
<svg id="strike" viewBox="0 0 900 60"><path id="line" d="M10 40 C 220 10, 520 55, 890 18" stroke="{GOLD}" stroke-width="22" stroke-linecap="round" fill="none" stroke-dasharray="1000" stroke-dashoffset="0"/></svg>
<div id="bur" class="w">BURGUNDY</div>
<div id="fri" class="w">FRIDAY</div>
<div id="pct"><b id="n">40</b><b>%</b><span>خصم</span></div>
<div id="date"><span class="chip">الخميس والجمعة ٢٦ و ٢٧ نوفمبر</span><div id="soon">جهّز سلتك من الحين 🛒</div></div>
{SCRIPT}'''
    return G.doc('#0B0B0D', '#fff', body, pf_ink='#fff', extra=CSS)


async def main():
    from playwright.async_api import async_playwright
    G.STORY = True; html = page(); p = OUT + '/burgundy-friday-story.html'; open(p, 'w').write(html)
    fr = OUT + '/frames'; os.makedirs(fr, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + p); await pg.wait_for_function('window.READY===1'); await pg.wait_for_timeout(800)
        await pg.evaluate('R(99)'); await pg.screenshot(path=OUT + '/974-burgundy-friday-story.png')
        for i in range(240):
            await pg.evaluate(f'R({i/30})'); await pg.screenshot(path=f'{fr}/{i:03d}.jpg', type='jpeg', quality=92)
        await b.close()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', fr + '/%03d.jpg', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', '-movflags', '+faststart',
                    OUT + '/974-burgundy-friday-story.mp4'], check=True)
    print('ok')

asyncio.run(main())
