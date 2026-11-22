# Photochromic Edition goggles (349 QAR, 275 in stock) - 22 Nov 2026. Post 1080x1350 + story 1080x1920.
# Fresh layout: background split down the middle - day (sun, sand) on the right / night (stars) on the left -
# with the goggle centred across the split.
import sys, os
sys.path.insert(0,'/home/claude/974-social/posts/2026-11/ig-ads-best-sellers'); import gen as G
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
GOG='/home/claude/974-social/reels/2026-11/src/g_photo.png'
SUN='#F2A541'
import random
random.seed(7)
STARS=''.join(f'<circle cx="{random.randint(10,530)}" cy="{random.randint(10,1900)}" r="{random.choice([1.2,1.6,2.2])}" fill="#fff" opacity="{random.choice([.35,.55,.8])}"/>' for _ in range(90))

def page(story):
    body=f'''
<div class="abs" style="left:0;top:0;bottom:0;width:540px;background:linear-gradient(180deg,#0B1026 0%,#141B3C 60%,#1E2550 100%)"></div>
<svg class="abs" style="left:0;top:0;width:540px;height:1920px" viewBox="0 0 540 1920">{STARS}<circle cx="120" cy="{150 if story else 300}" r="46" fill="#F4F1E6"/><circle cx="140" cy="{138 if story else 288}" r="42" fill="#121938"/></svg>
<div class="abs" style="left:540px;right:0;top:0;bottom:0;background:linear-gradient(180deg,#FBD38A 0%,#F6B860 45%,#E99A4A 100%)"></div>
<svg class="abs" style="left:540px;top:0;width:540px;height:1920px" viewBox="0 0 540 1920"><circle cx="420" cy="{150 if story else 300}" r="70" fill="#FFF3C4"/><circle cx="420" cy="{150 if story else 300}" r="110" fill="#FFF3C4" opacity=".25"/></svg>
<svg class="abs" style="left:0;right:0;bottom:0;width:1080px;height:calc(300px + var(--o))" viewBox="0 0 1080 300" preserveAspectRatio="none">
<path d="M0 120 C200 60 380 100 540 130 L540 300 L0 300Z" fill="#0A0E22"/><path d="M540 130 C700 160 880 70 1080 100 L1080 300 L540 300Z" fill="#C97B3A"/></svg><!--/bk-->
<img class="abs" src="file://{G.LW}" style="left:48px;top:46px;height:46px">
<div class="abs en" style="right:48px;top:58px;font-weight:700;font-size:16px;letter-spacing:5px;color:#3B2A12">PHOTOCHROMIC EDITION</div>
<div class="abs" style="left:0;right:0;top:120px;text-align:center;direction:rtl;font-weight:900;font-size:74px;line-height:1.1;color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.35)">
  تغمق في الشمس..<br>وتصفى بالليل</div>
<div class="abs en" style="left:70px;top:330px;font-weight:700;font-size:18px;letter-spacing:6px;color:#C9D1F2">NIGHT 🌙</div>
<div class="abs en" style="right:70px;top:330px;font-weight:700;font-size:18px;letter-spacing:6px;color:#4A3214">☀️ DAY</div>
<img class="abs" src="file://{GOG}" style="left:150px;top:380px;width:780px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.5))">
<div class="abs" style="left:0;right:0;top:930px;display:flex;justify-content:center;gap:12px;direction:rtl">
  <span class="tg">عدسة وحدة للنهار والليل</span><span class="tg">ضد الضباب</span><span class="tg">تحمي من الغبار</span>
</div>
<div class="abs" style="left:0;right:0;top:1020px;display:flex;justify-content:center;align-items:center;gap:30px;direction:rtl">
  <div style="font-weight:900;font-size:32px;color:#fff;text-shadow:0 3px 12px rgba(0,0,0,.4)"><span class="en" style="font-size:88px">349</span> ر.ق</div>
  {G.cta('اطلبها الحين','#fff','#0B1026')}
</div>'''
    extra=G.CTA_CSS+'''.tg{background:rgba(255,255,255,.9);border-radius:30px;padding:5px 18px 8px;font-weight:800;font-size:23px;color:#1B1B1B;box-shadow:0 6px 14px rgba(0,0,0,.2)}'''
    G.STORY=story
    return G.doc('#0B1026','#fff',body,pf_ink='#fff',extra=extra)

if __name__=='__main__':
    G.OUT=OUT
    G.shot('974-photochromic-v2-post',page(False))
    G.shot('974-photochromic-v2-story',page(True),1920)
