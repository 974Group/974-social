import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
from gen import SP,C,LOGO,NAVY,LIME,TEAL,SOCKS,ICO
FEAT=[('ضغط يدعم عضلة الساق','يخفف التعب والشد بالجري الطويل'),
      ('تهوية عالية','نسيج يتنفس.. وقدمك تبقى ناشفة'),
      ('كعب وأصابع مقوّاة','تتحمل الاحتكاك والكيلومترات'),
      ('طول نص الساق','ثابتة على رجلك وما تنزل')]
HEAD=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:radial-gradient(120% 70% at 50% 45%,#5DAEA9 0%,#3F8C88 55%,#2C6764 100%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;top:48px;left:48px;right:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:46px}} .top span{{font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:5px;color:#fff}}
.h{{position:absolute;top:120px;left:48px;right:48px;text-align:right;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:66px;line-height:1.15}} .h b em{{font-style:normal;color:{NAVY}}}
.h i{{display:block;font-style:normal;font-weight:600;font-size:26px;opacity:.85;margin-top:8px}}
.pf{{position:absolute;left:28px;right:28px;bottom:146px}}
{payfoot.css(1.0, text='#FFFFFF', label='#F2F2F2')}
.foot{{position:absolute;left:48px;right:48px;bottom:38px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:{NAVY};color:#fff;border-radius:40px;padding:2px 32px 8px;font-weight:900;font-size:38px;white-space:nowrap}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;color:{NAVY}}}
'''
FOOT=f'''<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«جري»</em> ونرسل لك الرابط 📩</div><div class="price"><b>59</b> ر.ق</div></div>'''
TOP='<div class="top"><span>THE RUNNER PRO SOCKS</span><img src="file://'+LOGO+'"></div>'

def slide1():
    socks=''.join(f'<div class="sk"><img src="file://{C}{k}.png"><div class="nm"><i style="background:{c}"></i>{n}</div></div>' for k,n,c in SOCKS)
    return HEAD+f'''
.row{{position:absolute;left:28px;right:28px;top:350px;height:720px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.sk{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-height:0}}
.sk img{{flex:0 1 auto;min-height:0;max-width:100%;max-height:100%;object-fit:contain}}
.nm{{margin-top:34px;display:flex;align-items:center;gap:10px;font-family:Poppins;font-weight:500;font-size:24px}}
.nm i{{width:15px;height:15px;border-radius:50%}}
.gl{{position:absolute;left:40px;right:40px;top:{350+720-70}px;height:3px;background:rgba(255,255,255,.55);border-radius:2px}}
</style></head><body>{TOP}
<div class="h"><b>ساقك تتحمل..<br><em>وتركض أبعد</em></b><i>دلاغات Compression للجري والتمرين</i></div>
<div class="gl"></div><div class="row">{socks}</div>{FOOT}</body></html>'''

def slide2():
    feats=''.join(f'<div class="f"><div class="ic">{ICO[i]}</div><div><b>{a}</b><em>{b}</em></div></div>' for i,(a,b) in enumerate(FEAT))
    return HEAD+f'''
.pair{{position:absolute;left:20px;top:290px;width:450px;height:800px;display:flex;align-items:center;justify-content:center}}
.pair img{{max-width:100%;max-height:100%}}
.feat{{position:absolute;right:48px;left:470px;top:290px;height:700px;display:flex;flex-direction:column;justify-content:space-between;direction:rtl}}
.f{{display:flex;align-items:center;gap:20px;padding-bottom:22px;border-bottom:1px solid rgba(255,255,255,.3)}} .f:last-child{{border-bottom:0;padding-bottom:0}}
.ic{{flex:none;width:84px;height:84px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center}}
.ic svg{{width:44px;height:44px;color:#fff}}
.f b{{display:block;font-weight:900;font-size:35px;line-height:1.3}}
.f em{{display:block;font-style:normal;font-weight:600;font-size:24px;opacity:.9;line-height:1.45}}
.mat{{position:absolute;right:48px;left:470px;top:1030px;direction:rtl;display:flex;gap:12px;font-family:Poppins;font-weight:500;font-size:20px}}
.mat span{{border:1.5px solid rgba(255,255,255,.6);border-radius:30px;padding:6px 18px 5px}}
</style></head><body>{TOP}
<div class="h"><b>ليش <em>Runner Pro</em>؟</b></div>
<div class="pair"><img src="file://{C}pair-blue.png"></div>
<div class="feat">{feats}</div>
<div class="mat"><span>91.5% Nylon</span><span>8.5% Spandex</span></div>
{FOOT}</body></html>'''

for n,f in (('974-runner-pro-1-look',slide1),('974-runner-pro-2-features',slide2)):
    open(n+'.html','w').write(f())
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1350}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
