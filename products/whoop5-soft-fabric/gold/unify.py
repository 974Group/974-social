import numpy as np, os
from PIL import Image
from scipy import ndimage as nd
from skimage import color
from mask import gold_mask, C
O='/home/claude/974-social/products/whoop5-soft-fabric/gold/cut-unified/'; os.makedirs(O,exist_ok=True)
mf,rf,af=gold_mask('forest'); labf=color.rgb2lab(rf)[mf]
mu=labf.mean(0); sd=labf.std(0); print('forest',mu.round(1),sd.round(1))
def fix(n):
    mk,rgb,a=gold_mask(n)
    if n=='forest': out=rgb
    else:
        lab=color.rgb2lab(rgb); g=lab[mk]; m2=g.mean(0); s2=g.std(0)+1e-3
        t=lab.copy()
        for c in (1,2): t[...,c]=(lab[...,c]-m2[c])/s2[c]*sd[c]+mu[c]
        t[...,0]=(lab[...,0]-m2[0])/s2[0]*(0.5*s2[0]+0.5*sd[0])+(0.5*m2[0]+0.5*mu[0])
        new=np.clip(color.lab2rgb(t),0,1)
        w=nd.gaussian_filter(mk.astype(float),1.2)[...,None]
        out=rgb*(1-w)+new*w
        print(n,m2.round(1))
    Image.fromarray((np.dstack([out,a])*255).astype('uint8')).save(O+n+'.png')
import sys
for n in (sys.argv[1:] or 'forest onyx granite twilight dune cloud sky pink orange'.split()): fix(n)
fs='onyx granite twilight forest dune cloud sky pink orange'.split()
s=Image.new('RGB',(9*300,700),(245,236,220))
for i,f in enumerate(fs):
  for j,d in enumerate([C,O]):
    m=Image.open(d+f+'.png');m.thumbnail((290,330));s.paste(m,(i*300,j*350),m)
s.save('cmp.jpg')
