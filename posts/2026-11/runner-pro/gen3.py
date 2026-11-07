import subprocess
from gen2 import HEAD,TOP,FOOT,C,SOCKS,ICO,NAVY
FEAT=[('ضغط يدعم الساق','يخفف التعب والشد'),('تهوية عالية','قدمك تبقى ناشفة'),('كعب وأصابع مقوّاة','تتحمل الكيلومترات'),('طول نص الساق','ثابتة وما تنزل')]
h=HEAD.replace('height:1350px','height:1920px').replace('top:48px;left:48px','top:200px;left:48px').replace('.h{{','.h{{').replace('top:120px;left:48px;right:48px;text-align:right','top:275px;left:48px;right:48px;text-align:right').replace('bottom:146px','bottom:240px').replace('bottom:38px','bottom:124px')
socks=''.join(f'<div class="sk"><img src="file://{C}{k}.png"><div class="nm"><i style="background:{c}"></i>{n}</div></div>' for k,n,c in SOCKS)
feats=''.join(f'<div class="f"><div class="ic">{ICO[i]}</div><div><b>{a}</b><em>{b}</em></div></div>' for i,(a,b) in enumerate(FEAT))
html=h+f'''
.row{{position:absolute;left:28px;right:28px;top:540px;height:640px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.sk{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-height:0}}
.sk img{{flex:0 1 auto;min-height:0;max-width:100%;max-height:100%;object-fit:contain}}
.nm{{margin-top:34px;display:flex;align-items:center;gap:10px;font-family:Poppins;font-weight:500;font-size:24px}}
.nm i{{width:15px;height:15px;border-radius:50%}}
.gl{{position:absolute;left:40px;right:40px;top:{540+640-70}px;height:3px;background:rgba(255,255,255,.55);border-radius:2px}}
.feat{{position:absolute;left:48px;right:48px;top:1250px;display:grid;grid-template-columns:1fr 1fr;gap:34px 28px;direction:rtl}}
.f{{display:flex;align-items:center;gap:16px}}
.ic{{flex:none;width:76px;height:76px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center}}
.ic svg{{width:40px;height:40px;color:#fff}}
.f b{{display:block;font-weight:900;font-size:30px;line-height:1.3;white-space:nowrap}}
.f em{{display:block;font-style:normal;font-weight:600;font-size:22px;opacity:.9;line-height:1.4}}
</style></head><body>{TOP}
<div class="h"><b>ساقك تتحمل..<br><em>وتركض أبعد</em></b><i>دلاغات Compression للجري والتمرين</i></div>
<div class="gl"></div><div class="row">{socks}</div><div class="feat">{feats}</div>{FOOT}</body></html>'''
n='974-runner-pro-story'
open(n+'.html','w').write(html)
js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1920}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
subprocess.run(['node','-e',js],check=True)
