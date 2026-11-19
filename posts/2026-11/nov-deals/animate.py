# Animated version of a November-deal story: takes the static story HTML, adds a frame-driven
# timeline (window.setT), screenshots every frame and encodes an MP4. 19 Nov 2026
# Motion rules (claude/motion-tools-learnings): ease-out entrances, staggered same-direction product entry,
# overshoot only on the price/badge pops, ambient tape scroll + dots drift, stillness at the end.
import subprocess, sys, os, shutil
D = '/home/claude/974-social/posts/2026-11/nov-deals/'
src = sys.argv[1] if len(sys.argv) > 1 else D + 'out/974-nov-deals-day7-apple-loops-story.html'
out = sys.argv[2] if len(sys.argv) > 2 else D + 'out/974-nov-deals-day7-apple-loops-story.mp4'
FPS, DUR = 30, 8.0

JS = r'''
<script>
const clamp=(x)=>Math.max(0,Math.min(1,x));
const bez=(p1x,p1y,p2x,p2y)=>t=>{let a=0,b=1,x,m;for(let i=0;i<30;i++){m=(a+b)/2;x=3*(1-m)*(1-m)*m*p1x+3*(1-m)*m*m*p2x+m*m*m;if(x<t)a=m;else b=m;}m=(a+b)/2;return 3*(1-m)*(1-m)*m*p1y+3*(1-m)*m*m*p2y+m*m*m;};
const easeOut=bez(0.05,0.7,0.1,1), pop=bez(0.175,0.885,0.32,1.275), inOut=bez(0.4,0,0.2,1);
const seg=(t,a,d)=>clamp((t-a)/d);
const $=(s)=>[...document.querySelectorAll(s)];
const prods=$('img[style*="object-fit:contain"]');
const big=document.querySelector('.big'), khasm=document.querySelector('.khasm'), sticker=document.querySelector('.sticker');
const tape=document.querySelector('.tape'), tapeSpan=tape.querySelector('span');
const tapeRot=tape.style.transform;
const all=$('body > div');
const titleBlk=all.find(d=>d.textContent.includes('Apple Watch')||d.querySelector('div[style*="font-size"]')&&d.style.textAlign==='center'&&d!==tape);
const chips=all.find(d=>d.style.justifyContent==='center'&&d.querySelector('s'));
const note=all.find(d=>d.textContent.includes('الخصم ينزل'));
const pf=document.querySelector('.pf'), dots=document.querySelector('.dots');
const head=all.find(d=>d.textContent.includes('NOVEMBER DEALS · DAY'));
const chipKids=chips?[...chips.children]:[];
window.setT=(t)=>{
  // ambient: dots drift, tape scrolls the whole time
  if(dots) dots.style.backgroundPosition=`${t*12}px ${t*18}px`;
  tapeSpan.style.display='inline-block'; tapeSpan.style.transform=`translateX(${-((t*90)%600)}px)`;
  // 0.0-0.6 header + logo fade/slide down
  const h=easeOut(seg(t,0,0.5)); [head,document.querySelector('.logo')].forEach(e=>{if(e){e.style.opacity=h;e.style.translate=`0 ${(1-h)*-24}px`;}});
  // 0.2-0.9 big % counts up and scales in
  const b=seg(t,0.2,0.7); const n=Math.round(40*easeOut(b));
  big.textContent=n+'%'; big.style.opacity=clamp(b*3); big.style.scale=0.6+0.4*pop(b);
  // 0.7 khasm badge pops with a small overshoot
  const k=seg(t,0.7,0.45); khasm.style.opacity=clamp(k*3); khasm.style.scale=0.3+0.7*pop(k); khasm.style.rotate=`${(1-pop(k))*-14}deg`;
  // 1.0 title rises
  if(titleBlk){const q=easeOut(seg(t,1.0,0.5)); titleBlk.style.opacity=q; titleBlk.style.translate=`0 ${(1-q)*30}px`;}
  // 1.3 products: all enter from the right (same direction), 70ms stagger
  prods.forEach((p,i)=>{const q=easeOut(seg(t,1.3+i*0.07,0.55)); p.style.opacity=q; p.style.translate=`${(1-q)*140}px ${(1-q)*10}px`;});
  // 2.0 sticker pops
  const s=seg(t,2.0,0.45); sticker.style.opacity=clamp(s*3); sticker.style.scale=0.2+0.8*pop(s);
  // 2.1 tape slides in from the left
  const tp=easeOut(seg(t,2.1,0.5)); tape.style.transform=`${tapeRot} translateX(${(1-tp)*-1200}px)`;
  // 2.5 price chips pop one by one
  chipKids.forEach((c,i)=>{const q=seg(t,2.5+i*0.12,0.45); c.style.opacity=clamp(q*3); c.style.scale=0.5+0.5*pop(q);});
  // 3.1 note + footer
  const f=easeOut(seg(t,3.1,0.5)); [note,pf].forEach(e=>{if(e){e.style.opacity=f;e.style.translate=`0 ${(1-f)*20}px`;}});
  // gentle breathing on the products after everything is in (ambient, sine)
  if(t>4) prods.forEach((p,i)=>{p.style.translate=`0 ${Math.sin((t-4)*2.2+i*0.6)*4}px`;});
  // sticker slow wobble
  if(t>2.5) sticker.style.rotate=`${Math.sin((t-2.5)*3)*4}deg`;
};
window.setT(0);
</script>'''


def main():
    html = open(src).read().replace('</body>', JS + '</body>')
    tmp = src.replace('.html', '-anim.html'); open(tmp, 'w').write(html)
    fr = '/tmp/frames'; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    n = int(FPS * DUR)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});"
          f"await p.goto('file://{tmp}');await p.waitForTimeout(1200);"
          f"for(let i=0;i<{n};i++){{await p.evaluate(t=>window.setT(t),i/{FPS});await p.screenshot({{path:'{fr}/f'+String(i).padStart(4,'0')+'.jpg',type:'jpeg',quality:92}});}}"
          f"await b.close();}})()")
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')
    part = out.replace('.mp4', '.part.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{fr}/f%04d.jpg', '-c:v', 'libx264', '-preset', 'veryfast',
                    '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', part], check=True)
    os.replace(part, out); print('ok', out)


if __name__ == '__main__':
    main()
