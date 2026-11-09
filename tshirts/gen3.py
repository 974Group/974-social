# "Now on the site" post: T-shirts live under Designy + size help (height & weight)
import sys
from gen2 import page, shot, C, LW, NAVY, A

def live(story=False):
    o=150 if story else 0; H=1920 if story else 1350
    sh=262 if not story else 256
    shirts=''.join(f'<img src="file://{C}{n}-back.png" style="height:{sh}px">' for n in ['beige','white','blue','navy'])
    body=f'''
<div class="abs en ol" style="left:-12px;top:{o+(150 if story else 120)}px;font-weight:700;font-size:{205 if story else 190}px;line-height:.86;letter-spacing:-7px;color:rgba(255,255,255,.12);white-space:nowrap">NOW<br>LIVE</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(170 if story else 130)}px">
 <div style="font-weight:900;font-size:{100 if story else 90}px;line-height:1.05">نزلت..<br><span style="color:#8EC0EA">في الموقع</span></div>
 <div style="font-weight:800;font-size:{36 if story else 33}px;margin-top:{22 if story else 16}px">تلقاها تحت قسم <span class="en" style="color:#8EC0EA">Designy</span></div>
 <div class="path" style="margin-top:10px">
  <span class="en">974group.net</span><i>›</i><span class="en dz">Designy</span><i>›</i><span class="en">T-shirts</span>
 </div>
</div>
<div class="abs shirts" style="left:0;right:0;top:{o+(660 if story else 570)}px">{shirts}</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1060 if story else 880)}px">
 <div style="font-weight:900;font-size:{56 if story else 50}px;line-height:1.15">مب عارف مقاسك؟</div>
 <div style="font-weight:700;font-size:{31 if story else 28}px;margin-top:6px;opacity:.9">اكتب <u>طولك</u> و<u>وزنك</u> في الموقع.. ويقترح لك المقاس الأنسب</div>
 <div class="calc"><span>175 سم</span><b>+</b><span>80 كغ</span><b>=</b><span class="res en">L</span></div>
</div>'''
    extra=f'''.path{{display:flex;gap:14px;align-items:center;direction:ltr;justify-content:flex-end;font-weight:700;font-size:{30 if story else 27}px}}
.path{{font-size:{24 if story else 22}px!important}} .path span{{opacity:.7}} .path .dz{{opacity:1;color:#fff;border-bottom:3px solid #8EC0EA;padding-bottom:2px}} .path i{{font-style:normal;opacity:.45;font-family:Poppins}}
.shirts{{display:flex;justify-content:center;gap:{14 if story else 12}px}} .shirts img{{filter:drop-shadow(0 18px 24px rgba(0,0,0,.45))}}
.calc{{display:flex;gap:14px;align-items:center;margin-top:{20 if story else 16}px;direction:rtl;font-weight:800;font-size:{28 if story else 26}px}}
.calc span{{border-bottom:2px dashed rgba(255,255,255,.5);padding:0 4px 4px}} .calc b{{opacity:.5;font-family:Poppins}}
.calc .res{{border:none;background:#8EC0EA;color:{NAVY};border-radius:40px;padding:2px 26px 4px;font-weight:700}}'''
    return page(1080,H,f'linear-gradient(180deg,#0F1630 0%,{NAVY} 60%,#1A2547 100%)','#FFFFFF',body,story,LW,extra)

if __name__=='__main__':
    shot('974-drop01-live-post',live(),1350)
    shot('974-drop01-live-story',live(True),1920)
