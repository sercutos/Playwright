from playwright.sync_api import Page
import pytest
import random

#EMAIL = 'sergio.cubero@uv.es'
#PASSWORD = 'ecoe20jornada'

EMAIL = 'ecoe@umh.es'
PASSWORD = 'Kui0chee'
ECOE_NAME = 'ECOE_NUEVA_26'
SERVER = 'http://sauron.uv.es:8081'

def test_create_ECOE(page: Page):
    # LOGIN
    page.goto(SERVER)
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(EMAIL)
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(PASSWORD)
    page.get_by_role("button", name="Iniciar sesión").click()
    # Add AREAS
    page.locator("nz-card").filter(has_text=ECOE_NAME).get_by_role("link").click()
    page.get_by_role("link", name="Configurar").click()
    page.get_by_role("button", name="Importar").click()
    
    with page.expect_file_chooser() as fc_info:        
        page.get_by_role("button", name="Pinche aquí o arrastre un").click()
    file_chooser = fc_info.value
    file_chooser.set_files("Areas.csv")
    
    
