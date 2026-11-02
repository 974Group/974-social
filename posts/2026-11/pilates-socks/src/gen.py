N={'orange':'Orange','tennis':'Court Club','lemonade':'Lemonade','cherrystripe':'Cherry Stripe','peach':'Peach',
   'juice':'Juice Bar','pinkbow':'Pink Bow','coffee':'Pilates & Coffee','strawpink':'Strawberry Milk','strawred':'Strawberry',
   'cherrybow':'Cherry Bow','redbow':'Red Bow'}
ORDER=['cherrybow','redbow','pinkbow','strawred','strawpink','cherrystripe','peach','orange','juice','lemonade','coffee','tennis']
def sock(k,x,y,h,extra=''):
    return f'<img class="sk" src="{k}.png" style="left:{x}px;top:{y}px;height:{h}px;{extra}">'
def name(k,cx,y,size=22):
    return f'<div class="nm en" style="left:{cx-160}px;top:{y}px;font-size:{size}px">{N[k]}</div>'
def grid(keys,cols,x0,y0,cw,ch,h,ny,size=20):
    o=''
    for i,k in enumerate(keys):
        cx=x0+(i%cols)*cw+cw//2; y=y0+(i//cols)*ch
        o+=f'<img class="sk" src="{k}.png" style="left:{cx}px;top:{y}px;height:{h}px;transform:translateX(-50%)">'+name(k,cx,y+ny,size)
    return o
CSS='''
@font-face{font-family:'Cairo';font-weight:400 900;src:url(../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}
@font-face{font-family:'Cairo';font-weight:400 900;src:url(../aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}
@font-face{font-family:'Poppins';font-weight:400;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf)}
@font-face{font-family:'Poppins';font-weight:500 600;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}
@font-face{font-family:'Poppins';font-weight:700 900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}
@font-face{font-family:'Lora';font-style:italic;font-weight:400 700;src:url(file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf)}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#777;display:flex;flex-wrap:wrap;gap:40px;padding:40px;width:4600px;align-items:flex-start}
.ab{position:relative;overflow:hidden;flex:none;background:#F7EFEA;color:#2A1418}
.P{width:1080px;height:1350px}.S{width:1080px;height:1920px}
.en{font-family:Poppins;direction:ltr;unicode-bidi:isolate}
.ar{font-family:Cairo;direction:rtl}
.abs{position:absolute}
.lora{font-family:Lora;font-style:italic;font-weight:600;direction:ltr;unicode-bidi:isolate}
.sk{position:absolute;filter:drop-shadow(0 22px 22px rgba(90,30,40,.16))}
.nm{position:absolute;width:320px;text-align:center;font-weight:600;letter-spacing:.06em;color:#2A1418}
.kick{position:absolute;font:600 20px Poppins;letter-spacing:.38em;color:#C3203A}
.logo{position:absolute;width:110px}
.cta{position:absolute;left:0;right:0;text-align:center;font:700 30px Cairo;direction:rtl;color:#2A1418}
.chip{display:inline-block;background:#C3203A;color:#fff;border-radius:999px;padding:4px 26px 8px;font:800 30px Cairo}
.dots{position:absolute;inset:0;background-image:radial-gradient(#E9C9CF 2.2px,transparent 2.6px);background-size:46px 46px;opacity:.55}
.callout{position:absolute;direction:rtl;font-family:Cairo}
.callout b{display:block;font:800 34px Cairo;color:#2A1418}
.callout span{display:block;font:500 24px Cairo;color:#6E5458;line-height:1.35}
.callout i{position:absolute;width:16px;height:16px;border-radius:50%;background:#C3203A;box-shadow:0 0 0 6px rgba(195,32,58,.18)}
.line{position:absolute;height:2px;background:#C3203A;opacity:.5;transform-origin:left center}
'''
A=[]
# ---------- T1 teaser post
A.append(('teaser-post','P',f'''
<img src="close_cherry.jpg" class="abs" style="left:0;top:0;width:1080px;height:1080px;object-fit:cover">
<div class="abs" style="left:0;right:0;top:880px;height:200px;background:linear-gradient(rgba(247,239,234,0),#F7EFEA)"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="abs lora" style="left:0;right:0;top:1010px;text-align:center;font-size:96px;color:#C3203A">Pilates Club</div>
<div class="abs ar" style="left:0;right:0;top:1140px;text-align:center;font:800 46px Cairo">قريب.. هالأسبوع 🎀</div>
<div class="abs en" style="left:0;right:0;top:1222px;text-align:center;font:600 20px Poppins;letter-spacing:.4em;color:#8A6E72">COMING SOON · 974GROUP.NET</div>
'''))
# ---------- T2 teaser story
A.append(('teaser-story','S',f'''
<img src="close_cherry.jpg" class="abs" style="left:0;top:0;width:1080px;height:1300px;object-fit:cover">
<div class="abs" style="left:0;right:0;top:1060px;height:240px;background:linear-gradient(rgba(247,239,234,0),#F7EFEA)"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:200px">
<div class="abs lora" style="left:0;right:0;top:1250px;text-align:center;font-size:120px;color:#C3203A">Pilates Club</div>
<div class="abs ar" style="left:0;right:0;top:1420px;text-align:center;font:800 58px Cairo">شي ناعم جاي لتمرينك..</div>
<div class="abs ar" style="left:0;right:0;top:1510px;text-align:center;font:600 36px Cairo;color:#6E5458">دلاغات بيلاتيس من 974 · هالأسبوع</div>
<div class="abs en" style="left:0;right:0;top:1640px;text-align:center;font:600 22px Poppins;letter-spacing:.4em;color:#8A6E72">COMING SOON</div>
'''))
# ---------- L1 launch hero post
L1=sock('cherrybow',45,520,540)+sock('strawpink',385,560,540)+sock('redbow',745,520,540)
A.append(('launch-post','P',f'''<div class="dots"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:60px">
<div class="kick en" style="right:64px;top:80px">NEW COLLECTION</div>
<div class="abs lora" style="left:0;right:0;top:150px;text-align:center;font-size:150px;line-height:1;color:#C3203A">Pilates Club</div>
<div class="abs ar" style="left:0;right:0;top:330px;text-align:center;font:900 60px Cairo">دلاغات البيلاتيس وصلت 🎀</div>
<div class="abs ar" style="left:0;right:0;top:430px;text-align:center;font:600 30px Cairo;color:#6E5458">ثبات بكل حركة.. وستايل بكل تفصيلة · <span class="en">12</span> تصميم</div>
{L1}
<div class="cta" style="top:1140px">اسحب وشوف كل التصاميم 👈</div>
<div class="abs en" style="left:0;right:0;top:1250px;text-align:center;font:600 20px Poppins;letter-spacing:.36em;color:#8A6E72">974GROUP.NET</div>
'''))
# ---------- L2 grid post
A.append(('collection-post','P',f'''
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="abs lora" style="right:64px;top:50px;font-size:64px;color:#C3203A">Pilates Club</div>
<div class="abs ar" style="right:64px;top:140px;font:800 32px Cairo">12 تصميم.. اختاري ستايلك</div>
{grid(ORDER,4,30,215,255,370,300,300,19)}
'''))
# ---------- L3 specs post
A.append(('specs-post','P',f'''<div class="dots" style="opacity:.3"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="kick en" style="right:64px;top:76px">THE DETAILS</div>
<div class="abs ar" style="right:64px;top:118px;font:900 58px Cairo">ليش دلاغات <span class="lora" style="color:#C3203A;font-size:62px">Pilates Club</span>؟</div>
{sock('strawred',30,300,820)}
<div class="callout" style="right:64px;top:300px;width:470px"><b>حافة مكشكشة 🎀</b><span>تفصيلة ناعمة ما تضغط على الرجل</span></div>
<div class="callout" style="right:64px;top:440px;width:470px"><b>تطريز فخم</b><span>رسمة مطرّزة مب مطبوعة.. تعيش معاك</span></div>
<div class="callout" style="right:64px;top:580px;width:470px"><b>قماش مضلّع ومريح</b><span>85% قطن · 10% نايلون · 5% سباندكس</span></div>
<div class="callout" style="right:64px;top:740px;width:470px"><b>نعل مانع للانزلاق</b><span>حبيبات سيليكون تثبّتك على الريفورمر والمات</span></div>
<img src="close_sole.jpg" class="abs" style="right:64px;top:900px;width:300px;height:300px;border-radius:50%;object-fit:cover;border:6px solid #fff;box-shadow:0 14px 30px rgba(90,30,40,.18)">
<div class="callout" style="right:390px;top:960px;width:260px"><b style="font-size:30px">مقاس واحد</b><span>يناسب أغلب المقاسات (Free Size)</span></div>
<div class="abs en" style="left:64px;top:1268px;font:600 18px Poppins;letter-spacing:.3em;color:#8A6E72">974GROUP.NET</div>
'''))
# ---------- L4 packaging post
A.append(('packaging-post','P',f'''
<img src="pack_c.jpg" class="abs" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover;filter:saturate(1.03)">
<div class="abs" style="left:0;right:0;bottom:0;height:420px;background:linear-gradient(rgba(42,20,24,0),rgba(42,20,24,.86) 55%)"></div>
<img class="logo" src="logo-white.png" style="left:64px;top:56px">
<div class="abs ar" style="right:64px;top:1030px;font:900 64px Cairo;color:#fff">جاهزة.. حتى للهدية 🎁</div>
<div class="abs ar" style="right:64px;top:1130px;font:600 32px Cairo;color:#F2DADF">كل جوز مغلّف بباكجنق 974 وبنافذة تشوف منها التطريز</div>
<div class="abs en" style="right:64px;top:1220px;font:600 20px Poppins;letter-spacing:.36em;color:#F2DADF">PILATES CLUB · 974GROUP.NET</div>
'''))
# ---------- Edits
def edit(slug,title,ar,keys,h,bg='#F7EFEA'):
    n=len(keys); cols=3
    cw=(1080-80)//cols; rows=(n+cols-1)//cols
    ch=(1350-330-60)//rows
    hh=min(h,ch-60)
    return (slug,'P',f'''<div class="dots" style="opacity:.35"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="abs lora" style="right:64px;top:46px;font-size:70px;color:#C3203A">{title}</div>
<div class="abs ar" style="right:64px;top:150px;font:800 34px Cairo">{ar}</div>
{grid(keys,cols,40,290,cw,ch,hh,hh+8,20)}
<div class="abs en" style="left:64px;top:1278px;font:600 18px Poppins;letter-spacing:.3em;color:#8A6E72">PILATES CLUB · 974GROUP.NET</div>''')
A.append(edit('fruit-edit','The Fruit Edit','فواكه.. بس للرجول 🍒🍓🍊',['cherrystripe','strawred','strawpink','peach','orange','lemonade'],420))
A.append(edit('bow-edit','The Bow Edit','فيونكة لكل مزاج 🎀',['pinkbow','cherrybow','redbow'],620))
A.append(('coffee-edit','P',f'''
<img src="close_coffee.jpg" class="abs" style="left:0;top:0;width:1080px;height:760px;object-fit:cover">
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="abs lora" style="right:64px;top:790px;font-size:76px;color:#6B3E2A">Pilates & Coffee ☕</div>
<div class="abs ar" style="right:64px;top:900px;font:800 36px Cairo">كلاس الصبح.. وبعدها قهوة وكرواسون 🥐</div>
{sock('coffee',70,960,360)}{sock('tennis',300,960,360)}
<div class="callout" style="right:64px;top:1020px;width:520px"><b style="font-size:30px">Pilates & Coffee · Court Club</b><span>تصميمين للي يحبون الكلاس بنفس حبهم للقهوة</span></div>
<div class="abs en" style="right:64px;top:1268px;font:600 18px Poppins;letter-spacing:.3em;color:#8A6E72">974GROUP.NET</div>
'''))
# ---------- Stories
sh=['cherrybow','pinkbow','strawred','coffee','redbow']
A.append(('launch-story','S',f'''<div class="dots"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:200px">
<div class="kick en" style="right:64px;top:222px">NEW COLLECTION</div>
<div class="abs lora" style="left:0;right:0;top:300px;text-align:center;font-size:170px;line-height:1;color:#C3203A">Pilates<br>Club</div>
<div class="abs ar" style="left:0;right:0;top:680px;text-align:center;font:900 64px Cairo">دلاغات البيلاتيس وصلت 🎀</div>
{sock('cherrybow',70,840,520)}{sock('strawpink',400,900,520)}{sock('redbow',740,840,520)}
<div class="abs ar" style="left:0;right:0;top:1470px;text-align:center;font:700 38px Cairo;color:#6E5458">12 تصميم · نعل مانع للانزلاق · تطريز</div>
<div class="cta" style="top:1580px"><span class="chip">علّقي «بيلاتيس» ونرسل لك الرابط</span></div>
<div class="abs en" style="left:0;right:0;top:1700px;text-align:center;font:600 22px Poppins;letter-spacing:.36em;color:#8A6E72">974GROUP.NET</div>
'''))
A.append(('collection-story','S',f'''
<img class="logo" src="logo-black.png" style="left:64px;top:200px">
<div class="abs lora" style="right:64px;top:190px;font-size:72px;color:#C3203A">Pilates Club</div>
<div class="abs ar" style="right:64px;top:290px;font:800 38px Cairo">12 تصميم.. أي وحدة لك؟</div>
{grid(ORDER,3,40,380,333,355,290,292,20)}
'''))
A.append(('specs-story','S',f'''<div class="dots" style="opacity:.3"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:200px">
<div class="abs ar" style="right:64px;top:300px;font:900 66px Cairo">التفاصيل تفرق ✨</div>
{sock('strawred',50,470,820)}
<div class="callout" style="right:64px;top:480px;width:430px"><b>حافة مكشكشة</b><span>ناعمة وما تضغط</span></div>
<div class="callout" style="right:64px;top:640px;width:430px"><b>تطريز فخم</b><span>رسمة مطرّزة تعيش</span></div>
<div class="callout" style="right:64px;top:800px;width:430px"><b>قطن مريح</b><span>85% قطن · 10% نايلون · 5% سباندكس</span></div>
<div class="callout" style="right:64px;top:990px;width:430px"><b>نعل مانع للانزلاق</b><span>ثبات على الريفورمر والمات</span></div>
<div class="callout" style="right:64px;top:1160px;width:430px"><b>مقاس واحد</b><span>Free Size</span></div>
<img src="close_sole.jpg" class="abs" style="right:64px;top:1300px;width:300px;height:300px;border-radius:50%;object-fit:cover;border:6px solid #fff;box-shadow:0 14px 30px rgba(90,30,40,.18)"><div class="cta" style="top:1700px"><span class="chip">علّقي «بيلاتيس» ونرسل لك الرابط</span></div>
'''))
html='<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>'+''.join(f'<div class="ab {t}" id="{s}">{b}</div>' for s,t,b in A)+'</body></html>'
open('d.html','w').write(html)
open('ids.txt','w').write('\n'.join(s for s,_,_ in A))
