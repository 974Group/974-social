# Trail Loop (Apple Watch) — post + story, 14 Nov 2026 18:30. Only in-stock colours, all facing the same way.
import subprocess, sys, math
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/trail-loop/'
S = D + 'src/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
INK = '#1F2A24'; ACC = '#E86A1A'
COLS = ['2025-black-natural', '2025-green-natural', '2025-blue-natural', '2024-green-grey',
        '2025-black-black', '2025-green-black', '2025-blue-black', 'white-green']
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}'''


def topo(W, H):
    paths = ''
    for k in range(26):
        y0 = -80 + k * (H + 160) / 26
        pts = []
        for x in range(-20, W + 40, 20):
            y = y0 + 38 * math.sin(x / 170 + k * .55) + 22 * math.sin(x / 63 + k * 1.3)
            pts.append(f'{x},{y:.1f}')
        paths += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#5E6B55" stroke-opacity=".13" stroke-width="1.6"/>'
    return f'<svg class="topo" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{paths}</svg>'


def page(story):
    W, H = 1080, (1920 if story else 1350)
    o = 230 if story else 0
    cw, gap = 236, 12
    bh = int(cw * 968 / 827)
    x0 = (W - (4 * cw + 3 * gap)) // 2
    gy = o + (330 if not story else 420)
    rowh = bh + (14 if not story else 40)
    cells = ''
    for n, f in enumerate(COLS):
        r, c = divmod(n, 4)
        cells += f'<img class="w" src="file://{S}{f}-c.png" style="left:{x0 + c*(cw+gap)}px;top:{gy + r*rowh}px;width:{cw}px">'
    after = gy + 2 * rowh
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;font-family:Cairo;color:{INK};position:relative;overflow:hidden;background:linear-gradient(170deg,#EEEDE6 0%,#E3E5DA 55%,#ECE9E2 100%)}}
.topo{{position:absolute;left:0;top:0}}
.top{{position:absolute;left:48px;right:48px;top:{44 if not story else o-10}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px}}
.h{{position:absolute;left:48px;right:48px;top:{o+(110 if not story else 70)}px;direction:rtl;display:flex;justify-content:space-between;align-items:flex-end}}
.h .r b{{display:block;font-weight:900;font-size:{56 if not story else 66}px;line-height:1.15}}
.h .r b em{{font-style:normal;color:{ACC}}}
.h .r i{{display:block;font-style:normal;font-weight:700;font-size:{24 if not story else 29}px;opacity:.75;margin-top:4px}}
.h .en{{font-family:Poppins;font-weight:700;font-size:{64 if not story else 74}px;line-height:.95;letter-spacing:-1.5px;direction:ltr;text-align:left}}
.h .en small{{display:block;font-weight:500;font-size:.3em;letter-spacing:4px;opacity:.6;margin-top:6px}}
.w{{position:absolute;filter:drop-shadow(0 14px 16px rgba(30,40,30,.22))}}
.chips{{position:absolute;left:48px;right:48px;top:{after+(4 if not story else 24)}px;display:flex;justify-content:center;gap:{10 if not story else 8}px;direction:rtl;flex-wrap:nowrap}}
.chips span{{background:#fff;border-radius:30px;padding:4px 18px 8px;font-weight:800;font-size:{20 if not story else 22}px;box-shadow:0 6px 16px rgba(30,40,30,.08)}}
.chips span.bo{{background:transparent;box-shadow:none;border:1.5px dashed currentColor;opacity:.75}}
.foot{{position:absolute;left:48px;right:48px;top:{after+(70 if not story else 112)}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.deal{{font-weight:900;font-size:{30 if not story else 37}px}} .deal b{{font-family:Poppins;color:{ACC}}}
.deal i{{display:block;font-style:normal;font-weight:700;font-size:{19 if not story else 23}px;opacity:.7}}
.pill{{background:{INK};color:#fff;border-radius:40px;padding:6px 28px 10px;font-weight:900;font-size:{36 if not story else 44}px;white-space:nowrap}}
.pill b{{font-family:Poppins}} .pill s{{font-family:Poppins;font-weight:500;font-size:.55em;opacity:.6;margin-right:10px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12)}
</style></head><body>{topo(W,H)}
<div class="top"><img src="file://{LOGO}"><span>APPLE WATCH · TRAIL LOOP</span></div>
<div class="h"><div class="r"><b>خفيف.. <em>ويتحمّل</em></b><i>للتمرين والطلعات وكل يوم</i></div>
<div class="en">Trail<br>Loop<small>NYLON WEAVE</small></div></div>
{cells}
<div class="chips"><span>نايلون منسوج يتنفّس</span><span>يتعدّل بسحبة</span><span style="direction:ltr;font-family:Poppins;font-weight:700">44 · 45 · 46 · 49mm</span><span class="bo">سير فقط · بدون الساعة</span></div>
<div class="foot"><div class="deal">أي ٣ سيور بـ <b>220</b> ر.ق<i>اخلط الألوان على كيفك</i></div><div class="pill"><b>79</b> ر.ق<s>99</s></div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(page(False), D + 'out/974-trail-loop-post.png', 1350)
    shot(page(True), D + 'out/974-trail-loop-story.png', 1920)
    print('ok')
