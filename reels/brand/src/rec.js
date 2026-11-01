// usage: node rec.js <theme> <out.mp4> [stillsOnly]
const {chromium}=require('playwright');const {spawn}=require('child_process');const path=require('path');
(async()=>{
  const [theme,out,stills]=process.argv.slice(2);
  const b=await chromium.launch({args:['--allow-file-access-from-files']});
  const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+path.resolve(__dirname,'logo.html'));
  await p.evaluate(t=>init(t),theme);
  if(stills){for(const t of [0.4,0.9,1.3,1.7,3]){await p.evaluate(t=>render(t),t);await p.screenshot({path:`still_${theme}_${t}.png`});}await b.close();return;}
  const fps=30,dur=3.6,N=Math.round(fps*dur);
  const tmp=out.replace(/\.mp4$/,'.part.mp4');
  const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',String(fps),tmp],{stdio:['pipe','inherit','inherit']});
  for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
  ff.stdin.end();await new Promise(r=>ff.on('close',c=>{if(c===0)require('fs').renameSync(tmp,out);r()}));
  await b.close();
})();
