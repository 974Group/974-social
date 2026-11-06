import sys,math,subprocess,os,random
from PIL import Image
CUT='/home/claude/974-social/posts/2026-11/face-mask/src/cut/'
NAMES='armygreen babyblue beige black brightred brown grey hotpink khaki lightgreen lilac navy orange pink purple red royalblue white'.split()
assert len(NAMES)==18
sky=os.path.abspath(sys.argv[1]); FPS=30; T=8.0; N=int(T*FPS)
random.seed(7)
base={n:Image.open(CUT+n+'.png').convert('RGBA') for n in NAMES}
for n in base: base[n]=base[n].crop(base[n].getbbox())
Ww=1080+2*420
order=NAMES[:]; random.shuffle(order)
M=[]
for i,n in enumerate(order):
    near = i%3==0          # every third mask is in front and moves faster
    z = random.uniform(1.0,1.15) if near else random.uniform(0.62,0.85)
    M.append(dict(n=n,z=z,v=2 if near else 1,x0=(i*Ww/18 + random.uniform(-30,30))%Ww,
      y0=random.uniform(620,1260),amp=random.uniform(25,55),k=random.choice([1,2]),ph=random.random(),
      r0=random.uniform(-12,12),ra=random.uniform(4,9),m=random.choice([1,2]),ph2=random.random()))
cache={}
def img(m,scale,rot):
    w=int(300*m['z']*scale); key=(m['n'],w,int(rot))
    if key not in cache:
        b=base[m['n']]; h=int(b.height*w/b.width)
        cache[key]=b.resize((w,h),Image.LANCZOS).rotate(int(rot),resample=Image.BICUBIC,expand=True)
    return cache[key]
os.makedirs('fr',exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',sky,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30','-frames:v',str(N+10),'sk_%04d.png'],check=True,cwd='fr')
skN=len([f for f in os.listdir('fr') if f.startswith('sk_')])
TXT=Image.open('txt.png').convert('RGBA')
X=30
for i in range(N):
    t=i/N
    a=Image.open(f'fr/sk_{(i%skN)+1:04d}.png').convert('RGB')
    if i>=N-X:
        b=Image.open(f'fr/sk_{(i-(N-X))+1:04d}.png').convert('RGB'); a=Image.blend(a,b,(i-(N-X))/X)
    fr=a.convert('RGBA')
    for m in sorted(M,key=lambda m:m['z']):
        x=(m['x0']-m['v']*t*Ww)%Ww-420
        y=m['y0']+m['amp']*math.sin(2*math.pi*(m['k']*t+m['ph']))
        r=m['r0']+m['ra']*math.sin(2*math.pi*(m['m']*t+m['ph2']))
        im=img(m,1,round(r))
        fr.alpha_composite(im,(int(x-im.width/2),int(y-im.height/2)))
    fr.alpha_composite(TXT,(0,0))
    fr.convert('RGB').save(f'fr/o_{i:04d}.jpg',quality=93)
subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i','fr/o_%04d.jpg','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','tmp.mp4'],check=True)
os.replace('tmp.mp4','974-mask-count.mp4'); print(N)
