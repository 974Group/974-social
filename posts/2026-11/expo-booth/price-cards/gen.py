# T100 booth price cards: A6 portrait (105 x 148 mm) + 3 mm bleed, one card per page, vector PDF. 19 Nov 2026
# Add band cards to CARDS once the owner decides which bands go to the expo.
import subprocess, qrcode, re
D = '/home/claude/974-social/posts/2026-11/expo-booth/price-cards/'
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
LOGO = open('/home/claude/974-social/posts/2026-11/expo-booth/backwall/logo-974.svg').read()
vb = re.search(r'viewBox="([^"]+)"', LOGO).group(1)
lpath = re.search(r'<path[^>]*d="([^"]+)"', LOGO).group(1)
M = '#720842'; DK = '#51022D'; GOLD = '#C9A24B'; INK = '#1A1E26'; SOFT = '#F4F1F2'
UTM = 'utm_source=expo&utm_medium=pricecard&utm_campaign=t100'
BW, BH, B = 105, 148, 3

# each card: eyebrow (EN), title (AR), sub (AR), price line(s), note, link path
CARDS = [
    dict(key='sunglasses', eb='SUNGLASSES', t='نظارات شمسية', te='Sunglasses', sub='10 موديلات.. كل وحدة باسم مكان في قطر', sube='10 models, each named after a place in Qatar',
         prices=[('كل الموديلات', 'All models', '319')], note='<div class=names>' + ''.join(f'<span>{n}</span>' for n in ['LUSAIL','HALUL','ZUBARAH','DOHA','THE PEARL','DUKHAN','FUWAIRIT','AL RUWAIS','SEALINE','KHOR AL ADAID']) + '</div>',
         link='/collections/sun-glasses'),
    dict(key='goggles-2in1', eb='GOGGLES · 2 IN 1', t='نظارة <span dir=ltr style="font-family:Poppins;font-weight:900">2 in 1</span>', te='2 in 1 Goggles', sub='للدراجة والبر.. 6 ألوان', sube='For bikes and the desert · 6 colours',
         prices=[('كل الألوان', 'All colours', '249')], note='', link='/products/summer-edition-goggles'),
    dict(key='runner-pro', eb='RUNNING SOCKS', t='جوارب الجري', te='The Runner Pro · V2', sub='خفيفة وتتنفس.. للجري والتمرين', sube='Light and breathable, for running and training',
         prices=[('الزوج', 'Per pair', '59')], note='', link='/collections/running-socks'),
    dict(key='grip', eb='GRIP SOCKS', t='جوارب Grip', te='Grip Socks', sub='ما تزلق.. للكورة والجيم', sube='Anti-slip, for football and the gym',
         prices=[('رمادي · أحمر · عنابي · أزرق', 'Grey · Red · Maroon · Blue', '39'), ('أبيض · أسود', 'White · Black', '60')], note='', link='/collections/grip-socks'),
    dict(key='pilates', eb='PILATES CLUB', t='جوارب البيلاتيس', te='Pilates Club Grip Socks', sub='12 تصميم', sube='12 designs',
         prices=[('الزوج', 'Per pair', '49')], note='', link='/products/pilates-club-grip-socks'),
]


def qr(url, mm):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    r = ''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" style="width:{mm}mm;height:{mm}mm;display:block" shape-rendering="crispEdges"><g fill="{INK}">{r}</g></svg>'


def card_html(c):
    W, H = BW + 2 * B, BH + 2 * B
    w0, h0 = map(float, vb.split()[2:])
    rows = ''
    for p in c['prices']:
        lab, labe, now = p[0], p[1], p[2]
        was = ''
        big = len(c['prices']) == 1
        rows += f'''<div class="row{' big' if big else ''}"><span class="lab">{lab}<em>{labe}</em></span><span class="pr">{was}<b>{now}</b><small style="font-family:Poppins">QAR</small></span></div>'''
    url = f"https://974group.net{c['link']}{'&' if '?' in c['link'] else '?'}{UTM}"
    return f'''<section style="width:{W}mm;height:{H}mm">
<div class="top"><svg viewBox="{vb}" style="height:9mm;width:{9*w0/h0:.1f}mm"><path fill-rule="evenodd" fill="#fff" d="{lpath}"/></svg><span>{c['eb']}</span></div>
<div class="body">
  <h1>{c['t']}</h1><div class="te">{c['te']}</div><div class="sub">{c['sub']}</div><div class="sube">{c['sube']}</div>
  <div class="prices">{rows}</div>
  {f'<div class="note">{c["note"]}</div>' if c['note'] else ''}
</div>
<div class="foot"><div class="q">{qr(url, 20)}</div><div class="ft"><b>امسح وشوف كل الألوان</b><span>SCAN FOR ALL COLOURS</span><span class="u">974group.net</span></div></div>
</section>'''


def page():
    W, H = BW + 2 * B, BH + 2 * B
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:{W}mm {H}mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}mm;background:#fff}}
section{{position:relative;overflow:hidden;background:{SOFT};page-break-after:always;font-family:Cairo;color:{INK}}}
.top{{position:absolute;left:0;right:0;top:0;height:{B+19}mm;background:linear-gradient(135deg,{M},{DK});display:flex;align-items:flex-end;justify-content:space-between;padding:0 {B+7}mm 5mm}}
.top span{{font-family:Poppins;font-weight:700;font-size:2.9mm;letter-spacing:.9mm;color:{GOLD}}}
.body{{position:absolute;left:{B+7}mm;right:{B+7}mm;top:{B+26}mm;text-align:right;direction:rtl}}
h1{{font-weight:900;font-size:9.5mm;line-height:1.15}}
.sub{{font-weight:700;font-size:3.9mm;color:#5a5560;margin-top:1mm}}
.prices{{margin-top:5mm;display:flex;flex-direction:column;gap:3mm}}
.row{{display:flex;justify-content:space-between;align-items:center;background:#fff;border-radius:3.5mm;padding:2.5mm 4mm;box-shadow:0 .6mm 1.5mm rgba(0,0,0,.08)}}
.row .lab{{font-weight:800;font-size:3.7mm;line-height:1.25}}
.row .lab em{{display:block;font-style:normal;font-family:Poppins;font-weight:700;font-size:2.6mm;color:#7a7380;direction:ltr;text-align:right}}
.te{{font-family:Poppins;font-weight:700;font-size:4.4mm;color:{M};direction:ltr;text-align:right;margin-top:-.5mm}}
.sube{{font-family:Poppins;font-weight:500;font-size:2.8mm;color:#7a7380;direction:ltr;text-align:right}}
.row .pr{{direction:ltr;font-family:Poppins;color:{M};white-space:nowrap}}
.row .pr b{{font-weight:900;font-size:8.5mm}}
.row .pr small{{font-family:Cairo;font-weight:800;font-size:3.4mm;margin-left:1mm}}
.row .pr s{{font-weight:700;font-size:3.6mm;color:#9a8f96;margin-right:1.5mm}}
.row.big{{flex-direction:column;align-items:flex-end;padding:3mm 5mm}}
.row.big .pr b{{font-size:17mm;line-height:1}}
.row.big .pr small{{font-size:5mm}}
.note{{margin-top:4mm;font-size:3.5mm;font-weight:700;color:#5a5560;line-height:1.55}}
.names{{display:flex;flex-wrap:wrap;gap:1.6mm;direction:ltr;justify-content:flex-end}}.names span{{font-family:Poppins;font-weight:700;font-size:2.6mm;background:#fff;border-radius:2mm;padding:.6mm 2mm;white-space:nowrap;color:{M}}}
.note b{{display:inline-block;background:{GOLD};color:{DK};border-radius:3mm;padding:.6mm 3mm 1.2mm;font-size:4.6mm;font-weight:900}}
.foot{{position:absolute;left:{B+7}mm;right:{B+7}mm;bottom:{B+6}mm;display:flex;align-items:center;gap:4mm;direction:rtl;border-top:.4mm solid rgba(114,8,66,.2);padding-top:4mm}}
.foot .q{{background:#fff;padding:1.5mm;border-radius:2mm}}
.ft{{display:flex;flex-direction:column}}
.ft b{{font-weight:900;font-size:3.8mm}}
.ft span{{font-family:Poppins;font-weight:700;font-size:2.4mm;letter-spacing:.4mm;color:{M};direction:ltr;text-align:right}}
.ft .u{{color:#5a5560;letter-spacing:0;font-size:2.8mm}}
</style></head><body>{''.join(card_html(c) for c in CARDS)}</body></html>'''


if __name__ == '__main__':
    html = page(); p = D + 'cards.html'; open(p, 'w').write(html)
    W, H = BW + 2 * B, BH + 2 * B
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{round(W*96/25.4)},height:{round(H*96/25.4)}}},deviceScaleFactor:2}});"
          f"await p.goto('file://{p}');await p.waitForTimeout(1200);"
          f"await p.pdf({{path:'{D}974-price-cards-A6-3mm-bleed.pdf',width:'{W}mm',height:'{H}mm',printBackground:true}});"
          f"await p.screenshot({{path:'{D}all.png',fullPage:true}});await b.close();}})()")
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')
    # contact sheet
    from PIL import Image
    im = Image.open(D + 'all.png'); n = len(CARDS); h = im.height // n
    tiles = [im.crop((0, i * h, im.width, (i + 1) * h)) for i in range(n)]
    sheet = Image.new('RGB', (im.width * n + 20 * (n - 1), h), 'white')
    for i, t in enumerate(tiles): sheet.paste(t, (i * (im.width + 20), 0))
    sheet.save(D + '974-price-cards-preview.png'); print('ok', n)
