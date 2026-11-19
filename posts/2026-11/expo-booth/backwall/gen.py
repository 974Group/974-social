# T100 expo booth — back-wall print (6000 x 2400 mm). 1 CSS px = 1 mm. 19 Nov 2026
# Outputs: vector PDF at 1:10 scale (600 x 240 mm) for the printer, PNG preview, and a preview with tables/shelves overlaid.
import subprocess, qrcode, re
D = '/home/claude/974-social/posts/2026-11/expo-booth/backwall/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'
W, H = 6000, 2400
URL = 'https://974group.net/?utm_source=expo&utm_medium=booth&utm_campaign=t100'

logo = open(D + 'logo-974.svg').read()
vb = re.search(r'viewBox="([^"]+)"', logo).group(1)
lpath = re.search(r'<path[^>]*d="([^"]+)"', logo).group(1)


def logo_svg(h, fill, extra=''):
    w0, h0 = map(float, vb.split()[2:])
    return f'<svg viewBox="{vb}" style="height:{h}px;width:{h*w0/h0:.0f}px;{extra}"><path fill-rule="evenodd" fill="{fill}" d="{lpath}"/></svg>'


def qr_svg(size):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
    q.add_data(URL); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    rects = ''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" style="width:{size}px;height:{size}px;display:block" shape-rendering="crispEdges"><g fill="#1A1E26">{rects}</g></svg>'


def ig_icon(s, col):
    return (f'<svg viewBox="0 0 100 100" style="width:{s}px;height:{s}px"><rect x="6" y="6" width="88" height="88" rx="26" fill="none" stroke="{col}" stroke-width="9"/>'
            f'<circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="9"/><circle cx="74" cy="26" r="6" fill="{col}"/></svg>')


def page(guides=False):
    g = ''
    if guides:
        # tables 0.9 m high at x 550-2950 and 3050-5450; side shelves 450 mm wide, 1.8 m high
        for x0 in (550, 3050):
            g += f'<div style="position:absolute;left:{x0}px;top:{H-900}px;width:2400px;height:900px;background:rgba(244,242,239,.93);border-top:40px solid #E2DED8"></div>'
            g += f'<div style="position:absolute;left:{x0}px;top:{H-900-110}px;width:2400px;height:110px;display:flex;gap:40px;padding:0 40px">' + ''.join('<div style="flex:1;background:#1A1E26;border-radius:20px"></div>' for _ in range(4)) + '</div>'
        g += f'<div style="position:absolute;left:0;top:{H-1800}px;width:450px;height:1800px;background:rgba(42,47,56,.93)"></div>'
        g += f'<div style="position:absolute;left:{W-450}px;top:{H-1800}px;width:450px;height:1800px;background:rgba(47,93,168,.93)"></div>'
        g += f'<div style="position:absolute;left:0;right:0;top:{H-900}px;border-top:8px dashed rgba(255,255,255,.6)"></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:600mm 240mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{background:{DK}}}html,body{{width:{W}px;height:{H}px}}
body{{position:relative;overflow:hidden;font-family:Cairo;color:#fff;
background:radial-gradient(ellipse 2600px 1300px at 50% 18%,#9A1460 0%,rgba(154,20,96,0) 70%),linear-gradient(180deg,{M} 0%,#650638 55%,{DK} 100%);background-repeat:no-repeat}}
.c{{position:absolute;left:0;right:0;text-align:center}}
.sell{{position:absolute;left:0;right:0;top:1100px;display:flex;justify-content:center;gap:46px}}
.sell .ch{{border:5px solid {GOLD};border-radius:60px;padding:14px 56px 18px;text-align:center}}
.sell .en{{font-family:Poppins;font-weight:700;font-size:62px;letter-spacing:8px;color:{GOLD};line-height:1.15}}
.sell .ar{{font-weight:800;font-size:58px;line-height:1.1;direction:rtl}}
.lbl{{position:absolute;top:1105px;width:2400px;text-align:center}}
.lbl .en{{font-family:Poppins;font-weight:700;font-size:88px;letter-spacing:20px;color:{GOLD}}}
.lbl .ar{{font-weight:800;font-size:66px;opacity:.9;margin-top:-6px}}
.lbl .ln{{width:1500px;height:6px;margin:26px auto 0;background:linear-gradient(90deg,transparent,{GOLD},transparent)}}
</style></head><body>
<!-- giant faded mark -->
{logo_svg(2300, 'rgba(255,255,255,.035)', f'position:absolute;right:-700px;top:300px')}
{logo_svg(2300, 'rgba(255,255,255,.035)', f'position:absolute;left:-900px;top:-900px')}
<!-- centre: logo + taglines -->
<div class="c" style="top:120px">{logo_svg(500, '#fff')}</div>
<div class="c" style="top:660px;font-family:Poppins;font-weight:700;font-size:100px;letter-spacing:26px">A QATARI BRAND · BUILT FOR RACE DAY</div>
<div class="c" style="top:790px;font-weight:900;font-size:140px;color:{GOLD};direction:rtl">براند قطري.. جاهز ليوم السباق</div>
<!-- left: instagram -->
<div style="position:absolute;left:600px;top:170px;width:860px;text-align:center">
  {ig_icon(230, '#fff')}
  <div style="font-family:Poppins;font-weight:700;font-size:96px;margin-top:20px">@974.group</div>
  <div style="font-family:Poppins;font-weight:700;font-size:62px;color:{GOLD};letter-spacing:4px">FOLLOW US</div>
  <div style="font-weight:800;font-size:66px;color:{GOLD};direction:rtl;margin-top:-10px">تابعنا على الانستا</div>
</div>
<!-- right: QR -->
<div style="position:absolute;left:4560px;top:150px;width:860px;text-align:center">
  <div style="display:inline-block;background:#fff;border-radius:44px;padding:44px">{qr_svg(380)}</div>
  <div style="font-family:Poppins;font-weight:700;font-size:62px;letter-spacing:4px;margin-top:22px">SCAN &amp; SHOP</div>
  <div style="font-weight:900;font-size:70px;direction:rtl;margin-top:-10px">امسح وتسوّق</div>
  <div style="font-family:Poppins;font-weight:700;font-size:66px;color:{GOLD}">974group.net</div>
</div>
<!-- what we sell: one centred row, not tied to where things stand -->
<div class="sell"><div class="ch"><div class="en">WHOOP BANDS</div><div class="ar">سيور ووب</div></div><div class="ch"><div class="en">GARMIN BANDS</div><div class="ar">سيور قارمن</div></div><div class="ch"><div class="en">FITBIT BANDS</div><div class="ar">سيور فت بت</div></div><div class="ch"><div class="en">SUNGLASSES</div><div class="ar">نظارات</div></div><div class="ch"><div class="en">SOCKS</div><div class="ar">دلاغات</div></div></div>
{g}
</body></html>'''


def run(html, name, pdf=False, guides=False):
    p = D + name + '.html'; open(p, 'w').write(html)
    if pdf:
        js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{p}');await p.waitForTimeout(1200);await p.pdf({{path:'{D}{name}.pdf',width:'600mm',height:'240mm',printBackground:true,scale:{600/(W*25.4/96):.6f},pageRanges:'1'}});await b.close();}})()"
    else:
        js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}},deviceScaleFactor:0.4}});await p.goto('file://{p}');await p.waitForTimeout(1200);await p.screenshot({{path:'{D}{name}.png'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    run(page(), '974-booth-backwall-6000x2400mm-scale-1to10', pdf=True)
    run(page(), '974-booth-backwall-preview')
    run(page(True), '974-booth-backwall-with-tables-preview')
    print('ok')
