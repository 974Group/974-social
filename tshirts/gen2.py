# "Drop 01" launch set — poster/editorial style, artwork as hero
import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'; A=os.path.abspath('art')+'/'; D=os.path.abspath('designy')+'/'
LW='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
LB='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
GRAIN="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}} .ar{{direction:rtl;text-align:right}}
.grain{{position:absolute;inset:0;background:{GRAIN};opacity:.16;mix-blend-mode:soft-light;pointer-events:none}}
.ol{{-webkit-text-stroke:2px currentColor;color:transparent}}'''
def page(W,H,bg,ink,body,story,logo,extra='',pf_ink=None):
    pf_b=240 if story else 140; ft_b=124 if story else 38; t=200 if story else 48
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:{bg};color:{ink};font-family:Cairo;position:relative;overflow:hidden}}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf_b}px}}
{payfoot.css(1.0 if not story else 1.12, text=pf_ink or ink, label=pf_ink or ink)}
.foot{{position:absolute;left:48px;right:48px;bottom:{ft_b}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.pill{{border:2px solid {ink};border-radius:40px;padding:4px 26px 8px;font-weight:900;font-size:30px;white-space:nowrap}} .pill b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;text-decoration:underline;text-underline-offset:6px}}
.top{{position:absolute;left:48px;right:48px;top:{t}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px}}
{extra}</style></head><body>
{body}<div class="grain"></div>
<div class="top"><img src="file://{logo}"><span>DROP 01 · DESIGNY × 974</span></div>
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«تيشيرت»</em> ونرسل لك الرابط 📩</div><div class="pill"><b>139</b> ر.ق</div></div>
</body></html>'''

NAVY='#131B35'; SKY='#8EC0EA'
def cover(story=False):
    o=150 if story else 0; H=1920 if story else 1350
    # artworks: palace (white) left-top, falling man right, lemon centre-low; big word behind
    body=f'''
<div class="abs en ol" style="left:-10px;top:{o+170}px;font-weight:700;font-size:{250 if story else 215}px;line-height:.85;letter-spacing:-8px;color:rgba(255,255,255,.22);white-space:nowrap">THE BACK<br>TALKS</div>
<img class="abs" src="file://{A}sb-palace.png" style="left:-30px;top:{o+(330 if story else 270)}px;width:560px">
<img class="abs" src="file://{A}fw-hero.png" style="right:-100px;top:{o+(220 if story else 150)}px;width:{700 if story else 640}px;transform:rotate(10deg)">
<img class="abs" src="file://{A}cz-hero.png" style="left:{560 if story else 600}px;top:{o+(680 if story else 575)}px;width:{340 if story else 300}px;transform:rotate(-8deg)">
<div class="abs ar" style="right:48px;left:48px;top:{o+(1010 if story else 840)}px">
 <div style="font-weight:900;font-size:{104 if story else 92}px;line-height:1.05">الظهر هو<br>اللي يتكلم.</div>
 <div style="font-weight:600;font-size:{30 if story else 27}px;margin-top:14px;opacity:.85">3 تصاميم مطبوعة على الظهر · 4 ألوان · S إلى XL</div>
</div>'''
    return page(1080,H,f'linear-gradient(180deg,#0F1630 0%,{NAVY} 60%,#1A2547 100%)','#FFFFFF',body,story,LW)

def summer(story=False):
    o=150 if story else 0; H=1920 if story else 1350
    body=f'''
<div class="abs en ol" style="right:-20px;top:{o+120}px;font-weight:700;font-size:{170 if story else 150}px;line-height:.9;letter-spacing:-5px;color:rgba(142,192,234,.35);white-space:nowrap">SUMMER<br>BREEZE</div>
<img class="abs" src="file://{A}sb-palace.png" style="left:50%;transform:translateX(-50%);top:{o+(300 if story else 230)}px;width:{900 if story else 820}px">
<div class="abs ar" style="right:48px;top:{o+(880 if story else 715)}px;width:{760 if story else 620}px">
 <div style="font-weight:900;font-size:{72 if story else 64}px;line-height:1.1">كلاسيك على الظهر..<br><span style="color:{SKY}">وهدوء على الصدر</span></div>
 <div class="en" style="font-weight:700;font-size:17px;letter-spacing:4px;margin-top:16px;opacity:.75;text-align:right">NAVY · SKY BLUE · S–XL</div>
</div>
<img class="abs" src="file://{C}navy-front.png" style="left:30px;top:{o+(1120 if story else 880)}px;width:{270 if story else 225}px">
<img class="abs" src="file://{C}blue-front.png" style="left:{300 if story else 255}px;top:{o+(1135 if story else 895)}px;width:{270 if story else 225}px">'''
    return page(1080,H,f'linear-gradient(180deg,{NAVY} 0%,#1C2A52 100%)','#FFFFFF',body,story,LW)

def falling(story=False):
    o=150 if story else 0; H=1920 if story else 1350; INK='#0E4D8A'
    body=f'''
<div class="abs en ol" style="right:-10px;top:{o+(430 if story else 330)}px;font-weight:700;font-size:{150 if story else 130}px;line-height:.88;letter-spacing:-5px;color:rgba(14,77,138,.22);white-space:nowrap;text-align:right">FALLING<br>WITH<br>GRACE</div>
<div class="abs ar" style="right:48px;top:{o+(300 if story else 130)}px;width:720px">
 <div style="font-weight:900;font-size:{84 if story else 74}px;line-height:1.1">حتى الطيحة..<br>لها ستايل.</div>
 <div class="en" style="font-weight:700;font-size:17px;letter-spacing:4px;margin-top:14px;opacity:.75;text-align:right">WHITE · S–XL</div>
</div>
<img class="abs" src="file://{C}white-back.png" style="left:34px;top:{o+(290 if story else 120)}px;width:{300 if story else 260}px">
<img class="abs" src="file://{A}fw-hero.png" style="left:-30px;top:{o+(640 if story else 420)}px;width:{1160 if story else 1060}px;transform:rotate(5deg)">'''
    return page(1080,H,'linear-gradient(180deg,#DCEEFB 0%,#A9D0F0 100%)',INK,body,story,LB)

def citraz(story=False):
    o=150 if story else 0; H=1920 if story else 1350; GREEN='#1F4D33'; YEL='#D9A520'
    body=f'''
<div class="abs en ol" style="left:-14px;top:{o+120}px;font-weight:700;font-size:{230 if story else 200}px;line-height:.85;letter-spacing:-7px;color:rgba(31,77,51,.25);white-space:nowrap">CITRAZ<br>VIBES</div>
<img class="abs" src="file://{A}cz-hero.png" style="right:40px;top:{o+(240 if story else 170)}px;width:{720 if story else 620}px;transform:rotate(-5deg)">
<div class="abs ar" style="right:48px;left:48px;top:{o+(980 if story else 780)}px">
 <div style="font-weight:900;font-size:{80 if story else 70}px;line-height:1.1">حامض؟ لا..<br><span style="color:{YEL}">جريء.</span></div>
 <div class="en" style="font-weight:700;font-size:17px;letter-spacing:4px;margin-top:14px;opacity:.75;text-align:right">BEIGE · BOLD FAVOR · S–XL</div>
</div>
<img class="abs" src="file://{C}beige-back.png" style="left:30px;top:{o+(1060 if story else 830)}px;width:{330 if story else 290}px">'''
    return page(1080,H,'linear-gradient(180deg,#EFE6D0 0%,#E0D2B3 100%)',GREEN,body,story,LB)

STOCK=[('Navy','#1C2340','#fff',[12,9,14,14]),('Sky Blue','#79B3E6','#fff',[12,11,2,25]),('White','#F4F4F4','#222',[14,8,12,12]),('Beige','#D8C7A4','#222',[12,11,14,14])]
def sizes(story=False):
    o=150 if story else 0; H=1920 if story else 1350
    rows=''
    for n,c,t,q in STOCK:
        cells=''.join(f'<span class="q" style="{"border-style:dashed;color:#F6C453;border-color:#F6C453" if v<=3 else ""}">{s}{"<i>باقي "+str(v)+"</i>" if v<=3 else ""}</span>' for s,v in zip('S M L XL'.split(),q))
        rows+=f'<div class="r"><span class="sw" style="background:{c}"></span><b class="en">{n}</b><div class="qs">{cells}</div></div>'
    body=f'''
<div class="abs ar" style="right:48px;left:48px;top:{o+130}px">
 <div style="font-weight:900;font-size:{84 if story else 76}px;line-height:1.1">كل لون..<br>من S إلى XL</div>
 <div style="font-weight:600;font-size:{28 if story else 26}px;margin-top:12px;opacity:.8">قصّة أوفرسايز · الكميات محدودة</div>
</div>
<div class="abs" style="left:48px;right:48px;top:{o+(460 if story else 400)}px;direction:rtl">{rows}</div>
<div class="abs ar" style="left:48px;right:48px;top:{o+(900 if story else 760)}px;direction:rtl">
 <div style="font-weight:800;font-size:22px;opacity:.7;margin-bottom:10px">القياسات بالسنتيمتر (مسطّح)</div>
 <table class="sz"><tr><th></th><th>S</th><th>M</th><th>L</th><th>XL</th></tr>
 <tr><td>الطول</td><td>74</td><td>75</td><td>77</td><td>78</td></tr><tr><td>الصدر</td><td>62</td><td>63</td><td>64</td><td>67</td></tr><tr><td>الأكتاف</td><td>58</td><td>60</td><td>61</td><td>63</td></tr></table>
</div>'''
    extra=f'''.r{{display:flex;align-items:center;gap:18px;padding:{22 if story else 20}px 0;border-bottom:1px solid rgba(255,255,255,.18)}}
.sw{{width:34px;height:34px;border-radius:50%;flex:none}} .r b{{font-weight:700;font-size:24px;width:150px;text-align:left}}
.qs{{display:flex;gap:10px;margin-right:auto;direction:ltr}} .q{{font-family:Poppins;font-weight:700;font-size:22px;border:1.5px solid rgba(255,255,255,.5);border-radius:30px;padding:4px 16px;position:relative}}
.q i{{position:absolute;left:50%;transform:translateX(-50%);top:-26px;font-style:normal;font-family:Cairo;font-weight:800;font-size:15px;white-space:nowrap;color:#F6C453}}
.sz{{border-collapse:collapse;width:100%;font-family:Poppins;font-weight:500;font-size:24px}} .sz td,.sz th{{padding:8px 6px;text-align:center;border-bottom:1px solid rgba(255,255,255,.18)}} .sz td:first-child,.sz th:first-child{{font-family:Cairo;font-weight:700;text-align:right}} .sz th{{font-weight:700;opacity:.7}}'''
    return page(1080,H,f'linear-gradient(180deg,#0F1630 0%,{NAVY} 100%)','#FFFFFF',body,story,LW,extra)

def shot(n,html,H):
    os.makedirs('out2',exist_ok=True); open(f'out2/{n}.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/out2/{n}.html');await pg.waitForTimeout(900);await pg.screenshot({{path:'out2/{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
if __name__=='__main__':
    which=sys.argv[1:] or ['cover','summer','falling','citraz','sizes']
    F={'cover':cover,'summer':summer,'falling':falling,'citraz':citraz,'sizes':sizes}
    for i,k in enumerate(['cover','summer','falling','citraz','sizes']):
        if k in which:
            shot(f'974-drop01-{i+1}-{k}',F[k](),1350)
            if '--story' in sys.argv or True: shot(f'974-drop01-story-{k}',F[k](True),1920)
