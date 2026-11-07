import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LOGO='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
BG='#141417'; INK='#FFFFFF'; MUTE='rgba(255,255,255,.7)'
# hex grip pattern (from the sole pads)
HEX="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='97' viewBox='0 0 56 97'%3E%3Cg fill='none' stroke='%23ffffff' stroke-opacity='.06' stroke-width='2'%3E%3Cpath d='M28 2l24 14v28L28 58 4 44V16z'/%3E%3Cpath d='M28 58v39M0 0'/%3E%3C/g%3E%3C/svg%3E\")"
HEAD=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:__H__px;background:{HEX},radial-gradient(90% 60% at 30% 45%,#2A2A30 0%,{BG} 70%);font-family:Cairo;color:{INK};position:relative;overflow:hidden}}
.top{{position:absolute;top:__T__px;left:48px;right:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:46px}} .top span{{font-family:Poppins;font-weight:700;font-size:17px;letter-spacing:5px;color:{MUTE}}}
.pf{{position:absolute;left:28px;right:28px;bottom:__PF__px}}
{payfoot.css(1.0, text='#FFFFFF', label='#E8E8E8')}
.foot{{position:absolute;left:48px;right:48px;bottom:__FB__px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.price{{direction:rtl;background:#fff;color:{BG};border-radius:40px;padding:2px 30px 8px;font-weight:900;font-size:36px;white-space:nowrap}}
.price b{{font-family:Poppins}} .price small{{font-size:.55em;font-weight:700}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;text-decoration:underline;text-underline-offset:6px}}
'''
def head(H=1350,story=False):
    return (HEAD.replace('__H__',str(H)).replace('__T__',str(200 if story else 48))
            .replace('__PF__',str(240 if story else 146)).replace('__FB__',str(124 if story else 38)))
TOP='<div class="top"><span>974 GRIP SOCKS</span><img src="file://'+LOGO+'"></div>'
FOOT=f'''<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«جريب»</em> ونرسل لك الرابط 📩</div><div class="price"><small>من </small><b>39</b> ر.ق</div></div>'''
COLS=[('White','#F4F4F4'),('Black','#0B0B0B'),('Red','#D9262E'),('Maroon','#7A1426'),('Blue','#1F4FD8'),('Grey','#8A8D93')]

def slide1(story=False):
    o=150 if story else 0
    chips=lambda names:''.join(f'<span class="ch"><i style="background:{c}"></i>{n}</span>' for n,c in COLS if n in names)
    return head(1920 if story else 1350,story)+f'''
.h{{position:absolute;top:{o+128}px;right:48px;width:560px;text-align:right;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:76px;line-height:1.1}}
.h i{{display:block;font-style:normal;font-weight:600;font-size:26px;color:{MUTE};margin-top:14px;line-height:1.45}}
.hero{{position:absolute;left:30px;top:{o+110}px;width:440px;height:{860 if story else 760}px;display:flex;align-items:center;justify-content:center}}
.hero img{{max-width:100%;max-height:100%;transform:rotate(-6deg)}}
.info{{position:absolute;right:48px;width:560px;top:{o+(560 if story else 470)}px;direction:rtl}}
.lab{{font-weight:800;font-size:20px;color:{MUTE};margin:0 0 12px}}
.row{{display:flex;flex-wrap:wrap;gap:10px 10px;margin-bottom:10px}}
.ch{{display:inline-flex;align-items:center;gap:9px;border:1.5px solid rgba(255,255,255,.35);border-radius:30px;padding:6px 16px 7px;font-family:Poppins;font-weight:500;font-size:21px}}
.ch i{{width:16px;height:16px;border-radius:50%;box-shadow:0 0 0 1.5px rgba(255,255,255,.55)}}
.pr{{font-weight:800;font-size:24px;margin:2px 0 26px}} .pr b{{font-family:Poppins;font-size:30px}} .pr s{{font-family:Poppins;opacity:.5;margin-right:6px}} .pr em{{font-style:normal;background:#fff;color:{BG};border-radius:20px;padding:0 12px 3px;font-size:18px;margin-right:8px}}
.sz{{display:flex;gap:12px}} .sz span{{flex:1;border-radius:18px;background:rgba(255,255,255,.08);padding:12px 10px;text-align:center}}
.sz b{{display:block;font-family:Poppins;font-weight:700;font-size:32px;line-height:1.1}} .sz em{{display:block;font-style:normal;font-family:Poppins;font-weight:500;font-size:19px;color:{MUTE}}}
</style></head><body>{TOP}
<div class="hero"><img src="file://{C}white.png"></div>
<div class="h"><b>ثبات من<br>أول خطوة</b><i>دلاغات Grip بقطع مطاط تحت القدم.. رجلك ما تزحلق داخل الجوتي</i></div>
<div class="info">
<div class="lab">الألوان المتوفرة</div>
<div class="row">{chips(['White','Black'])}</div>
<div class="pr"><b>60</b> ر.ق</div>
<div class="row">{chips(['Red','Maroon','Blue','Grey'])}</div>
<div class="pr"><b>39</b> ر.ق <s>60</s><em>خصم</em></div>
<div class="lab">المقاسات</div>
<div class="row"><span class="ch" style="direction:ltr"><b>M</b>&nbsp;38–43</span><span class="ch" style="direction:ltr"><b>L</b>&nbsp;43–46</span></div>
</div>
{FOOT}</body></html>'''

ROWS=[('المسك على الجوتي','ينزلق مع كل حركة','ضعف قوة المسك'),
      ('الدوران والتوقف','رجلك تتحرك داخل الجوتي','حركة القدم أقل باللفات الحادة'),
      ('السرعة','أبطأ بتغيير الاتجاه','أسرع بالتمارين السريعة'),
      ('الاستخدام','للبس اليومي','مصمم للملاعب والتمارين')]
def slide2(story=False):
    o=150 if story else 0
    rows=''.join(f'<div class="r"><div class="k">{k}</div><div class="a">{a}</div><div class="g">{g}</div></div>' for k,a,g in ROWS)
    return head(1920 if story else 1350,story)+f'''
.h{{position:absolute;top:{o+120}px;left:48px;right:48px;text-align:right;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:60px;line-height:1.15}}
.h i{{display:block;font-style:normal;font-weight:600;font-size:24px;color:{MUTE};margin-top:6px}}
.stat{{position:absolute;top:{o+(330 if story else 270)}px;left:48px;right:48px;display:flex;align-items:center;gap:28px;direction:rtl}}
.stat .n{{font-family:Poppins;font-weight:700;font-size:150px;line-height:.9}}
.stat .t b{{display:block;font-weight:900;font-size:36px;line-height:1.25}} .stat .t em{{display:block;font-style:normal;font-weight:600;font-size:21px;color:{MUTE};line-height:1.45}}
.sole{{position:absolute;left:20px;top:{o+(260 if story else 236)}px;height:260px;opacity:.95}}
.tb{{position:absolute;left:48px;right:48px;top:{o+(620 if story else 520)}px;direction:rtl}}
.hd,.r{{display:grid;grid-template-columns:1.05fr 1fr 1.35fr;gap:16px;align-items:center}}
.hd{{font-weight:900;font-size:24px;padding-bottom:12px;border-bottom:2px solid rgba(255,255,255,.5)}} .hd span:nth-child(2){{color:{MUTE}}}
.r{{padding:{24 if story else 18}px 0;border-bottom:1px solid rgba(255,255,255,.16)}}
.k{{font-weight:900;font-size:26px}} .a{{font-weight:600;font-size:21px;color:rgba(255,255,255,.55)}} .g{{font-weight:800;font-size:23px}}
.g::before{{content:'✓ ';color:#fff;font-weight:900}}
.src{{position:absolute;left:48px;right:48px;top:{o+(1290 if story else 1080)}px;direction:rtl;font-weight:500;font-size:16px;color:rgba(255,255,255,.5)}}
.sp{{position:absolute;left:48px;right:48px;top:{o+(1210 if story else 1030)}px;direction:rtl;font-weight:700;font-size:22px}}
</style></head><body>{TOP}
<div class="h"><b>ليش Grip؟</b><i>وش الفرق عن الدلاغ العادي</i></div>
<div class="stat"><div class="n" style="direction:ltr">×2</div><div class="t"><b>مسك أقوى من الدلاغ العادي</b><em>القطع المطاطية تثبّت رجلك داخل الجوتي<br>بالتسارع والتوقف والدوران</em></div></div>
<div class="tb"><div class="hd"><span></span><span>دلاغ عادي</span><span>974 Grip</span></div>{rows}</div>
<div class="sp">للكورة · البادل · السلة · الجيم</div>
<div class="src">* حسب دراسة منشورة في Journal of Sports Sciences (2022): معامل الاحتكاك 1.17 مقابل 0.60</div>
{FOOT}</body></html>'''

def shot(n,html,H):
    open(n+'.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
if __name__=='__main__':
    shot('974-grip-1-colours',slide1(),1350)
    shot('974-grip-2-why',slide2(),1350)
