const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2400,height:2100}});
await p.goto('file://'+__dirname+'/d.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.locator('#p').screenshot({path:'974-fitbit2-post.png'});await p.locator('#s').screenshot({path:'974-fitbit2-story.png'});await b.close();})();
