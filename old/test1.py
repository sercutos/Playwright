import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright
from playwright.async_api import async_playwright, Playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # abre el navegador visualmente    
    page = browser.new_page()
    page.goto("https://test-openecoe.umh.es")       
    input1 = page.getByPlaceholder("Correo electrónico")

    print (input1)
    # sergio.cubero@uv.es/ecoe20jornada
    
    browser.close()