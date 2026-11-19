# Full range in one design (owner 19 Nov 2026): one of every band type + goggles, sunglasses, socks.
# Feed 1080x1350. Every item same height inside its group, all bands facing the same way.
import sys, os, subprocess
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); C=D+'/cut/'; OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
WHOOP=[('w-sil','Silicone','سيليكون'),('w-wp','Waterproof','ووتر بروف'),('w-soft','Soft fabric','قماش ناعم'),('w-rolex','Rolex 3D','رولكس'),('w-wool','Wool','صوف'),('w-fab','Fabric','قماش')]
GARMIN=[('g-fab3','CIRQA fabric 3.0','نسيج'),('g-sil','CIRQA silicone','سيليكون'),('g-20','QuickFit 20mm','كويك فت')]
FITBIT=[('f-fab','Fabric','قماش'),('f-sil','Silicone','سيليكون'),('f-mag','Magnetic','مغناطيس')]
APPLE=[('a-trail','Trail loop','ترايل'),('a-alp','Alpine loop','ألباين')]
GEAR=[('goggle','2 in 1 goggles','نظارة 2 in 1','w'),('sun','Sunglasses','نظارات شمسية','w'),('sock','Grip socks','دلاغات','h')]

def cells(items,h=170):
    return ''.join(f'<div class="c"><div class="im" style="height:{h}px"><img src="file://{C}{k}.png" style="height:{h}px"></div><b>{ar}</b><i class="en">{en}</i></div>' for k,en,ar in items)
def gear():
    out=''
    for k,en,ar,m in GEAR:
        st='width:150px' if m=='w' else 'height:165px'
        out+=f'<div class="c"><div class="im" style="height:170px"><img src="file://{C}{k}.png" style="{st}"></div><b>{ar.replace("2 in 1","<span class=en>2 in 1</span>")}</b><i class="en">{en}</i></div>'
    return out
def sec(label,body,flex=1):
    return f'<div class="sec" style="flex:{flex}"><div class="lb en">{label}</div><div class="row">{body}</div></div>'

def page():
    body=f'''
<div class="abs" style="inset:0;background:#F4F1F2"></div>
<div class="abs" style="left:0;right:0;top:0;height:300px;background:linear-gradient(160deg,#720842,#51022D)"></div>
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#E9C9D8">THE 974 RANGE</div>
<div class="abs ar" style="right:48px;left:48px;top:118px;color:#fff">
  <div style="font-weight:900;font-size:66px;line-height:1.1">كل اللي تحتاجه.. <span style="color:#C9A24B">من مكان واحد</span></div>
  <div style="font-weight:700;font-size:26px;opacity:.85;margin-top:6px">سيور <span class="en">Whoop</span> و <span class="en">Garmin</span> و <span class="en">Fitbit</span> و <span class="en">Apple Watch</span> · نظارات · دلاغات</div>
</div>
<div class="abs" style="left:24px;right:24px;top:318px;display:flex;flex-direction:column;gap:12px">
  {sec('WHOOP 5.0',cells(WHOOP,150))}
  <div style="display:flex;gap:12px">{sec('GARMIN',cells(GARMIN))}{sec('FITBIT AIR',cells(FITBIT))}</div>
  <div style="display:flex;gap:12px">{sec('APPLE WATCH',cells(APPLE),2)}{sec('GOGGLES · SUNGLASSES · SOCKS',gear(),3)}</div>
</div>
<div class="abs" style="left:0;right:0;top:1176px;text-align:center">{G.cta('تسوّق الحين من 974group.net','#720842','#fff')}</div>'''
    extra=G.CTA_CSS+'''.cta{font-size:26px;padding:6px 26px 10px}
.pf{bottom:20px} .pf .site{display:none!important}
.sec{background:#fff;border-radius:24px;padding:12px 8px 10px;box-shadow:0 6px 18px rgba(81,2,45,.07)}
.lb{font-weight:700;font-size:15px;letter-spacing:4px;color:#720842;text-align:center;margin-bottom:6px}
.row{display:flex;justify-content:space-around}
.c{display:flex;flex-direction:column;align-items:center;min-width:0}
.im{display:flex;align-items:center;justify-content:center}
.im img{filter:drop-shadow(0 8px 8px rgba(40,10,25,.18))}
.c b{font-weight:800;font-size:19px;color:#51022D;margin-top:6px;white-space:nowrap}
.c i{font-style:normal;font-weight:500;font-size:12px;color:#7E3D5C;letter-spacing:.5px;white-space:nowrap}'''
    return G.doc('#F4F1F2','#51022D',body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT; G.shot('974-full-range-post',page())
