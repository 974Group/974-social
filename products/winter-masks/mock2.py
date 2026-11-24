# Product-style neck-gaiter mockup (our own geometry): tilted top opening, scrunched folds low down, flared bottom.
# One image per design, 1200x1200 on a light studio background.
import numpy as np, glob, os, math
from PIL import Image, ImageFilter, ImageDraw
D = os.path.dirname(os.path.abspath(__file__))
S = 1200; CX = 600
YT, YB = 300, 1000          # rim centres
RT, RB = 300, 345           # half widths at top/bottom
RYT, RYB = 70, 62           # ellipse half-heights
TILT = 0.10                 # top rim higher on the right
FOLDS = [(0.58, 1.1), (0.72, 1.4), (0.85, 1.2)]

def prof(t):                # half-width multiplier with bulges at the folds
    b = sum(a * 0.035 * np.exp(-((t - c) / 0.05) ** 2) for c, a in FOLDS)
    return 1 + b

def make(src, out):
    im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255; ih, iw = im.shape[:2]
    ys, xs = np.mgrid[0:S, 0:S].astype(float)
    t0 = np.clip((ys - YT) / (YB - YT), 0, 1)
    hw = (RT + (RB - RT) * t0) * prof(t0)
    nx = (xs - CX) / hw; inside = np.abs(nx) < 1
    nc = np.clip(nx, -.999, .999); dep = np.sqrt(1 - nc ** 2)
    ytop = YT + RYT * dep - TILT * (xs - CX); ybot = YB + RYB * dep
    v = (ys - ytop) / (ybot - ytop)
    body = inside & (v >= 0) & (v <= 1)
    # folds: compress the print at each crease, shade above/below
    vv = v.copy(); sh = np.zeros_like(v)
    for c, a in FOLDS:
        wob = c + 0.018 * np.sin(nc * 3.2 + c * 17)
        g = np.exp(-((v - wob) / 0.04) ** 2) * a
        vv = vv + 0.010 * g
        sh += 0.20 * g * np.tanh((wob - v) / 0.02)
    u = 0.5 + np.arcsin(nc) / np.pi * 0.80
    px = np.clip((u * (iw - 1)).astype(int), 0, iw - 1); py = np.clip((np.clip(vv, 0, 1) * (ih - 1)).astype(int), 0, ih - 1)
    col = im[py, px]
    light = 0.60 + 0.40 * dep ** 0.55 + 0.10 * np.clip(-nc, 0, 1) * dep
    # fabric grain
    rng = np.random.default_rng(1); grain = rng.normal(0, 0.012, (S, S))
    col = np.clip(col * np.clip(light + sh, .35, 1.15)[..., None] + grain[..., None], 0, 1)
    # inside of the tube visible through the tilted opening
    ell = ((xs - CX) / (RT + 2)) ** 2 + ((ys - (YT - TILT * (xs - CX))) / RYT) ** 2
    inner = (ell < 1.02) & ~body
    base_in = im[ih // 2, :, :].mean(axis=0)
    shade_in = 0.30 + 0.25 * ((xs - CX) / RT + 1) / 2
    rgb = np.where(body[..., None], col, base_in * shade_in[..., None])
    a = (body | inner).astype(float)
    # rim highlight (hem) on the front lip
    hem = body & (v < 0.012)
    rgb = np.where(hem[..., None], np.clip(rgb * 1.18, 0, 1), rgb)
    A = Image.fromarray((a * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.1))
    obj = Image.fromarray((rgb * 255).astype('uint8')).convert('RGBA'); obj.putalpha(A)
    bg = Image.new('RGBA', (S, S), (247, 247, 248, 255))
    shd = Image.new('L', (S, S), 0); ImageDraw.Draw(shd).ellipse([CX - 360, YB + 15, CX + 360, YB + 95], fill=90)
    bg.paste((0, 0, 0, 255), (0, 0), shd.filter(ImageFilter.GaussianBlur(26)))
    bg.alpha_composite(obj); bg.convert('RGB').save(out, quality=93)

if __name__ == '__main__':
    for f in sorted(glob.glob(D + '/flat/*.png')):
        make(f, D + '/single/974-mask-' + os.path.basename(f)[:-4] + '.jpg')
    print('ok')
