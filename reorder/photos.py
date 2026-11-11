# One photo per item to send to suppliers: site photo on white + a small label (product · colour). Grouped per supplier.
import os, sys, re, zipfile, subprocess
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, D)
from rows import ROWS, BASE
order = [l.split()[1] for l in open(D + 'urls.txt')]
sheets = [Image.open(D + f'sheets/s{i}.png').convert('RGBA') for i in range(8)]
FB = ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf', 34)
FM = ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf', 30)
S = 680
SUP = {'1': 'Supplier-1', '2': 'Supplier-2', '3': 'Supplier-3', 'X': 'Other-suppliers'}
out = D + 'photos/'; os.makedirs(out, exist_ok=True)
made = {}
for sup, p, v, q, s30, s60, img in ROWS:
    rate = max(s30 / 30, s60 / 60); days = 0 if q <= 0 else round(q / rate); sug = max(0, round(rate * 60 - q))
    if (q > 0 and days > 45) or sug <= 0: continue
    i = order.index(BASE + img); sh = sheets[i // 9]; c = i % 9
    cell = sh.crop(((c % 3) * S, (c // 3) * S, (c % 3) * S + S, (c // 3) * S + S))
    W = 1000; canvas = Image.new('RGB', (W, W + 150), 'white')
    bb = cell.getbbox() or (0, 0, S, S); cell = cell.crop(bb); cell.thumbnail((880, 880), Image.LANCZOS)
    canvas.paste(cell, ((W - cell.width) // 2, 40 + (900 - cell.height) // 2), cell)
    d = ImageDraw.Draw(canvas)
    d.line((60, W - 30, W - 60, W - 30), fill='#E7E1E4', width=2)
    def fit(t, f, mw=880):
        while d.textlength(t, font=f) > mw and len(t) > 4: t = t[:-2]
        return t
    d.text((W / 2, W + 20), fit(p, FB), font=FB, fill='#1d1a1c', anchor='mm')
    if v: d.text((W / 2, W + 72), fit(v, FM), font=FM, fill='#720842', anchor='mm')
    folder = out + SUP[sup] + '/'; os.makedirs(folder, exist_ok=True)
    name = re.sub(r'[^A-Za-z0-9]+', '-', f'{p} {v}').strip('-')
    canvas.save(folder + name + '.jpg', quality=90)
    made.setdefault(sup, []).append(name)
for sup, names in made.items():
    z = D + f'out/974-reorder-photos-{SUP[sup]}.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for n in names: zf.write(out + SUP[sup] + '/' + n + '.jpg', SUP[sup] + '/' + n + '.jpg')
    print(SUP[sup], len(names))
