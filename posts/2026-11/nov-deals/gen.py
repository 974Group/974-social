# November daily deals — announcement + day 1 (iPhone 18 cases 40%), post + story each. 14 Nov 2026 18:00
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/nov-deals/'
S = D + 'src/'
LOGOW = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
M = '#720842'; DK = '#3A0222'; LIME = '#D8FF3C'; GOLD = '#C9A24B'
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'PoppinsB';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}'''


def tape(top, rot, txt, bg=LIME, fg=DK, H=None):
    s = (txt + '  ✦  ') * 12
    return f'<div class="tape" style="top:{top}px;transform:rotate({rot}deg);background:{bg};color:{fg}"><span>{s}</span></div>'


def base(story, body):
    H = 1920 if story else 1350
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;font-family:Cairo;color:#fff;position:relative;overflow:hidden;
background:radial-gradient(900px 700px at 80% 20%,#9C0B5A 0%,transparent 60%),radial-gradient(800px 700px at 0% 100%,#4A022B 0%,transparent 60%),{M}}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.10) 2.2px,transparent 2.6px);background-size:22px 22px;-webkit-mask-image:linear-gradient(160deg,#000 0%,transparent 55%);mask-image:linear-gradient(160deg,#000 0%,transparent 55%)}}
.tape{{position:absolute;left:-120px;width:1320px;height:58px;display:flex;align-items:center;overflow:hidden;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.tape span{{white-space:nowrap;font-family:PoppinsB;font-weight:900;font-size:26px;letter-spacing:2px}}
.logo{{position:absolute;height:46px}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12, text='#fff', label='#fff')}
.big{{font-family:PoppinsB;font-weight:900;line-height:.8;letter-spacing:-6px;direction:ltr}}
.out{{color:transparent;-webkit-text-stroke:4px {LIME}}}
.khasm{{display:inline-block;background:{LIME};color:{DK};font-weight:900;border-radius:26px;transform:rotate(-6deg);box-shadow:8px 8px 0 {DK}}}
.sticker{{position:absolute;width:190px;height:190px;border-radius:50%;background:{GOLD};color:{DK};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(12deg);box-shadow:6px 6px 0 {DK};font-weight:900;line-height:1.1}}
</style></head><body><div class="dots"></div>{body}<div class="pf">{payfoot.html()}</div></body></html>'''


def announce(story):
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS</div>
<div style="position:absolute;left:0;right:0;top:{o+(120 if not story else 150)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(46*k)}px;color:{LIME}">موسم الخصومات بدأ 🔥</div>
  <div style="font-weight:900;font-size:{int(104*k)}px;line-height:1.1;margin-top:6px">كل يوم..<br><span class="khasm" style="font-size:{int(96*k)}px;padding:0 34px 12px">خصم جديد</span></div>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(520 if not story else 640)}px;text-align:center">
  <div style="font-weight:800;font-size:{int(34*k)}px;direction:rtl">لين</div>
  <div class="big out" style="font-size:{int(300*k)}px">40%</div>
</div>
{tape(o+(905 if not story else 1000), -4, 'DAILY DEAL  ✦  عرض اليوم')}
<div style="position:absolute;left:60px;right:60px;top:{o+(1000 if not story else 1100)}px;direction:rtl;text-align:center;font-weight:800;font-size:{int(28*k)}px;line-height:1.55">
  كل يوم منتج مختلف بخصم <b style="color:{LIME}">35% لين 40%</b><br>العرض ٢٤ ساعة بس.. <b style="color:{LIME}">تابعنا</b> عشان ما يفوتك</div>'''
    return base(story, body)


def day1(story):
    o = 230 if story else 0
    k = 1.0 if not story else 1.12
    ph = int(300 * k)
    cases = [('cloudy-gray', 'Cloudy'), ('solid-black', 'Solid'), ('fading-blue', 'Fading')]
    imgs = ''
    cw = int(300 * k); gap = 20
    x0 = (1080 - (3 * cw + 2 * gap)) // 2
    for i, (f, nm) in enumerate(cases):
        imgs += f'<img src="file://{S}{f}-c.png" style="position:absolute;left:{x0+i*(cw+gap)}px;top:{o+(560 if not story else 615)}px;width:{cw}px;height:{int(cw*1.18)}px;object-fit:contain;filter:drop-shadow(0 18px 20px rgba(0,0,0,.45))">'
    body = f'''
<img class="logo" src="file://{LOGOW}" style="left:48px;top:{o+40 if story else 44}px">
<div style="position:absolute;right:48px;top:{(o+44) if story else 50}px;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px;color:{LIME}">NOVEMBER DEALS · DAY 1</div>
<div style="position:absolute;left:40px;right:40px;top:{o+(110 if not story else 140)}px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <span class="khasm" style="font-size:{int(118*k)}px;padding:0 30px 14px">خصم</span>
  <span class="big" style="font-size:{int(250*k)}px;color:{LIME};text-shadow:8px 8px 0 {DK}">40%</span>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(400 if not story else 470)}px;text-align:center;direction:rtl">
  <div style="font-weight:900;font-size:{int(52*k)}px">كفرات <span style="font-family:Poppins">iPhone 18</span></div>
  <div style="font-weight:800;font-size:{int(26*k)}px;color:{LIME};margin-top:2px">تركب على <span style="font-family:Poppins">iPhone 17</span> و <span style="font-family:Poppins">18</span> · Pro و Pro Max</div>
</div>
{imgs}
<div class="sticker" style="left:{36 if not story else 30}px;top:{o+(470 if not story else 560)}px"><span style="font-size:22px">بس</span><span style="font-family:PoppinsB;font-size:52px">24</span><span style="font-size:22px">ساعة</span></div>
{tape(o+(935 if not story else 1012), 3, 'عرض اليوم  ✦  DAY 1  ✦  NOVEMBER DEALS', bg=GOLD)}
<div style="position:absolute;left:48px;right:48px;top:{o+(1025 if not story else 1095)}px;display:flex;justify-content:center;gap:16px;direction:rtl">
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px">Solid · Cloudy</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">69</s> 41.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
  <div style="background:#fff;color:{DK};border-radius:24px;padding:6px 22px 10px;text-align:center"><div style="font-weight:800;font-size:{int(20*k)}px">Fading</div><div style="font-family:Poppins;font-weight:700;font-size:{int(34*k)}px;direction:ltr"><s style="opacity:.45;font-size:.6em">79</s> 47.40 <small style="font-family:Cairo;font-size:.55em">ر.ق</small></div></div>
</div>
<div style="position:absolute;left:0;right:0;top:{o+(1140 if not story else 1218)}px;text-align:center;direction:rtl;font-weight:800;font-size:{int(22*k)}px;opacity:.9">الخصم ينزل تلقائي في الموقع · ينتهي بكرة الساعة ٦ المغرب ⏳</div>'''
    return base(story, body)


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(announce(False), D + 'out/974-nov-deals-announce-post.png', 1350)
    shot(announce(True), D + 'out/974-nov-deals-announce-story.png', 1920)
    shot(day1(False), D + 'out/974-nov-deals-day1-cases-post.png', 1350)
    shot(day1(True), D + 'out/974-nov-deals-day1-cases-story.png', 1920)
    print('ok')
