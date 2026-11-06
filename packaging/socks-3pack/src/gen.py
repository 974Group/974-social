import subprocess,os
D=os.path.dirname(os.path.abspath(__file__))
MID=45  # middle (top of pack) in mm
W,P=60,80; B=3
TW=W+2*B; TH=P*2+MID+2*B
CARE=open('/home/claude/974-social/packaging/974x180-socks/src/card-free.html').read()
icons=CARE[CARE.index('<div class="icons">'):CARE.index('</div><div class="made">')+6]
soc=CARE[CARE.index('<div class="soc">'):CARE.index('<div class="mini">')]
def html(dieline):
    fy=B; my=B+P; by=B+P+MID
    dl=''
    if dieline:
        dl=f'''<svg style="position:absolute;left:0;top:0" width="{TW}mm" height="{TH}mm" viewBox="0 0 {TW} {TH}">
<g fill="none" stroke="#EC008C" stroke-width="0.25">
<rect x="{B}" y="{B}" width="{W}" height="{P*2+MID}"/>
<line x1="{B}" y1="{my}" x2="{B+W}" y2="{my}" stroke-dasharray="1.5 1"/><line x1="{B}" y1="{by}" x2="{B+W}" y2="{by}" stroke-dasharray="1.5 1"/>
<rect x="{B+W/2-6}" y="{my+MID/2-1}" width="12" height="2" rx="1"/>
<circle cx="{B+W/2}" cy="{B+27.4}" r="1"/><circle cx="{B+W/2}" cy="{by+P-27.4}" r="1"/></g></svg>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-SemiBold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:800;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-ExtraBold.ttf)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file:///tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
@page{{size:{TW}mm {TH}mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{TW}mm;height:{TH}mm;font-family:Poppins}}
.sheet{{position:relative;width:{TW}mm;height:{TH}mm;overflow:hidden}}
.bg{{position:absolute;left:0;right:0}}
.panel{{position:absolute;left:{B}mm;width:{W}mm}}
.rot{{transform:rotate(180deg)}}
.c{{position:absolute;left:0;right:0;text-align:center}}
.logo{{width:30mm;filter:invert(1)}}
.big{{font:900 26pt/1 Poppins;color:#fff;letter-spacing:.02em}}
.sub{{font:700 7pt Poppins;letter-spacing:.45em;padding-left:.45em;color:#F4C6DC}}
.pill{{display:inline-block;border:0.35mm solid #fff;border-radius:5mm;padding:1.2mm 4mm 1.4mm;font:700 7.5pt Poppins;letter-spacing:.2em;color:#fff}}
.care h4{{font:800 7pt Poppins;letter-spacing:.12em;color:#51022D}}
.care p{{font:500 5.6pt/1.45 Poppins;margin-top:1.2mm;color:#333}}
.icons{{display:flex;justify-content:center;gap:2.6mm;margin-top:1.8mm}}
.icons svg{{width:4.4mm;height:4.4mm}}
.info{{font:700 6.6pt/1.5 Poppins;color:#51022D;letter-spacing:.08em}}
.soc{{position:absolute;left:6mm;bottom:6mm;font:600 6pt/1.6 Poppins;color:#161616}}
.soc div{{display:flex;align-items:center;gap:1.4mm}}
.soc svg{{width:3.2mm;height:3.2mm}}
.mini{{position:absolute;right:6mm;bottom:6.5mm;height:6.5mm}}
</style></head><body><div class="sheet">
<div class="bg" style="top:0;height:{my}mm;background:#720842"></div>
<div class="bg" style="top:{my}mm;height:{MID}mm;background:#51022D"></div>
<div class="bg" style="top:{by}mm;height:{TH-by}mm;background:#F4F1F2"></div>
<!-- FRONT (rotated: reads upright when folded) -->
<div class="panel rot" style="top:{fy}mm;height:{P}mm">
 <div class="c" style="top:9mm"><img class="logo" src="file://{D}/mark-black.png"></div>
 <div class="c big" style="top:30mm">3 PACK</div>
 <div class="c sub" style="top:41mm">SOCKS</div>
 <div class="c" style="top:63mm"><span class="pill">FREE SIZE</span></div>
</div>
<!-- MIDDLE / top of pack (rotated with front) -->
<div class="panel rot" style="top:{my}mm;height:{MID}mm">
 <div class="c" style="top:{MID/2+5}mm;font:700 6.5pt Poppins;letter-spacing:.35em;padding-left:.35em;color:#F4C6DC">974GROUP.NET</div>
 <div class="c" style="top:{MID/2-10}mm;font:800 7pt Poppins;letter-spacing:.3em;padding-left:.3em;color:#fff">3 PAIRS · FREE SIZE</div>
</div>
<!-- BACK (upright) -->
<div class="panel" style="top:{by}mm;height:{P}mm">
 <div class="c" style="top:7mm"><div class="info">3 PAIRS · FREE SIZE</div><div style="font:700 7.5pt Cairo,sans-serif;color:#51022D;direction:rtl">٣ أزواج · مقاس واحد</div></div>
 <div class="c care" style="top:21mm;padding:0 4mm"><h4>CARE</h4>
 <p>Machine wash cold · Turn inside out<br>Do not bleach or iron · Do not tumble dry</p>
 {icons}</div>
 {soc}
 <img class="mini" src="file://{D}/mark-black.png">
</div>
{dl}
</div></body></html>'''
for name,dl in (('974-socks-3pack-card-print',False),('974-socks-3pack-card-dieline',True)):
    p=os.path.join(D,name+'.html'); open(p,'w').write(html(dl))
    out=os.path.join(D,'..',name)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage();await pg.goto('file://{p}');await pg.waitForTimeout(600);await pg.pdf({{path:'{out}.pdf',width:'{TW}mm',height:'{TH}mm',printBackground:true}});await pg.setViewportSize({{width:{round(TW*3.7795)},height:{round(TH*3.7795)}}});await pg.screenshot({{path:'{out}.png',scale:'device'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
print(TW,TH)
