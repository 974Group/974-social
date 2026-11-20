# Designy "دراجتك فالشارع.. وعلى الهودي" - customer's Polaris Slingshot photo -> printed hoodie mockup.
# Post 1080x1350 + story 1080x1920, Designy identity (blue). Owner 20 Nov 2026.
import subprocess, os
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D=os.path.dirname(os.path.abspath(__file__)); OUT=D+'/out'; os.makedirs(OUT,exist_ok=True)
LOGO='/home/claude/974-social/tshirts/designy/designy-logo-white-hd.png'
PH=D+'/src/photo.jpg'; MK=D+'/src/mockup.jpg'
BLUE='#2560a4'; DEEP='#173f72'; SKY='#01a7e1'; MINT='#edf7f6'
CSS=f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} .abs{{position:absolute}} .en{{font-family:Poppins;direction:ltr;unicode-bidi:isolate}}
body{{width:1080px;background:radial-gradient(120% 80% at 50% 40%,#2d6cb4 0%,{BLUE} 45%,{DEEP} 100%);color:#fff;font-family:Cairo;position:relative;overflow:hidden}}
.card{{border-radius:28px;overflow:hidden;border:5px solid #fff;box-shadow:0 22px 40px rgba(5,20,45,.45);background:#fff}}
.card img{{width:100%;height:100%;object-fit:cover;display:block}}
.tag{{position:absolute;background:{SKY};color:#fff;font-weight:900;font-size:26px;border-radius:30px;padding:2px 20px 6px;white-space:nowrap;box-shadow:0 8px 16px rgba(5,20,45,.3)}}
.st{{display:flex;align-items:center;gap:16px;direction:rtl}}
.st b{{flex:none;width:58px;height:58px;border-radius:50%;background:#fff;color:{BLUE};font-family:Poppins;font-size:28px;display:flex;align-items:center;justify-content:center}}
.st span{{font-weight:800;font-size:31px;line-height:1.25}}
.arrow{{font-family:Poppins;font-weight:700;color:{SKY}}}
'''
HEAD='<div style="font-weight:900;font-size:{fs}px;line-height:1.12;direction:rtl;text-align:right">دراجتك فالشارع..<br><span style="color:{sky}">وعلى الهودي 😉</span></div>'
STEPS='''<div class="st"><b>1</b><span>اختار لون الهودي</span></div>
<div class="st"><b>2</b><span>طرش لنا صورة الدراجة</span></div>
<div class="st"><b>3</b><span>وخل الباقي علينا ✌️</span></div>'''
CTA=f'<div style="display:inline-flex;align-items:center;gap:12px;background:#fff;color:{BLUE};border-radius:44px;padding:8px 34px 12px;font-weight:900;font-size:30px;direction:rtl">للطلب راسلنا على الخاص 📩</div>'

def html(body,h):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{height:{h}px}}</style></head><body>{body}</body></html>'

HC=D+'/src/back-cut.png'
EXTRA='''.hd{filter:drop-shadow(0 30px 40px rgba(5,20,45,.55))}
.ov{position:absolute;left:0;right:0}
.stw .st span{text-shadow:0 2px 10px rgba(0,0,0,.35)}'''
def html2(b,h): return html(b,h).replace('</style>',EXTRA+'</style>')

def post():
    b=f'''
<div class="abs" style="inset:0;background:url(file://{PH}) 50% 35%/cover no-repeat"></div>
<div class="ov" style="top:0;height:560px;background:linear-gradient(180deg,rgba(23,63,114,.88) 0%,rgba(37,96,164,.55) 70%,rgba(37,96,164,0) 100%)"></div>
<div class="ov" style="bottom:0;height:200px;background:linear-gradient(0deg,rgba(23,63,114,.85) 0%,rgba(23,63,114,0) 100%)"></div>
<img class="abs" src="file://{LOGO}" style="left:44px;top:40px;height:58px">
<img class="abs hd" src="file://{HC}" style="left:52px;top:120px;width:300px">
<div class="tag" style="left:230px;top:118px;font-size:22px">على الهودي 🔥</div>
<div class="abs" style="right:48px;top:44px">{HEAD.format(fs=62,sky='#9BDDF7')}</div>
<div class="abs stw" style="right:48px;top:240px;display:flex;flex-direction:column;gap:14px">{STEPS.replace('<b>','<b style="width:46px;height:46px;font-size:22px">').replace('<span>','<span style="font-size:27px">')}</div>
<div class="abs" style="right:40px;top:1245px">{CTA}</div>'''
    return html2(b,1350)

def story():
    b=f'''
<div class="abs" style="inset:0;background:url(file://{PH}) center/cover no-repeat"></div>
<div class="ov" style="top:0;height:800px;background:linear-gradient(180deg,rgba(23,63,114,.9) 0%,rgba(37,96,164,.55) 70%,rgba(37,96,164,0) 100%)"></div>
<div class="ov" style="bottom:0;height:380px;background:linear-gradient(0deg,rgba(23,63,114,.9) 0%,rgba(23,63,114,0) 100%)"></div>
<img class="abs" src="file://{LOGO}" style="left:52px;top:200px;height:66px">
<div class="abs" style="right:52px;top:190px">{HEAD.format(fs=72,sky='#9BDDF7')}</div>
<div class="abs stw" style="right:52px;top:440px;display:flex;flex-direction:column;gap:18px">{STEPS.replace('<b>','<b style="width:50px;height:50px;font-size:24px">').replace('<span>','<span style="font-size:29px">')}</div>
<img class="abs hd" src="file://{HC}" style="left:60px;top:330px;width:315px">
<div class="tag" style="left:250px;top:325px;font-size:22px">على الهودي 🔥</div>
<div class="abs" style="left:0;right:0;top:1660px;text-align:center">{CTA}</div>'''
    return html2(b,1920)

def shot(name,doc,h):
    p=f'{OUT}/{name}.html'; open(p,'w').write(doc)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:{h}}}}});await pg.goto('file://{p}');await pg.waitForTimeout(900);await pg.screenshot({{path:'{OUT}/{name}.png'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True,env={**os.environ,'PLAYWRIGHT_BROWSERS_PATH':'/opt/pw-browsers','NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})

if __name__=='__main__':
    shot('designy-bike-hoodie-post',post(),1350)
    shot('designy-bike-hoodie-story',story(),1920)
