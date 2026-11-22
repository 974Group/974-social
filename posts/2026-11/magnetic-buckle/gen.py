# Apple Watch magnetic buckle bands (79 QAR): one best-selling colour per style, post + story, 22 Nov 2026 15:30.
# Picks by units sold: plain Black, stripe Orange & black, two-tone Army green & black, leather Black, elastic Black.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D = os.path.dirname(os.path.abspath(__file__)); S = D + '/src/'
G.OUT = D + '/out'; os.makedirs(G.OUT, exist_ok=True)
INK = '#141414'; OR = '#F26A1B'
BANDS = [('plain', 'ساده', 'Black'), ('stripe', 'بخط', 'Orange × Black'), ('twotone', 'لونين', 'Army Green × Black'),
         ('leather', 'جلد', 'Black Leather'), ('elastic', 'إلاستيك', 'Black Elastic')]
CSS = G.CTA_CSS + f'''
.card{{width:318px;height:368px;background:#fff;border-radius:34px;box-shadow:0 18px 40px rgba(0,0,0,.08);position:relative;display:flex;flex-direction:column;align-items:center}}
.card img{{height:252px;margin-top:22px;filter:drop-shadow(0 14px 16px rgba(0,0,0,.18))}}
.card b{{font-weight:900;font-size:34px;line-height:1;margin-top:16px;color:{INK}}}
.card i{{font-family:Poppins;font-style:normal;font-weight:500;font-size:17px;color:#6d6d6d;margin-top:8px}}
.row{{display:flex;justify-content:center;gap:24px;direction:rtl}}
.chip{{display:inline-block;border:2px solid {INK};border-radius:30px;padding:2px 18px 6px;font-weight:800;font-size:22px}}
'''


def card(k, ar, en):
    return f'<div class="card"><img src="file://{S}{k}-cut.png"><b>{ar}</b><i>{en}</i></div>'


def page():
    r1 = ''.join(card(*b) for b in BANDS[:3]); r2 = ''.join(card(*b) for b in BANDS[3:])
    body = f'''
<div class="abs" style="inset:0;background:radial-gradient(90% 60% at 80% 10%,#FFFFFF 0%,#EFECE8 60%,#E6E2DD 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="left:48px;top:104px;font-weight:700;font-size:16px;letter-spacing:4px;color:#555">APPLE WATCH · MAGNETIC BUCKLE</div>
<div class="abs ar" style="right:48px;top:36px;color:{INK}">
  <div style="font-weight:900;font-size:66px;line-height:1.12">قفل مغناطيسي..<br><span style="color:{OR}">يتسكر بثانية 🧲</span></div>
  <div style="font-weight:700;font-size:26px;color:#444;margin-top:8px">5 أشكال.. وهذا الأكثر طلب من كل شكل</div>
</div>
<div class="abs" style="left:0;right:0;top:268px"><div class="row">{r1}</div></div>
<div class="abs" style="left:0;right:0;top:660px"><div class="row">{r2}</div></div>
<div class="abs" style="left:48px;right:48px;top:1050px;display:flex;align-items:center;justify-content:space-between;direction:rtl">
  <div style="direction:rtl;color:{INK}">
    <div style="font-weight:900;font-size:30px"><span class="en" style="font-size:76px;font-weight:900">79</span> ر.ق</div>
  </div>
  <div style="display:flex;flex-direction:column;align-items:flex-start;gap:12px">
    <span class="chip">يناسب <span class="en">44–49mm</span></span>
    {G.cta('اطلبه الحين', INK, '#fff')}
  </div>
</div>'''
    return G.doc('#EFECE8', INK, body, extra=CSS)


if __name__ == '__main__':
    G.STORY = False; G.shot('974-magnetic-buckle-post', page())
    G.STORY = True; G.shot('974-magnetic-buckle-story', page(), 1920)
    print('ok')
