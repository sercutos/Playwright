
from playwright.sync_api import Playwright, sync_playwright, expect
from decouple import config



def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    # LOGIN
    page.goto(config('SERVER'))
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(config('EMAIL'))
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(config('PASSWORD'))
    page.get_by_role("button", name="Iniciar sesión").click()
    # ---------------------
    context.close()
    browser.close()


