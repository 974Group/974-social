# Garmin CIRQA band guide carousel (17 Nov 2026, for 19 Nov)
import sys; sys.path.insert(0, '/home/claude/974-social/templates')
from guide import *
R = '/home/claude/974-social/products/'; D = '/home/claude/974-social/posts/2026-11/cirqa-guide/'
S1 = R + 'garmin-cirqa-silicone-v1/cut/'; S2 = R + 'garmin-cirqa-silicone-v2/src/'; MG = R + 'garmin-cirqa-magnetic/src/'
F1 = R + 'garmin-cirqa-fabric/cut/'; F3 = R + 'garmin-cirqa-fabric3/cut/'
TAG = 'GARMIN CIRQA'
S = {
 'silicone': dict(ar='السيليكون', en='SILICONE · 1.0 & 2.0', head='للاستخدام اليومي', chips=['يومي', 'رياضة', 'سباحة', 'شاور'],
   line='ما يتأثر بالعرق ولا الماي.. و2.0 مخرّم يتنفس أكثر', price=89, frm=True,
   rows=[('SILICONE 1.0 · 99 QAR', [(S1+'orange.png','Orange'),(S1+'white.png','White'),(S1+'black.png','Black'),(S1+'lemon.png','Lemon'),(S1+'dusty-pink.png','Dusty pink')]),
         ('SILICONE 2.0 · 89 QAR', [(S2+'orange-cut.png','Orange'),(S2+'lime-cut.png','Lime'),(S2+'midnight-blue-cut.png','Midnight'),(S2+'mousse-pink-cut.png','Mousse pink'),(S2+'sea-mist-blue-cut.png','Sea mist')])],
   bg='linear-gradient(170deg,#FFF4EC 0%,#FBDCC6 100%)', ink='#3A1E0E', acc='#D9581E'),
 'magnetic': dict(ar='المغناطيس', en='MAGNETIC', head='للدوام والكاجوال', chips=['يومي', 'دوام', 'كاجوال', 'رياضة'],
   line='يتسكر بالمغناطيس بثانية.. ويثبت وانت تتحرك', price=99,
   bands=[(MG+'black-cut.png','Black'),(MG+'pink-cut.png','Pink'),(MG+'lime-cut.png','Lime'),(MG+'wine-red-cut.png','Wine red'),(MG+'dark-blue-cut.png','Dark blue')],
   bg='radial-gradient(110% 70% at 50% 40%,#2A2C30 0%,#17181B 60%,#0E0F11 100%)', ink='#FFFFFF', acc='#D7E64A'),
 'fabric': dict(ar='الفابريك', en='FABRIC · 1.0 & 3.0', head='للكاجوال ووقت النوم', chips=['كاجوال', 'دوام', 'نوم', 'تمرين'],
   line='خفيف ويتنفس ويتسكر باللزقة.. ومنه نسخة تلبسها على الزند', price=109,
   rows=[('FABRIC 1.0 · WRIST & BICEPS', [(F1+'v1-pink.png','Pink'),(F1+'v1-navy.png','Navy'),(F1+'v1-lime.png','Lime'),(F1+'v1-army-green.png','Army green'),(F1+'v1-blue.png','Blue')]),
         ('FABRIC 3.0 · S/M & L/XL', [(F3+'pink.png','Pink'),(F3+'navy.png','Navy'),(F3+'orange.png','Orange'),(F3+'purple.png','Purple'),(F3+'green.png','Green')])],
   bg='linear-gradient(170deg,#F4EFF7 0%,#E3D8EF 100%)', ink='#2A1F3D', acc='#7B5CC4'),
}
ORDER = ['silicone', 'magnetic', 'fabric']; N = len(ORDER) + 2
if __name__ == '__main__':
    picks = [(S2+'orange-cut.png','Silicone'),(MG+'pink-cut.png','Magnetic'),(F1+'v1-lime.png','Fabric')]
    sl = [('01-hook', lambda: hook(N, 'عندك <span class="en" style="font-weight:700">Garmin CIRQA</span>؟', 'كل سير له استخدامه.. اختار اللي يناسب يومك', picks, TAG, 89, h=250))]
    sl += [(f'{i+2:02d}-{k}', (lambda k=k, i=i: slide(S[k], i+2, N, TAG))) for i, k in enumerate(ORDER)]
    sl += [(f'{N:02d}-cta', lambda: cta(N, [(S[k]['ar'], S[k]['head']) for k in ORDER], TAG, 89, 'كل السيور تركب على <span class="en">Garmin CIRQA</span>'))]
    build(sl, D)
