import pytest
from playwright.sync_api import Page, expect

## sergio.cubero@uv.es/ecoe20jornada
def test_login(page:Page):
    #launch browserstack demo    
    page.goto("https://test-openecoe.umh.es")
    #page.getByPlaceholder("Correo electrónico")
    date = page.locator('type=text')
    date.fill("ecoe20jornada")