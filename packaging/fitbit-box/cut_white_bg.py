import numpy as np, sys
from PIL import Image
from scipy import ndimage as nd
def cut(src,dst,maxw):
    im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(np.float32)
    L=a.min(-1)                                   # min channel: white bg ~250+
    white=L>238
    lab,n=nd.label(white); sizes=nd.sum(white,lab,range(1,n+1))
    H,W=L.shape; border=set(np.unique(np.r_[lab[0],lab[-1],lab[:,0],lab[:,-1]]))-{0}
    bgids=[i+1 for i,s in enumerate(sizes) if (i+1) in border or s>0.01*H*W]
    bg=np.isin(lab,bgids)
    near=nd.binary_dilation(bg,iterations=4)&~bg
    alpha=np.where(bg,0.0,1.0)
    soft=np.clip((250-L)/70,0,1)
    alpha=np.where(near,np.minimum(alpha,soft),alpha)
    alpha=nd.gaussian_filter(alpha,0.6)
    # un-premultiply against white so edges don't glow
    al=np.clip(alpha,1e-3,1)[...,None]
    rgb=np.clip((a-255*(1-al))/al,0,255)
    out=np.dstack([rgb,alpha*255]).astype(np.uint8)
    o=Image.fromarray(out,'RGBA'); o=o.crop(o.getbbox())
    if o.width>maxw: o=o.resize((maxw,round(o.height*maxw/o.width)),Image.LANCZOS)
    o.save(dst); print(dst,o.size)
cut(sys.argv[1],sys.argv[2],int(sys.argv[3]))
