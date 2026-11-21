# UAE Edition goggles v2 (owner didn't like v1, 22 Nov 00:34): dark desert-night, "the full look" -
# goggle stacked above a mask like an outfit (small gap, no overlap), mask colour swatches, two price chips.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'
GOG='/home/claude/974-social/products/goggles/uae-edition-render.png'
MK='/home/claude/974-social/posts/2026-11/face-mask/src/cut/'
RED='#E0263E'; GRN='#1F9D55'
DUNES='''<svg class="abs" style="left:0;right:0;bottom:0;width:1080px;height:calc(380px + var(--o))" viewBox="0 0 1080 380" preserveAspectRatio="none">
<path d="M0 150 C200 70 360 110 520 160 C690 210 840 100 1080 120 L1080 380 L0 380Z" fill="#1E1A16"/>
<path d="M0 240 C180 190 340 210 500 245 C680 285 820 205 1080 225 L1080 380 L0 380Z" fill="#14110E"/></svg>'''

def page(story):
    sw=''.join(f'<div class="sw"><b style="background:{c}"></b><i class="en">{n}</i></div>' for c,n in [(RED,'RED'),(GRN,'GREEN'),('#F4F4F2','WHITE'),('#111','BLACK')])
    body=f'''
<div class="abs" style="inset:0;background:radial-gradient(70% 50% at 50% 38%,#3A332B 0%,#221E1A 55%,#14110E 100%)"></div>
{DUNES}<!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">

<div class="abs" style="left:48px;right:48px;top:100px;text-align:center;color:#fff;direction:rtl">
  <div class="en" style="font-weight:700;font-size:18px;letter-spacing:7px;color:#CFC6B8">974 GUARDS · UAE EDITION</div>
  <div style="font-weight:900;font-size:84px;line-height:1.05;margin-top:6px">اللوك كامل.. <span style="color:{RED}">للبر</span> 🇦🇪</div>
</div>
<img class="abs" src="file://{GOG}" style="left:190px;top:270px;width:700px;filter:drop-shadow(0 26px 30px rgba(0,0,0,.6))">
<img class="abs" src="file://{MK}white.png" style="left:410px;top:{770 if story else 755}px;width:260px;filter:drop-shadow(0 20px 24px rgba(0,0,0,.6))">
<div class="abs" style="left:56px;top:{820 if story else 800}px;width:300px;color:#fff;direction:rtl">
  <div style="font-weight:800;font-size:22px;color:#CFC6B8">النظارة</div>
  <div style="font-weight:900;font-size:28px"><span class="en" style="font-size:64px">319</span> ر.ق <span class="en" style="font-size:24px;opacity:.5;text-decoration:line-through">379</span></div>
  <div style="font-weight:700;font-size:20px;opacity:.75">عدستين مغناطيس · ضد الضباب</div>
</div>
<div class="abs" style="right:56px;top:{820 if story else 800}px;width:300px;color:#fff;direction:rtl;text-align:right">
  <div style="font-weight:800;font-size:22px;color:#CFC6B8">+ الماسك</div>
  <div style="font-weight:900;font-size:28px"><span class="en" style="font-size:64px">39</span> ر.ق</div>
  <div style="font-weight:700;font-size:20px;opacity:.75">بألوان العلم 👇</div>
</div>
<div class="abs" style="left:0;right:0;top:{1060 if story else 1050}px;display:flex;justify-content:center;gap:34px">{sw}</div>
<div class="abs" style="left:0;right:0;top:{1170 if story else 1150}px;text-align:center;display:{'block' if story else 'none'}">{G.cta('كمّل لوكك الحين','#fff','#14110E')}</div>'''
    extra=G.CTA_CSS+'''.sw{display:flex;flex-direction:column;align-items:center;gap:6px}.sw b{width:54px;height:54px;border-radius:50%;border:3px solid rgba(255,255,255,.85);box-shadow:0 6px 14px rgba(0,0,0,.5)}
.sw i{font-style:normal;font-weight:700;font-size:13px;letter-spacing:3px;color:#CFC6B8}'''
    G.STORY=story
    return G.doc('#14110E','#fff',body,pf_ink='#fff',extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-uae-goggles-v2-post',page(False))
    G.shot('974-uae-goggles-v2-story',page(True),1920)
