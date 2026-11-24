import asyncio, sys, glob, os
from playwright.async_api import async_playwright
SRC = '/home/claude/974-social/products/winter-masks/flat/'; OUT = '/home/claude/974-social/products/winter-masks/worn/'
os.makedirs(OUT, exist_ok=True)
async def main(keys):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1200, 'height': 1200})
        pg.on('console', lambda m: print('console', m.text))
        for k in keys:
            await pg.goto(f'file:///home/claude/three/gaiter.html?tex=file://{SRC}{k}.png&ox={OX}&oy={OY}&ry={RY}')
            await pg.wait_for_function('window.DONE === true', timeout=60000)
            await pg.screenshot(path=f'{OUT}974-mask-{k}.png')
        await b.close()
RY = os.environ.get('RY','-0.95'); OX = os.environ.get('OX','0.62'); OY = os.environ.get('OY','-0.22')
keys = sys.argv[1:] or [os.path.basename(f)[:-4] for f in sorted(glob.glob(SRC + '*.png'))]
asyncio.run(main(keys))
print('ok')
