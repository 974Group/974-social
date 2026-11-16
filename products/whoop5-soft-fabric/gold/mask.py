import numpy as np, sys
from PIL import Image
from scipy import ndimage as nd
from skimage import color
C='/home/claude/974-social/products/whoop5-soft-fabric/gold/cut/'
def gold_mask(n, gsd=None):
    gsd = gsd if gsd is not None else (0.008 if n=='cloud' else 0.03)
    im=np.array(Image.open(C+n+'.png').convert('RGBA')).astype(float)/255
    rgb=im[...,:3]; a=im[...,3]
    hsv=color.rgb2hsv(rgb); h=hsv[...,0]*360; s=hsv[...,1]; v=hsv[...,2]
    L=color.rgb2gray(rgb)
    m=nd.uniform_filter(L,9); sd=np.sqrt(np.maximum(nd.uniform_filter(L*L,9)-m*m,0))
    H,W=a.shape; yy,xx=np.mgrid[0:H,0:W]
    region=(xx>W*0.38)&(yy<H*0.80)
    cand=(a>0.8)&(h>25)&(h<70)&(s>0.06)&(v>0.38)&(sd<0.05)&region
    cand=nd.binary_opening(cand,iterations=2)
    lab,k=nd.label(cand)
    if k==0: return cand,rgb,a
    sz=nd.sum(cand,lab,range(1,k+1))
    keep=[i+1 for i,z in enumerate(sz) if z>sz.max()*0.05]
    mk=np.isin(lab,keep); mk=nd.binary_closing(mk,iterations=4)
    # include low-sat highlights inside metal hull
    hull=nd.binary_fill_holes(nd.binary_closing(nd.binary_dilation(mk,iterations=3),iterations=25))
    hl=hull&(a>0.8)&(v>0.55)&(sd<0.07)&(s<0.45)&(((h>20)&(h<75))|(s<0.1))
    mk=mk|hl
    near=nd.binary_dilation(mk,iterations=30)
    m2=nd.uniform_filter(L,5); sd2=np.sqrt(np.maximum(nd.uniform_filter(L*L,5)-m2*m2,0))
    add=near&(a>0.8)&(v>0.6)&(s<0.4)&(sd2<0.025)&region
    mk=mk|add
    base=mk.copy()
    for _ in range(4):
        grow=nd.binary_dilation(mk,iterations=15)&(a>0.8)&(v>0.82)&(s<0.15)&(sd2<gsd)&region
        mk=mk|grow
    g=mk&~base
    g=nd.binary_opening(g,iterations=(5 if n=='cloud' else 1))
    mk=base|g
    lb,k=nd.label(mk)
    if k:
        z=nd.sum(mk,lb,range(1,k+1)); mk=np.isin(lb,[i+1 for i,q in enumerate(z) if q>3000])
    mk=nd.binary_closing(mk,iterations=2)
    return mk,rgb,a
if __name__=='__main__':
    fs=sys.argv[1:]
    tiles=[]
    for n in fs:
        mk,rgb,a=gold_mask(n)
        vis=rgb.copy(); vis[mk]=[1,0,1]
        t=Image.fromarray((vis*255).astype('uint8')); t.thumbnail((300,340)); tiles.append(t)
        print(n, mk.mean())
    s=Image.new('RGB',(300*len(tiles),340),'white')
    for i,t in enumerate(tiles): s.paste(t,(i*300,0))
    s.save('masks.jpg')
