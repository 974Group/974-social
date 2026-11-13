import subprocess,sys,os
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
ns={}; exec(open('gen.py').read(),ns)
CSS=ns['CSS'].replace('../aw/fonts',SP+'/aw/fonts'); sock=ns['sock']; grid=ns['grid']
FOOT=f'<div class="pf" style="position:absolute;left:28px;right:28px;top:1252px">{payfoot.html()}</div>'
bow=f'''<div class="dots" style="opacity:.35"></div>
<img class="logo" src="logo-black.png" style="left:64px;top:56px">
<div class="abs lora" style="right:64px;top:46px;font-size:70px;color:#C3203A">The Bow Edit</div>
<div class="abs ar" style="right:64px;top:150px;font:800 34px Cairo">فيونكة لكل مزاج 🎀</div>
{grid(['pinkbow','cherrybow','redbow'],3,40,350,333,860,560,570,22)}
<div class="abs ar" style="left:0;right:0;top:1020px;text-align:center;font:800 40px Cairo;color:#2A1418">49 ر.ق · أي ٣ بـ ١٣٤ 🎀</div>
{FOOT}'''
coffee=f'''
<img src="close_coffee.jpg" class="abs" style="left:0;top:0;width:1080px;height:720px;object-fit:cover">
<img class="logo" src="logo-white.png" style="left:64px;top:56px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.35))">
<div class="abs lora" style="right:64px;top:745px;font-size:76px;color:#6B3E2A">Pilates & Coffee ☕</div>
<div class="abs ar" style="right:64px;top:855px;font:800 36px Cairo">كلاس الصبح.. وبعدها قهوة وكرواسون 🥐</div>
{sock('coffee',80,925,265)}{sock('tennis',280,925,265)}
<div class="callout" style="right:64px;top:985px;width:520px"><b style="font-size:30px">Pilates & Coffee · Court Club</b><span>تصميمين للي يحبون الكلاس بنفس حبهم للقهوة</span></div>
<div class="callout" style="right:64px;top:1125px;width:520px"><span style="font-weight:800;color:#2A1418">49 ر.ق · أي ٣ بـ ١٣٤</span></div>
{FOOT}'''
def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}\nbody{{padding:0;width:1080px;background:#F4ECE6}}\n{payfoot.css(1.0,text="#3A1A24",label="#6B4A55")}</style></head><body><div class="ab P">{body}</div></body></html>'
for name,body in (('bow-edit',bow),('coffee-edit',coffee)):
    fn=f'v2_{name}.html'; open(fn,'w').write(page(body))
    out=f'../974-pilates-{name}-v2.png'
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});await p.goto('file://'+process.cwd()+'/{fn}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
from PIL import Image
for name in ('bow-edit','coffee-edit'):
    im=Image.open(f'../974-pilates-{name}-v2.png').convert('RGB')
    bg=im.getpixel((540,1345)) if name=='bow-edit' else im.getpixel((1070,1345))
    st=Image.new('RGB',(1080,1920),bg); st.paste(im,(0,285)); st.save(f'../974-pilates-{name}-story-v2.png')
print('ok')
