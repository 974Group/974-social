import numpy as np, colorsys, os
from PIL import Image
M=np.asarray(Image.open('cut/maroon.png').convert('RGBA')).astype(float)
rgb=M[...,:3]/255; a=M[...,3]
hsv=np.vectorize(colorsys.rgb_to_hsv)
r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
mx=rgb.max(-1); mn=rgb.min(-1); sat=np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0)
L=0.299*r+0.587*g+0.114*b
band=(a>200)&(sat>0.25)                     # saturated maroon = band body
stud=(a>40)&(~band)                         # metal stud / grey bits
Lb=np.median(L[band])
rel=np.clip(L/Lb,0,3)
def target_color(name):
    T=np.asarray(Image.open(f'cut/{name}.png').convert('RGBA')).astype(float)
    t=T[...,:3]; ta=T[...,3]
    m=ta>220
    tl=(0.299*t[...,0]+0.587*t[...,1]+0.114*t[...,2])
    # body: median of mid-luminance pixels (avoid highlights, holes, pins)
    lo,hi=np.percentile(tl[m],[30,75]); sel=m&(tl>=lo)&(tl<=hi)
    return np.median(t[sel],axis=0)/255
names=[f[:-4] for f in os.listdir('cut') if f.endswith('.png')]
for n in names:
    c=target_color(n)
    lum=0.299*c[0]+0.587*c[1]+0.114*c[2]
    # soften contrast for very light / very dark colours so shading looks natural
    k=0.75 if lum>0.75 else (0.85 if lum<0.18 else 1.0)
    shade=1+(rel-1)*k
    out=np.clip(c[None,None,:]*shade[...,None],0,1)
    # light colours: add highlight lift where master is bright
    if lum>0.75: out=np.clip(out+np.clip(rel-1.2,0,1)[...,None]*0.15,0,1)
    res=np.where(stud[...,None],rgb,out)
    O=np.dstack([res*255,a]).astype(np.uint8)
    im=Image.fromarray(O,'RGBA'); im=im.crop(im.getbbox()); im.save(f'uni/{n}.png')
    print(n, (c*255).round().astype(int), round(lum,2))
