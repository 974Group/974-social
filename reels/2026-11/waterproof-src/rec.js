const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/tl.html');await p.waitForTimeout(800);
const fps=30,dur=6.5;require('fs').mkdirSync('fr',{recursive:true});
for(let i=0;i<Math.round(fps*dur);i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`fr/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close()})()
