# All Black box: darken the light loops of band3 / rear-03-black into charcoal (keeps weave), protecting clasp highlight + LED.
import numpy as np
from PIL import Image
def blk(src,dst,protect):
    im=np.asarray(Image.open(src).convert('RGBA')).astype(np.float32)
    H,W=im.shape[:2]; yy,xx=np.mgrid[:H,:W]
    rgb=im[...,:3]; L=rgb@np.array([.299,.587,.114]); mx=rgb.max(-1); mn=rgb.min(-1)
    sat=(mx-mn)/np.maximum(mx,1)
    w=np.clip((L-70)/60,0,1)*np.clip((0.25-sat)/0.1,0,1)*~protect(xx,yy)
    newL=L*(1-w)+(26+0.18*(L-70))*w
    im[...,:3]=np.clip(rgb*(1-w[...,None])+newL[...,None]*w[...,None],0,255)
    Image.fromarray(im.astype(np.uint8)).save(dst)
blk('band3.png','band12.png',lambda x,y:((x-262)**2+(y-105)**2<32**2))
blk('rear-03-black.png','rear-12-all-black.png',lambda x,y:(x>40)&(x<110)&(y>80)&(y<230))
