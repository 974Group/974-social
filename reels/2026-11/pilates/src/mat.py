from PIL import Image, ImageFilter, ImageDraw
import numpy as np, random
random.seed(4); np.random.seed(4)
H=1920; SW=640; GAP=180; N=12; M=520
W=M*2+N*SW+(N-1)*GAP
# floor: warm light oak-ish beige with soft grain
fl=np.zeros((H,W,3),np.float32); fl[:]= (226,214,198)
grain=np.random.normal(0,1,(H//8,W//8)).astype(np.float32)
g=np.array(Image.fromarray(((grain*20+128).clip(0,255)).astype('uint8')).resize((W,H),Image.BICUBIC)).astype(np.float32)-128
fl+=g[...,None]*0.18
# mat
mt,mb=250,H-250; ml,mr=200,W-200
mat=np.zeros((H,W),np.float32); mat[mt:mb,ml:mr]=1
mi=Image.fromarray((mat*255).astype('uint8'))
d=ImageDraw.Draw(mi); 
mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).rounded_rectangle((ml,mt,mr,mb),60,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(1.5))
pink=np.zeros((H,W,3),np.float32); pink[:]=(236,196,201)
fine=np.random.normal(0,1,(H,W)).astype(np.float32)
pink+=fine[...,None]*3.0
# mat shadow
sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((ml+6,mt+14,mr+6,mb+14),60,fill=110); sh=np.array(sh.filter(ImageFilter.GaussianBlur(18)),np.float32)/255
fl*= (1-sh[...,None]*0.35)
m=np.array(mask,np.float32)[...,None]/255
img=fl*(1-m)+pink*m
# soft window light: brighter top-left band, slight vignette top/bottom
yy=np.linspace(-1,1,H)[:,None]; img*= (1.04-0.06*yy**2)[...,None]
canvas=Image.fromarray(img.clip(0,255).astype('uint8')).convert('RGBA')
for k in range(N):
    s=Image.open(f'cut/s{k+1:02d}_c.png').convert('RGBA'); s=s.crop(s.getbbox()); s.putalpha(s.split()[3].filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(0.8)))
    h=1300; s=s.resize((int(s.width*h/s.height),h),Image.LANCZOS)
    s=s.rotate(random.uniform(-4,4),expand=True,resample=Image.BICUBIC)
    x=M+k*(SW+GAP)+(SW-s.width)//2; y=(H-s.height)//2+random.randint(-25,25)
    a=s.split()[3]
    shadow=Image.new('RGBA',s.size,(70,30,40,0)); shadow.putalpha(a.point(lambda v:int(v*0.33)).filter(ImageFilter.GaussianBlur(16)))
    canvas.alpha_composite(shadow,(x+14,y+20))
    canvas.alpha_composite(s,(x,y))
canvas.convert('RGB').save('mat_wide.jpg',quality=93)
print(W,H)
