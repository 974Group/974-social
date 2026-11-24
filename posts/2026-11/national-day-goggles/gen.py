# National Day Limited Edition goggles (399 QAR) — only 5 left, each a numbered piece: 54, 62, 64, 73, 93.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
M = '#8A1538'; DK = '#51022D'; BG = '#FFFFFF'
NUMS = ['54', '62', '64', '73', '93']
CSS = G.CTA_CSS + f'''.num{{width:150px;height:150px;border-radius:24px;background:{M};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(138,21,56,.25)}}
.num b{{font-family:Poppins;font-weight:900;font-size:64px;line-height:1}}.num i{{font-family:Poppins;font-style:normal;font-weight:700;font-size:13px;letter-spacing:3px;opacity:.8;margin-top:2px}}
.saw{{position:absolute;top:0;bottom:0;width:46px;background:{M};-webkit-mask:linear-gradient(135deg,#000 50%,transparent 50%) 0 0/46px 46px, linear-gradient(45deg,transparent 50%,#000 50%) 0 23px/46px 46px}}'''


def flag_edge():  # 9-point serrated maroon edge on the right side
    pts = []
    for i in range(9):
        y0 = i * (100 / 9); pts += [f'0% {y0:.2f}%', f'100% {y0 + 100/18:.2f}%']
    pts += ['0% 100%']
    return f'<div class="abs" style="right:0;top:0;bottom:0;width:120px;background:{M}"></div><div class="abs" style="right:120px;top:0;bottom:0;width:44px;background:{M};clip-path:polygon(100% 0%, {", ".join(pts)}, 100% 100%)"></div>'


def nums():
    return ''.join(f'<div class="num"><i>NO.</i><b>{n}</b></div>' for n in NUMS)


def post():
    body = f'''<div class="abs" style="inset:0;background:{BG}"></div>{flag_edge()}<!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:16px;letter-spacing:4px;color:{M}">NATIONAL DAY · LIMITED EDITION</div>
<div class="abs ar" style="right:200px;top:36px;color:{DK};text-align:right">
 <div style="font-weight:900;font-size:58px;line-height:1.12">النسخة الخاصة<br>لليوم الوطني 🇶🇦</div></div>
<img class="abs" src="file://{S}hero.png" style="left:30px;top:240px;width:780px;mix-blend-mode:multiply">
<div class="abs ar" style="left:48px;right:200px;top:800px;color:{DK};text-align:right">
 <div style="font-weight:900;font-size:46px">باقي <span style="color:{M}">٥ حبات</span> بس 🔥</div>
 <div style="font-weight:700;font-size:24px;color:#6b4a58;margin-top:2px">كل نظارة مرقّمة.. وهذي الأرقام اللي باقية</div></div>
<div class="abs" style="left:48px;right:200px;top:935px;display:flex;justify-content:space-between;direction:ltr;transform:scale(.88);transform-origin:left top">{nums()}</div>
<div class="abs" style="left:48px;right:200px;top:1075px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{DK}"><span class="en" style="font-size:70px;font-weight:900">399</span> ر.ق</div>{G.cta('احجز رقمك', M, '#fff')}</div>'''
    return G.doc(BG, DK, body, extra=CSS)


def story():
    body = f'''<div class="abs" style="inset:0;background:{BG}"></div>{flag_edge()}<!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:0;height:46px">
<div class="abs ar" style="right:200px;top:80px;color:{DK};text-align:right"><div style="font-weight:900;font-size:66px;line-height:1.1">النسخة الخاصة<br>لليوم الوطني 🇶🇦</div>
 <div class="en" style="font-weight:700;font-size:18px;letter-spacing:4px;color:{M};margin-top:10px">NATIONAL DAY · LIMITED EDITION</div></div>
<img class="abs" src="file://{S}side.png" style="left:10px;top:290px;width:820px;mix-blend-mode:multiply">
<div class="abs ar" style="left:48px;right:200px;top:800px;color:{DK};text-align:right">
 <div style="font-weight:900;font-size:56px">باقي <span style="color:{M}">٥ حبات</span> بس 🔥</div>
 <div style="font-weight:700;font-size:26px;color:#6b4a58;margin-top:4px">كل نظارة مرقّمة.. اختار رقمك قبل لا يخلص</div></div>
<div class="abs" style="left:48px;right:200px;top:955px;display:flex;gap:10px;direction:ltr;transform:scale(.97);transform-origin:left top">{nums()}</div>
<div class="abs" style="left:48px;right:200px;top:1150px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
 <div style="font-weight:900;font-size:30px;color:{DK}"><span class="en" style="font-size:74px;font-weight:900">399</span> ر.ق</div>{G.cta('احجز رقمك', M, '#fff')}</div>'''
    return G.doc(BG, DK, body, extra=CSS)


if __name__ == '__main__':
    G.STORY = False; G.shot('974-national-day-post', post())
    G.STORY = True; G.shot('974-national-day-story', story(), 1920)
    print('ok')
