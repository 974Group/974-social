# T100 expo booth — mock-up render (6m x 2.4m cabin). 18 Nov 2026
import subprocess
R = '/home/claude/974-social/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
LOGO = R + 'posts/2026-11/pilates-socks/src/logo-white.png'
SUN = R + 'posts/2026-11/sunglasses/cut/'
WS = R + 'posts/2026-11/whoop5-silicone-all/cut/'
SF = R + 'products/whoop5-soft-fabric/cut/'
CQ = R + 'products/garmin-cirqa-fabric3/cut/'
SOCK = R + 'posts/2026-11/runner-pro/cut/'
GRIP = R + 'posts/2026-11/grip-socks/cut/'
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'
W, H = 1600, 1000
# geometry (front opening and back wall)
FX0, FX1, FY0, FY1 = 140, 1460, 236, 830
BX0, BX1, BY0, BY1 = 300, 1300, 318, 742

sun = ['lusail-mirror', 'halul-mirror', 'ruwais-mirror', 'zubarah-mirror', 'sealine-mirror', 'pearl-mirror']
bands = [WS + 'maroon.png' if False else WS + 'iceblue.png', WS + 'black.png', WS + 'orange.png', WS + 'pink.png', WS + 'babyblue.png',
         SF + 'onyx.png', SF + 'cloud.png', SF + 'forest.png', SF + 'phoenix.png', SF + 'sky.png',
         CQ + 'black.png', CQ + 'navy.png', CQ + 'orange.png', CQ + 'green.png', CQ + 'purple.png']
socks = [SOCK + 'pair-white.png', SOCK + 'pair-blue.png', SOCK + 'pair-yellow.png', GRIP + 'maroon.png', GRIP + 'black.png', GRIP + 'white.png']


def img(src, x, y, w, h, extra=''):
    return f'<img src="file://{src}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:contain;{extra}">'


def page():
    # pegboard of bands (centre of back wall)
    peg = ''
    px0, py0, cw, ch, gx, gy = 640, 462, 58, 62, 8, 6
    for i, b in enumerate(bands):
        r, c = divmod(i, 5)
        peg += img(b, px0 + c * (cw + gx), py0 + r * (ch + gy), cw, ch, 'filter:drop-shadow(0 4px 4px rgba(0,0,0,.35))')
    # sunglasses tower (left)
    tower = ''
    for i, s in enumerate(sun):
        r, c = divmod(i, 2)
        tower += img(SUN + s + '.png', 352 + c * 92, 470 + r * 78, 86, 44, 'filter:drop-shadow(0 4px 4px rgba(0,0,0,.3))')
    # socks shelves (right)
    sk = ''
    for i, s in enumerate(socks):
        r, c = divmod(i, 3)
        sk += img(s, 1062 + c * 72, 478 + r * 104, 66, 84, 'filter:drop-shadow(0 4px 4px rgba(0,0,0,.3))')
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Poppins;
background:linear-gradient(180deg,#9FC6E6 0%,#D9E9F4 45%,#E9E4DA 72%,#CFC7B8 100%)}}
.poly{{position:absolute;inset:0}}
.t{{position:absolute;white-space:nowrap}}
</style></head><body>
<!-- distant palms / stadium haze -->
<div style="position:absolute;left:0;right:0;top:300px;height:160px;background:linear-gradient(180deg,transparent,rgba(255,255,255,.55))"></div>
<!-- ground -->
<div style="position:absolute;left:0;right:0;top:{FY1}px;bottom:0;background:linear-gradient(180deg,#BDB5A6,#A79F90)"></div>
<!-- cabin shadow -->
<div style="position:absolute;left:{FX0-30}px;width:{FX1-FX0+60}px;top:{FY1-6}px;height:60px;background:radial-gradient(ellipse at center,rgba(0,0,0,.35),transparent 70%)"></div>
<!-- interior: floor, side walls, ceiling, back wall -->
<div class="poly" style="clip-path:polygon({FX0}px {FY1}px,{FX1}px {FY1}px,{BX1}px {BY1}px,{BX0}px {BY1}px);background:linear-gradient(180deg,#B9B3AA,#E2DED7)"></div>
<div class="poly" style="clip-path:polygon({FX0}px {FY0}px,{BX0}px {BY0}px,{BX0}px {BY1}px,{FX0}px {FY1}px);background:linear-gradient(90deg,#EDEBE8,#D6D2CD)"></div>
<div class="poly" style="clip-path:polygon({FX1}px {FY0}px,{BX1}px {BY0}px,{BX1}px {BY1}px,{FX1}px {FY1}px);background:linear-gradient(270deg,#EDEBE8,#D6D2CD)"></div>
<div class="poly" style="clip-path:polygon({FX0}px {FY0}px,{FX1}px {FY0}px,{BX1}px {BY0}px,{BX0}px {BY0}px);background:#F4F2EF"></div>
<!-- back wall maroon graphic -->
<div style="position:absolute;left:{BX0}px;top:{BY0}px;width:{BX1-BX0}px;height:{BY1-BY0}px;background:radial-gradient(500px 300px at 50% 30%,#9C0B5A,transparent 70%),linear-gradient(180deg,{M},{DK})"></div>
<div style="position:absolute;left:{BX0}px;top:{BY0}px;width:{BX1-BX0}px;height:{BY1-BY0}px;background-image:radial-gradient(rgba(255,255,255,.08) 1.6px,transparent 2px);background-size:16px 16px"></div>
<img src="file://{LOGO}" style="position:absolute;left:{(BX0+BX1)//2-62}px;top:{BY0+14}px;height:50px">
<div class="t" style="left:{BX0}px;width:{BX1-BX0}px;top:{BY0+68}px;text-align:center;color:#fff;font-weight:700;font-size:14px;letter-spacing:6px">MADE IN QATAR · BUILT FOR RACE DAY</div>
<div class="t" style="left:{BX0}px;width:{BX1-BX0}px;top:{BY0+86}px;text-align:center;color:{GOLD};font-family:Cairo;font-weight:800;font-size:14px">صُنع في قطر.. وجاهز ليوم السباق</div>
<!-- spotlights glow -->
<div style="position:absolute;left:{BX0}px;width:{BX1-BX0}px;top:{BY0}px;height:200px;background:radial-gradient(160px 120px at 18% 0%,rgba(255,240,210,.35),transparent),radial-gradient(160px 120px at 50% 0%,rgba(255,240,210,.35),transparent),radial-gradient(160px 120px at 82% 0%,rgba(255,240,210,.35),transparent)"></div>
<!-- LEFT: sunglasses tower + mirror -->
<div style="position:absolute;left:340px;top:440px;width:196px;height:300px;background:#fff;border-radius:6px;box-shadow:0 8px 20px rgba(0,0,0,.35)"></div>
<div style="position:absolute;left:340px;top:440px;width:196px;height:26px;background:{M};border-radius:6px 6px 0 0;color:#fff;font-size:12px;font-weight:700;letter-spacing:4px;text-align:center;line-height:26px">SUNGLASSES</div>
{''.join(f'<div style="position:absolute;left:346px;width:184px;top:{514+r*78}px;height:4px;background:#D8D4CF"></div>' for r in range(3))}
{tower}
<div style="position:absolute;left:350px;top:704px;width:176px;height:30px;background:linear-gradient(90deg,#cfd8e0,#f6f8fa,#cfd8e0);border-radius:3px;font-size:11px;font-weight:700;color:#4D5566;text-align:center;line-height:30px;letter-spacing:0">☀ UV DEMO</div>
<div style="position:absolute;left:548px;top:430px;width:56px;height:300px;background:linear-gradient(110deg,#e9eef2,#ffffff 40%,#cfd8df);border:5px solid #fff;border-radius:28px;box-shadow:0 8px 18px rgba(0,0,0,.3)"></div>
<!-- CENTRE: pegboard with bands -->
<div style="position:absolute;left:626px;top:436px;width:350px;height:236px;background:#F7F5F2;border-radius:6px;box-shadow:0 8px 20px rgba(0,0,0,.35);background-image:radial-gradient(#cfc9c2 1.5px,transparent 2px);background-size:14px 14px"></div>
<div style="position:absolute;left:626px;top:436px;width:350px;height:22px;background:{M};border-radius:6px 6px 0 0;color:#fff;font-size:11.5px;font-weight:700;letter-spacing:3px;text-align:center;line-height:22px">WHOOP · GARMIN · FITBIT · APPLE</div>
{peg}
<!-- RIGHT: socks shelves -->
<div style="position:absolute;left:1050px;top:440px;width:228px;height:300px;background:#fff;border-radius:6px;box-shadow:0 8px 20px rgba(0,0,0,.35)"></div>
<div style="position:absolute;left:1050px;top:440px;width:228px;height:26px;background:{M};border-radius:6px 6px 0 0;color:#fff;font-size:12px;font-weight:700;letter-spacing:4px;text-align:center;line-height:26px">RUNNING SOCKS</div>
{''.join(f'<div style="position:absolute;left:1056px;width:216px;top:{566+r*104}px;height:5px;background:#D8D4CF"></div>' for r in range(2))}
{sk}
<!-- front counter (left of centre, keeps entrance open) -->
<div style="position:absolute;left:600px;top:690px;width:400px;height:24px;background:#F4F2EF;border-radius:4px;box-shadow:0 -2px 0 #fff inset"></div>
<div style="position:absolute;left:606px;top:712px;width:388px;height:116px;background:linear-gradient(180deg,{M},{DK});border-radius:0 0 6px 6px;box-shadow:0 14px 26px rgba(0,0,0,.35)"></div>
<img src="file://{LOGO}" style="position:absolute;left:730px;top:736px;height:40px">
<div class="t" style="left:606px;width:388px;top:786px;text-align:center;color:{GOLD};font-size:13px;font-weight:700;letter-spacing:3px">974GROUP.NET</div>
<div style="position:absolute;left:640px;top:676px;width:52px;height:30px;background:#1A1E26;border-radius:6px;transform:skewX(-12deg);box-shadow:0 4px 8px rgba(0,0,0,.4)"><div style="margin:3px;height:24px;background:linear-gradient(135deg,#3a4250,#6b7686);border-radius:3px"></div></div>
<div style="position:absolute;left:706px;top:690px;width:24px;height:14px;background:#2A2F38;border-radius:4px"></div>
<div style="position:absolute;left:930px;top:674px;width:34px;height:34px;background:#fff;border:3px solid {M};border-radius:4px;background-image:repeating-linear-gradient(0deg,#1A1E26 0 3px,transparent 3px 6px),repeating-linear-gradient(90deg,#1A1E26 0 3px,transparent 3px 6px);background-blend-mode:multiply"></div>
<!-- cabin frame (white) -->
<div style="position:absolute;left:{FX0-18}px;top:{FY0-96}px;width:{FX1-FX0+36}px;height:96px;background:linear-gradient(180deg,{M},{DK});box-shadow:0 10px 18px rgba(0,0,0,.3)"></div>
<div style="position:absolute;left:{FX0-18}px;top:{FY0-100}px;width:{FX1-FX0+36}px;height:6px;background:#F4F2EF"></div>
<div style="position:absolute;left:{FX0-18}px;top:{FY0-4}px;width:{FX1-FX0+36}px;height:10px;background:#E8E6E3"></div>
<div style="position:absolute;left:{FX0-18}px;top:{FY0}px;width:18px;height:{FY1-FY0}px;background:linear-gradient(90deg,#F4F2EF,#D9D6D2)"></div>
<div style="position:absolute;left:{FX1}px;top:{FY0}px;width:18px;height:{FY1-FY0}px;background:linear-gradient(90deg,#D9D6D2,#F4F2EF)"></div>
<!-- fascia content -->
<img src="file://{LOGO}" style="position:absolute;left:{FX0+30}px;top:{FY0-78}px;height:58px">
<div class="t" style="left:{FX0+190}px;top:{FY0-74}px;color:#fff;font-weight:900;font-size:34px;letter-spacing:2px">974GROUP</div>
<div class="t" style="left:{FX0+192}px;top:{FY0-34}px;color:{GOLD};font-weight:700;font-size:15px;letter-spacing:5px">SMARTWATCH BANDS · SUNGLASSES · RUNNING SOCKS</div>
<div class="t" style="right:{W-FX1+30}px;top:{FY0-90}px;color:#fff;font-family:Cairo;font-weight:900;font-size:26px;direction:rtl">براند قطري 🇶🇦</div>
<div class="t" style="right:{W-FX1+30}px;top:{FY0-34}px;color:#fff;font-weight:700;font-size:16px;letter-spacing:1px">974group.net</div>
<!-- floor sign at entrance -->
<div style="position:absolute;left:1296px;top:712px;width:150px;height:150px">
  <div style="position:absolute;left:20px;top:0;width:110px;height:120px;background:#fff;border-radius:8px;border-top:10px solid {M};box-shadow:0 10px 20px rgba(0,0,0,.35);text-align:center;padding-top:8px">
    <div style="font-family:Cairo;font-weight:900;font-size:15px;color:{M};direction:rtl;line-height:1.2">عرض المعرض</div>
    <div style="font-weight:900;font-size:13px;color:#1A1E26;margin-top:4px;line-height:1.25">SUNGLASSES<br>+ SOCKS</div>
    <div style="font-weight:900;font-size:20px;color:{M};margin-top:4px">BUNDLE</div>
  </div>
  <div style="position:absolute;left:68px;top:120px;width:14px;height:30px;background:#9a948b"></div>
</div>
<div class="t" style="left:24px;bottom:18px;font-size:12px;color:rgba(0,0,0,.45);font-weight:700;letter-spacing:2px">CONCEPT MOCK-UP · 6M × 2.4M CABIN · NOT TO SCALE</div>
</body></html>'''


if __name__ == '__main__':
    out = R + 'posts/2026-11/expo-booth/974-t100-booth-mockup.png'
    p = out.replace('.png', '.html'); open(p, 'w').write(page())
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}},deviceScaleFactor:1.5}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd=R)
    print('ok')
