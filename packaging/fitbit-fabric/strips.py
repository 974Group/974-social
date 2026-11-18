# Flat fabric strip as it lies in the white drawer. Texture = a clean patch of the real band photo,
# kept at true weave scale (band face ~30% of photo width = 19 mm) and tiled with feathered seams.
import numpy as np
from PIL import Image, ImageFilter
SRC = '/home/claude/974-social/products/fitbit-fabric-blush/src/'
PX = 300/25.4
SW, SH = round(19*PX), round(52*PX)
def feather_tile(p, W, H, ov=14):
    p = np.asarray(p).astype(np.float32); ph, pw = p.shape[:2]
    out = np.zeros((H, W, 3), np.float32); wt = np.zeros((H, W, 1), np.float32)
    ramp_x = np.minimum(1, np.minimum(np.arange(pw)+1, pw-np.arange(pw)) / ov)
    ramp_y = np.minimum(1, np.minimum(np.arange(ph)+1, ph-np.arange(ph)) / ov)
    m = (ramp_y[:, None] * ramp_x[None, :])[..., None]
    sy = ph - ov; sx = pw - ov
    for r, y in enumerate(range(-ov, H, sy)):
        off = (r * pw // 3) % sx
        for x in range(-ov - off, W, sx):
            y0, x0 = max(y, 0), max(x, 0); y1, x1 = min(y+ph, H), min(x+pw, W)
            if y1 <= y0 or x1 <= x0: continue
            sl = (slice(y0-y, y1-y), slice(x0-x, x1-x))
            out[y0:y1, x0:x1] += p[sl] * m[sl]; wt[y0:y1, x0:x1] += m[sl]
    return out / np.maximum(wt, 1e-3)
def strip(colour, rel=(.15, .36, .25, .60), ang=-6):
    im = Image.open(SRC + colour + '-cut.png').convert('RGBA')
    x0, y0, x1, y1 = im.getbbox(); w, h = x1-x0, y1-y0
    im = im.rotate(ang, resample=Image.BICUBIC, center=((x0+x1)/2, (y0+y1)/2))
    c = im.crop((x0+int(rel[0]*w), y0+int(rel[1]*h), x0+int(rel[2]*w), y0+int(rel[3]*h)))
    ok = (np.asarray(c)[..., 3] > 250).mean()
    k = SW / (0.30*w)
    c = c.convert('RGB').resize((max(8, int(c.width*k)), max(8, int(c.height*k))), Image.LANCZOS)
    # flatten the photo's lighting so tiles don't show light/dark bands
    a = np.asarray(c).astype(np.float32); lo = np.asarray(c.filter(ImageFilter.GaussianBlur(18))).astype(np.float32)
    a = a / np.maximum(lo, 1) * a.reshape(-1, 3).mean(0)
    c = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    arr = feather_tile(c, SW, SH)
    edge = int(SW*.06)
    sh = np.array([.72 if min(i, SW-1-i) < edge else .94 + .06*np.sin(np.pi*i/SW) for i in range(SW)], np.float32)
    s = Image.fromarray(np.clip(arr*sh[None, :, None], 0, 255).astype(np.uint8))
    out = Image.new('RGBA', (SW+40, SH), (0, 0, 0, 0))
    shadow = Image.new('RGBA', (SW, SH), (0, 0, 0, 90)).filter(ImageFilter.GaussianBlur(6))
    out.alpha_composite(shadow, (24, 0)); out.paste(s, (20, 0))
    out.save(f'strips/{colour}.png')
    return ok
if __name__ == '__main__':
    for col in ['grey', 'blush', 'fog', 'olive', 'black', 'purple', 'pinky-red', 'light-pink']:
        print(col, round(strip(col), 3))
