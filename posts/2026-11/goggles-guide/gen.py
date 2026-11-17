# 974 Guards goggles guide carousel (17 Nov 2026): «عندك دراجة في العزبة؟» + every goggle type we stock
import sys; sys.path.insert(0, '/home/claude/974-social/templates')
from guide import *
R = '/home/claude/974-social/'; D = R + 'posts/2026-11/goggles-guide/'
G = R + 'products/goggles/'; GC = R + 'posts/2026-11/goggles-26-27/src/cut/'; SG = R + 'posts/2026-11/summer-goggles/cut/'; C = D + 'cut/'
TAG = '974 GUARDS · GOGGLES'
S = {
 'photo': dict(ar='الفوتوكروميك', en='PHOTOCHROMIC EDITION', head='نظارة وحدة للنهار والليل', chips=['نهار', 'ليل', 'غبار', 'بر'],
   line='عدسة ذكية تغمق بروحها في الشمس وترجع شفافة بالليل', price=349,
   bands=[(C+'photochromic.png','Photochromic')], h=330, top=500, chips_top=900,
   bg='radial-gradient(110% 70% at 50% 40%,#2A2C30 0%,#17181B 60%,#0E0F11 100%)', ink='#FFFFFF', acc='#C9CED6'),
 'editions': dict(ar='الإيديشن', en='EDITIONS · 2 LENSES', head='عدستين.. للشمس والليل', chips=['شمس', 'ليل', 'دراجة', 'بقي'],
   line='عدسة شمس + عدسة شفافة بالمغناطيس تبدلها بثانية.. وضد الضباب', price=299, frm=True,
   rows=[('319 QAR', [(G+'red-edition-render.png','Red'),(G+'green-edition-render.png','Green'),(G+'maroon-edition-render.png','Maroon'),(G+'uae-edition-render.png','UAE')]),
         ('319 · BLACK 299 QAR', [(G+'iceblue-edition-render.png','Ice blue'),(GC+'br1.png','Brown'),(G+'black-edition-render.png','Black')])],
   bg='linear-gradient(180deg,#FFE7C4 0%,#F8CC96 55%,#EDB07A 100%)', ink='#3A1E0E', acc='#B5471B'),
 'twoin1': dict(ar='الخفيفة', en='2 IN 1', head='خفيفة.. لكل طلعة', chips=['بحر', 'بقي', 'طلعات', 'بر'],
   line='خفيفة ومعها عدستين: عدسة شمس وعدسة شفافة', price=209, frm=True,
   rows=[('YELLOW & PINK 209 QAR', [(SG+'yellow.png','Yellow'),(SG+'pink.png','Pink'),(SG+'red.png','Red')]),
         ('249 QAR', [(SG+'black.png','Black'),(SG+'grey.png','Grey'),(SG+'blue.png','Blue')])],
   bg='linear-gradient(170deg,#FFF3E2 0%,#FFD9B0 100%)', ink='#3B2412', acc='#E0661E'),
 'mx': dict(ar='MX كلير', en='MX CLEAR', head='للموتوكروس والليل', chips=['موتو', 'ليل', 'غبار', 'تدريب'],
   line='عدسة شفافة ضد الضباب والخدوش + UV400.. وإطار مرن', price=109,
   bands=[(C+'mx-black.png','Black'),(C+'mx-white.png','White'),(C+'mx-grey.png','Grey')], h=260, top=520, chips_top=860,
   bg='linear-gradient(170deg,#F1F2F4 0%,#D9DCE1 100%)', ink='#15181D', acc='#3A4250'),
}
ORDER = ['photo', 'editions', 'twoin1', 'mx']; N = len(ORDER) + 2
if __name__ == '__main__':
    picks = [(C+'photochromic.png','Photochromic'),(G+'green-edition-render.png','Editions'),(SG+'red.png','2 in 1'),(C+'mx-black.png','MX Clear')]
    sl = [('01-hook', lambda: hook(N, 'عندك دراجة<br><span style="color:#C9A24B">فالعنه؟</span>', 'نظارتك لازم تكون جاهزة للشمس والغبار والليل', picks, TAG, 109))]
    sl += [(f'{i+2:02d}-{k}', (lambda k=k, i=i: slide(S[k], i+2, N, TAG))) for i, k in enumerate(ORDER)]
    sl += [(f'{N:02d}-cta', lambda: cta(N, [(S[k]['ar'], S[k]['head']) for k in ORDER], TAG, 109, 'وعندنا ستراب إضافي بـ 99 ر.ق لنظارات 974 Guards', what='نظارة'))]
    build(sl, D)
