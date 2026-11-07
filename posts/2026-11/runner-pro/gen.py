import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
NAVY='#232838'; LIME='#D8E03A'; TEAL='#6FC1BC'
SOCKS=[('white','White','#F4F4F4'),('blue','Blue',TEAL),('yellow','Yellow',LIME)]
I=lambda d:f'<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
ICO=[I('<path d="M17 6v16c0 4-7 8-7 14 0 4 3 6 7 6h14c3 0 5-2 5-4 0-3-4-4-8-6l-3-2V6"/><path d="M19 14h8M19 20h8"/>'),
     I('<path d="M8 18c6-6 12 6 18 0s10-2 14 0"/><path d="M8 28c6-6 12 6 18 0s10-2 14 0"/><path d="M8 38c6-6 12 6 18 0s10-2 14 0"/>'),
     I('<path d="M24 6l14 6v10c0 10-6 17-14 20C16 39 10 32 10 22V12z"/><path d="M18 24l4 4 8-9"/>'),
     I('<path d="M24 6v36"/><path d="M17 13l7-7 7 7M17 35l7 7 7-7"/>')]
FEAT=[('ضغط يدعم الساق','يخفف التعب والشد'),('تهوية عالية','قدمك تبقى ناشفة'),('كعب وأصابع مقوّاة','تتحمل الكيلومترات'),('طول نص الساق','ثابتة وما تنزل')]
def page(story):
    W,H=(1080,1920) if story else (1080,1350); s=1.12 if story else 1
    T=150 if story else 0
    hT=T+120; sT=hT+(300 if story else 215); sH=700 if story else 560
    fT=sT+sH+(110 if story else 72)
    socks=''.join(f'<div class="sk"><img src="file://{C}{k}.png"><div class="nm"><i style="background:{c}"></i>{n}</div></div>' for k,n,c in SOCKS)
    feats=''.join(f'<div class="f">{ICO[i]}<b>{a}</b><em>{b}</em></div>' for i,(a,b) in enumerate(FEAT))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:radial-gradient(120% 70% at 50% 45%,#5DAEA9 0%,#3F8C88 55%,#2C6764 100%);font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
/*x*/.trk{{position:absolute;left:0;right:0;top:{sT+sH-150}px;height:{300 if story else 260}px;background:linear-gradient(180deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.07) 100%)}}
/*x*/.trk svg{{position:absolute;inset:0;width:100%;height:100%}}
.top{{position:absolute;top:{T+48}px;left:48px;right:48px;display:flex;justify-content:space-between;align-items:center}}
.gl{{position:absolute;left:40px;right:40px;top:{sT+sH-(76 if story else 66)}px;height:3px;background:rgba(255,255,255,.55);border-radius:2px}}
.top img{{height:46px}} .top span{{font-family:Poppins;font-weight:700;font-size:{17*s}px;letter-spacing:5px;color:#fff}}
.h{{position:absolute;top:{hT}px;left:48px;right:48px;text-align:right;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:{66*s}px;line-height:1.15}} .h b em{{font-style:normal;color:{NAVY}}}
.h i{{display:block;font-style:normal;font-weight:600;font-size:{26*s}px;opacity:.8;margin-top:8px}}
.row{{position:absolute;left:40px;right:40px;top:{sT}px;height:{sH}px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.sk{{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-height:0}}
.sk img{{flex:0 1 auto;min-height:0;max-width:100%;max-height:100%;object-fit:contain}}
.nm{{margin-top:{30*s}px;display:flex;align-items:center;gap:10px;font-family:Poppins;font-weight:500;font-size:{21*s}px}}
.nm i{{width:14px;height:14px;border-radius:50%}}
.feat{{position:absolute;left:40px;right:40px;top:{fT}px;display:grid;grid-template-columns:repeat(4,1fr);direction:rtl}}
.f{{text-align:center;padding:0 8px;border-left:1px solid rgba(255,255,255,.3)}} .f:last-child{{border-left:0}}
.f svg{{width:{44*s}px;height:{44*s}px;color:{NAVY};display:block;margin:0 auto 10px}}
.f b{{display:block;font-weight:800;font-size:{21*s}px;line-height:1.3;white-space:nowrap}}
.f em{{display:block;font-style:normal;font-weight:600;font-size:{17*s}px;opacity:.85;line-height:1.4}}
.pf{{position:absolute;left:28px;right:28px;bottom:{146 if not story else 240}px}}
{payfoot.css(1.0 if not story else 1.12, text='#FFFFFF', label='#F2F2F2')}
.foot{{position:absolute;left:48px;right:48px;bottom:{38 if not story else 122}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:{NAVY};color:#fff;border-radius:40px;padding:2px 32px 8px;font-weight:900;font-size:{38*s}px;white-space:nowrap}}
.price b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{25*s}px}} .cta em{{font-style:normal;color:{NAVY}}}
</style></head><body>
<div class="gl"></div>
<div class="top"><span>THE RUNNER PRO SOCKS</span><img src="file://{LOGO}"></div>
<div class="h"><b>ساقك تتحمل..<br><em>وتركض أبعد</em></b><i>دلاغات Compression للجري والتمرين</i></div>
<div class="row">{socks}</div>
<div class="feat">{feats}</div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«جري»</em> ونرسل لك الرابط 📩</div><div class="price"><b>59</b> ر.ق</div></div>
</body></html>'''
if __name__=='__main__':
    for kind,st in (('post',False),('story',True)):
        n=f'974-runner-pro-{kind}'; H=1920 if st else 1350
        open(n+'.html','w').write(page(st))
        js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
        subprocess.run(['node','-e',js],check=True)
