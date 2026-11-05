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
import sys as _s
JOBS={'specs':[('974-pilates-specs-post.png',1.0,1245,(0,1255,560,1300)),('974-pilates-specs-story.png',1.12,1780,None)],
 'pack':[('974-pilates-packaging-post.png',1.0,1238,(120,1234,960,1282)),('974-pilates-packs-post.png',1.0,1240,None),('974-pilates-packaging-story.png',1.12,1785,None)]}
for f,scale,y,cover in JOBS[_s.argv[1] if len(_s.argv)>1 else 'specs']:
    strip(scale,'/tmp/strip.png')
    im=Image.open(f).convert('RGBA')
    if cover:
        h=cover[3]-cover[1]
        patch=im.crop((cover[0],cover[1]-h-5,cover[2],cover[1]-5))
        from PIL import ImageFilter, ImageDraw
        m=Image.new('L',patch.size,0); ImageDraw.Draw(m).rectangle((0,0,patch.width,patch.height),fill=255); m=m.filter(ImageFilter.GaussianBlur(1.5))
        im.paste(patch,(cover[0],cover[1]),m)
    st=Image.open('/tmp/strip.png').convert('RGBA'); im.alpha_composite(st,(0,y))
    im.convert('RGB').save(f.replace('.png','-v2.png'))
print('ok')
