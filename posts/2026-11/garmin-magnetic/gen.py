# Garmin CIRQA magnetic silicone (live 11 Nov, 100/colour, 99 QAR). Light, no boxes: 10 colours on two staggered rows, lime accent from the band.
import sys
sys.path.insert(0, '/home/claude/974-social/posts/2026-11/best-sellers-3')
from gen import page, shot, LB
C = '/home/claude/974-social/posts/2026-11/garmin-magnetic/cut/'
INK = '#1E1F22'; LIME = '#C9DA2A'
COLS = [('black', 'Black'), ('white', 'White'), ('starlight', 'Starlight'), ('grey', 'Grey'), ('dark-blue', 'Dark Blue'),
        ('wine-red', 'Wine Red'), ('pink', 'Pink'), ('orange', 'Orange'), ('lime', 'Lime'), ('army-green', 'Army Green')]

def g(story=False):
    o = 150 if story else 0; H = 1920 if story else 1350
    bh = 236 if story else 212
    r1 = o + (500 if story else 380); r2 = r1 + bh + (170 if story else 104)
    step = 984 / 5
    bands = ''
    for i, (f, n) in enumerate(COLS):
        row = i // 5; col = i % 5
        cx = 48 + step * (4 - col) + step / 2  # RTL: first colour on the right
        top = (r1 if row == 0 else r2) + (0 if (col + row) % 2 == 0 else 34)
        bands += f'<div class="b" style="left:{cx-100:.0f}px;top:{top}px"><img src="file://{C}{f}.png" style="height:{bh}px"><i>{n}</i></div>'
    body = f'''
<div class="abs en" style="left:-14px;top:{r1+bh+(20 if story else 0)}px;font-weight:700;font-size:{205 if story else 190}px;line-height:.84;letter-spacing:-8px;color:rgba(30,31,34,.045);white-space:nowrap">MAGNETIC</div>
<div class="abs ar" style="right:48px;left:48px;top:{o+(118 if story else 108)}px">
 <div style="font-weight:900;font-size:{84 if story else 74}px;line-height:1.1">بدون قفل..<br><span class="mk">يتسكّر بالمغناطيس</span></div>
 <div style="font-weight:700;font-size:{29 if story else 26}px;margin-top:14px;opacity:.78">سير سيليكون لـ <span class="en">Garmin CIRQA</span> · ينضبط على أي معصم بثانية</div>
</div>
{bands}
<div class="abs ar" style="right:48px;left:48px;top:{r2 + bh + (130 if story else 74)}px;display:flex;justify-content:space-between;align-items:center">
 <div style="font-weight:800;font-size:{30 if story else 27}px">10 ألوان.. <span style="opacity:.65">اختار لونك</span></div>
 <div class="bo" style="margin:0">سير فقط · بدون الجهاز</div>
</div>'''
    extra = f'''.b{{position:absolute;width:200px;display:flex;flex-direction:column;align-items:center}}
.b img{{filter:drop-shadow(0 16px 18px rgba(30,31,34,.22))}}
.b i{{font-style:normal;font-family:Poppins;font-weight:700;font-size:{15 if story else 14}px;letter-spacing:1.5px;margin-top:10px;opacity:.62;text-transform:uppercase;white-space:nowrap}}
.mk{{background:linear-gradient(transparent 62%,{LIME} 62%,{LIME} 92%,transparent 92%);padding:0 6px}}
.pill{{background:{INK};color:{LIME};border:none!important}}'''
    cta = 'اطلبه من <em>974group.net</em> 🛒' if story else 'علّق <em>«قارمن»</em> ونرسل لك الرابط 📩'
    return page(H, 'radial-gradient(80% 55% at 50% 50%,#FBFAF7 0%,#F1EFEA 60%,#E7E4DE 100%)', INK, body, story, LB,
                'GARMIN CIRQA · MAGNETIC', 99, cta, extra)

if __name__ == '__main__':
    shot('974-garmin-magnetic-post', g(), 1350)
    shot('974-garmin-magnetic-story', g(True), 1920)
