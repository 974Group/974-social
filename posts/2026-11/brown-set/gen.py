# Brown Edition goggles + matching brown / beige face masks. 19 Nov 2026 (for 16:30)
import subprocess, sys, os
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/brown-set/'
G = '/home/claude/974-social/reels/2026-11/src/g_brown.png'
MB = '/home/claude/974-social/posts/2026-11/face-mask/src/cut/brown.png'
MG = '/home/claude/974-social/posts/2026-11/face-mask/src/cut/beige.png'
MARK = '/home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'
BR = '#5A3A26'; BRD = '#3B2417'; SAND = '#E9D9BF'; CREAM = '#F6EEDF'; M = '#720842'
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}'''


def page(story):
    H = 1920 if story else 1350
    o = 210 if story else 0
    k = 1.08 if story else 1.0
    # dune waves (svg) behind the goggles
    dunes = f'''<svg viewBox="0 0 1080 900" preserveAspectRatio="xMidYMin slice" style="position:absolute;left:0;top:{o+(560 if story else 430)}px;width:1080px;height:{H-o-(560 if story else 430)}px">
<path d="M0,170 C180,90 330,230 540,150 C750,70 900,190 1080,120 L1080,900 L0,900 Z" fill="#DCC6A2"/>
<path d="M0,250 C200,190 380,300 600,240 C800,185 930,270 1080,230 L1080,900 L0,900 Z" fill="#CFB68E"/></svg>'''
    gw = 900 if story else 820
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;position:relative;overflow:hidden;font-family:Cairo;color:{BRD};
background:linear-gradient(180deg,{CREAM} 0%,{SAND} 100%)}}
.top{{position:absolute;left:54px;right:54px;top:{o+44}px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:{int(42*k)}px}}
.top span{{font-family:Poppins;font-weight:700;font-size:{int(17*k)}px;letter-spacing:5px;color:{BR}}}
.h{{position:absolute;right:54px;left:54px;top:{o+(120 if story else 112)}px;text-align:right;direction:rtl}}
.h h1{{font-weight:900;font-size:{int(76*k)}px;line-height:1.1}}
.h h1 em{{font-style:normal;color:{BR}}}
.h p{{font-weight:700;font-size:{int(26*k)}px;color:{BR};margin-top:8px}}
.g{{position:absolute;left:{(1080-gw)//2}px;top:{o+(300 if story else 272)}px;width:{gw}px;filter:drop-shadow(0 30px 30px rgba(59,36,23,.35))}}
.feat{{position:absolute;left:54px;right:54px;top:{o+(925 if story else 845)}px;display:flex;justify-content:center;gap:10px;direction:rtl;flex-wrap:wrap}}
.feat div{{background:rgba(255,255,255,.75);border-radius:40px;padding:5px 18px 7px;font-weight:800;font-size:{int(20*k)}px}}
.gp{{position:absolute;left:54px;top:{o+(150 if story else 140)}px;background:{BRD};color:{CREAM};border-radius:20px;padding:4px 22px 9px;font-family:Poppins;font-weight:900;font-size:{int(42*k)}px;box-shadow:5px 5px 0 rgba(59,36,23,.25)}}
.gp small{{font-family:Cairo;font-size:.45em;font-weight:800}}
.set{{position:absolute;left:54px;right:54px;top:{o+(1010 if story else 925)}px;height:{int(280*k)}px;background:{CREAM};border-radius:30px;box-shadow:0 14px 30px rgba(59,36,23,.16);border:2px solid rgba(90,58,38,.15)}}
.set .t{{position:absolute;right:30px;top:24px;text-align:right;direction:rtl;width:{int(380*k)}px}}
.set .t b{{display:block;font-weight:900;font-size:{int(38*k)}px;line-height:1.15}}
.set .t span{{display:block;font-weight:700;font-size:{int(21*k)}px;color:{BR};margin-top:6px;line-height:1.4}}
.set .t i{{display:inline-block;font-style:normal;margin-top:12px;background:{BR};color:#fff;border-radius:30px;padding:3px 18px 6px;font-weight:900;font-size:{int(24*k)}px}}
.set .t i em{{font-style:normal;font-family:Poppins}}
.m{{position:absolute;top:18px;width:{int(190*k)}px;text-align:center}}
.m img{{height:{int(205*k)}px;filter:drop-shadow(0 10px 12px rgba(59,36,23,.3))}}
.m div{{font-weight:800;font-size:{int(19*k)}px;margin-top:-4px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{250 if story else 26}px}}
{payfoot.css(1.12 if story else 1.0)}
</style></head><body>
{dunes}
<div class="top"><img src="file://{MARK}"><span>974 GUARDS · BROWN EDITION</span></div>
<div class="h"><h1>بني <em>بلون البر</em></h1><p>عدستين مغناطيس · وحدة للشمس ووحدة لليل والغبار</p></div>
<div class="gp">319 <small>ر.ق</small></div>
<img class="g" src="file://{G}">
<div class="feat"><div>ضد الضباب</div><div>تحمي من الغبار والرمل</div><div>تبدّل العدسة بيدك في ثواني</div></div>
<div class="set">
  <div class="t"><b>كمّل اللوك 👌</b><span>تحتاج ماسك راكب مع النظارة؟<br>عندنا البني والبيج</span><i>الماسك بـ <em>39</em> ر.ق</i></div>
  <div class="m" style="left:30px"><img src="file://{MG}"><div>بيج</div></div>
  <div class="m" style="left:{30+int(205*k)}px"><img src="file://{MB}"><div>بني</div></div>
</div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, Hh):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{Hh}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    os.makedirs(D + 'out', exist_ok=True)
    shot(page(False), D + 'out/974-brown-set-post.png', 1350)
    shot(page(True), D + 'out/974-brown-set-story.png', 1920)
    print('ok')
