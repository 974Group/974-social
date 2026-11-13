import subprocess,sys
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
R='/home/claude/974-social/'
G=R+'posts/2026-11/goggles-26-27/src/cut/ph4.png'
MK=R+'posts/2026-11/face-mask/src/cutd/black.png'
PL=R+'reels/2026-11/pilates/end/logos/paylater.png'
LOGO=R+'posts/2026-11/pilates-socks/src/logo-black.png'
P='#4A35C8'; T='#1FB8C9'; INK='#1B1446'
def page(story):
    W,H=1080,(1920 if story else 1350); s=1.12 if story else 1; o=170 if story else 0
    steps=[('اليوم','عند الطلب'),('بعد شهر',''),('بعد شهرين',''),('بعد 3 شهور','')]
    st=''.join(f'<div class="st{" now" if i==0 else ""}"><div class="dot">{i+1}</div><b><span>97</span> ر.ق</b><i>{a}</i></div>' for i,(a,_) in enumerate(steps))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:800;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:radial-gradient(900px 700px at 85% 0%,#E4E0FF 0%,transparent 60%),radial-gradient(800px 600px at 0% 100%,#D7F6F8 0%,transparent 60%),#F6F5FC;font-family:Cairo;color:{INK};position:relative;overflow:hidden}}
.top{{position:absolute;top:{44+o-(30 if story else 0)}px;left:48px;right:48px;display:flex;justify-content:space-between;align-items:center}}
.top .l974{{height:{46*s}px}} .top .pl{{height:{44*s}px}}
.h{{position:absolute;top:{120+o}px;left:48px;right:48px;text-align:center;direction:rtl}}
.h b{{display:block;font-weight:900;font-size:{74*s}px;line-height:1.15}}
.h b em{{font-style:normal;background:linear-gradient(90deg,{P},{T});-webkit-background-clip:text;color:transparent}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:{27*s}px;color:#5A5390;margin-top:6px}}
.card{{position:absolute;left:48px;right:48px;top:{318+o+(30 if story else 0)}px;height:{500*s}px;border-radius:36px;background:#fff;box-shadow:0 20px 50px rgba(74,53,200,.14);overflow:hidden}}
.tag{{position:absolute;top:26px;right:28px;background:{INK};color:#fff;font-weight:800;font-size:{20*s}px;padding:4px 18px 7px;border-radius:30px;direction:rtl}}
.prods{{position:absolute;left:0;right:0;top:{48*s}px;height:{300*s}px}}
.prods .g{{position:absolute;left:{60*s}px;top:0;width:{430*s}px;filter:drop-shadow(0 18px 18px rgba(0,0,0,.25))}}
.prods .m{{position:absolute;right:{70*s}px;top:{14*s}px;height:{265*s}px;filter:drop-shadow(0 14px 14px rgba(0,0,0,.25))}}
.sum{{position:absolute;left:28px;right:28px;bottom:24px;display:flex;align-items:center;justify-content:space-between;direction:rtl;background:#F3F1FF;border-radius:24px;padding:14px 24px}}
.sum .it{{font-weight:700;font-size:{21*s}px;color:#5A5390;line-height:1.35}}
.sum .it b{{color:{INK};font-weight:800}}
.sum .tot{{font-weight:900;font-size:{40*s}px;white-space:nowrap}} .sum .tot span{{font-family:Poppins;font-weight:800}} .sum .tot small{{font-size:{20*s}px;color:#5A5390;font-weight:700;display:block;text-align:center;line-height:1}}
.split{{position:absolute;left:48px;right:48px;top:{318+o+(30 if story else 0)+500*s+30}px;direction:rtl}}
.split .lbl{{text-align:center;font-weight:800;font-size:{28*s}px;margin-bottom:16px}}
.split .lbl em{{font-style:normal;color:{P}}}
.row{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;position:relative}}
.st{{background:#fff;border-radius:24px;padding:22px 6px 20px;text-align:center;box-shadow:0 10px 26px rgba(74,53,200,.10)}}
.st .dot{{width:{40*s}px;height:{40*s}px;margin:0 auto 6px;border-radius:50%;background:#ECE9FF;color:{P};font-family:Poppins;font-weight:800;font-size:{20*s}px;display:flex;align-items:center;justify-content:center}}
.st b{{display:block;font-weight:900;font-size:{24*s}px;white-space:nowrap}} .st b span{{font-family:Poppins;font-weight:800;font-size:{38*s}px}}
.st i{{display:block;font-style:normal;font-weight:700;font-size:{20*s}px;color:#5A5390}}
.st.now{{background:linear-gradient(150deg,{P},{T});color:#fff}} .st.now i{{color:#E8E6FF}} .st.now .dot{{background:rgba(255,255,255,.25);color:#fff}}
.note{{margin-top:22px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap;direction:rtl}}
.note span{{background:#fff;border-radius:30px;padding:4px 18px 7px;font-weight:700;font-size:{20*s}px;color:#3C3570;box-shadow:0 4px 12px rgba(0,0,0,.06)}}
.pf{{position:absolute;left:28px;right:28px;bottom:{36 if not story else 150}px}}
{payfoot.css(1.0 if not story else 1.12)}
</style></head><body>
<div class="top"><img class="pl" src="file://{PL}"><img class="l974" src="file://{LOGO}"></div>
<div class="h"><b>قسّمها على <em>4 دفعات</em></b><i>بدون فوايد · ادفع ربع المبلغ اليوم والباقي على 3 شهور</i></div>
<div class="card"><div class="tag">مثال</div>
 <div class="prods"><img class="g" src="file://{G}"><img class="m" src="file://{MK}"></div>
 <div class="sum"><div class="it"><b>Photochromic Edition</b> نظارة 349<br>+ ماسك 974 &nbsp;39</div><div class="tot"><small>المجموع</small><span>388</span> ر.ق</div></div>
</div>
<div class="split"><div class="lbl">تدفع بـ<em>PayLater</em> كذا 👇</div><div class="row">{st}</div>
<div class="note"><span>✔ للطلبات فوق 300 ر.ق</span><span>✔ داخل قطر</span><span>✔ اختار PayLater عند الدفع</span></div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''
for kind,stv in (('post',False),('story',True)):
    n=f'974-paylater-{kind}'; H=1920 if stv else 1350
    open(n+'.html','w').write(page(stv))
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
