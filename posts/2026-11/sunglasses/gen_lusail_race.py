# LUSAIL sunglasses — standalone "race day" design (post + story). 18 Nov 2026, for T100 expo period.
import subprocess, sys, os
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/sunglasses/'
C = D + 'cut/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
M = '#720842'; DK = '#51022D'; SL = '#4D5566'; INK = '#1A1E26'
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}'''


def page(story):
    H = 1920 if story else 1350
    o = 210 if story else 0          # story safe-zone offset
    k = 1.1 if story else 1.0
    hero_w = 860 if story else 800
    hero_top = o + (410 if story else 300)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;color:{INK};
background:linear-gradient(180deg,#F7F8FA 0%,#E6E9EE 62%,#D5DAE2 100%)}}
.lanes{{position:absolute;left:-200px;right:-200px;top:{o+(640 if story else 500)}px;height:{460 if story else 340}px;transform:skewY(-8deg);
background:repeating-linear-gradient(180deg,transparent 0 {int(96*k)}px,rgba(77,85,102,.16) {int(96*k)}px {int(100*k)}px)}}
.wm{{position:absolute;left:0;right:0;top:{o+(300 if story else 200)}px;text-align:center;font-family:Poppins;font-weight:900;font-size:{int(300*k)}px;letter-spacing:-8px;line-height:1;
color:transparent;-webkit-text-stroke:3px rgba(77,85,102,.22)}}
.top{{position:absolute;left:48px;right:48px;top:{o+44}px;display:flex;justify-content:space-between;align-items:center}}
.logo{{background:{M};border-radius:18px;padding:12px 18px;display:flex}}
.logo img{{height:{int(34*k)}px}}
.coord{{font-family:Poppins;font-weight:700;font-size:{int(20*k)}px;letter-spacing:6px;color:{SL}}}
.name{{position:absolute;left:56px;top:{o+(150 if story else 130)}px;font-family:Poppins;font-weight:900;font-size:{int(118*k)}px;letter-spacing:-3px;line-height:1;color:{INK}}}
.tag{{position:absolute;left:60px;top:{o+(150 if story else 130)+int(124*k)}px;font-family:Poppins;font-weight:700;font-size:{int(22*k)}px;letter-spacing:8px;color:{M}}}
.head{{position:absolute;right:56px;top:{o+(160 if story else 138)}px;text-align:right;direction:rtl;font-weight:900;font-size:{int(46*k)}px;line-height:1.25}}
.head small{{display:block;font-weight:700;font-size:{int(24*k)}px;color:{SL};margin-top:4px}}
.hero{{position:absolute;left:{(1080-hero_w)//2 + (10 if story else 20)}px;top:{hero_top}px;width:{hero_w}px;filter:drop-shadow(0 40px 40px rgba(26,30,38,.28))}}
.bib{{position:absolute;left:56px;top:{o+(1090 if story else 840)}px;background:#fff;border-radius:22px;padding:14px 22px 16px;box-shadow:0 10px 24px rgba(26,30,38,.14);border-top:{int(10*k)}px solid {M};transform:rotate(-3deg)}}
.bib .t{{font-family:Poppins;font-weight:700;font-size:{int(13*k)}px;letter-spacing:4px;color:{SL}}}
.bib .n{{font-family:Poppins;font-weight:900;font-size:{int(56*k)}px;line-height:1;color:{INK}}}
.bib .s{{font-family:Poppins;font-weight:700;font-size:{int(15*k)}px;letter-spacing:3px;color:{M};margin-top:2px}}
.ph{{position:absolute;right:56px;top:{o+(1000 if story else 860)}px;background:{INK};color:#fff;border-radius:24px;padding:14px 18px 12px;direction:rtl;text-align:center}}
.ph b{{display:block;font-weight:900;font-size:{int(22*k)}px;margin-bottom:8px}}
.ph .row{{display:flex;align-items:center;gap:10px;direction:ltr}}
.ph .l{{background:#fff;border-radius:14px;padding:8px 10px;text-align:center}}
.ph .l img{{height:{int(52*k)}px;display:block}}
.ph .l span{{display:block;font-size:{int(15*k)}px;font-weight:800;color:{INK};direction:rtl}}
.ph .arr{{font-size:{int(26*k)}px;color:#C9A24B;font-weight:900}}
.chips{{position:absolute;left:48px;right:48px;top:{o+(1220 if story else 1075)}px;display:flex;justify-content:center;gap:{int(12*k)}px;direction:rtl}}
.chip{{background:#fff;border:2px solid rgba(77,85,102,.25);border-radius:40px;padding:{int(8*k)}px {int(20*k)}px;font-weight:800;font-size:{int(22*k)}px;white-space:nowrap}}
.chip em{{font-style:normal;font-family:Poppins;font-weight:900;color:{M}}}
.price{{position:absolute;left:56px;top:{o+(1030 if story else 885)}px;display:flex;flex-direction:column;align-items:flex-start;align-items:center;gap:18px;direction:rtl}}
.price .p{{background:{M};color:#fff;border-radius:22px;padding:4px 30px 8px;font-family:Poppins;font-weight:900;font-size:{int(54*k)}px;direction:ltr;box-shadow:6px 6px 0 {DK}}}
.price .p small{{font-family:Cairo;font-size:.45em;font-weight:800}}
.price .u{{direction:rtl;font-weight:800;font-size:{int(22*k)}px;color:{SL};line-height:1.3}}
.pf{{position:absolute;left:28px;right:28px;bottom:{250 if story else 26}px}}
{payfoot.css(1.12 if story else 1.0)}
</style></head><body>
<div class="lanes"></div>
<div class="wm">LUSAIL</div>
<div class="top"><div class="logo"><img src="file://{LOGO}"></div><div class="coord">25.42° N · QATAR</div></div>
<div class="name">LUSAIL</div>
<div class="tag">MADE TO LEAD</div>
<div class="head">33 جرام..<br>ما تحس فيها<small>للجري والدراجة والترايثلون</small></div>
<img class="hero" src="file://{C}lusail-hero.png">
<div class="ph"><b>تغمق بروحها في الشمس</b><div class="row"><div class="l"><img src="file://{C}lusail-clear.png"><span>بالظل</span></div><div class="arr">→</div><div class="l"><img src="file://{C}lusail-dark.png"><span>بالشمس</span></div></div></div>
<div class="chips"><div class="chip">عدسة <em>Photochromic</em></div><div class="chip">ضد الصدمات</div><div class="chip">تتعدّل <em>4</em> وضعيات</div></div>
<div class="price"><div class="u">جاهزة ليوم السباق 🏁</div><div class="p">319 <small>ر.ق</small></div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    os.makedirs(D + 'out/race', exist_ok=True)
    shot(page(True), D + 'out/race/974-lusail-race-story.png', 1920)
    shot(page(False), D + 'out/race/974-lusail-race-post.png', 1350)
    print('ok')
