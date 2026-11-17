# 974 "Doha city" comic-panel poster (GTA loading-screen genre, original wordmark, no Rockstar marks)
import sys, math
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
sys.path.insert(0, '/home/claude/974-social/templates')
from gen import FONTS, shot, LW
import payfoot
D = '/home/claude/974-social/posts/2026-11/gta/'
T = D + 'toon/'
GOLD = '#C9A24B'; INK = '#140910'

def palm(x, y, h, col='#1a0b1e', flip=False):
    s = h / 300
    t = f'translate({x},{y}) scale({-s if flip else s},{s})'
    fr = ''.join(f'<path d="M0,0 Q{dx*0.5},{dy-40} {dx},{dy}" stroke="{col}" stroke-width="14" fill="none" stroke-linecap="round"/>'
                 for dx, dy in [(-110, 40), (-90, -30), (-40, -70), (40, -70), (95, -25), (115, 45), (-60, 80), (60, 80)])
    return f'<g transform="{t}"><path d="M-6,300 Q10,150 0,0 L8,0 Q22,150 10,300 Z" fill="{col}"/>{fr}</g>'

def skyline(y, col, scale=1.0, x0=0):
    # simple Doha-like skyline: towers, a twisted tower, a rocket-shaped tower
    b = [(0,90,40),(44,140,34),(82,210,30),(116,120,40),(160,250,26),(190,170,36),(230,300,22),(256,190,38),(300,130,34),(338,230,28),(370,110,44),(418,160,30)]
    h = ''
    for bx, bh, bw in b:
        X = x0 + bx*scale; H = bh*scale; W = bw*scale
        h += f'<rect x="{X}" y="{y-H}" width="{W}" height="{H+2}" fill="{col}"/>'
    # rocket tower (rounded tip)
    X = x0 + 470*scale
    h += f'<path d="M{X},{y} L{X},{y-230*scale} Q{X+16*scale},{y-300*scale} {X+32*scale},{y-230*scale} L{X+32*scale},{y} Z" fill="{col}"/>'
    # hourglass tower
    X = x0 + 512*scale
    h += f'<path d="M{X},{y} L{X+8*scale},{y-130*scale} L{X},{y-260*scale} L{X+36*scale},{y-260*scale} L{X+28*scale},{y-130*scale} L{X+36*scale},{y} Z" fill="{col}"/>'
    return h

def qflag(x, y, w=120):
    h = w * 0.4; band = w * 0.3; n = 9; st = h / n
    pts = [(x, y), (x+band, y)]
    for i in range(n):
        pts += [(x+band+w*0.1, y+st*(i+0.5)), (x+band, y+st*(i+1))]
    pts += [(x, y+h)]
    p = ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts)
    return (f'<rect x="{x-6}" y="{y-6}" width="6" height="260" fill="#ddd"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#8A1538"/><polygon points="{p}" fill="#fff"/>')

POLY = {
 1: '28px 28px,554px 28px,524px 388px,28px 388px',
 2: '566px 28px,1052px 28px,1052px 388px,536px 388px',
 3: '28px 400px,494px 400px,524px 760px,28px 760px',
 4: '506px 400px,1052px 400px,1052px 760px,536px 760px',
 5: '28px 772px,534px 772px,500px 1180px,28px 1180px',
 6: '546px 772px,1052px 772px,1052px 1180px,512px 1180px',
}

def panel(n, bg, inner):
    return f'<div class="pn" style="background:{bg};clip-path:polygon({POLY[n]})">{inner}<div class="ht"></div></div>'

def cap(r, y, title, price, sub='', rot=0):
    # r = right edge x on the 1080 canvas
    return (f'<div class="cap" style="right:{1080-r}px;top:{y}px;transform:rotate({rot}deg)">'
            f'<b>{title}</b>{f"<s>{sub}</s>" if sub else ""}<em><span class="en">{price}</span> ر.ق</em></div>')

def build(story=False):
    H = 1920 if story else 1350; dy = 180 if story else 0
    svg = lambda c: f'<svg class="abs" width="1080" height="1350" viewBox="0 0 1080 1350">{c}</svg>'
    # 1 — masks pile, warm paper
    p1 = panel(1, 'linear-gradient(160deg,#E9D6C1 0%,#D7B897 100%)',
        f'<img class="abs" src="file://{T}mask-white.png" style="left:250px;top:70px;height:250px;transform:rotate(9deg)">'
        f'<img class="abs" src="file://{T}mask-black.png" style="left:60px;top:90px;height:255px;transform:rotate(-8deg)">'
        f'<img class="abs" src="file://{T}mask-red.png" style="left:150px;top:120px;height:265px">'
        + cap(505, 318, 'الماسك اللي الكل لابسه', '39', rot=-2))
    # 2 — phone notification, pink/purple dusk
    phone = f'''<div class="abs phone" style="left:800px;top:56px;transform:rotate(7deg)">
      <div class="scr"><div class="nt"><img src="file://{LW}"><div><b>974 Group</b><span>طلبك وصل! 📦</span></div></div>
      <div class="nt2"><span>974group.net</span></div></div></div>'''
    p2 = panel(2, 'linear-gradient(200deg,#F08A6B 0%,#C2457A 45%,#5A2A7A 100%)',
        svg(skyline(388, '#3A1550', 0.75, 560)) + phone +
        f'<div class="abs ar bub" style="left:590px;top:200px">ألو؟<br>وصل الطلب؟</div>')
    # 3 — goggles over desert dunes at sunset
    dunes = ('<circle cx="250" cy="560" r="80" fill="#FFD27A"/>'
             '<path d="M28,640 Q160,560 300,620 T540,600 L540,760 L28,760Z" fill="#D9874A"/>'
             '<path d="M28,700 Q200,630 380,690 T560,680 L560,760 L28,760Z" fill="#B8612F"/>')
    p3 = panel(3, 'linear-gradient(180deg,#FF9F5A 0%,#F2665C 55%,#8E2F5E 100%)',
        svg(dunes) + f'<img class="abs" src="file://{T}gog-red.png" style="left:40px;top:470px;width:360px;transform:rotate(-6deg)">'
        + cap(400, 690, 'نظارات 974 Guards', '209', rot=-2))
    # 4 — gold buckle Whoop, fort + flag, blue sky
    fort = ('<path d="M760,760 L760,610 L790,610 L790,590 L810,590 L810,610 L1052,610 L1052,760Z" fill="#D9B58A"/>'
            + ''.join(f'<rect x="{x}" y="598" width="14" height="14" fill="#D9B58A"/>' for x in range(820, 1052, 26))
            + '<rect x="900" y="560" width="70" height="200" fill="#C99E6F"/>'
            + ''.join(f'<rect x="{x}" y="548" width="12" height="14" fill="#C99E6F"/>' for x in range(900, 970, 20)))
    p4 = panel(4, 'linear-gradient(180deg,#5FA7D8 0%,#9FD0EA 60%,#F4D9B0 100%)',
        svg(fort + qflag(985, 500, 50)) +
        f'<img class="abs" src="file://{T}ff-olive.png" style="left:860px;top:430px;height:240px;transform:rotate(8deg)">'
        f'<img class="abs" src="file://{T}ff-pinkyred.png" style="left:740px;top:445px;height:245px;transform:rotate(-6deg)">'
        + cap(1040, 692, 'يتسكر باللزقة', '74', rot=2))
    # 5 — CIRQA magnetic, neon night
    neon = ('<rect x="412" y="800" width="54" height="250" rx="6" fill="#2A0E3A" stroke="#FF4FD8" stroke-width="3"/>'
            + ''.join(f'<text x="439" y="{850+i*58}" text-anchor="middle" class="neon">{c}</text>' for i, c in enumerate('DOHA'))
            + skyline(1180, '#241040', 0.8, 150) + palm(80, 880, 250, '#12061c', True))
    p5 = panel(5, 'linear-gradient(180deg,#2B1460 0%,#7A2A8C 60%,#E0508A 100%)',
        svg(neon) + f'<img class="abs" src="file://{T}mag-lime.png" style="left:100px;top:810px;height:250px;transform:rotate(-8deg)">'
        f'<img class="abs" src="file://{T}mag-black.png" style="left:230px;top:860px;height:210px;transform:rotate(7deg)">'
        + cap(470, 1108, 'يتسكر بالمغناطيس', '99', sub='CIRQA', rot=-1))
    # 6 — waterproof Whoop on the corniche at sunset
    sea = ('<circle cx="800" cy="950" r="70" fill="#FFD27A"/>'
           + skyline(960, '#5B2A6E', 0.85, 560)
           + '<rect x="516" y="958" width="540" height="90" fill="#6E4C9E"/><rect x="516" y="990" width="540" height="6" fill="#FFB27A" opacity=".5"/>'
           + '<path d="M512,1180 L640,1060 L1052,1060 L1052,1180Z" fill="#3A2340"/><path d="M690,1180 L760,1090" stroke="#fff" stroke-width="6" stroke-dasharray="20 16"/>'
           + palm(1010, 860, 260, '#2a1030', True))
    p6 = panel(6, 'linear-gradient(180deg,#F59A6B 0%,#E9667A 45%,#8A3C8E 100%)',
        svg(sea) + f'<img class="abs" src="file://{T}wp-maroon.png" style="left:600px;top:820px;height:240px;transform:rotate(-8deg)">'
        f'<img class="abs" src="file://{T}wp-black.png" style="left:790px;top:860px;height:220px;transform:rotate(9deg)">'
        + cap(1030, 1108, 'اسبح فيه', '99', sub='WHOOP 5.0', rot=2))
    title = f'''<div class="ttl"><img src="file://{T}logo-gta.png"><div class="t2">Group</div><div class="t3">doha city</div></div>'''
    body = p1 + p2 + p3 + p4 + p5 + p6 + title
    if story:
        body = (f'<div class="wrap" style="top:{dy}px">{body}</div>'
                '<div class="scta"><b>كل منتجات 974</b> بمكان واحد<br><span>اطلب الحين من <i>974group.net</i> 🛒</span></div>')
    css = f'''@font-face{{font-family:Anton;src:url(file://{D}fonts/anton.woff2)}}
@font-face{{font-family:Pricedown;src:url(file://{D}fonts/pricedown.ttf)}}
body{{width:1080px;height:{H}px;background:#1A0611;position:relative;overflow:hidden;font-family:Cairo;color:{INK}}}
.pn{{position:absolute;inset:0}}
.ht{{position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.22) 1.2px,transparent 1.6px);background-size:7px 7px;mix-blend-mode:multiply;opacity:.45}}
img.abs{{filter:drop-shadow(6px 8px 0 rgba(20,9,16,.35))}}
.cap{{position:absolute;background:#F4F1F2;border:4px solid {INK};padding:4px 16px 8px;direction:rtl;box-shadow:6px 6px 0 {INK};z-index:3;white-space:nowrap;display:flex;align-items:center;gap:12px}}
.cap b{{font-weight:900;font-size:27px}} .cap s{{text-decoration:none;font-family:Poppins;font-weight:600;font-size:14px;opacity:.7;direction:ltr}}
.cap em{{font-style:normal;font-weight:900;font-size:22px;background:#720842;color:#fff;padding:0 12px 3px;border-radius:4px}} .cap em .en{{font-family:Poppins;font-weight:700}}
.phone{{width:210px;height:300px;background:#111;border-radius:34px;padding:12px;border:4px solid {INK};box-shadow:8px 10px 0 rgba(20,9,16,.4)}}
.scr{{width:100%;height:100%;border-radius:24px;background:linear-gradient(180deg,#F6E7EF,#E6D3F0);padding:40px 12px;direction:rtl}}
.nt{{display:flex;gap:10px;align-items:center;background:#fff;border-radius:16px;padding:10px;box-shadow:0 4px 10px rgba(0,0,0,.15)}}
.nt img{{width:38px;height:38px;border-radius:10px;background:#720842;padding:6px;object-fit:contain}}
.nt b{{display:block;font-family:Poppins;font-size:13px;direction:ltr;text-align:right}} .nt span{{font-weight:800;font-size:14px;white-space:nowrap}}
.nt2{{margin-top:130px;text-align:center}} .nt2 span{{font-family:Poppins;font-weight:700;font-size:15px;background:#720842;color:#fff;border-radius:20px;padding:5px 14px}}
.bub{{position:absolute;background:#fff;border:4px solid {INK};border-radius:22px;padding:6px 18px 10px;font-weight:900;font-size:26px;line-height:1.25;box-shadow:5px 5px 0 {INK}}}
.neon{{font-family:Anton;font-size:46px;fill:#FFD6F6;filter:drop-shadow(0 0 6px #FF4FD8) drop-shadow(0 0 14px #FF4FD8)}}
.ttl{{position:absolute;left:330px;width:420px;top:440px;text-align:center;z-index:5;transform:rotate(-3deg)}}
.ttl img{{width:330px;display:block;margin:0 auto}}
.ttl div{{font-family:Pricedown;color:#fff;-webkit-text-stroke:10px {INK};paint-order:stroke fill;line-height:.9;text-shadow:6px 7px 0 {INK}}}
.t2{{font-size:118px;margin-top:-6px}}
.ttl .t3{{font-size:58px;color:{GOLD};-webkit-text-stroke:8px {INK};margin-top:2px;text-shadow:4px 5px 0 {INK}}}
.pf{{position:absolute;left:28px;right:28px;bottom:{250 if story else 30}px}}
.wrap{{position:absolute;left:0;width:1080px;height:1350px}}
.scta{{position:absolute;left:60px;right:60px;top:1400px;background:#F4F1F2;border:5px solid {INK};box-shadow:8px 8px 0 #720842;padding:10px 24px 16px;text-align:center;direction:rtl;font-weight:900;font-size:40px;line-height:1.35;transform:rotate(-1.5deg)}}
.scta b{{color:#720842}} .scta span{{font-size:30px;font-weight:800}} .scta i{{font-style:normal;font-family:Poppins;font-weight:700;color:#720842}}
{payfoot.css(1.12 if story else 1.0, text='#fff', label='#fff')}
.url{{position:absolute;left:0;right:0;bottom:22px;text-align:center;font-weight:800;font-size:24px;color:#fff;direction:rtl}} .url b{{font-family:Poppins;color:{GOLD}}}'''
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}{css}</style></head><body>{body}
<div class="pf">{payfoot.html()}</div></body></html>'''
    shot('gta-story' if story else 'gta-post', html, H)

if __name__ == '__main__':
    build(); build(True)
