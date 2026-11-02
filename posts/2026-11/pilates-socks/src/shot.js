const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:4600,height:3000}});
await p.goto('file://'+__dirname+'/d.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(700);
for(const id of fs.readFileSync(__dirname+'/ids.txt','utf8').split('\n')) await p.locator('#'+id).screenshot({path:`out/974-pilates-${id}.png`});await b.close();})();
