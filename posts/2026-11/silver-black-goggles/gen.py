# Silver & Black Edition goggles (last season, 319 QAR, 108 in stock) — post + story, colours from the product (graphite / silver / black)
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LW
C = '/home/claude/974-social/posts/2026-11/silver-black-goggles/cut/'
INK = '#ECEEF1'
BG = 'radial-gradient(90% 55% at 50% 40%,#43474D 0%,#24272B 50%,#0E0F11 100%)'

def g(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    feats = [('عدستين', 'شمس للنهار + شفافة لليل'), ('مغناطيس', 'تبدّل العدسة بثواني'), ('ضد الضباب', 'رؤية واضحة طول الطلعة')]
    fe = ''.join(f'<div class="ft"><b>{a}</b><span>{b}</span></div>' for a, b in feats)
    hw = 980 if story else 940
    body = f'''
<div class="abs en ol" style="left:-14px;top:{o+(330 if story else 250)}px;font-weight:700;font-size:{205 if story else 190}px;line-height:.86;letter-spacing:-7px;color:rgba(236,238,241,.10);white-space:nowrap">SILVER<br>&amp; BLACK</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(120 if story else 112)}px">
 <div style="font-weight:900;font-size:{84 if story else 72}px;line-height:1.08">موسم الطلعات بدا..<br><span class="sil">وهي جاهزة</span></div>
 <div class="en" style="font-weight:700;font-size:{24 if story else 22}px;letter-spacing:4px;margin-top:14px;opacity:.6;text-align:right">SILVER &amp; BLACK EDITION</div>
</div>
<img class="abs hero" src="file://{C}0c.png" style="left:{(1080-hw)//2}px;top:{o+(470 if story else 395)}px;width:{hw}px">
<div class="abs fts" style="top:{o+(1060 if story else 960)}px">{fe}</div>'''
    if story:
        body += f'''<div class="abs ar" style="right:48px;left:48px;top:{o+1240}px;display:flex;align-items:center;gap:26px;direction:rtl">
 <img src="file://{C}3c.png" style="height:170px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.5))">
 <div><div style="font-weight:900;font-size:34px">ومعاها عدسة لليل بلمعة ice blue</div><div style="font-weight:700;font-size:24px;opacity:.7">للكشتة والطلعات بعد المغرب</div></div></div>'''
    extra = f'''.sil{{background:linear-gradient(180deg,#FFFFFF 0%,#B9BEC5 55%,#8C9199 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.hero{{filter:drop-shadow(0 40px 46px rgba(0,0,0,.6))}}
.fts{{left:48px;right:48px;display:flex;direction:rtl}} .ft{{flex:1;padding:0 18px;border-left:1.5px solid rgba(236,238,241,.22);text-align:right}} .ft:last-child{{border-left:none}} .ft:first-child{{padding-right:0}}
.ft b{{display:block;font-weight:900;font-size:{34 if story else 31}px}} .ft span{{display:block;font-weight:700;font-size:{21 if story else 19}px;opacity:.7;line-height:1.35}}
.pill{{background:{INK};color:#16181B;border:none!important}}'''
    cta = 'اطلبها من <em>974group.net</em> 🛒' if story else 'علّق <em>«نظارة»</em> ونرسل لك الرابط'
    return page(H, BG, INK, body, story, LW, '974 GUARDS', 319, cta, extra, pf_ink='#FFFFFF')

if __name__ == '__main__':
    shot('974-silver-black-post', g(), 1350)
    shot('974-silver-black-story', g(True), 1920)
