# Plain face mask — "camping season" post + story (12 Nov 2026). Night desert, warm campfire glow.
import sys, os
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LW
D = '/home/claude/974-social/posts/2026-11/face-mask/'
C = D + 'src/cutd/'
ROW = ['black', 'khaki', 'white', 'orange', 'armygreen', 'navy', 'red', 'beige']
SAND = '#E9B871'

def mask(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350; INK = '#F4ECE2'
    hero_h = 520 if story else 430
    mini = 118; cw = 126
    x0 = (1080 - cw * len(ROW)) // 2
    row = ''.join(f'<img class="abs mm" src="file://{C}{f}.png" style="left:{x0+i*cw+(cw-mini*0.92)/2:.0f}px;height:{mini}px">' for i, f in enumerate(ROW))
    body = f'''
<div class="abs" style="left:-160px;right:-160px;bottom:{-260 if story else -300}px;height:900px;background:radial-gradient(50% 50% at 50% 50%,rgba(240,140,60,.30) 0%,rgba(240,140,60,0) 70%)"></div>
<div class="abs" style="left:-100px;top:{o+(250 if story else 170)}px;width:{hero_h+240}px;height:{hero_h+240}px;border-radius:50%;background:radial-gradient(circle,rgba(233,184,113,.20) 0%,rgba(233,184,113,0) 62%)"></div>
<img class="abs" src="file://{C}khaki.png" style="left:{40 if story else 36}px;top:{o+(330 if story else 250)}px;height:{hero_h}px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))">
<div class="abs ar" style="right:48px;top:{o+(150 if story else 120)}px;width:{520 if story else 500}px">
 <div class="en" style="font-weight:700;font-size:{18 if story else 16}px;letter-spacing:5px;color:{SAND}">CAMPING SEASON</div>
 <div style="font-weight:900;font-size:{86 if story else 76}px;line-height:1.05;margin-top:6px">موسم البر<br><span style="color:{SAND}">بدأ 🏕️</span></div>
</div>
<div class="abs ar" style="right:48px;top:{o+(470 if story else 380)}px;width:{470 if story else 450}px">
 <div style="font-weight:700;font-size:{29 if story else 26}px;line-height:1.45;opacity:.85">للكشتة والدبّاب والطلعات..<br>يحميك من الشمس والغبار والهوا</div>
 <div class="use"><span>وجه</span><span>رقبة</span><span>باندانا</span></div>
 <div class="facts">خفيف 45 غرام · يتنفّس · يناسب النظارة</div>
</div>
<div class="abs" style="left:0;right:0;top:{o+(1010 if story else 800)}px;height:{mini+60}px">{row}</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(1180 if story else 960)}px;font-weight:800;font-size:{30 if story else 27}px">23 لون <span style="opacity:.6">.. اختار لون شلتك</span></div>'''
    extra = f'''.mm{{top:0;filter:drop-shadow(0 12px 14px rgba(0,0,0,.5))}}
.use{{display:flex;gap:10px;margin-top:22px;justify-content:flex-start;direction:rtl}}
.use span{{font-weight:800;font-size:{24 if story else 22}px;border:2px solid {SAND};color:{SAND};border-radius:30px;padding:2px 20px 5px}}
.facts{{margin-top:18px;font-weight:700;font-size:{22 if story else 20}px;opacity:.7}}
.pill{{background:{SAND};border-color:{SAND}!important;color:#2A1D16}}'''
    return page(H, 'linear-gradient(180deg,#15141C 0%,#1F1A20 45%,#3A2620 100%)', INK, body, story, LW,
                '974 GUARDS · FACE MASK', 39, 'علّق <em>«ماسك»</em> ونرسل لك الرابط 📩', extra, pf_ink=INK)

if __name__ == '__main__':
    os.chdir(D)
    shot('974-mask-season-post', mask(), 1350); shot('974-mask-season-story', mask(True), 1920)
