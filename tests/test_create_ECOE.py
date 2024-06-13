from playwright.sync_api import Page
import pytest
import random
from decouple import config


#ECOE_NAME = f"ECOE_NUEVA_{random.randint(0,99)}"

@pytest.mark.order(2)
def test_create_ECOE(page: Page):
    # LOGIN
    page.goto(config('SERVER'))
    page.get_by_placeholder("Correo electrónico").click()        
    page.get_by_placeholder("Correo electrónico").fill(config('EMAIL'))
    page.get_by_placeholder("Contraseña").click()    
    page.get_by_placeholder("Contraseña").fill(config('PASSWORD'))
    page.get_by_role("button", name="Iniciar sesión").click()
    # Create ECOE
    page.goto("http://sauron.uv.es:8081/ecoe")
    page.locator("nz-card").filter(has_text="Crear nueva ECOE").locator("a").click()
    page.get_by_placeholder("Nombre de la ECOE").click()
    page.get_by_placeholder("Nombre de la ECOE").fill(ECOE_NAME)
    page.get_by_role("button", name="Aceptar").click()
    page.locator("#cdk-overlay-2").get_by_role("button", name="Aceptar").click()
    