# Elastic Loop v2 (21 Nov 2026): fresh layout - all 26 colours as two tilted rows of strips (same size,
# same direction, no overlap), headline «لون لكل طقم». Post 1080x1350 + story 1080x1920. Price 99.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); S=D+'/src/'; OUT=D+'/out'
COLS=['black','grey-black','black-grey','dark-grey','grey','grey-white','black-white','white','black-red','red','maroon','maroon-beige','orange',
      'yellow','khaki','khaki-white','black-khaki','green','green-white','green-yellow','tiffany','lightblue-white','blue','navy','darkblue-white','navy-white-orange']
M='#720842'; INK='#2A0F1C'

def page(story):
    sh=290 if not story else 330
    r1=''.join(f'<img src="file://{S}{c}-v.png" style="height:{sh}px">' for c in COLS[:13])
    r2=''.join(f'<img src="file://{S}{c}-v.png" style="height:{sh}px">' for c in COLS[13:])
    body=f'''
<div class="abs" style="inset:0;background:linear-gradient(180deg,#F7F3F4 0%,#EDE5E8 100%)"></div><!--/bk-->
<img class="abs" src="file://{G.LB}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#8A5A6E">ELASTIC LOOP · 26 COLOURS</div>
<div class="abs" style="right:48px;left:48px;top:112px;color:{INK};direction:rtl;text-align:right">
  <div style="font-weight:900;font-size:80px;line-height:1.05">لون لكل طقم.. <span style="color:{M}">٢٦ لون</span></div>
  <div style="font-weight:700;font-size:29px;opacity:.8;margin-top:6px">سير مطاطي منسوج · تلبسه بسحبة بدون قفل</div>
</div>
<div class="abs" style="left:0;right:0;top:{320 if not story else 325}px;height:{2*sh+60}px;display:flex;flex-direction:column;align-items:center;gap:26px;transform:rotate(-8deg)">
  <div class="rw">{r1}</div><div class="rw">{r2}</div>
</div>
<div class="abs" style="left:48px;right:48px;top:{1015 if not story else 1085}px;direction:rtl;display:flex;justify-content:center;gap:12px">
  <span class="ch en">Apple Watch</span><span class="ch">ساعات <span class="en">20mm</span></span><span class="ch en">MoonSwatch</span>
</div>
<div class="abs" style="left:48px;right:48px;top:{1100 if not story else 1170}px;direction:rtl;display:flex;align-items:center;justify-content:space-between;color:{INK}">
  <div style="font-weight:900;font-size:32px"><span class="en" style="font-size:88px;color:{M}">99</span> ر.ق</div>
  {G.cta('اختار لونك',M,'#fff')}
</div>'''
    extra=G.CTA_CSS+'''.rw{display:flex;gap:16px;justify-content:center}.rw img{filter:drop-shadow(0 10px 10px rgba(42,15,28,.18))}
.ch{background:#fff;border:2px solid #E3D3DA;border-radius:30px;padding:5px 22px 8px;font-weight:800;font-size:24px;color:#2A0F1C}'''
    G.STORY=story
    return G.doc('#F4F1F2',INK,body,extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-elastic-v2-post',page(False))
    G.shot('974-elastic-v2-story',page(True),1920)
