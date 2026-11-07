import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
C=os.path.abspath('cut')+'/'
LW='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-white.png'
LB='/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
PRICE=None   # set when the owner gives the price, e.g. '99'
FONTS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:'Poppins';font-weight:900;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Black.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr}} .ar{{direction:rtl}}'''
def page(W,H,bg,ink,body,story=False,logo=LW,extra=''):
    pf_b=240 if story else 140; ft_b=124 if story else 38
    price = f'<b class="en">{PRICE}</b> ر.ق' if PRICE else 'XL'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{width:{W}px;height:{H}px;background:{bg};color:{ink};font-family:Cairo;position:relative;overflow:hidden}}
.pf{{position:absolute;left:28px;right:28px;bottom:{pf_b}px}}
{payfoot.css(1.0 if not story else 1.12, text=ink, label=ink)}
.foot{{position:absolute;left:48px;right:48px;bottom:{ft_b}px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.pill{{border:2px solid {ink};border-radius:40px;padding:4px 26px 8px;font-weight:900;font-size:30px;white-space:nowrap}}
.cta{{font-weight:700;font-size:25px}} .cta em{{font-style:normal;text-decoration:underline;text-underline-offset:6px}}
{extra}</style></head><body>
<img class="abs" src="file://{logo}" style="left:48px;top:{198 if story else 48}px;height:44px">
<div class="abs en" style="right:48px;top:{206 if story else 56}px;font-weight:700;font-size:17px;letter-spacing:5px">DESIGNY STUDIOS × 974</div>
{body}
<div class="pf">{payfoot.html()}</div>
<div class="foot"><div class="cta">علّق <em>«تيشيرت»</em> ونرسل لك الرابط 📩</div><div class="pill">{price}</div></div>
</body></html>'''
def img(name,css): return f'<img class="abs" src="file://{C}{name}.png" style="{css}">'

def cover(story=False):
    o=150 if story else 0
    top=o+(400 if story else 330); rh=(420 if story else 340); gap=(70 if story else 50)
    items=[('navy-back','SUMMER BREEZE','Navy'),('blue-back','SUMMER BREEZE','Sky Blue'),('white-back','FALLING WITH GRACE','White'),('beige-back','CITRAZ VIBES','Beige')]
    cells=''
    for i,(n,a,c) in enumerate(items):
        x=i%2; y=i//2
        cells+=f'''<div class="abs" style="left:{40+x*510}px;width:490px;top:{top+y*(rh+gap)}px;height:{rh}px;display:flex;justify-content:center;align-items:flex-end"><img src="file://{C}{n}.png" style="max-width:100%;max-height:100%"></div>
<div class="abs en" style="left:{40+x*510}px;width:490px;top:{top+y*(rh+gap)+rh+8}px;text-align:center;font-weight:700;font-size:16px;letter-spacing:2px">{a} <span style="font-weight:500;opacity:.6;letter-spacing:0">· {c}</span></div>'''
    body=f'''
<div class="abs en" style="left:40px;right:40px;top:{o+120}px;font-weight:900;font-size:150px;line-height:.9;letter-spacing:-4px">T-SHIRTS</div>
<div class="abs ar" style="right:48px;top:{o+(270 if story else 262)}px;font-weight:900;font-size:40px">وصلت تيشيرتات 974 ✦ 4 تصاميم</div>
{cells}'''
    if story: body+=f'<div class="abs ar" style="right:48px;left:48px;top:{top+2*(rh+gap)+20}px;text-align:center;font-weight:700;font-size:30px;opacity:.85">قصّة أوفرسايز · طباعة على الظهر</div>'
    return page(1080,1920 if story else 1350,'#ECE8E1','#1D1B1A',body,story,logo=LB)

def design(key,story=False):
    D={
     'summer':dict(bg='linear-gradient(180deg,#1A2547 0%,#141C38 100%)',ink='#FFFFFF',logo=LW,title='SUMMER',script='Breeze',
          ar='رسمة مبنى كلاسيكي على الظهر.. وتوقيع Designy على الصدر',
          shirts=[('navy-back','Navy'),('blue-back','Sky Blue')],colors='Navy · Sky Blue'),
     'falling':dict(bg='linear-gradient(180deg,#EAF4FB 0%,#D6E9F6 100%)',ink='#1B5FA8',logo=LB,title='FALLING',script='with Grace',
          ar='رسمة كوميك ملونة على الظهر بين الغيوم',
          shirts=[('white-back','White')],colors='White'),
     'citraz':dict(bg='linear-gradient(180deg,#E9E0CC 0%,#DED2B8 100%)',ink='#1F4D33',logo=LB,title='CITRAZ',script='Vibes',
          ar='ليمونة بستايل فنتج على الظهر.. وشعار CITRAZ على الصدر',
          shirts=[('beige-back','Beige'),('beige-front','')],colors='Beige'),
    }[key]
    o=150 if story else 0
    if key=='summer':
        sh=img('navy-back',f'left:30px;top:{o+(470 if story else 400)}px;width:520px')+img('blue-back',f'right:30px;top:{o+(470 if story else 400)}px;width:520px')
    elif key=='citraz':
        sh=img('beige-back',f'left:20px;top:{o+(450 if story else 380)}px;width:640px')+img('beige-front',f'right:30px;top:{o+(620 if story else 530)}px;width:360px')
    else:
        sh=img('white-back',f'left:50%;transform:translateX(-50%);top:{o+(440 if story else 370)}px;width:{720 if story else 640}px')
    extra=".scr{font-family:'Cairo';font-style:italic;font-weight:600}"
    body=f'''
<div class="abs en" style="left:44px;top:{o+120}px;font-weight:900;font-size:120px;line-height:.9;letter-spacing:-3px">{D['title']}</div>
<div class="abs en" style="left:50px;top:{o+232}px;font-weight:500;font-size:44px;font-style:italic;letter-spacing:1px;opacity:.9">{D['script']}</div>
<div class="abs ar" style="right:48px;width:470px;top:{o+150}px;text-align:right;font-weight:700;font-size:25px;line-height:1.5">{D['ar']}</div>
<div class="abs en" style="right:48px;top:{o+262}px;font-weight:700;font-size:18px;letter-spacing:3px;opacity:.75">{D['colors'].upper()} · XL</div>
{sh}'''
    return page(1080,1920 if story else 1350,D['bg'],D['ink'],body,story,logo=D['logo'],extra=extra)

def teaser_story():
    body=f'''
<div class="abs en" style="left:0;right:0;top:620px;text-align:center;font-weight:900;font-size:190px;line-height:.9;letter-spacing:-5px;color:#ECE8E1">NEW<br>DROP</div>
<div class="abs" style="left:0;right:0;top:1060px;height:300px;overflow:hidden;filter:blur(14px);opacity:.85;display:flex;justify-content:center;gap:10px">
{''.join(f'<img src="file://{C}{n}.png" style="height:420px">' for n in ['navy-back','blue-back','white-back','beige-back'])}</div>
<div class="abs ar" style="left:0;right:0;top:1400px;text-align:center;font-weight:900;font-size:48px;color:#ECE8E1">شي جديد ينزل في 974.. خمّن شنو؟ 👀</div>'''
    return page(1080,1920,'#151515','#ECE8E1',body,True,logo=LW)

def shot(n,html,H):
    os.makedirs('out',exist_ok=True)
    open(f'out/{n}.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await pg.goto('file://'+process.cwd()+'/out/{n}.html');await pg.waitForTimeout(800);await pg.screenshot({{path:'out/{n}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
if __name__=='__main__':
    shot('974-tshirts-1-cover',cover(),1350)
    shot('974-tshirts-2-summer',design('summer'),1350)
    shot('974-tshirts-3-falling',design('falling'),1350)
    shot('974-tshirts-4-citraz',design('citraz'),1350)
    shot('974-tshirts-story-cover',cover(True),1920)
    shot('974-tshirts-story-teaser',teaser_story(),1920)
