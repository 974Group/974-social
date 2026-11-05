import sys,subprocess
sys.path.insert(0,'/home/claude/974-social/templates'); import payfoot
from PIL import Image
SP='/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
def strip(scale,out):
    W=1080; H=int(90*scale)
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{background:transparent;width:{W}px;height:{H}px}}
.w{{position:absolute;left:28px;right:28px;top:50%;transform:translateY(-50%)}}
{payfoot.css(scale,text='#3A1A24',label='#6B4A55')}
</style></head><body><div class="w">{payfoot.html()}</div></body></html>'''
    open('/tmp/strip.html','w').write(html)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('file:///tmp/strip.html');await p.waitForTimeout(600);await p.screenshot({{path:'{out}',omitBackground:true}});await b.close();}})()"
    subprocess.run(['node','-e',js],check=True)
for f,scale,y,cover in [('974-pilates-specs-post.png',1.0,1245,(0,1255,560,1300)),('974-pilates-specs-story.png',1.12,1780,None)]:
    strip(scale,'/tmp/strip.png')
    im=Image.open(f).convert('RGBA')
    if cover:
        bg=Image.new('RGBA',(cover[2]-cover[0],cover[3]-cover[1]),(244,236,230,255)); im.alpha_composite(bg,(cover[0],cover[1]))
    st=Image.open('/tmp/strip.png').convert('RGBA'); im.alpha_composite(st,(0,y))
    im.convert('RGB').save(f.replace('.png','-v2.png'))
print('ok')
