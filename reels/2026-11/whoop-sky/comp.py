import sys,math,subprocess,os
from PIL import Image
ORDER='black-ed darkgrey greyblack whitegrey creamy creamyblue iceblue babyblue blue navyyellow yellownavy yellow greenarmy turquoise drenched splash pink scarlet red orange black'.split()
FPB=int(sys.argv[2]) if len(sys.argv)>2 else 10
sky=os.path.abspath(sys.argv[1])
N=len(ORDER)*FPB; FPS=30
bands=[Image.open(f'cut/{n}.png').convert('RGBA') for n in ORDER]
os.makedirs('fr',exist_ok=True)
# sky frames
subprocess.run(['ffmpeg','-v','error','-y','-i',os.path.abspath(sky),'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30','-frames:v',str(N+30),'sk_%04d.png'],check=True,cwd='fr')
skN=len([f for f in os.listdir('fr') if f.startswith('sk_')])
logo=Image.open('/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png').convert('RGBA')
logo=logo.resize((150,int(logo.height*150/logo.width)),Image.LANCZOS)
X=30  # crossfade frames for sky loop
for i in range(N):
    t=i/N
    # sky loop: frame i, last X frames crossfade into first frames
    a=Image.open(f'fr/sk_{(i%skN)+1:04d}.png').convert('RGB')
    if i>=N-X and N+ (i-(N-X)) < skN:
        pass
    if i>=N-X:
        k=(i-(N-X))/X
        b=Image.open(f'fr/sk_{(i-(N-X))+1:04d}.png').convert('RGB')
        a=Image.blend(a,b,k)
    fr=a.convert('RGBA')
    bi=i//FPB; j=i%FPB
    b=bands[bi]
    pop=1+0.07*max(0,1-j/4)**2
    w=int(720*pop); h=int(b.height*w/b.width)
    im=b.resize((w,h),Image.LANCZOS).rotate(6*math.sin(2*math.pi*t*3),resample=Image.BICUBIC,expand=True)
    cy=930+45*math.sin(2*math.pi*t*2)
    fr.alpha_composite(im,(540-im.width//2,int(cy-im.height/2)))
    fr.alpha_composite(logo,(540-logo.width//2,210))
    fr.convert('RGB').save(f'fr/o_{i:04d}.jpg',quality=93)
subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i','fr/o_%04d.jpg','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','tmp_sky.mp4'],check=True)
os.replace('tmp_sky.mp4','974-whoop-silicone-sky.mp4'); print(N,N/30)
