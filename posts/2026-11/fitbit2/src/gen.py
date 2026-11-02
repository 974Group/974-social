C=[('black','BLACK','#1D1D1F','#fff'),('white','WHITE','#FFFFFF','#1D1D1F'),('orange','ORANGE','#F47B2A','#fff'),
   ('pink','PINK','#F4AFC0','#5A1F2E'),('red','RED','#D9262E','#fff'),('yellow','YELLOW','#F4CC1C','#3A2E00'),
   ('grey','GREY','#9FB2CF','#fff'),('beige','BEIGE','#E9E0CF','#4A3D2A'),('purple','PURPLE','#C89CEB','#fff')]
def chips(w,h,photo,gap,x0,y0):
    out=[]
    for i,(f,n,bg,fg) in enumerate(C):
        x=x0+(i%3)*(w+gap); y=y0+(i//3)*(h+gap)
        out.append(f'''<div class="chip" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{f}.jpg" style="height:{photo}px"><div class="strip" style="background:{bg};color:{fg};height:{h-photo}px"><b>{n}</b><span>974·{i+1:02d}</span></div></div>''')
    return '\n'.join(out)
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500 600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700 900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#777;display:flex;gap:40px;padding:40px;align-items:flex-start;width:2400px}}
.ab{{position:relative;overflow:hidden;flex:none;background:#F2EEE9}}
.en{{font-family:Poppins;direction:ltr;unicode-bidi:isolate}}
.ar{{font-family:Cairo;direction:rtl}}
.chip{{position:absolute;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 14px 30px rgba(40,30,20,.12),0 2px 6px rgba(40,30,20,.08);display:flex;flex-direction:column;align-items:center}}
.chip img{{display:block}}
.strip{{width:100%;display:flex;justify-content:space-between;align-items:center;padding:0 18px;margin-top:auto}}
.strip b{{font:700 22px Poppins;letter-spacing:.12em}}
.strip span{{font:600 15px Poppins;letter-spacing:.1em;opacity:.75}}
.logo{{position:absolute;width:110px}}
.kick{{position:absolute;font:600 19px Poppins;letter-spacing:.32em;color:#720842}}
.h{{position:absolute;right:70px;font:900 Cairo;color:#1D1D1F}}
.sub{{position:absolute;right:70px;font:600 Cairo;color:#5B5450}}
.pill{{position:absolute;display:flex;align-items:baseline;gap:10px;background:#720842;color:#fff;border-radius:999px;padding:8px 34px 12px}}
.pill b{{font:800 54px Poppins;line-height:1}}.pill span{{font:800 26px Cairo}}
.url{{position:absolute;font:600 22px Poppins;letter-spacing:.14em;color:#5B5450}}
</style></head><body>
<div class="ab" id="p" style="width:1080px;height:1350px">
  <img class="logo" src="logo-black.png" style="left:70px;top:62px">
  <div class="kick en" style="left:70px;top:168px">FITBIT 2.0 · SILICONE</div>
  <div class="h ar" style="top:28px;font-size:70px;font-weight:900">9 ألوان.. اختار لونك</div>
  <div class="sub ar" style="top:160px;font-size:27px;font-weight:600">سيور سيليكون <span class="en">Fitbit 2.0</span> · ناعمة وخفيفة</div>
  {chips(300,300,236,20,70,225)}
  <div class="url en" style="left:70px;top:1268px">974GROUP.NET</div>
  <div class="pill" style="right:70px;top:1248px"><b class="en">79</b><span>ر.ق</span></div>
</div>
<div class="ab" id="s" style="width:1080px;height:1920px">
  <img class="logo" src="logo-black.png" style="left:70px;top:200px">
  <div class="kick en" style="left:70px;top:290px">FITBIT 2.0 · SILICONE</div>
  <div class="h ar" style="top:330px;font-size:92px;font-weight:900">9 ألوان..</div>
  <div class="h ar" style="top:440px;font-size:92px;font-weight:900;color:#720842">اختار لونك</div>
  <div class="sub ar" style="top:575px;font-size:32px;font-weight:600">سيور سيليكون <span class="en">Fitbit 2.0</span> · ناعمة وخفيفة</div>
  {chips(300,340,270,20,70,660)}
  <div class="pill" style="right:70px;top:1750px"><b class="en">79</b><span>ر.ق</span></div>
  <div class="url en" style="left:70px;top:1772px">974GROUP.NET</div>
</div>
</body></html>'''
open('d.html','w').write(html)
