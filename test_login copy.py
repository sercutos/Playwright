import re
from playwright.sync_api import Playwright, sync_playwright, expect
#from decouple import config
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()




def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://test-openecoe.umh.es/")
    page.goto("https://test-openecoe.umh.es/login?returnUrl=%2Fecoe")
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(os.getenv('EMAIL'))
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(os.getenv('PASSWORD'))
    page.get_by_role("button", name="Iniciar sesión").click()
    # ---------------------
    context.close()
    browser.close()


""" with sync_playwright() as playwright:
    test_run(playwright) """