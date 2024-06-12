from playwright.sync_api import Page
import pytest


email = 'sergio.cubero@uv.es'
password = 'ecoe20jornada'

def test_login(page: Page):
    page.goto("https://test-openecoe.umh.es/")
    page.goto("https://test-openecoe.umh.es/login?returnUrl=%2Fecoe")
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(email)
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(password)
    page.get_by_role("button", name="Iniciar sesión").click()