import asyncio, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flat import D10, FONT
from playwright.async_api import async_playwright
D = os.path.dirname(os.path.abspath(__file__))
cards = ''.join(f'''<div class="c"><div class="n en">{i+1:02d}</div><img class="m" src="file://{D}/mock/{k}.png"><img class="f" src="file://{D}/flat/{k}.png">
<div class="t en">{name}</div><div class="d ar">{ar}</div></div>''' for i, (k, _, _, name, ar) in enumerate(D10))
html = f'''<html><head><style>{FONT}
body{{width:2000px;height:auto;background:#F4F1F2;padding:60px}}
h1{{font-family:Cairo;font-weight:900;font-size:58px;color:#51022D;direction:rtl;text-align:right}}
.s{{font-family:Poppins;font-weight:700;letter-spacing:4px;color:#720842;font-size:18px;margin:6px 0 40px}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:26px}}
.c{{background:#fff;border-radius:28px;padding:18px 18px 22px;position:relative;box-shadow:0 10px 26px rgba(81,2,45,.08)}}
.n{{position:absolute;left:18px;top:14px;font-weight:900;font-size:30px;color:#720842}}
.m{{width:100%;display:block}}.f{{width:100%;border-radius:12px;margin-top:6px}}
.t{{font-weight:800;font-size:20px;color:#1b1b1b;margin-top:12px}}.d{{font-weight:700;font-size:20px;color:#666;margin-top:2px;text-align:right}}
</style></head><body><h1>ماسكات 974 الشتوية: 10 تصاميم للاختيار</h1><div class="s en">WINTER FACE MASKS 26/27 · CONCEPTS (MOCKUP + FLAT PRINT)</div><div class="g">{cards}</div></body></html>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 2000, 'height': 1000})
        open(D + '/sheet.html', 'w').write(html); await pg.goto('file://' + D + '/sheet.html'); await pg.wait_for_timeout(1500)
        await pg.screenshot(path=D + '/974-winter-masks-10-concepts.png', full_page=True); await b.close()
asyncio.run(main())
