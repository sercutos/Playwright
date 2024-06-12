# playwright: 1.44.0

import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect

# funcion asincrona
async def main():
    #with statemen en python
    async with async_playwright() as p:
        #browser = await p.chromium.launch(headless=False) # abre el navegador visualmente    
        browser = await p.firefox.launch(headless=False) # abre el navegador visualmente    
        page = await browser.new_page()
        await page.goto("https://test-openecoe.umh.es")
        # sergio.cubero@uv.es/ecoe20jornada
        print(await page.title())
        await page.getByPlaceholder('Correo electrónico').fill('sergio.cubero@uv.es')
        

        #await page.locator('type=text').fill('sergio.cubero@uv.es')
        #await page.locator('type=password').click()
        # Page.Locator("//button[@routerlink='/web/click']").ClickAsync();
        await browser.close()

asyncio.run(main())
