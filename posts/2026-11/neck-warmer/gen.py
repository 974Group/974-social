# Reversible Neck Warmer (974 Guards, 39 QAR, black outside / grey inside) — post + story. Colours from the product: black on winter grey.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
C = '/home/claude/974-social/posts/2026-11/neck-warmer/cut/'
INK = '#17181A'
BG = 'radial-gradient(85% 55% at 34% 50%,#F4F5F6 0%,#D5D8DC 55%,#B4B8BE 100%)'

def g(story=False):
    o = 150 if story else 0
    H = 1920 if story else 1350
    feats = [('دافي', 'يحفظ حرارتك في البرد'), ('ناعم', 'قماش مريح على البشرة'), ('خفيف', 'ما تحس إنك لابسه')]
    fe = ''.join(f'<div class="ft"><b>{a}</b><span>{b}</span></div>' for a, b in feats)
    pw = 640 if story else 590
    body = f'''
<div class="abs en ol" style="left:-16px;top:{o+(300 if story else 236)}px;font-weight:700;font-size:{300 if story else 280}px;line-height:.82;letter-spacing:-12px;color:rgba(23,24,26,.10);white-space:nowrap">WARM</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(118 if story else 108)}px">
 <div style="font-weight:900;font-size:{88 if story else 76}px;line-height:1.08">البرد ياي..<br><span style="color:#6E737B">ودفا رقبتك عندنا</span></div>
 <div class="en" style="font-weight:700;font-size:{24 if story else 22}px;letter-spacing:4px;margin-top:14px;opacity:.6;text-align:right">REVERSIBLE NECK WARMER</div>
</div>
<img class="abs prod" src="file://{C}warmer.png" style="left:{40 if story else 44}px;top:{o+(590 if story else 425)}px;height:{600 if story else 490}px">
<div class="abs ar" style="right:48px;top:{o+(640 if story else 500)}px;width:380px">
 <div style="font-weight:900;font-size:{40 if story else 36}px;line-height:1.2">وجهين..<br>تلبسه على كيفك</div>
 <div class="sw"><i style="background:#17181A"></i><div><b>أسود</b><span>من برع</span></div></div>
 <div class="sw"><i style="background:#8D9198"></i><div><b>رصاصي</b><span>من داخل</span></div></div>
</div>
<div class="abs fts" style="top:{o+(1270 if story else 965)}px">{fe}</div>'''
    extra = f'''.prod{{filter:drop-shadow(0 36px 40px rgba(20,22,26,.38))}}
.sw{{display:flex;align-items:center;gap:16px;direction:rtl;margin-top:{22 if story else 18}px}} .sw i{{width:{62 if story else 56}px;height:{62 if story else 56}px;border-radius:50%;border:4px solid #fff;box-shadow:0 8px 16px rgba(20,22,26,.25);flex:none}}
.sw b{{display:block;font-weight:900;font-size:{30 if story else 27}px;line-height:1.1}} .sw span{{font-weight:700;font-size:{22 if story else 20}px;opacity:.65}}
.fts{{left:48px;right:48px;display:flex;direction:rtl}} .ft{{flex:1;padding:0 18px;border-left:1.5px solid rgba(23,24,26,.2);text-align:right}} .ft:last-child{{border-left:none}} .ft:first-child{{padding-right:0}}
.ft b{{display:block;font-weight:900;font-size:{36 if story else 32}px}} .ft span{{display:block;font-weight:700;font-size:{21 if story else 19}px;opacity:.7;line-height:1.35}}
.pill{{background:{INK};color:#fff;border:none!important}}'''
    return page(H, BG, INK, body, story, LB, '974 GUARDS', 39, 'اطلبه من <em>974group.net</em> 🛒', extra)

if __name__ == '__main__':
    shot('974-neck-warmer-post', g(), 1350)
    shot('974-neck-warmer-story', g(True), 1920)
