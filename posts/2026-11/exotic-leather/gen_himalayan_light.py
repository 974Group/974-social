# Himalayan croc Whoop band — light design (owner: not dark, band must stand out). 19 Nov 2026
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/exotic-leather/'
FRONT = D + 'cut/himalayan.png'
ANGLE = '/home/claude/974-social/products/whoop5-exotic-leather-nov26/cut/himalayan-2-angle.png'
MARK = '/home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'
M = '#720842'; DK = '#51022D'; INK = '#2B2420'; TAUPE = '#7A6553'; GOLD = '#B08A3E'
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}'''


def page(story):
    H = 1920 if story else 1350
    o = 200 if story else 0
    k = 1.08 if story else 1.0
    band_h = 860 if story else 810
    band_top = o + (300 if story else 250)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;color:{INK};
background:radial-gradient(ellipse 700px 900px at 30% {45 if story else 50}%,#F6F0E9 0%,rgba(246,240,233,0) 70%),linear-gradient(165deg,#EFE6DC 0%,#D9C9B8 55%,#C7B39E 100%)}}
.ring{{position:absolute;border:2px solid rgba(122,101,83,.18);border-radius:50%}}
.top{{position:absolute;left:56px;right:56px;top:{o+48}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:{int(44*k)}px}}
.top span{{font-family:Poppins;font-weight:700;font-size:{int(17*k)}px;letter-spacing:5px;color:{TAUPE}}}
.band{{position:absolute;left:{70 if story else 60}px;top:{band_top}px;height:{band_h}px;filter:drop-shadow(18px 30px 30px rgba(60,40,25,.32))}}
.txt{{position:absolute;right:56px;top:{o+(300 if story else 250)}px;width:{560 if story else 560}px;text-align:right;direction:rtl}}
.eb{{font-family:Poppins;font-weight:700;font-size:{int(18*k)}px;letter-spacing:4px;color:{M};direction:ltr;text-align:right}}
h1{{font-weight:900;font-size:{int(60*k)}px;line-height:1.15;margin-top:8px}}
h1 em{{font-style:normal;color:{M}}}
.sub{{font-weight:700;font-size:{int(25*k)}px;color:{TAUPE};margin-top:12px;line-height:1.45}}
.detail{{position:absolute;right:56px;top:{o+(690 if story else 640)}px;width:{int(500*k)}px;height:{int(330*k)}px;border-radius:28px;background:#FBF8F4;overflow:hidden;box-shadow:0 18px 36px rgba(60,40,25,.18)}}
.detail img{{position:absolute;right:-40px;top:-60px;width:{int(560*k)}px}}
.detail span{{position:absolute;left:18px;bottom:16px;background:rgba(43,36,32,.82);color:#fff;font-weight:800;font-size:{int(18*k)}px;border-radius:30px;padding:4px 16px 6px;direction:rtl}}
.chips{{position:absolute;right:56px;top:{o+(1070 if story else 1000)}px;display:flex;flex-wrap:wrap;justify-content:flex-start;gap:10px;width:{int(560*k)}px;direction:rtl}}
.chip{{background:rgba(255,255,255,.7);border:1.5px solid rgba(122,101,83,.35);border-radius:40px;padding:5px 18px 7px;font-weight:800;font-size:{int(20*k)}px}}
.chip b{{font-family:Poppins;color:{M}}}
.price{{position:absolute;left:{90 if story else 70}px;top:{o+(1185 if story else 1095)}px;background:{M};color:#fff;border-radius:22px;padding:4px 30px 10px;font-family:Poppins;font-weight:900;font-size:{int(54*k)}px;box-shadow:6px 6px 0 {DK}}}
.price small{{font-family:Cairo;font-size:.42em;font-weight:800}}
.pf{{position:absolute;left:28px;right:28px;bottom:{250 if story else 26}px}}
{payfoot.css(1.12 if story else 1.0)}
</style></head><body>
<div class="ring" style="left:-260px;top:{o+120}px;width:980px;height:980px"></div>
<div class="ring" style="left:-160px;top:{o+220}px;width:780px;height:780px"></div>
<div class="top"><img src="file://{MARK}"><span>EDITION X · LIMITED</span></div>
<img class="band" src="file://{FRONT}">
<div class="txt">
  <div class="eb">HIMALAYAN CROCODILE</div>
  <h1>جلد <em>هيمالايا</em><br>لونه يتكلم</h1>
  <div class="sub">أبيض كريمي مع طرف بنقشة التمساح الأصلية<br>كل قطعة نقشتها غير عن الثانية</div>
</div>
<div class="detail"><img src="file://{ANGLE}"><span>شوف التفاصيل عن قرب</span></div>
<div class="chips"><div class="chip">لـ <b>Whoop 5.0</b> و <b>MG</b></div><div class="chip">قفل معدني بشعار 974</div><div class="chip">إصدار محدود · <b>15</b> قطعة</div></div>
<div class="price">849 <small>ر.ق</small></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, Hh):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{Hh}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(page(False), D + 'out/974-himalayan-light-post.png', 1350)
    shot(page(True), D + 'out/974-himalayan-light-story.png', 1920)
    print('ok')
