from playwright.sync_api import Page
import pytest
import test_login

# https://www.saucedemo.com/
# standard_user / secret_sauce
# https://trace.playwright.dev/
#pytest .\test_1.py 
@pytest.mark.only_browser("chromium") #ejecuta test_title solo en chrome
#@pytest.mark.skip_browser("chromium") # no lo ejecuta en chrome
def test_title(page: Page):    
    page.goto("/")
    assert page.title() == "Swag Labs"

def test_inventory_page(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("H3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."

def test_login(page: Page):
    page.goto("https://test-openecoe.umh.es/")
    page.goto("https://test-openecoe.umh.es/login?returnUrl=%2Fecoe")
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(test_login.email)
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(password)
    page.get_by_role("button", name="Iniciar sesión").click()