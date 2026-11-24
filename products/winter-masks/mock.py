# Wrap a flat print onto a neck-gaiter tube mockup (front view, folds, soft shading). Output 900x1000 RGBA.
import numpy as np, glob, os
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__))
W, H = 900, 1000; CX = 450; YT, YB = 170, 880; RY = 62

def halfw(y):  # tube flares slightly at the bottom
    t = (y - YT) / (YB - YT); return 300 + 40 * t

def fold(v, nx):
    # soft horizontal scrunch folds in the lower half: tiny displacement + light/dark bands
    d = np.zeros_like(v); sh = np.zeros_like(v)
    for c, a in ((0.66, 1.0), (0.80, 1.2), (0.92, 0.9)):
        wob = c + 0.02 * np.sin(nx * 3.5 + c * 20)
        g = np.exp(-((v - wob) / 0.035) ** 2) * a
        d += 0.012 * g
        sh += 0.22 * g * np.sign(v - wob + 1e-6) * -1   # lighter above the crease, darker below
    return d, sh

def make(src, out):
    im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255; ih, iw = im.shape[:2]
    ys, xs = np.mgrid[0:H, 0:W].astype(float)
    hw = halfw(ys); nx = (xs - CX) / hw
    inside = np.abs(nx) < 1
    nxc = np.clip(nx, -0.999, 0.999); depth = np.sqrt(1 - nxc ** 2)
    ytop = YT + RY * depth; ybot = YB + RY * 1.05 * depth
    v = (ys - ytop) / (ybot - ytop)
    # gentle wavy folds: wobble v
    v2 = v
    d, sh = fold(v2, nxc)
    vv = np.clip(v2 + d, 0, 1)
    u = 0.5 + np.arcsin(nxc) / np.pi        # front half of the tube = whole flat print
    px = np.clip((u * (iw - 1)).astype(int), 0, iw - 1); py = np.clip((vv * (ih - 1)).astype(int), 0, ih - 1)
    col = im[py, px]
    light = 0.62 + 0.38 * depth ** 0.6 + 0.08 * np.clip(-nxc, 0, 1) * depth   # soft light from left
    shade = np.clip(light + sh, 0.35, 1.15)[..., None]
    col = np.clip(col * shade, 0, 1)
    body = inside & (v >= 0) & (v <= 1)
    # inner back rim at top: ellipse band seen inside
    ell = ((xs - CX) / (halfw(YT) - 4)) ** 2 + ((ys - YT) / RY) ** 2
    inner = (ell < 1) & (ys < YT + RY * depth) & ~body
    rim = im[min(ih - 1, 20), :, :].mean(axis=0) * 0.45
    rgb = np.where(body[..., None], col, 0)
    rgb = np.where(inner[..., None], rim, rgb)
    a = (body | inner).astype(float)
    A = Image.fromarray((a * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    img = Image.fromarray((rgb * 255).astype('uint8')); img.putalpha(A)
    # soft floor shadow
    sh_ = Image.new('L', (W, H), 0); import PIL.ImageDraw as Dr
    Dr.Draw(sh_).ellipse([CX - 330, YB + 30, CX + 330, YB + 110], fill=110)
    sh_ = sh_.filter(ImageFilter.GaussianBlur(22))
    base = Image.new('RGBA', (W, H), (0, 0, 0, 0)); base.putalpha(sh_)
    base.alpha_composite(img); base.save(out)

for f in sorted(glob.glob(D + '/flat/*.png')):
    make(f, D + '/mock/' + os.path.basename(f))
print('ok')
