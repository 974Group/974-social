import json,sys
from PIL import Image,ImageDraw,ImageFilter
geo=json.load(open('blank/geo2.json'))
logo=Image.open('../hero/mark-c.png').convert('RGBA')
bb=logo.getbbox(); logo=logo.crop(bb).rotate(90,expand=True)  # CCW
for k in (sys.argv[1:] or geo):
    g=geo[k]; im=Image.open(f'blank/{k}.png').convert('RGB')
    cx,cy,r=g['cx'],g['cy'],g['r']; rr=r-4
    box=(cx-rr,cy-rr,cx+rr,cy+rr)
    disk=im.crop(box).rotate(90)
    m=Image.new('L',disk.size,0); ImageDraw.Draw(m).ellipse((2,2,disk.size[0]-3,disk.size[1]-3),255)
    m=m.filter(ImageFilter.GaussianBlur(2))
    im.paste(disk,box[:2],m)
    gap=cx-r-g['left']; w=int(0.62*gap)
    L=logo.resize((w,int(logo.height*w/logo.width)),Image.LANCZOS)
    if L.height>1.3*r: L=logo.resize((int(logo.width*1.3*r/logo.height),int(1.3*r)),Image.LANCZOS)
    a=L.split()[3].point(lambda v:int(v*0.94)); L.putalpha(a)
    x=int((g['left']+cx-r)/2-L.width/2); y=int(cy-L.height/2)
    im.paste(L,(x,y),L)
    im.save(f'pkfinal/{k}.png')
print('ok')
