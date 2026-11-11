# Two Snapchat ad creatives (1080x1920) for the maroon Whoop 5.0/MG silicone band, 99 QAR.
# Snap safe zone: keep the bottom ~320px clear (Shop now bar) and the top ~150px light.
#  A) light  - "لون علمنا.. على يدك" (the IG version the owner liked)
#  B) dark   - National Day angle: "اليوم الوطني قرّب"
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB, LW
C = '/home/claude/974-social/posts/2026-11/maroon-qatar/cut/'
MAR = '#6A0B12'

def serr(fill):
    n = 9; st = 1080 / n; y0 = 14; d = 22
    pts = '0,0 1080,0 1080,%d ' % y0 + ' '.join(f'{1080-i*st:.0f},{y0} {1080-(i+.5)*st:.0f},{y0+d}' for i in range(n)) + f' 0,{y0}'
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="40"><polygon fill="{fill}" points="{pts}"/></svg>'

def snapify(html):
    # lift payment footer + price/CTA row above Snap's bottom UI
    return html.replace('bottom:250px', 'bottom:440px').replace('bottom:124px', 'bottom:330px')

def A():
    INK = '#2A1013'; bh = 600; btop = 520
    body = f'''{serr(MAR)}
<div class="abs en" style="left:-10px;top:500px;font-weight:700;font-size:250px;line-height:.84;letter-spacing:-9px;color:rgba(106,11,18,.07);white-space:nowrap">MAROON</div>
<div class="abs ar" style="right:48px;left:48px;top:250px">
 <div style="font-weight:900;font-size:96px;line-height:1.05;color:{MAR}">لون علمنا..<br>على يدك</div>
 <div style="font-weight:700;font-size:32px;margin-top:14px;color:{INK};opacity:.8">سير سيليكون عنابي لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></div>
</div>
<div class="abs" style="left:50%;transform:translateX(-50%);top:{btop+bh-36}px;width:{bh*.9:.0f}px;height:56px;border-radius:50%;background:radial-gradient(closest-side,rgba(60,10,15,.28),transparent)"></div>
<img class="abs band" src="file://{C}p49m-0.png" style="left:50%;transform:translateX(-50%);top:{btop}px;height:{bh}px">
<div class="abs ar" style="right:48px;left:48px;top:{btop+bh+40}px">
 <div class="pts"><span>عنابي برّا.. أبيض داخل</span><i></i><span>حديدة فضية لمّاعة</span><i></i><span>خفيف وما يتأثر بالعرق</span></div>
</div>'''
    extra = f'''.top{{top:90px!important}} .band{{filter:drop-shadow(0 26px 30px rgba(80,10,18,.22))}}
.pts{{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;direction:rtl;font-weight:800;font-size:28px;color:{INK}}} .pts i{{width:7px;height:7px;border-radius:50%;background:{MAR};opacity:.6}}
.pill{{background:{MAR};color:#fff;border:none!important;font-size:40px!important}} .cta{{font-size:30px!important}}'''
    return snapify(page(1920, 'radial-gradient(70% 45% at 50% 48%,#FFFFFF 0%,#F6F1F1 55%,#EDE3E4 100%)', INK, body, True, LB,
                        '974 BANDS', 99, 'اطلبه الحين من <em>974group.net</em>', extra, pf_ink=INK))

def B():
    bh = 680; btop = 550
    body = f'''{serr('#fff')}
<div class="abs ar" style="right:48px;left:48px;top:250px">
 <div style="font-weight:700;font-size:34px;opacity:.8">اليوم الوطني قرّب 🇶🇦</div>
 <div style="font-weight:900;font-size:92px;line-height:1.05;margin-top:6px">خلّ العنابي<br>على معصمك</div>
</div>
<img class="abs band" src="file://{C}p49m-0.png" style="left:50%;transform:translateX(-50%);top:{btop}px;height:{bh}px">
<div class="abs ar" style="right:48px;left:48px;top:{btop+bh+30}px">
 <div class="pts"><span>سيليكون لـ <span class="en">Whoop 5.0</span> و <span class="en">MG</span></span><i></i><span>عنابي برّا.. أبيض داخل</span></div>
</div>'''
    extra = '''.top{top:90px!important} .band{filter:drop-shadow(0 40px 46px rgba(0,0,0,.55))}
.pts{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;direction:rtl;font-weight:800;font-size:28px} .pts i{width:7px;height:7px;border-radius:50%;background:#fff;opacity:.55}
.pill{background:#fff;color:#5A0A0F;border:none!important;font-size:40px!important} .cta{font-size:30px!important}'''
    return snapify(page(1920, 'radial-gradient(75% 50% at 50% 50%,#6A0B0F 0%,#3E0306 50%,#1E0102 100%)', '#FFFFFF', body, True, LW,
                        '974 BANDS', 99, 'اطلبه الحين من <em>974group.net</em>', extra, pf_ink='#FFFFFF'))

if __name__ == '__main__':
    shot('974-maroon-snap-A-light', A(), 1920)
    shot('974-maroon-snap-B-national-day', B(), 1920)
