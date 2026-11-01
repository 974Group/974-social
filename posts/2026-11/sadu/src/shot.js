const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:4600,height:2100}});
await p.goto('file://'+__dirname+'/d.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const o={p1:'974-sadu-1-post',s1:'974-sadu-1-story',p2:'974-sadu-2-post',s2:'974-sadu-2-story'};
for(const k in o) await p.locator('#'+k).screenshot({path:o[k]+'.png'});await b.close();})();
