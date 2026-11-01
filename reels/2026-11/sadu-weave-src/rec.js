// node rec.js out.mp4 dur [still t]
const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const [out,dur,still]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/endcard.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
if(still){await p.evaluate(t=>render(t),+still);await p.screenshot({path:out});await b.close();return;}
const fps=30,N=Math.round(fps*dur),tmp=out.replace('.mp4','.part.mp4');
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30',tmp],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',c=>{if(c===0)require('fs').renameSync(tmp,out);r()}));await b.close();})();
