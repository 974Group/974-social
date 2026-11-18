# T100 expo booth — floor plan (top view) + back-wall elevation, to scale. No products. 18 Nov 2026
import subprocess
R = '/home/claude/974-social/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'; INK = '#1A1E26'
S = 190            # px per metre
OX, OY = 150, 190  # plan origin (back-left inner corner)
W, H = 1640, 1520


def r(x, y, w, h, fill, label='', sub='', fs=19, col='#fff', extra=''):
    """rect in metres on the plan"""
    return (f'<div style="position:absolute;left:{OX+x*S}px;top:{OY+y*S}px;width:{w*S}px;height:{h*S}px;background:{fill};'
            f'border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;'
            f'color:{col};font-family:Cairo;font-weight:800;font-size:{fs}px;line-height:1.15;direction:rtl;{extra}">'
            f'{label}{f"<small style=font-size:{int(fs*.72)}px;font-weight:700;opacity:.85>{sub}</small>" if sub else ""}</div>')


def dim(x0, y0, x1, y1, txt, side='top'):
    # simple dimension line in metres
    if y0 == y1:
        return (f'<div style="position:absolute;left:{OX+x0*S}px;top:{OY+y0*S}px;width:{(x1-x0)*S}px;border-top:2px solid #8A8F99"></div>'
                f'<div style="position:absolute;left:{OX+x0*S}px;top:{OY+y0*S-(28 if side=="top" else -4)}px;width:{(x1-x0)*S}px;text-align:center;font:700 16px Poppins;color:#5A606B">{txt}</div>')
    return (f'<div style="position:absolute;left:{OX+x0*S}px;top:{OY+y0*S}px;height:{(y1-y0)*S}px;border-left:2px solid #8A8F99"></div>'
            f'<div style="position:absolute;left:{OX+x0*S-(64 if side=="left" else -10)}px;top:{OY+(y0+y1)/2*S-10}px;font:700 16px Poppins;color:#5A606B">{txt}</div>')


def page():
    plan = ''
    # walls
    plan += f'<div style="position:absolute;left:{OX-14}px;top:{OY-14}px;width:{6*S+28}px;height:14px;background:#9BA0A8"></div>'
    plan += f'<div style="position:absolute;left:{OX-14}px;top:{OY-14}px;width:14px;height:{2.4*S+14}px;background:#9BA0A8"></div>'
    plan += f'<div style="position:absolute;left:{OX+6*S}px;top:{OY-14}px;width:14px;height:{2.4*S+14}px;background:#9BA0A8"></div>'
    plan += f'<div style="position:absolute;left:{OX}px;top:{OY}px;width:{6*S}px;height:{2.4*S}px;background:#F3F1EE;background-image:linear-gradient(#e6e2dc 1px,transparent 1px),linear-gradient(90deg,#e6e2dc 1px,transparent 1px);background-size:{S/2}px {S/2}px"></div>'
    # back tables (bands lying flat)
    plan += r(0.55, 0, 2.4, 0.6, M, 'طاولة سيور ①', '<span dir=ltr style=font-family:Poppins>Whoop · 2.4 × 0.6 m</span>')
    plan += r(3.05, 0, 2.4, 0.6, M, 'طاولة سيور ②', 'Garmin · Fitbit · Apple')
    # left wall: sunglasses shelf + mirror
    plan += r(0, 0.75, 0.4, 1.15, INK, 'نظارات', 'رف جداري', fs=15)
    plan += r(0.08, 1.98, 0.28, 0.32, '#CFD8E0', '🪞', '', fs=18, col=INK)
    # right wall: socks shelf
    plan += r(5.6, 0.75, 0.4, 1.15, '#2F5DA8', 'جوارب', 'رف جداري', fs=15)
    # try-on / UV high table
    plan += r(0.6, 1.55, 0.6, 0.6, '#4D5566', 'UV', 'تجربة', fs=16)
    # cashier
    plan += r(4.35, 1.75, 1.05, 0.55, GOLD, 'الكاشير', 'POS · أكياس', col=INK, fs=17)
    # staff spot
    plan += f'<div style="position:absolute;left:{OX+4.75*S}px;top:{OY+1.38*S}px;width:40px;height:40px;border-radius:50%;background:#fff;border:3px dashed {GOLD};display:flex;align-items:center;justify-content:center;font-size:20px">🧍</div>'
    # aisle
    plan += f'<div style="position:absolute;left:{OX+1.4*S}px;top:{OY+0.85*S}px;width:{2.8*S}px;height:{1.2*S}px;border:3px dashed rgba(114,8,66,.35);border-radius:14px;display:flex;align-items:center;justify-content:center;font:800 20px Cairo;color:rgba(114,8,66,.7)">مساحة الزباين · <span dir=ltr style=font-family:Poppins>1.2 m</span></div>'
    # front opening + arrows
    plan += f'<div style="position:absolute;left:{OX}px;top:{OY+2.4*S}px;width:{6*S}px;height:6px;background:repeating-linear-gradient(90deg,{M} 0 18px,transparent 18px 30px)"></div>'
    plan += f'<div style="position:absolute;left:{OX}px;top:{OY+2.4*S+16}px;width:{6*S}px;text-align:center;font:800 20px Cairo;color:{M};direction:rtl">⬆ المدخل مفتوح كامل · اللوحة فوقه ⬆</div>'
    # floor sign
    plan += r(2.7, 2.78, 0.6, 0.22, '#fff', 'لوحة العرض', '', fs=12, col=M, extra=f'border:2px solid {M}')
    # dims
    plan += dim(0, -0.42, 6, -0.42, '6.0 m')
    plan += dim(-0.32, 0, -0.32, 2.4, '2.4 m', side='left')

    # ---------- back wall elevation ----------
    EY = 900; EH = 2.5 * S * 0.9; ES = S * 0.9  # elevation scale
    ex = lambda m: OX + m * ES * (6 * S) / (6 * ES)  # same width as plan
    sx = (6 * S) / 6   # px per metre horizontally (match plan width)
    sy = ES            # px per metre vertically
    el = f'<div style="position:absolute;left:{OX}px;top:{EY}px;width:{6*sx}px;height:{2.5*sy}px;background:linear-gradient(180deg,{M},{DK})"></div>'
    el += f'<div style="position:absolute;left:{OX}px;top:{EY}px;width:{6*sx}px;height:{2.5*sy}px;background-image:radial-gradient(rgba(255,255,255,.08) 1.6px,transparent 2px);background-size:16px 16px"></div>'
    # banner logo zone
    el += f'<div style="position:absolute;left:{OX+2.2*sx}px;top:{EY+0.15*sy}px;width:{1.6*sx}px;height:{0.55*sy}px;border:2px dashed rgba(255,255,255,.6);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font:800 18px Cairo;direction:rtl">شعار 974 + جملة البراند</div>'
    # slatwall strip above tables for price cards / photos
    el += f'<div style="position:absolute;left:{OX+0.55*sx}px;top:{EY+0.9*sy}px;width:{4.9*sx}px;height:{0.55*sy}px;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.35);border-radius:8px;display:flex;align-items:center;justify-content:space-around;color:#fff;font:700 15px Cairo;direction:rtl"><span>لوحة أسعار + صورة السير على اليد</span><span>لوحة أسعار + صورة السير على اليد</span></div>'
    # tables (0.9m high) with flat trays, slightly tilted
    for x0 in (0.55, 3.05):
        el += f'<div style="position:absolute;left:{OX+x0*sx}px;top:{EY+(2.5-0.9)*sy}px;width:{2.4*sx}px;height:{0.9*sy}px;background:#F4F2EF;border-top:10px solid #E2DED8;box-shadow:0 8px 16px rgba(0,0,0,.35)"></div>'
        el += f'<div style="position:absolute;left:{OX+x0*sx+8}px;top:{EY+(2.5-0.9)*sy+14}px;width:{2.4*sx-16}px;height:{0.9*sy-28}px;border:2px dashed #C9C3BB;display:flex;align-items:center;justify-content:center;font:800 15px Cairo;color:#8A8F99;direction:rtl">مفرش عنابي · المخزون تحت الطاولة</div>'
        # trays on top
        for i in range(4):
            el += f'<div style="position:absolute;left:{OX+x0*sx+10+i*(2.4*sx-20)/4+6}px;top:{EY+(2.5-0.9)*sy-26}px;width:{(2.4*sx-20)/4-12}px;height:24px;background:{INK};border-radius:4px;transform:perspective(200px) rotateX(35deg);box-shadow:0 4px 6px rgba(0,0,0,.4)"></div>'
    # side shelves seen at edges (sunglasses left, socks right) 1.8m tall
    el += f'<div style="position:absolute;left:{OX}px;top:{EY+0.7*sy}px;width:{0.45*sx}px;height:{1.8*sy}px;background:#2A2F38;border-radius:4px 4px 0 0;box-shadow:0 8px 16px rgba(0,0,0,.35)"></div>'
    for i in range(5):
        el += f'<div style="position:absolute;left:{OX+6}px;top:{EY+0.7*sy+20+i*0.34*sy}px;width:{0.45*sx-12}px;height:4px;background:#8A8F99"></div>'
    el += f'<div style="position:absolute;left:{OX+6*sx-0.45*sx}px;top:{EY+0.7*sy}px;width:{0.45*sx}px;height:{1.8*sy}px;background:#2F5DA8;border-radius:4px 4px 0 0;box-shadow:0 8px 16px rgba(0,0,0,.35)"></div>'
    for i in range(5):
        el += f'<div style="position:absolute;left:{OX+6*sx-0.45*sx+6}px;top:{EY+0.7*sy+20+i*0.34*sy}px;width:{0.45*sx-12}px;height:4px;background:#C9D6EE"></div>'
    # height labels
    el += f'<div style="position:absolute;left:{OX+6*sx+18}px;top:{EY+(2.5-0.9)*sy-10}px;font:700 15px Poppins;color:#5A606B">— 90 cm</div>'
    el += f'<div style="position:absolute;left:{OX+6*sx+18}px;top:{EY+0.7*sy-10}px;font:700 15px Poppins;color:#5A606B">— 180 cm</div>'
    el += f'<div style="position:absolute;left:{OX+6*sx+18}px;top:{EY-10}px;font:700 15px Poppins;color:#5A606B">— 250 cm</div>'
    el += f'<div style="position:absolute;left:{OX}px;top:{EY+2.5*sy}px;width:{6*sx}px;height:8px;background:#9BA0A8"></div>'

    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;position:relative;background:#FBFAF8;font-family:Cairo;color:{INK}}}
h2{{position:absolute;right:110px;font-weight:900;font-size:30px;direction:rtl}}
h2 span{{font-family:Poppins;font-size:16px;letter-spacing:4px;color:{M};margin-right:12px}}
.key{{position:absolute;left:{OX+6*S+60}px;width:{W-(OX+6*S+60)-30}px;direction:rtl;font-weight:700;font-size:17px;line-height:1.5}}
.key div{{margin-bottom:10px;display:flex;gap:10px;align-items:flex-start}}
.key i{{flex:0 0 22px;height:22px;border-radius:5px;margin-top:4px}}
</style></head><body>
<h2 style="top:40px">مخطط البوث من فوق <span>TOP VIEW · TO SCALE</span></h2>
{plan}
<div class="key" style="top:{OY}px">
<div><i style="background:{M}"></i><span><b>طاولتين للسيور على الجدار الخلفي.</b> السيور مفرودة في صواني سودا مايلة شوي، كل صينية لنوع.</span></div>
<div><i style="background:{INK}"></i><span><b>النظارات على الجدار اليسار.</b> رف عالي، وجنبه مراية.</span></div>
<div><i style="background:#4D5566"></i><span><b>طاولة تجربة صغيرة</b> عليها كشاف الـ UV.</span></div>
<div><i style="background:#2F5DA8"></i><span><b>الجوارب على الجدار اليمين</b>، مقسمة حسب المقاس.</span></div>
<div><i style="background:{GOLD}"></i><span><b>الكاشير قدام على اليمين</b>، عند طريق الطلعة.</span></div>
</div>
<h2 style="top:{900-72}px">الجدار الخلفي من قدام <span>BACK WALL VIEW</span></h2>
{el}
<div style="position:absolute;left:24px;bottom:16px;font:700 13px Poppins;color:#9AA0AA;letter-spacing:2px">974GROUP · T100 EXPO BOOTH PLAN · 6.0 × 2.4 M</div>
</body></html>'''


if __name__ == '__main__':
    out = R + 'posts/2026-11/expo-booth/974-t100-booth-plan.png'
    p = out.replace('.png', '.html'); open(p, 'w').write(page())
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}},deviceScaleFactor:1.25}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd=R)
    print('ok')
