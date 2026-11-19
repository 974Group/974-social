# Full range in one story (owner 19 Nov 2026, v2): one of every band type + glasses + socks. Story 1080x1920.
# v2 feedback: all Whoop facing the same way (the right-facing ones are mirrored to face left like the
# silicone and Rolex print); Fitbit silicone -> 2.0; Garmin = watch QuickFit vs CIRQA (not materials);
# glasses on their own (2 in 1, sunglasses, brown goggles); one Apple Watch; socks = running, grip, pilates.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); C=D+'/cut/'; OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
WHOOP=[('w-sil','Silicone','سيليكون'),('w-wp-L','Waterproof','ووتر بروف'),('w-soft-L','Soft fabric','قماش ناعم'),('w-rolex','Rolex 3D','رولكس'),('w-wool-L','Wool','صوف'),('w-fab-L','Fabric','قماش')]
GARMIN=[('g-20','QuickFit · watches','حق الساعات'),('g-fab3','CIRQA','حق السيركا')]
FITBIT=[('f-fab-grey','Fabric','قماش'),('f-sil2','Silicone 2.0','سيليكون'),('f-mag','Magnetic','مغناطيس')]
APPLE=[('a-trail','38 · 40 · 41 · 42 · 44 · 45 · 46 · 49','<span class="en">38–49mm</span>')]
GLASS=[('goggle','2 in 1','بر وبحر'),('sun','Sunglasses','جري وسيكل'),('g-brown','Brown Edition','بر وتزلج')]
SOCKS=[('s-run','Running','جري'),('sock-white','Grip','قريب'),('s-pil','Pilates','بيلاتيس')]

def lab(ar): return ar.replace('2 in 1','<span class="en">2 in 1</span>')
def cells(items,h,mode='h'):
    out=''
    for k,en,ar in items:
        st=f'height:{h}px' if mode=='h' else f'width:{h}px'
        out+=f'<div class="c"><div class="im" style="height:{h}px"><img src="file://{C}{k}.png" style="{st}"></div><b>{lab(ar)}</b><i class="en">{en}</i></div>'
    return out
def sec(label,body,flex=1):
    return f'<div class="sec" style="flex:{flex}"><div class="lb en">{label}</div><div class="row">{body}</div></div>'

def page(feed=False):
    h=140 if feed else 145; hg=150 if feed else 165
    body=f'''
<div class="abs" style="inset:0;background:#F4F1F2"></div>
<div class="abs" style="left:0;right:0;top:0;height:{455 if not feed else 250}px;background:linear-gradient(160deg,#720842,#51022D)"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:{210 if not feed else 40}px;height:{50 if not feed else 42}px">
<div class="abs en" style="right:48px;top:{226 if not feed else 54}px;font-weight:700;font-size:17px;letter-spacing:5px;color:#E9C9D8">THE 974 RANGE</div>
<div class="abs ar" style="right:48px;left:48px;top:{285 if not feed else 95}px;color:#fff">
  <div style="font-weight:900;font-size:{58 if not feed else 52}px;line-height:1.1">كل اللي تحتاجه.. <span style="color:#C9A24B">من مكان واحد</span></div>
</div>
<div class="abs" style="left:24px;right:24px;top:{472 if not feed else 262}px;display:flex;flex-direction:column;gap:{12 if not feed else 9}px">
  {sec('WHOOP 5.0',cells(WHOOP,h))}
  <div style="display:flex;gap:14px">{sec('GARMIN',cells(GARMIN,h),2)}{sec('FITBIT AIR',cells(FITBIT,h),3)}</div>
  <div style="display:flex;gap:14px">{sec('APPLE WATCH',cells(APPLE,h),1)}{sec('GLASSES',cells(GLASS,hg,'w'),3)}</div>
  {sec('SOCKS',cells(SOCKS,h))}
</div>
<div class="abs" style="right:48px;top:{370 if not feed else 172}px">{G.cta('تسوّق الحين من 974group.net','#C9A24B','#51022D')}</div>'''
    extra=G.CTA_CSS+''''''+('.pf{bottom:22px!important} body{height:1350px!important} .c b{font-size:18px!important;margin-top:2px!important} .c i{font-size:12px!important} .sec{padding:7px 8px 7px!important} .lb{font-size:14px!important;margin-bottom:2px!important} .cta{font-size:24px!important;padding:5px 24px 9px!important}' if feed else '.pf{bottom:250px!important} body{height:1920px!important}')+''' .pf .site{display:none!important}
.cta{font-size:28px}
.sec{background:#fff;border-radius:26px;padding:10px 8px 10px;box-shadow:0 6px 18px rgba(81,2,45,.07)}
.lb{font-weight:700;font-size:16px;letter-spacing:5px;color:#720842;text-align:center;margin-bottom:4px}
.row{display:flex;justify-content:space-around}
.c{display:flex;flex-direction:column;align-items:center;min-width:0}
.im{display:flex;align-items:center;justify-content:center}
.im img{filter:drop-shadow(0 8px 8px rgba(40,10,25,.18))}
.c b{font-weight:800;font-size:21px;color:#51022D;margin-top:4px;white-space:nowrap}
.c i{font-style:normal;font-weight:500;font-size:13px;color:#7E3D5C;letter-spacing:.5px;white-space:nowrap}'''
    G.STORY=False
    return G.doc('#F4F1F2','#51022D',body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT; G.shot('974-full-range-story',page(),1920); G.shot('974-full-range-feed',page(True),1350)
