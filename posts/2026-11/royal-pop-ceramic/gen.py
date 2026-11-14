# Royal Pop X Swatch bio-ceramic bands — post + story, 14 Nov 2026 14:30
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/royal-pop-ceramic/'
S = D + 'src/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
INK = '#2A1A22'
ORDER = [0, 1, 5, 2, 7, 6, 4, 3]   # black, white, light green, green, light pink, pink, blue, navy
GLOW = ['#9a9a9a', '#ffffff', '#d9f2b0', '#7ed38a', '#ffd6dc', '#ff9cc0', '#8fb0ff', '#6f7fd6']
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}'''


def page(story):
    W, H = 1080, (1920 if story else 1350)
    o = 230 if story else 0
    cw, gap = 240, 14
    bh = int(cw * 0.92 * 1726 / 1497)
    x0 = (W - (4 * cw + 3 * gap)) // 2
    gy = o + (395 if not story else 470)
    rowh = bh + (34 if not story else 60)
    cells = ''
    for n, k in enumerate(ORDER):
        r, c = divmod(n, 4)
        x = x0 + c * (cw + gap); y = gy + r * rowh
        cells += f'''<div class="c" style="left:{x}px;top:{y}px;width:{cw}px;height:{bh}px">
 <div class="gl"></div>
 <img src="file://{S}k{k}.png" style="width:{int(cw*0.92)}px"></div>'''
    after = gy + 2 * rowh
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;font-family:Cairo;color:{INK};position:relative;overflow:hidden;
background:radial-gradient(700px 520px at 92% 8%,#FFE1EC 0%,transparent 70%),radial-gradient(640px 520px at 0% 40%,#E3F6D6 0%,transparent 70%),radial-gradient(700px 600px at 100% 85%,#DCE6FF 0%,transparent 70%),#F7F4F5}}
.top{{position:absolute;left:48px;right:48px;top:{o+44 if not story else o-10}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px}}
.h{{position:absolute;right:48px;left:48px;top:{o+(120 if not story else 70)}px;direction:rtl;text-align:center}}
.en{{font-family:Poppins;font-weight:700;font-size:{96 if not story else 120}px;line-height:1;letter-spacing:-2px;direction:ltr;
background:linear-gradient(90deg,#3B5BDB 0%,#2FB45A 30%,#E8458B 62%,#1E1E1E 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.ar{{font-weight:900;font-size:{50 if not story else 62}px;line-height:1.25;margin-top:{10 if not story else 18}px}}
.ar em{{font-style:normal;color:#C2185B}}
.s{{font-weight:700;font-size:{24 if not story else 30}px;opacity:.75;margin-top:6px}} .s b{{font-family:Poppins;font-weight:500}}
.c{{position:absolute;display:flex;align-items:center;justify-content:center}}
.c .gl{{position:absolute;left:14%;right:14%;bottom:-2%;height:9%;border-radius:50%;background:rgba(60,30,45,.22);filter:blur(10px)}}
.c img{{position:relative;filter:drop-shadow(0 16px 18px rgba(40,20,30,.22))}}
.feat{{position:absolute;left:48px;right:48px;top:{after+(6 if not story else 20)}px;display:flex;justify-content:center;gap:12px;direction:rtl}}
.feat span{{background:#fff;border-radius:30px;padding:4px 20px 8px;font-weight:800;font-size:{21 if not story else 26}px;box-shadow:0 6px 16px rgba(60,30,50,.08)}}
.foot{{position:absolute;left:48px;right:48px;top:{after+(78 if not story else 120)}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.pill{{background:{INK};color:#fff;border-radius:40px;padding:6px 30px 10px;font-weight:900;font-size:{34 if not story else 42}px;white-space:nowrap}} .pill b{{font-family:Poppins}}
.cta{{font-weight:700;font-size:{24 if not story else 30}px}} .cta b{{font-family:Poppins;color:#51022D}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12)}
</style></head><body>
<div class="top"><img src="file://{LOGO}"><span>BIO CERAMIC · 8 COLOURS</span></div>
<div class="h"><div class="en">Royal Pop</div>
<div class="ar">٨ ألوان.. <em>واختار مزاجك</em></div>
<div class="s">سيور بايو سيراميك لساعة <b>Swatch × AP Royal Pop</b></div></div>
{cells}
<div class="feat"><span>أخف من البلاستيك</span><span>تقاوم الخدوش</span><span>قفل ستيل</span></div>
<div class="foot"><div class="cta">اطلبه من <b>974group.net</b> 🛒</div><div class="pill"><b>249</b> ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(page(False), D + 'out/974-royal-pop-post.png', 1350)
    shot(page(True), D + 'out/974-royal-pop-story.png', 1920)
    print('ok')
