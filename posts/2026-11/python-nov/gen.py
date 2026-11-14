# Python leather Whoop bands (new: White, Black · back in stock: Pink, Grey, Natural) — feminine + snake style. 14 Nov 2026
import subprocess, sys, math
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C = '/home/claude/974-social/posts/2026-11/exotic-leather/cut/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
INK = '#3A1424'; ROSE = '#C9708E'; GOLD = '#B88A3E'
BANDS = [('pink-python', 'Pink', 'رجع متوفر'), ('white-python', 'White', 'جديد'), ('black-python', 'Black', 'جديد'),
         ('grey-python', 'Grey', 'رجع متوفر'), ('natural-python', 'Natural', 'رجع متوفر')]
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Lora';font-style:italic;font-weight:400 700;src:url(file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf)}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}'''


def scales(W, H):
    # python-scale texture: rows of rounded diamonds, very faint
    s = ''
    w, h = 54, 40
    for r in range(int(H / (h / 2)) + 2):
        for c in range(int(W / w) + 2):
            x = c * w + (w / 2 if r % 2 else 0); y = r * h / 2
            s += f'<path d="M{x:.0f},{y-h/2:.0f} Q{x+w/2:.0f},{y:.0f} {x:.0f},{y+h/2:.0f} Q{x-w/2:.0f},{y:.0f} {x:.0f},{y-h/2:.0f}Z"/>'
    return f'<svg class="scales" width="{W}" height="{H}"><g fill="none" stroke="#B2627F" stroke-opacity=".10" stroke-width="1.4">{s}</g></svg>'


def snake(W, y0, amp, story):
    pts = []
    for x in range(-40, W + 60, 20):
        pts.append(f'{x},{y0 + amp*math.sin((x/W)*2*math.pi*1.15 + .4):.1f}')
    d = 'M' + ' L'.join(pts)
    return f'''<svg class="snake" width="{W}" height="2000"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#E7C27A"/><stop offset=".5" stop-color="{GOLD}"/><stop offset="1" stop-color="#E7C27A"/></linearGradient></defs>
<path d="{d}" fill="none" stroke="url(#g)" stroke-width="{10 if not story else 12}" stroke-linecap="round" opacity=".55"/>
<path d="{d}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 14" stroke-linecap="round" opacity=".7"/></svg>'''


def page(story):
    W, H = 1080, (1920 if story else 1350)
    o = 230 if story else 0
    bw = 150 if not story else 160
    bh = int(bw * 1600 / 610)
    gap = 34 if not story else 30
    x0 = (W - (5 * bw + 4 * gap)) // 2
    base = o + (430 if not story else 520)
    amp = 46 if not story else 52
    items = ''
    for i, (f, nm, tag) in enumerate(BANDS):
        cx = x0 + i * (bw + gap)
        dy = amp * math.sin(((cx + bw / 2) / W) * 2 * math.pi * 1.15 + .4)
        y = base + dy
        cls = 'new' if tag == 'جديد' else 'back'
        items += f'''<div class="b" style="left:{cx}px;top:{y:.0f}px;width:{bw}px"><img src="file://{C}{f}.png" style="width:{bw}px;height:{bh}px">
<span class="nm">{nm}</span><em class="{cls}">{tag}</em></div>'''
    sy = base + bh * .45
    after = base + bh + amp + (90 if not story else 110)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;font-family:Cairo;color:{INK};position:relative;overflow:hidden;
background:radial-gradient(800px 600px at 85% 5%,#F6D2DE 0%,transparent 65%),radial-gradient(900px 700px at 0% 100%,#EFD9CF 0%,transparent 65%),#F8ECEF}}
.scales{{position:absolute;left:0;top:0}}
.snake{{position:absolute;left:0;top:0}}
.logo{{position:absolute;left:52px;top:{o+(44 if not story else -10)}px;height:44px}}
.kick{{position:absolute;right:52px;top:{o+(56 if not story else 2)}px;font-family:Poppins;font-weight:500;font-size:16px;letter-spacing:5px;color:{ROSE}}}
.t1{{position:absolute;left:0;right:0;top:{o+(88 if not story else 46)}px;text-align:center;font-family:Lora;font-style:italic;font-weight:600;font-size:{150 if not story else 176}px;line-height:1.3;padding-bottom:12px;
background:linear-gradient(100deg,#B85A7B 0%,#D98EA8 40%,{GOLD} 75%,#D3A55A 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.t2{{position:absolute;left:0;right:0;top:{o+(268 if not story else 262)}px;text-align:center;direction:rtl;font-weight:900;font-size:{46 if not story else 54}px}}
.t2 i{{font-style:normal;color:{ROSE}}}
.t3{{position:absolute;left:0;right:0;top:{o+(336 if not story else 342)}px;text-align:center;direction:rtl;font-weight:700;font-size:{23 if not story else 27}px;opacity:.7}}
.t3 b{{font-family:Poppins;font-weight:500}}
.b{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 18px 18px rgba(80,20,40,.25))}}
.nm{{font-family:Poppins;font-weight:700;font-size:{17 if not story else 19}px;letter-spacing:2px;text-transform:uppercase;margin-top:12px}}
.b em{{font-style:normal;font-weight:800;font-size:{15 if not story else 17}px;border-radius:20px;padding:0 12px 2px;margin-top:6px}}
.b em.new{{background:{INK};color:#fff}} .b em.back{{background:#fff;color:{ROSE};box-shadow:0 0 0 1.5px {ROSE} inset}}
.foot{{position:absolute;left:52px;right:52px;top:{after}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.boxl{{display:flex;align-items:center;gap:14px}} .boxl img{{height:{78 if not story else 96}px;filter:drop-shadow(0 10px 12px rgba(0,0,0,.25))}}
.boxl div{{font-weight:700;font-size:{21 if not story else 25}px;line-height:1.35}} .boxl b{{font-family:Poppins;letter-spacing:1px;color:{GOLD}}}
.price{{background:{INK};color:#F8ECEF;border-radius:40px;padding:6px 32px 10px;font-weight:900;font-size:{38 if not story else 46}px;white-space:nowrap}} .price b{{font-family:Poppins}}
.cta{{position:absolute;left:0;right:0;top:{after+(105 if not story else 130)}px;text-align:center;direction:rtl;font-weight:700;font-size:{22 if not story else 27}px}}
.cta em{{font-style:normal;color:{ROSE};font-weight:900}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12)}
</style></head><body>{scales(W,H)}{snake(W, sy, amp, story)}
<img class="logo" src="file://{LOGO}"><div class="kick">GENUINE PYTHON · EDITION X</div>
<div class="t1">Python</div>
<div class="t2">جلد بايثون طبيعي.. <i>ناعم وجريء</i></div>
<div class="t3">سيور لـ <b>Whoop 5.0</b> و <b>MG</b> · لونين جداد ورجعت ٣ ألوان</div>
{items}
<div class="foot"><div class="boxl"><img src="file://{C}box-closed.png"><div>يوصلك في بوكس<br><b>EDITION X</b></div></div><div class="price"><b>299</b> ر.ق</div></div>
<div class="cta">علّقي <em>«جلد»</em> ونرسل لك الرابط 📩</div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    D = '/home/claude/974-social/posts/2026-11/python-nov/'
    shot(page(False), D + '974-python-post.png', 1350)
    shot(page(True), D + '974-python-story.png', 1920)
    print('ok')
