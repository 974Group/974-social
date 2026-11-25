# Whoop Enamel charms launch (69 QAR, 18 designs) — post + story, 25 Nov.
# Photo tiles from the real velvet shots (no cutouts: bars get eaten by rembg).
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); P = '/home/claude/charms/out/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
M, DEEP, GOLD, PAPER = '#720842', '#51022D', '#C9A24B', '#F4F1F2'
F = {n.split('-',1)[1][:-4]: P+n for n in os.listdir(P)}
NAME = {'matcha-cup':'Matcha Cup','handbag':'Handbag','pink-car':'Pink Car','black-car':'Black Car','tennis-ball':'Tennis Ball','ladybug':'Ladybug','horse':'Horse','pink-flower':'Pink Flower','cherry':'Cherry','heart':'Red Heart','pink-x':'Skis','football':'Football','sun':'Sun','snowflake':'Snowflake','airplane':'Airplane','bitcoin':'Bitcoin','evil-eye':'Evil Eye','padel':'Padel Racket'}
CSS = G.CTA_CSS + '''
.grid{position:absolute;display:grid;gap:18px}
.t{position:relative;border-radius:30px;overflow:hidden;box-shadow:0 18px 30px rgba(40,0,20,.28)}
.t img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.25)}
.t span{position:absolute;left:0;right:0;bottom:0;padding:26px 0 12px;text-align:center;font-family:Poppins;font-weight:700;font-size:21px;color:#fff;letter-spacing:.5px;background:linear-gradient(0deg,rgba(0,0,0,.75),rgba(0,0,0,0))}
'''
def tiles(keys, size):
    return ''.join(f'<div class="t" style="width:{size}px;height:{size}px"><img src="file://{F[k]}"><span>{NAME[k]}</span></div>' for k in keys)

def post():
    keys = ['evil-eye','heart','padel','football','matcha-cup','bitcoin','tennis-ball','airplane','cherry']
    body = f'''
<div class="abs" style="inset:0;background:{PAPER}"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:52px;top:52px;height:46px">
<div class="abs en" style="left:52px;top:110px;font-weight:700;font-size:17px;letter-spacing:4px;color:{M}">WHOOP CHARMS · NEW</div>
<div class="abs ar" style="right:52px;top:30px;text-align:right;color:{DEEP}">
  <div style="font-weight:900;font-size:66px;line-height:1.15">تشارمز الووب وصلت</div>
  <div style="font-weight:700;font-size:30px;margin-top:4px;color:{M}"><span class="en" style="font-weight:800">18</span> تصميم · ركّبها على سيرك وغيّر الستايل</div>
</div>
<div class="grid" style="left:132px;top:225px;grid-template-columns:repeat(3,260px)">{tiles(keys,260)}</div>
<div class="abs" style="left:132px;right:132px;top:1060px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <div style="font-weight:900;font-size:30px;color:{DEEP}"><span class="en" style="font-size:76px;font-weight:900">69</span> ر.ق <span style="font-size:24px;font-weight:700;color:{M}">للحبة</span></div>
  {G.cta('اختار تصميمك', M, '#fff')}
</div>'''
    return G.doc(PAPER, DEEP, body, extra=CSS)

def story():
    keys = ['sun','snowflake','pink-x','horse','pink-flower','ladybug','handbag','pink-car','black-car']
    body = f'''
<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 50% 40%,{M} 0%,{DEEP} 70%)"></div><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:50%;transform:translateX(-50%);top:0px;height:52px">
<div class="abs ar" style="left:0;right:0;top:80px;text-align:center;color:#fff">
  <div style="font-weight:900;font-size:78px;line-height:1.1">اختار ستايلك</div>
  <div style="font-weight:700;font-size:32px;margin-top:8px;color:{GOLD}">تشارمز يديدة لسير الووب · <span class="en">18</span> تصميم</div>
</div>
<div class="grid" style="left:110px;top:290px;grid-template-columns:repeat(3,274px)">{tiles(keys,274)}</div>
<div class="abs" style="left:110px;right:110px;top:1185px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <div style="font-weight:900;font-size:32px;color:#fff"><span class="en" style="font-size:84px;font-weight:900;color:{GOLD}">69</span> ر.ق للحبة</div>
  {G.cta('اطلب الحين', GOLD, DEEP)}
</div>'''
    return G.doc(DEEP, '#fff', body, extra=CSS)

if __name__ == '__main__':
    G.STORY = False; G.shot('974-whoop-charms-post', post())
    G.STORY = True; G.shot('974-whoop-charms-story', story(), 1920)
    print('ok')
