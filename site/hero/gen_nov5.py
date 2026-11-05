import subprocess
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C='/home/claude/974-social/site/hero/cut/'
MARK_C='/home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'
MARK_W='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}'''
fit=['f_black','f_white','f_grey','f_beige','f_yellow','f_orange','f_red','f_pink','f_purple']
cq=['c_f1_blue','c_f2_whitegrey','c_f3_orange','c_s1_beige','c_s2_lime']

def grid(items,cols,cw,ch,gap,stagger=0):
    out=''
    for i,f in enumerate(items):
        r,c=divmod(i,cols)
        dy=stagger if c%2 else 0
        out+=f'<div class="b" style="left:{c*(cw+gap)}px;top:{r*(ch+gap)+dy}px;width:{cw}px;height:{ch}px"><img src="file://{C}{f}.png"></div>'
    return out

def page(kind,W,H):
    mob=W<2000
    if kind=='fit':
        bg='radial-gradient(ellipse at 22% 55%,#FFFFFF 0%,#F7EEF2 40%,#EADDE3 100%)'
        ink='#51022D'; acc='#720842'; mark=MARK_C
        eb='FITBIT AIR'; h='سيليكون <em>2.0</em>'; sub='9 ألوان · خفيف وضد العرق'; price='<b>79</b> ر.ق'
        items=fit
        if mob: cols,cw,ch,gap,st=3,170,175,12,0
        else: cols,cw,ch,gap,st=5,215,235,70,30
    else:
        bg='radial-gradient(ellipse at 25% 50%,#8A1450 0%,#720842 35%,#51022D 75%,#3A0120 100%)'
        ink='#FFFFFF'; acc='#C9A24B'; mark=MARK_W
        eb='GARMIN CIRQA'; h='كل سيور <em>CIRQA</em>'; sub='5 أنواع · قماش وسيليكون'; price='من <b>89</b> ر.ق'
        items=cq
        if mob: cols,cw,ch,gap,st=3,175,250,20,0
        else: cols,cw,ch,gap,st=5,215,390,45,0
    rows=(len(items)+cols-1)//cols
    gw=cols*cw+(cols-1)*gap; gh=rows*ch+(rows-1)*gap+st
    if mob: gx=40; gy=(H-gh)//2
    else: gx=110; gy=(H-gh)//2
    sc=1 if not mob else .78
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:{bg};font-family:Cairo;color:{ink};position:relative;overflow:hidden}}
.mk{{position:absolute;right:{-60 if not mob else -40}px;bottom:{-90 if not mob else -60}px;height:{520 if not mob else 330}px;opacity:.06}}
.g{{position:absolute;left:{gx}px;top:{gy}px;width:{gw}px;height:{gh}px}}
.b{{position:absolute;display:flex;align-items:center;justify-content:center}}
.b img{{max-width:100%;max-height:100%;object-fit:contain;filter:drop-shadow(0 {int(14*sc)}px {int(14*sc)}px rgba(0,0,0,.28))}}
.t{{position:absolute;right:{110 if not mob else 44}px;top:50%;transform:translateY(-50%);text-align:right;direction:rtl;width:{760 if not mob else 470}px}}
.t .lg{{height:{58 if not mob else 40}px;margin-bottom:{18 if not mob else 10}px}}
.t .eb{{font-family:Poppins;font-weight:700;letter-spacing:{6 if not mob else 4}px;font-size:{26 if not mob else 19}px;color:{acc};direction:ltr;text-align:right}}
.t h2{{font-weight:900;font-size:{(118 if kind=='fit' else 104) if not mob else 72}px;line-height:1.05;{'white-space:nowrap;' if not mob else ''}margin-top:{6 if not mob else 2}px}}
.t h2 em{{font-style:normal;font-family:Poppins;font-weight:700;color:{acc}}}
.t .sub{{font-weight:700;font-size:{40 if not mob else 27}px;opacity:.85;margin-top:{12 if not mob else 6}px}}
.t .row{{display:flex;gap:{18 if not mob else 12}px;align-items:center;margin-top:{34 if not mob else 20}px}}
.t .pr{{font-weight:900;font-size:{46 if not mob else 30}px}}
.t .pr b{{font-family:Poppins}}
.t .btn{{background:{acc};color:{'#fff' if kind=='fit' else '#3A0120'};border-radius:60px;padding:{10 if not mob else 6}px {40 if not mob else 26}px {14 if not mob else 9}px;font-weight:800;font-size:{36 if not mob else 25}px}}
</style></head><body>
<img class="mk" src="file://{MARK_C if kind=='fit' else MARK_W}">
<div class="g">{grid(items,cols,cw,ch,gap,st)}</div>
<div class="t"><img class="lg" src="file://{mark}"><div class="eb">{eb}</div><h2>{h}</h2><div class="sub">{sub}</div>
<div class="row"><div class="btn">تسوّق الحين ←</div><div class="pr">{price}</div></div></div>
</body></html>'''
for kind in ('fit','cirqa'):
    for nm,W,H in (('desktop',2400,630),('mobile',1200,630)):
        name=f'{kind}-{nm}'
        open(name+'.html','w').write(page(kind,W,H))
        js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file://'+process.cwd()+'/{name}.html');await p.waitForTimeout(900);await p.screenshot({{path:'{name}.png'}});await b.close();}})()"
        subprocess.run(['node','-e',js],check=True)
print('ok')
