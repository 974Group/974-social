# Cel-shade a product cutout (RGBA png) into a comic/poster look:
# smoothed + colour-quantised fills, ink lines on edges, thick black outline.
import sys, cv2, numpy as np
def toon(src, dst, k=7, line=2, outline=7, maxside=900):
    im = cv2.imread(src, cv2.IMREAD_UNCHANGED)
    if im.shape[2] == 3:
        im = np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])
    s = maxside / max(im.shape[:2])
    if s < 1: im = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    a = im[:, :, 3]; rgb = im[:, :, :3].copy()
    for _ in range(3): rgb = cv2.bilateralFilter(rgb, 9, 40, 9)
    m = a > 128
    px = rgb[m].reshape(-1, 3).astype(np.float32)
    _, lab, cen = cv2.kmeans(px, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1), 3, cv2.KMEANS_PP_CENTERS)
    q = rgb.copy(); q[m] = cen[lab.flatten()].astype(np.uint8)
    # boost saturation/contrast a bit (poster look)
    hsv = cv2.cvtColor(q, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] = np.clip(hsv[..., 1] * 1.25, 0, 255); hsv[..., 2] = np.clip((hsv[..., 2] - 128) * 1.1 + 132, 0, 255)
    q = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    g = cv2.cvtColor(cv2.medianBlur(rgb, 5), cv2.COLOR_BGR2GRAY)
    e = cv2.Canny(g, 40, 110)
    e = cv2.dilate(e, np.ones((line, line), np.uint8))
    e[cv2.erode(a, np.ones((5, 5), np.uint8)) < 128] = 0
    q[e > 0] = (20, 12, 16)
    # thick outer outline
    ao = cv2.dilate(a, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*outline+1, 2*outline+1)))
    out = np.zeros((*a.shape, 4), np.uint8); out[..., :3] = (20, 12, 16); out[..., 3] = ao
    inner = a > 128
    out[inner, :3] = q[inner]
    cv2.imwrite(dst, out)
if __name__ == '__main__':
    toon(sys.argv[1], sys.argv[2], *[int(x) for x in sys.argv[3:]])
