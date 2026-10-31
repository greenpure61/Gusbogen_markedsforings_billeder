import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for name,h in [('feed',1350),('tiktok',1920)]:
            pg=await b.new_page(viewport={'width':1080,'height':h})
            import os
            await pg.goto('file://'+os.path.abspath(name+'.html'))
            await pg.evaluate('document.fonts.ready')
            await pg.screenshot(path=f'olieskolen-{name}.png')
        await b.close()
asyncio.run(main())
