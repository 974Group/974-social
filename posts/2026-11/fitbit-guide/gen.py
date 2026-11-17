# Google Fitbit Air band guide carousel (17 Nov 2026, for 18 Nov)
import sys; sys.path.insert(0, '/home/claude/974-social/templates')
from guide import *
R = '/home/claude/974-social/products/'; D = '/home/claude/974-social/posts/2026-11/fitbit-guide/'
V1 = R + 'fitbit-silicone-v1/uni/'; C = D + 'cut/'; FF = R + 'fitbit-fabric-blush/src/'; MG = R + 'fitbit-air-magnetic/'
TAG = 'GOOGLE FITBIT AIR'
S = {
 'silicone': dict(ar='السيليكون', en='SILICONE · 1.0 & 2.0', head='للاستخدام اليومي', chips=['يومي', 'رياضة', 'سباحة', 'شاور'],
   line='ما يتأثر بالعرق ولا الماي.. و2.0 أنعم وأخف', price=69, frm=True,
   rows=[('SILICONE 1.0 · 69 QAR', [(V1+'orange.png','Orange'),(V1+'tiffany.png','Tiffany'),(V1+'maroon.png','Maroon'),(V1+'white.png','White'),(V1+'navy.png','Navy')]),
         ('SILICONE 2.0 · 79 QAR', [(C+'sil2-black.png','Black'),(C+'sil2-pink.png','Pink'),(C+'sil2-yellow.png','Yellow'),(C+'sil2-beige.png','Beige'),(C+'sil2-purple.png','Purple')])],
   bg='linear-gradient(170deg,#ECF8F6 0%,#D3EEEA 100%)', ink='#123A36', acc='#1E8C80'),
 'fabric': dict(ar='الفابريك', en='FABRIC', head='للكاجوال ووقت النوم', chips=['كاجوال', 'دوام', 'مشي', 'نوم'],
   line='خفيف ويتنفس.. يتسكر باللزقة وتعدله على مقاسك', price=74, frm=True,
   bands=[(FF+'black-crop.png','Black'),(FF+'fog-crop.png','Fog'),(FF+'pinky-red-crop.png','Pinky red'),(FF+'olive-crop.png','Olive'),(FF+'purple-crop.png','Purple')],
   bg='linear-gradient(170deg,#FFF6EF 0%,#F6D9CB 100%)', ink='#3B2320', acc='#C2563A'),
 'magnetic': dict(ar='المغناطيس', en='MAGNETIC WOVEN', head='للدوام والكاجوال', chips=['يومي', 'دوام', 'كاجوال', 'مشاوير'],
   line='منسوج ومطاطي.. يتسكر بالمغناطيس بثانية', price=89,
   bands=[(MG+'black-cut.png','Black'),(MG+'dark-blue-cut.png','Dark blue'),(MG+'wine-red-cut.png','Wine red'),(MG+'green-cut.png','Green'),(MG+'starlight-cut.png','Starlight')],
   bg='radial-gradient(110% 70% at 50% 40%,#2A2C30 0%,#17181B 60%,#0E0F11 100%)', ink='#FFFFFF', acc='#D7E64A'),
 'leather': dict(ar='الجلد', en='LEATHER', head='للمناسبات والدوام', chips=['مناسبات', 'دوام', 'مع الثوب', 'مع البدلة'],
   line='جلد ناعم بقطع معدنية فضية.. بالأسود والبني', price=99,
   bands=[(C+'leather-black.png','Black')], h=420, top=440, chips_top=940,
   bg='linear-gradient(170deg,#F4EDE6 0%,#E4D5C6 100%)', ink='#2B1D14', acc='#8A5A3B'),
}
ORDER = ['silicone', 'fabric', 'magnetic', 'leather']; N = len(ORDER) + 2
if __name__ == '__main__':
    picks = [(C+'sil2-pink.png','Silicone'),(FF+'olive-crop.png','Fabric'),(MG+'wine-red-cut.png','Magnetic'),(C+'leather-black.png','Leather')]
    sl = [('01-hook', lambda: hook(N, 'عندك <span class="en" style="font-weight:700">Fitbit Air</span>؟', 'كل سير له استخدامه.. اختار اللي يناسب يومك', picks, TAG, 69))]
    sl += [(f'{i+2:02d}-{k}', (lambda k=k, i=i: slide(S[k], i+2, N, TAG))) for i, k in enumerate(ORDER)]
    sl += [(f'{N:02d}-cta', lambda: cta(N, [(S[k]['ar'], S[k]['head']) for k in ORDER], TAG, 69, 'كل السيور تركب على <span class="en">Google Fitbit Air</span>'))]
    build(sl, D)
