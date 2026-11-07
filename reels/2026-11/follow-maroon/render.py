# Follow the Maroon — reel renderer (1080x1920, 30fps)
import random, math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(974)
W,H,FPS=1080,1920,30
BG=(15,13,14,255)
C='/home/claude/974-social/posts/2026-11/whoop5-silicone-all/cut/'
MAROON='/home/claude/974-social/packaging/whoop-box/qatar/img/p49w-50.png'
BH=215  # band height
COLORS=['blue','babyblue','iceblue','turquoise','creamy','orange','yellow','pink','red','greenarmy','black','navyyellow','splash','drenched','scarlet']

def load(p,rot=0):
    im=Image.open(p).convert('RGBA')
    if rot: im=im.rotate(rot,resample=Image.BICUBIC,expand=True)
    bb=im.getbbox(); im=im.crop(bb)
    s=BH/im.height; return im.resize((round(im.width*s),BH),Image.LANCZOS)

white=load(C+'whitegrey.png',-6)
maroon=load(MAROON)
cols={c:load(C+c+'.png',-6) for c in COLORS}
# glow for maroon
a=maroon.split()[3].resize((maroon.width+80,maroon.height+80)).filter(ImageFilter.GaussianBlur(28))
glow=Image.new('RGBA',a.size,(224,74,134,0)); glow.putalpha(a.point(lambda v:int(v*0.9)))

# grid slots (3x4)
XS=[270,540,810]; YS=[570,830,1090,1350]
SLOTS=[(x,y) for y in YS for x in XS]
N=12

# ---------- timeline ----------
T0,T1,T2,T3,T4,T5,T6,T7,T8,END=0,2.5,5.5,7.0,15.0,25.0,31.0,32.5,36.0,40.0
m0=random.choice([4,5,7,8])  # start slot of the maroon band (middle-ish)
band_slot=list(range(N))      # band i sits in slot band_slot[i]; band m0 is the maroon one

moves=[]  # (t_start, dur, [(band, from_slot, to_slot),...])
def schedule(t_from,t_to,dur,k,gap=0.08):
    t=t_from
    while t+dur<=t_to:
        bands=random.sample(range(N),2*k)
        prs=[]
        for j in range(k):
            a,b=bands[2*j],bands[2*j+1]
            sa,sb=band_slot[a],band_slot[b]
            prs+=[(a,sa,sb),(b,sb,sa)]
            band_slot[a],band_slot[b]=sb,sa
        moves.append((t,dur,prs)); t+=dur+gap
schedule(T3+0.3,T4-0.2,0.95,2)
schedule(T4+0.6,T5-0.2,0.72,2)
schedule(T5+0.5,T6-0.3,0.42,3)
final_slot=band_slot[:]
answer=final_slot[m0]+1
print('maroon start slot',m0+1,'answer',answer,file=sys.stderr)

# band colours in phase 4
colour_of={i:random.choice(COLORS) for i in range(N)}

def ease(u): return 0.5-0.5*math.cos(math.pi*max(0,min(1,u)))
def pos_at(i,t):
    # slot before any move: i; walk moves
    cur=i
    for (ts,d,prs) in moves:
        if t<ts: break
        for (b,fs,to) in prs:
            if b==i:
                if t<ts+d:
                    u=ease((t-ts)/d); x0,y0=SLOTS[fs]; x1,y1=SLOTS[to]
                    # slight arc
                    arc=math.sin(math.pi*u)*40*(1 if (fs%2) else -1)
                    return (x0+(x1-x0)*u, y0+(y1-y0)*u+arc, True)
                cur=to
    x,y=SLOTS[cur]; return (x,y,False)

def tex(k): return Image.open(f'txt/{k}.png').convert('RGBA')
TX={k:tex(k) for k in ['title','c1','c2','c3','c4','c5','c6','c7','c8','c9']}
def alpha(im,a):
    if a>=1: return im
    im=im.copy(); im.putalpha(im.split()[3].point(lambda v:int(v*a))); return im
def fade(t,a,b,d=0.3):  # opacity of a layer shown from a to b
    if t<a or t>b: return 0
    return min(1,(t-a)/d,(b-t)/d)

font=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',40)

def blend(im_a,im_b,u):
    if u<=0: return im_a
    if u>=1: return im_b
    # same size assumption not guaranteed -> composite on canvas
    w=max(im_a.width,im_b.width); h=BH
    ca=Image.new('RGBA',(w,h)); ca.paste(im_a,((w-im_a.width)//2,0))
    cb=Image.new('RGBA',(w,h)); cb.paste(im_b,((w-im_b.width)//2,0))
    return Image.blend(ca,cb,u)

def band_img(i,t):
    if i==m0:
        if t<T1: return white
        if t<T1+0.5: return blend(white,maroon,(t-T1)/0.5)
        if t<T2: return maroon
        if t<T2+0.5: return blend(maroon,white,(t-T2)/0.5)
    col=cols[colour_of[i]]
    if t<T4: return white
    if t<T4+0.5: return blend(white,col,(t-T4)/0.5)
    if t<T5: return col
    if t<T5+0.5: return blend(col,white,(t-T5)/0.5)
    return white

def frame(t):
    im=Image.new('RGBA',(W,H),BG)
    d=ImageDraw.Draw(im)
    # faint grid cells
    g=min(1,t/0.8)
    gc=(255,255,255,int(18*g))
    for x in [135,405,675,945]: d.line([(x,440),(x,1480)],fill=gc,width=2)
    for y in [440,700,960,1220,1480]: d.line([(135,y),(945,y)],fill=gc,width=2)
    im.alpha_composite(alpha(TX['title'],min(1,t/0.6)))
    # bands
    gin=min(1,max(0,(t-0.3)/0.9))
    order=sorted(range(N),key=lambda i:pos_at(i,t)[2])  # moving ones on top
    for i in order:
        x,y,mv=pos_at(i,t)
        b=band_img(i,t)
        if i==m0 and T1<t<T2:
            p=0.6+0.4*math.sin((t-T1)*5)
            ga=alpha(glow,p*min(1,(t-T1)/0.5)*min(1,(T2-t)/0.4))
            im.alpha_composite(ga,(int(x-ga.width/2),int(y-ga.height/2)))
        if mv: b=b.resize((int(b.width*1.06),int(b.height*1.06)),Image.BILINEAR)
        b=alpha(b,gin)
        im.alpha_composite(b,(int(x-b.width/2),int(y-b.height/2)))
        if t>=T7:
            u=min(1,(t-T7-0.04*i)/0.3)
            if u>0:
                s=final_slot[i]; sx,sy=SLOTS[s]
                r=34; cx,cy=sx+95,sy+70
                bd=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(bd)
                dd.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(244,241,242,255))
                txt=str(s+1); tw=dd.textbbox((0,0),txt,font=font)
                dd.text((cx-(tw[2]-tw[0])/2-tw[0],cy-(tw[3]-tw[1])/2-tw[1]-2),txt,font=font,fill=(15,13,14,255))
                im.alpha_composite(alpha(bd,u))
    # captions
    caps=[('c1',T0+0.4,T1),('c2',T1+0.2,T2),('c3',T2+0.1,T3),('c4',T3,T4),('c5',T4,T5),('c6',T5,T6),('c7',T6,T7),('c8',T7,T8),('c9',T8,END)]
    for k,a,b in caps:
        f=fade(t,a,b,0.25)
        if f>0: im.alpha_composite(alpha(TX[k],f))
    return im

if __name__=='__main__':
    preview=len(sys.argv)>1 and sys.argv[1]=='preview'
    if preview:
        for t in [1.0,4.0,6.2,9.0,18.0,27.0,33.5,38.0]:
            frame(t).convert('RGB').resize((270,480)).save(f'/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad/fm_{t}.jpg')
        sys.exit()
    nf=int(END*FPS)
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','video.tmp.mp4'],stdin=subprocess.PIPE)
    for n in range(nf):
        p.stdin.write(frame(n/FPS).convert('RGB').tobytes())
        if n%150==0: print(n,file=sys.stderr)
    p.stdin.close(); p.wait()
    # audio: ticks per move, whoosh at phases, chime at reveal
    SR=48000; aud=np.zeros(int(END*SR)+SR)
    def add(sig,t):
        s=int(t*SR); e=min(len(aud),s+len(sig)); aud[s:e]+=sig[:e-s]
    def tick(dur=0.04,f=1800,v=0.25):
        n=int(dur*SR); tt=np.arange(n)/SR; return v*np.sin(2*np.pi*f*tt)*np.exp(-tt*120)
    def whoosh(dur=0.45,v=0.35):
        n=int(dur*SR); x=np.random.randn(n);
        # simple bandpass via FFT
        X=np.fft.rfft(x); fr=np.fft.rfftfreq(n,1/SR); X*=np.exp(-((np.log(fr+1)-np.log(900))**2)/0.5); x=np.fft.irfft(X,n)
        env=np.sin(np.pi*np.arange(n)/n)**2; return v*x/np.abs(x).max()*env
    def chime(v=0.3):
        n=int(0.9*SR); tt=np.arange(n)/SR
        return v*(np.sin(2*np.pi*660*tt)+0.5*np.sin(2*np.pi*990*tt))*np.exp(-tt*4)
    def thump(v=0.6):
        n=int(0.35*SR); tt=np.arange(n)/SR; return v*np.sin(2*np.pi*60*tt)*np.exp(-tt*10)
    for (ts,d,prs) in moves: add(tick(),ts)
    for t in [T1,T2,T4,T5]: add(whoosh(),t-0.02)
    add(chime(),T1+0.1); add(thump(),T6); add(chime(0.25),T7+0.1)
    aud=np.clip(aud,-1,1)
    import wave, struct
    with wave.open('sfx.wav','wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((aud*32767).astype('<i2').tobytes())
    subprocess.run(['ffmpeg','-v','error','-y','-i','video.tmp.mp4','-i','sfx.wav','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart','974-follow-the-maroon.mp4'],check=True)
    open('answer.txt','w').write(f'maroon start slot {m0+1}, answer {answer}\n')
    print('done answer',answer,file=sys.stderr)
