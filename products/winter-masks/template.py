# Fit the 8 chosen designs onto the factory template: 490 x 460 mm (1388.98 x 1303.94 pt), full fabric piece.
# Background is scaled to cover (sides cropped, they wrap to the back seam); text block is centred on the front,
# a little above the middle (face area). Output: vector PDF saved as .ai (Illustrator opens it) + PNG preview.
import asyncio, os
from flat import D10, FONT
from playwright.async_api import async_playwright
D = os.path.dirname(os.path.abspath(__file__))
SKIP = {'sadu', 'flag-edge'}
W, H = 1389, 1304            # CSS px == pt at 1px:1pt; page size set in mm
SC = max(W / 1200, H / 900)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        for k, bg, ov, name, _ in D10:
            if k in SKIP: continue
            css = FONT.replace('body{width:1200px;height:900px', f'body{{width:{W}px;height:{H}px')
            html = f'''<html><head><style>{css}
@page{{size:{1388.98/72:.5f}in {1303.94/72:.5f}in;margin:0}} html,body{{margin:0}}
#bg{{position:absolute;left:{(W-1200*SC)/2:.1f}px;top:{(H-900*SC)/2:.1f}px;width:1200px;height:900px;transform:scale({SC:.4f});transform-origin:0 0;overflow:hidden}}
#ov{{position:absolute;left:0;top:0;width:1200px;height:900px;transform-origin:0 0}}
</style></head><body><div id="bg">{bg}</div><div id="ov">{ov}</div>
<script>
const ov=document.getElementById('ov'); let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
for(const e of ov.children){{const r=e.getBoundingClientRect(); if(!r.width) continue; x0=Math.min(x0,r.left);y0=Math.min(y0,r.top);x1=Math.max(x1,r.right);y1=Math.max(y1,r.bottom);}}
const s=1.25, cx=(x0+x1)/2, cy=(y0+y1)/2;
ov.style.transform=`translate(${{{W}/2 - cx*s}}px, ${{{H}*0.40 - cy*s}}px) scale(${{s}})`;
window.READY=1;
</script></body></html>'''
            path = f'{D}/print/_t.html'; open(path, 'w').write(html)
            await pg.goto('file://' + path); await pg.wait_for_function('window.READY===1'); await pg.wait_for_timeout(600)
            await pg.pdf(path=f'{D}/print/974-mask-{k}-490x460mm.pdf', width=f'{1388.98/72:.5f}in', height=f'{1303.94/72:.5f}in', print_background=True)
            await pg.screenshot(path=f'{D}/print/974-mask-{k}-preview.png')
            print(k)
        await b.close()
asyncio.run(main())
