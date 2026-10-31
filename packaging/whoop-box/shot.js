const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const m of ['sil','fab']){for(const d of (process.env.D||'W1,W2,W3,W4,W5').split(',')){const p=await b.newPage({viewport:{width:3600,height:4200}});await p.goto('file://'+__dirname+'/w-'+m+'.html');await p.evaluate(()=>document.fonts.ready);
await p.evaluate((d)=>{document.body.style.padding="0";for(const x of document.querySelectorAll('.die')) if(x.id!==d) x.remove();},d);await p.waitForTimeout(300);await p.locator('#'+d).screenshot({path:`die-${d}-${m}.jpg`,type:'jpeg',quality:92});await p.close();}}
await b.close();})();
