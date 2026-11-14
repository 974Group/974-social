# Edition X — Genuine Crocodile (Whoop 5.0 / MG) — post + story, 14 Nov 2026
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/croc-edition-x/'
S = D + 'src/'
BOX = '/home/claude/974-social/posts/2026-11/exotic-leather/cut/box-closed.png'
BANDS = [('redwine', 'Red Wine', ''), ('tiffany', 'Tiffany', ''), ('grey', 'Grey', ''), ('pink', 'Pink', 'آخر قطعتين')]
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:300;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf)}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}'''
SILVER = 'background:linear-gradient(180deg,#FFFFFF 0%,#E9E9EE 38%,#A9A9B3 62%,#F2F2F5 100%);-webkit-background-clip:text;background-clip:text;color:transparent'
CHAMP = '#D8C3A1'


def page(story):
    W, H = 1080, (1920 if story else 1350)
    bgy = -120 if story else -340             # horizon of bg sits at ~1216 (story) / ~916 (post)
    hz = 1216 + bgy                         # floor line
    bw = 236 if not story else 240; gap = 14
    bh = int(bw * 1359 / 1153)
    x0 = (W - (4 * bw + 3 * gap)) // 2
    top_logo = 44 if not story else 230
    items = ''
    for i, (f, nm, tag) in enumerate(BANDS):
        x = x0 + i * (bw + gap)
        items += f'''<div class="b" style="left:{x}px;top:{hz-bh+18}px;width:{bw}px;height:{bh}px">
  <img class="main" src="file://{S}{f}-a-c.png"><img class="refl" src="file://{S}{f}-a-c.png"></div>
<div class="nm" style="left:{x}px;width:{bw}px;top:{hz+ (78 if not story else 100)}px"><span>{nm}</span>{f'<em>{tag}</em>' if tag else ''}</div>'''
    head_top = top_logo + (178 if not story else 250)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#050304 url(file://{S}bg-up.png) no-repeat center {bgy}px/1080px auto;font-family:Cairo;color:#fff;position:relative;overflow:hidden}}
.vig{{position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 30%,transparent 55%,rgba(0,0,0,.55) 100%)}}
.logo{{position:absolute;left:50%;transform:translateX(-50%);top:{top_logo}px;height:{150 if not story else 205}px;filter:drop-shadow(0 4px 14px rgba(0,0,0,.6))}}
.kick{{position:absolute;left:0;right:0;top:{head_top}px;text-align:center;font-family:Poppins;font-weight:500;font-size:{17 if not story else 21}px;letter-spacing:{9 if not story else 11}px;color:{CHAMP};direction:ltr}}
.kick:before,.kick:after{{content:'';display:inline-block;width:{60 if not story else 80}px;height:1px;background:{CHAMP};opacity:.6;vertical-align:middle;margin:0 18px 4px}}
h1{{position:absolute;left:0;right:0;top:{head_top+(30 if not story else 42)}px;text-align:center;font-weight:900;font-size:{74 if not story else 96}px;line-height:1.2;{SILVER};filter:drop-shadow(0 3px 10px rgba(0,0,0,.55))}}
.sub{{position:absolute;left:0;right:0;top:{head_top+(126 if not story else 168)}px;text-align:center;font-weight:600;font-size:{25 if not story else 31}px;color:#E9DED3;direction:rtl}}
.sub b{{font-family:Poppins;font-weight:500;color:#fff}}
.b{{position:absolute}}
.b .main{{position:absolute;left:0;top:0;width:100%;filter:drop-shadow(0 22px 22px rgba(0,0,0,.75))}}
.b .refl{{position:absolute;left:0;top:100%;width:100%;transform:scaleY(-1);transform-origin:top;margin-top:-6px;opacity:.28;filter:blur(1.5px);-webkit-mask-image:linear-gradient(to top,rgba(0,0,0,.9) 0%,transparent 42%);mask-image:linear-gradient(to top,rgba(0,0,0,.9) 0%,transparent 42%)}}
.nm{{position:absolute;text-align:center}}
.nm span{{display:block;font-family:Poppins;font-weight:500;font-size:{15 if not story else 18}px;letter-spacing:4px;text-transform:uppercase;color:#EDE6DD}}
.nm em{{display:inline-block;margin-top:6px;font-style:normal;font-weight:800;font-size:{15 if not story else 18}px;color:#1A0A10;background:{CHAMP};border-radius:20px;padding:0 12px 2px}}
.offer{{position:absolute;left:44px;right:44px;top:{hz+(148 if not story else 196)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl}}
.price{{display:flex;flex-direction:column;align-items:flex-start;direction:rtl}}
.price b{{font-family:Poppins;font-weight:700;font-size:{64 if not story else 84}px;line-height:1;{SILVER}}}
.price b small{{font-family:Cairo;font-weight:800;font-size:.42em}}
.price i{{font-style:normal;font-weight:700;font-size:{19 if not story else 24}px;color:#CFC4BA;margin-top:4px}}
.boxl{{display:flex;align-items:center;gap:16px;direction:rtl}}
.boxl img{{height:{82 if not story else 110}px;filter:drop-shadow(0 10px 14px rgba(0,0,0,.7))}}
.boxl div{{font-weight:700;font-size:{21 if not story else 27}px;line-height:1.35;color:#EDE6DD}}
.boxl div b{{font-family:Poppins;font-weight:700;letter-spacing:1px;color:{CHAMP}}}
.line{{position:absolute;left:44px;right:44px;top:{hz+(130 if not story else 172)}px;height:1px;background:linear-gradient(90deg,transparent,rgba(216,195,161,.45),transparent)}}
.cta{{position:absolute;left:0;right:0;top:{hz+(268 if not story else 352)}px;text-align:center;font-weight:700;font-size:{21 if not story else 27}px;color:#CFC4BA;direction:rtl}}
.cta em{{font-style:normal;color:#fff;font-weight:900}}
.pf{{position:absolute;left:28px;right:28px;bottom:{26 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12, text='#EDE6DD', label='#EDE6DD')}
</style></head><body><div class="vig"></div>
<img class="logo" src="file://{S}logo-silver.png">
<div class="kick">GENUINE CROCODILE</div>
<h1>جلد تمساح طبيعي</h1>
<div class="sub">سيور <b>Whoop 5.0</b> و <b>MG</b> · ٤ ألوان بكمية محدودة</div>
{items}
<div class="line"></div>
<div class="offer">
 <div class="boxl"><img src="file://{BOX}"><div>يوصلك في بوكس<br><b>EDITION X</b> الخاص</div></div>
 <div class="price"><b>600 <small>ر.ق</small></b><i>جلد طبيعي <span style="font-family:Poppins;direction:ltr;unicode-bidi:isolate">100%</span></i></div>
</div>
<div class="cta">علّق <em>«جلد»</em> ونرسل لك الرابط 📩</div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(page(False), D + 'out/974-croc-edition-x-post.png', 1350)
    shot(page(True), D + 'out/974-croc-edition-x-story.png', 1920)
    print('ok')
