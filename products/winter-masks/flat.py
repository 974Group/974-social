# 10 original 974 winter face-mask (neck gaiter) prints. Flat print = gaiter laid flat (front face), 1200x900.
import asyncio, os
from playwright.async_api import async_playwright
D = os.path.dirname(os.path.abspath(__file__))
LOGO_W = '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers/'
FONT = '''@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,500;0,700;0,800;0,900;1,900&family=Cairo:wght@700;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}body{width:1200px;height:900px;overflow:hidden;position:relative;font-family:Poppins}
.a{position:absolute}.en{font-family:Poppins}.ar{font-family:Cairo;direction:rtl}
.tag{font-weight:800;font-size:15px;letter-spacing:3px;line-height:1.25}'''
import math, random


def svg(inner, bg='none'):
    return f'<svg class="a" style="left:0;top:0" width="1200" height="900" viewBox="0 0 1200 900"><rect width="1200" height="900" fill="{bg}"/>{inner}</svg>'


def topo(col, n=26, seed=3, amp=60, sw=2.2, op=.55):
    random.seed(seed); out = ''
    for i in range(n):
        y0 = -60 + i * 40; pts = []
        ph = random.random() * 6
        for x in range(-50, 1260, 40):
            y = y0 + amp * math.sin(x / 170 + ph + i * .23) + 25 * math.sin(x / 61 + i)
            pts.append(f'{x},{y:.1f}')
        out += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    return out


def blobs(cols, n=60, seed=7):
    random.seed(seed); out = ''
    for i in range(n):
        c = random.choice(cols); x = random.randint(-100, 1250); y = random.randint(-100, 950); r = random.randint(60, 170)
        pts = []
        for k in range(10):
            a = k / 10 * 6.283; rr = r * (0.6 + random.random() * .6)
            pts.append(f'{x + rr * math.cos(a):.0f},{y + rr * .7 * math.sin(a):.0f}')
        out += f'<polygon points="{" ".join(pts)}" fill="{c}" stroke-linejoin="round" stroke="{c}" stroke-width="40"/>'
    return out


def stars(n=140, seed=2):
    random.seed(seed)
    return ''.join(f'<circle cx="{random.randint(0,1200)}" cy="{random.randint(0,560)}" r="{random.choice([1,1,1.5,2,2.6])}" fill="#fff" opacity="{random.random()*.7+.3:.2f}"/>' for _ in range(n))


def crackle(col, n=55, seed=9):
    random.seed(seed); out = ''
    for i in range(n):
        x, y = random.randint(-50, 1250), random.randint(-50, 950); pts = [f'{x},{y}']
        ang = random.random() * 6.28
        for k in range(random.randint(4, 8)):
            ang += random.uniform(-.7, .7); L = random.randint(30, 80)
            x += L * math.cos(ang); y += L * math.sin(ang); pts.append(f'{x:.0f},{y:.0f}')
        out += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{random.choice([2,3,5])}" stroke-linejoin="round" stroke-linecap="round" opacity=".8"/>'
    return out


def sadu():
    # Gulf Sadu-inspired horizontal bands: triangles, diamonds, zigzags
    M, C, K, R = '#7A1030', '#EFE3CC', '#1A1414', '#C9A24B'
    out = f'<rect width="1200" height="900" fill="{M}"/>'
    bands = [(0, 70, K), (70, 30, C), (100, 120, M), (220, 26, C), (246, 90, K), (336, 26, C), (362, 180, M), (542, 26, C), (568, 90, K), (658, 26, C), (684, 120, M), (804, 26, C), (830, 70, K)]
    for y, h, c in bands: out += f'<rect y="{y}" width="1200" height="{h}" fill="{c}"/>'
    # triangles row in band 100-220
    for x in range(0, 1240, 60):
        out += f'<polygon points="{x},210 {x+30},120 {x+60},210" fill="{C}"/><polygon points="{x+18},200 {x+30},160 {x+42},200" fill="{R}"/>'
        out += f'<polygon points="{x},694 {x+30},784 {x+60},694" fill="{C}"/><polygon points="{x+18},704 {x+30},744 {x+42},704" fill="{R}"/>'
    for x in range(0, 1240, 80):
        for yy in (291, 613):
            out += f'<polygon points="{x+40},{yy-36} {x+76},{yy} {x+40},{yy+36} {x+4},{yy}" fill="{M}"/><polygon points="{x+40},{yy-16} {x+56},{yy} {x+40},{yy+16} {x+24},{yy}" fill="{C}"/>'
    zz = ' '.join(f'{x},{(85 if (x//30)%2 else 15)+0}' for x in range(-30, 1260, 30))
    for yy in (20, 845):
        out += f'<polyline transform="translate(0,{yy-10})" points="{zz}" fill="none" stroke="{R}" stroke-width="8" stroke-linejoin="miter" opacity=".9"/>'
    return out


def flagedge():
    M = '#8A1538'; h = 900 / 9
    pts = ['0,0', '330,0']
    for i in range(9):
        pts += [f'430,{i*h + h/2:.1f}', f'330,{(i+1)*h:.1f}']
    pts += ['0,900']
    return f'<rect width="1200" height="900" fill="{M}"/><polygon points="{" ".join(pts)}" fill="#F4F1F2"/>'


D10 = [
 # key, bg/svg, overlay html, name, colour line
 ('dune-lines', svg(topo('#5E4630', amp=55, op=.45), '#D8C3A1'),
  '<div class="a en" style="left:520px;top:300px;color:#4A3524;font-weight:900;font-size:110px;line-height:.86;letter-spacing:-2px">KHOR AL<br>ADAID</div><div class="a en tag" style="left:525px;top:520px;color:#4A3524">24.63° N · DESERT ISSUE<br>WINTER 26/27</div>',
  'Khor Al Adaid · Sand', 'رمل وخطوط كثبان'),
 ('maroon-mono', svg(''.join(f'<text x="{x}" y="{y}" font-family="Poppins" font-weight="900" font-size="54" fill="#6A0E2C" opacity=".9" transform="rotate(-12 {x} {y})">974</text>' for y in range(40, 980, 80) for x in range(((y // 80) % 2) * 70 - 100, 1300, 140)), '#7E1236') + svg('<rect x="0" y="0" width="1200" height="14" fill="#F4F1F2"/><rect x="0" y="886" width="1200" height="14" fill="#F4F1F2"/>'),
  '<div class="a en" style="left:470px;top:360px;color:#fff;font-weight:900;font-size:64px;line-height:.95">RIDE<br>THE WIND</div><div class="a ar" style="left:475px;top:500px;color:#F4D9A0;font-weight:900;font-size:30px">عنابي.. على البر</div>',
  'Maroon 974 · Monogram', 'عنابي بشعار 974 مكرر'),
 ('sealine', '<div class="a" style="inset:0;background:linear-gradient(170deg,#0F5E86 0%,#2C93B8 34%,#8FD1D9 52%,#EAD9B6 66%,#D7B98A 100%)"></div>' + svg(topo('#ffffff', n=14, seed=11, amp=30, sw=3, op=.25)),
  '<div class="a en" style="left:480px;top:330px;color:#fff;font-weight:900;font-size:120px;letter-spacing:-3px;line-height:.85">SEALINE</div><div class="a en tag" style="left:486px;top:450px;color:#fff">24.85° N · WHERE SEA MEETS SAND</div>',
  'Sealine · Sea to Sand', 'بحر لين الرمل'),
 ('night-ride', svg(''.join(f'<path d="M-50 {200+i*55} C 300 {80+i*55}, 700 {420+i*55}, 1250 {140+i*55}" stroke="#fff" stroke-width="{1.5 if i%3 else 3}" fill="none" opacity="{.18 if i%3 else .55}"/>' for i in range(14)), '#0E0F12'),
  '<div class="a en" style="left:470px;top:320px;color:#fff;font-weight:900;font-style:italic;font-size:96px;line-height:.9">NIGHT<br>RIDE</div><div class="a en tag" style="left:476px;top:510px;color:#C9A24B">FOR THE ONES WHO RIDE AFTER SUNSET</div>',
  'Night Ride · Black', 'أسود بخطوط سرعة'),
 ('race-974', svg('<rect width="1200" height="900" fill="#E9ECEF"/>' + ''.join(f'<rect x="-200" y="{y}" width="1700" height="{h}" fill="#F26A1B" transform="rotate(-18 600 450)"/>' for y, h in [(600, 34), (650, 12), (676, 12)]) + topo('#AEB5BD', n=10, seed=5, amp=40, op=.35), 'none'),
  '<div class="a en" style="left:440px;top:240px;color:#1B1F24;font-weight:900;font-style:italic;font-size:260px;letter-spacing:-10px;line-height:.8">974</div><div class="a en tag" style="left:452px;top:470px;color:#F26A1B">DUNE RACING TEAM · WINTER 26/27</div>',
  '974 Racing · Grey × Orange', 'رمادي مع برتقالي ورقم 974'),
 ('desert-camo', svg(blobs(['#C7A878', '#A88456', '#7D6143', '#E2CDA6']), '#D9C29A'),
  '<div class="a en" style="left:470px;top:350px;color:#2E241A;font-weight:900;font-size:84px;line-height:.9">BLEND<br>IN.</div><div class="a ar" style="left:476px;top:520px;color:#2E241A;font-weight:900;font-size:30px">مموّه البر</div>',
  'Desert Camo', 'تمويه صحراوي'),
 ('sadu', svg(sadu()),
  '<div class="a" style="left:460px;top:395px;background:#1A1414;padding:10px 24px 14px;border:3px solid #C9A24B"><div class="en" style="color:#EFE3CC;font-weight:900;font-size:44px;letter-spacing:6px">S A D U</div><div class="ar" style="color:#C9A24B;font-weight:900;font-size:24px;text-align:center">نقشة السدو</div></div>',
  'Sadu · Heritage', 'نقشة السدو الخليجية'),
 ('flag-edge', svg(flagedge()),
  '<div class="a en" style="left:560px;top:320px;color:#fff;font-weight:900;font-size:150px;line-height:.82;letter-spacing:-4px">974</div><div class="a en tag" style="left:566px;top:455px;color:#F4D9A0">A QATARI BRAND · <span style="font-family:Cairo">براند قطري</span></div>',
  'Flag Edge · Maroon × White', 'حافة العلم ٩ رؤوس'),
 ('desert-night', '<div class="a" style="inset:0;background:linear-gradient(180deg,#0B1534 0%,#1E2A5A 55%,#3A2F5E 75%)"></div>' + svg(stars() + '<path d="M0 700 C 200 600, 380 640, 560 690 S 900 620, 1200 680 L1200 900 L0 900 Z" fill="#7A5A3C"/><path d="M0 780 C 260 700, 520 760, 760 740 S 1050 700, 1200 760 L1200 900 L0 900Z" fill="#5C4229"/><circle cx="980" cy="160" r="46" fill="#F4E7C0"/><circle cx="1000" cy="148" r="44" fill="#0F1A3E"/>'),
  '<div class="a en" style="left:460px;top:300px;color:#fff;font-weight:900;font-size:76px;line-height:.92">UNDER<br>THE STARS</div><div class="a ar" style="left:466px;top:470px;color:#F4E7C0;font-weight:900;font-size:30px">كشتة الليل</div>',
  'Desert Night', 'سما البر بالليل'),
 ('rose-crackle', svg(crackle('#FFFFFF', n=140), '#E9A7BC'),
  '<div class="a en" style="left:470px;top:350px;color:#5B1E36;font-weight:900;font-size:96px;line-height:.86;letter-spacing:-2px">ROSE<br>DUNE</div><div class="a en tag" style="left:476px;top:535px;color:#5B1E36">974 · WINTER 26/27</div>',
  'Rose Dune · Pink', 'وردي بخطوط متشققة'),
]


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        for k, bg, ov, *_ in D10:
            logo = f'<div class="a en" style="right:40px;bottom:30px;font-weight:900;font-size:34px;color:rgba(255,255,255,.0)"></div>'
            html = f'<html><head><style>{FONT}</style></head><body>{bg}{ov}</body></html>'
            await pg.set_content(html); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'{D}/flat/{k}.png')
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
