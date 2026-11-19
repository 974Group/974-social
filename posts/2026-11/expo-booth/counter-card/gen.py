# Counter card for the T100 booth: A5 portrait (148 x 210 mm) + 3 mm bleed, vector PDF. 19 Nov 2026
import subprocess, qrcode, re, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
D = '/home/claude/974-social/posts/2026-11/expo-booth/counter-card/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
LOGO = open('/home/claude/974-social/posts/2026-11/expo-booth/backwall/logo-974.svg').read()
vb = re.search(r'viewBox="([^"]+)"', LOGO).group(1)
lpath = re.search(r'<path[^>]*d="([^"]+)"', LOGO).group(1)
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'; INK = '#1A1E26'
IG = 'https://instagram.com/974.group'
WEB = 'https://974group.net/?utm_source=expo&utm_medium=counter&utm_campaign=t100'
BW, BH, B = 148, 210, 3   # trim size + bleed (mm)


def qr(url, mm):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    r = ''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" style="width:{mm}mm;height:{mm}mm;display:block;margin:0 auto" shape-rendering="crispEdges"><g fill="{INK}">{r}</g></svg>'


def ig_icon(mm, col):
    return (f'<svg viewBox="0 0 100 100" style="width:{mm}mm;height:{mm}mm"><rect x="6" y="6" width="88" height="88" rx="26" fill="none" stroke="{col}" stroke-width="10"/>'
            f'<circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="10"/><circle cx="74" cy="26" r="6.5" fill="{col}"/></svg>')


def globe_icon(mm, col):
    return (f'<svg viewBox="0 0 100 100" style="width:{mm}mm;height:{mm}mm"><circle cx="50" cy="50" r="42" fill="none" stroke="{col}" stroke-width="9"/>'
            f'<ellipse cx="50" cy="50" rx="18" ry="42" fill="none" stroke="{col}" stroke-width="8"/><line x1="8" y1="50" x2="92" y2="50" stroke="{col}" stroke-width="8"/></svg>')


def page():
    W, H = BW + 2 * B, BH + 2 * B
    w0, h0 = map(float, vb.split()[2:])
    lh = 17
    card = lambda icon, en, ar, url, handle: f'''<div class="card">
  <div class="ic">{icon}</div>
  <div class="en">{en}</div><div class="ar">{ar}</div>
  <div class="q">{qr(url, 42)}</div>
  <div class="hd">{handle}</div></div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:{W}mm {H}mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{background:{DK};overflow:hidden;width:{W}mm;height:{H}mm}}
body{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;font-family:Cairo;color:#fff;
background:radial-gradient(ellipse 120mm 90mm at 50% 18%,#9A1460 0%,rgba(154,20,96,0) 70%),linear-gradient(180deg,{M} 0%,{DK} 100%);background-repeat:no-repeat}}
.wm{{position:absolute;right:-40mm;bottom:-18mm;opacity:.05}}
.logo{{position:absolute;left:0;right:0;top:{B+12}mm;text-align:center}}
.tag{{position:absolute;left:0;right:0;top:{B+33}mm;text-align:center;font-family:Poppins;font-weight:700;font-size:3.6mm;letter-spacing:1.6mm;color:{GOLD}}}
.tagar{{position:absolute;left:0;right:0;top:{B+38.5}mm;text-align:center;font-weight:900;font-size:7mm;direction:rtl}}
.cards{{position:absolute;left:{B+8}mm;right:{B+8}mm;top:{B+56}mm;display:flex;gap:6mm}}
.card{{flex:1;background:#fff;border-radius:6mm;color:{INK};text-align:center;padding:5mm 3mm 4.5mm}}
.card .ic{{display:flex;justify-content:center}}
.card .en{{font-family:Poppins;font-weight:700;font-size:3.4mm;letter-spacing:.6mm;margin-top:2mm;color:{M}}}
.card .ar{{font-weight:900;font-size:4.6mm;direction:rtl;margin-top:-.6mm}}
.card .q{{margin-top:3mm}}
.card .hd{{font-family:Poppins;font-weight:700;font-size:3.5mm;margin-top:3mm}}
.pay{{position:absolute;left:{B+8}mm;right:{B+8}mm;top:{B+150}mm;text-align:center}}
.pay .t{{font-weight:800;font-size:4.2mm;direction:rtl;margin-bottom:2.5mm}}
.pay .t span{{font-family:Poppins;font-weight:700;font-size:3.2mm;letter-spacing:.5mm;color:{GOLD};margin-right:2mm}}
.pf{{display:inline-block;transform-origin:top center}}
.thanks{{position:absolute;left:0;right:0;bottom:{B+10}mm;text-align:center;direction:rtl;font-weight:800;font-size:4.4mm;color:{GOLD}}}
{payfoot.css(1.0)}
.pf .payfoot .av{{display:none}}
</style></head><body>
<svg class="wm" viewBox="{vb}" style="width:150mm"><path fill-rule="evenodd" fill="#fff" d="{lpath}"/></svg>
<div class="logo"><svg viewBox="{vb}" style="height:{lh}mm;width:{lh*w0/h0:.1f}mm"><path fill-rule="evenodd" fill="#fff" d="{lpath}"/></svg></div>
<div class="tag">SCAN · FOLLOW · SHOP</div>
<div class="tagar">امسح.. وخلك قريب منّا</div>
<div class="cards">
{card(ig_icon(11, M), 'FOLLOW US', 'تابعنا على الانستا', IG, '@974.group')}
{card(globe_icon(11, M), 'SHOP ONLINE', 'تسوّق من الموقع', WEB, '974group.net')}
</div>
<div class="pay"><div class="t">طرق الدفع<span>WE ACCEPT</span></div><div class="pf">{payfoot.html()}</div></div>
<div class="thanks">شكراً لزيارتكم 🤍 THANK YOU</div>
</body></html>'''


def run():
    html = page(); p = D + 'counter.html'; open(p, 'w').write(html)
    W, H = BW + 2 * B, BH + 2 * B
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{round(W*96/25.4)},height:{round(H*96/25.4)}}},deviceScaleFactor:3}});"
          f"await p.goto('file://{p}');await p.waitForTimeout(1200);"
          f"await p.pdf({{path:'{D}974-counter-card-A5-3mm-bleed.pdf',width:'{W}mm',height:'{H}mm',printBackground:true,pageRanges:'1'}});"
          f"await p.screenshot({{path:'{D}974-counter-card-preview.png'}});await b.close();}})()")
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    run(); print('ok')
