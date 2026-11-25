# Synthesised SFX for the 4-years story: impacts, confetti sparkle, whooshes, ticks, shimmer.
import numpy as np, wave, subprocess, os
SR = 44100; T = 8.0; N = int(SR*T); L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(974)
def add(sig, t0, gain=1.0, pan=0.0):
    i = int(t0*SR); n = min(len(sig), N-i)
    if n <= 0: return
    L[i:i+n] += sig[:n]*gain*(1-max(0,pan)); R[i:i+n] += sig[:n]*gain*(1+min(0,pan))
def env(n, a, d):
    t = np.arange(n)/SR; return np.minimum(1, t/a) * np.exp(-t/d)
def lp(x, k):  # simple one-pole low-pass
    y = np.zeros_like(x); c = 0.0
    for i, v in enumerate(x): c += k*(v-c); y[i] = c
    return y
def impact():
    n = int(1.6*SR); t = np.arange(n)/SR
    f = 120*np.exp(-t*6)+38; boom = np.sin(2*np.pi*np.cumsum(f)/SR)*env(n, .002, .45)
    click = rng.standard_normal(n)*env(n, .0005, .02)
    body = lp(rng.standard_normal(n), .08)*env(n, .002, .18)*3
    return boom*1.0 + click*.5 + body*.6
def sparkle(dur=2.4, count=90):
    n = int(dur*SR); out = np.zeros(n)
    for k in range(count):
        t0 = rng.uniform(0, dur*0.75)**1.4/((dur*0.75)**0.4); i = int(t0*SR); m = int(.12*SR)
        if i+m >= n: continue
        f = rng.uniform(2800, 7500); tt = np.arange(m)/SR
        out[i:i+m] += np.sin(2*np.pi*f*tt)*np.exp(-tt/rng.uniform(.015, .05))*rng.uniform(.15, .45)*(1-t0/dur)
    crinkle = (rng.standard_normal(n)*(rng.random(n) < .04))*np.exp(-np.arange(n)/SR/0.8)*.5
    hp = crinkle - lp(crinkle, .3)
    return out + hp
def whoosh(dur, up=True):
    n = int(dur*SR); t = np.arange(n)/SR; x = rng.standard_normal(n)
    sweep = np.linspace(.03, .35, n) if up else np.linspace(.35, .03, n)
    y = np.zeros(n); c = 0.0
    for i in range(n): c += sweep[i]*(x[i]-c); y[i] = c
    return y*np.sin(np.pi*t/dur)**2*2.2
def tick():
    n = int(.06*SR); t = np.arange(n)/SR; return np.sin(2*np.pi*1900*t)*np.exp(-t/.008)*.5
def shimmer(dur):
    n = int(dur*SR); t = np.arange(n)/SR; s = np.zeros(n)
    for f in (1318.5, 1661.2, 1975.5, 2637.0):
        s += np.sin(2*np.pi*f*t + 3*np.sin(2*np.pi*5*t))*.12
    return s*np.sin(np.pi*t/dur)
def swish(dur=.3):
    n = int(dur*SR); x = rng.standard_normal(n); y = x - lp(x, .15); return y*np.sin(np.pi*np.arange(n)/n)*.5

def clk(hi=True):
    n = int(.05*SR); t = np.arange(n)/SR
    return (np.sin(2*np.pi*(2400 if hi else 1700)*t)*np.exp(-t/.006) + (rng.standard_normal(n)*np.exp(-t/.002))*.4)*.6
# 0 -> 40 count: a clock tick every 2 %
for k in range(1, 21): add(clk(k % 2 == 0), 0.68*(2*k)/41, 1.6 + k*0.04, (-.2 if k % 2 else .2))
add(impact(), 0.68, 1.0); add(sparkle(), 0.72, .55, -.3); add(sparkle(), 0.74, .55, .3)
add(whoosh(.8), 0.72, 1.1)                    # burgundy wipe
add(swish(), 1.2, 1.4)                        # strike through BLACK
add(whoosh(.45, up=False), 1.93, 1.2, .4)      # 0% slides out
add(shimmer(1.2), 2.1, 1.8)                   # 4 grows into the outline
for k in range(5): add(clk(k % 2 == 0), 2.7+k*0.2, 2.6)   # 2022 -> 2026 tick-tock
add(whoosh(.5), 4.95, 1.1, -.3)               # 4 returns
add(impact(), 5.52, 1.0); add(sparkle(), 5.56, .55, -.3); add(sparkle(), 5.58, .55, .3)
add(swish(), 5.85, 1.2)
add(shimmer(1.3), 6.6, 1.2)                   # final glow
st = np.stack([L, R], 1); st /= np.max(np.abs(st))*1.12
fade = np.ones(N); fn = int(.4*SR); fade[-fn:] = np.linspace(1, 0, fn); st *= fade[:, None]
with wave.open('out/sfx.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
v = 'out/974-4years-story.mp4'; tmp = 'out/974-4years-story-sfx.tmp.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', v, '-i', 'out/sfx.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', tmp], check=True)
os.replace(tmp, 'out/974-4years-story.mp4'); print('ok')
