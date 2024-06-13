from playwright.sync_api import Page
import pytest
import random
from decouple import config

@pytest.mark.order(6)
def test_create_ECOE(page: Page):
    # LOGIN
    page.goto(config('SERVER'))
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(config('EMAIL'))
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(config('PASSWORD'))
    page.get_by_role("button", name="Iniciar sesión").click()
    # Add Stations
    page.locator("nz-card").filter(has_text=config('ECOE_NAME')).get_by_role("link").click()
    page.locator("nz-card").filter(has_text="Estaciones Configurar 12").get_by_role("button").click()   
    page.get_by_role("button", name="Configuración Cronómetros").click()
    page.get_by_role("button", name="Añadir Fase").click()
    page.get_by_placeholder("Introduzca el nombre...").click()
    page.get_by_placeholder("Introduzca el nombre...").fill(config('NOMBRE_FASE'))
    page.get_by_placeholder("minutos").click()
    page.get_by_placeholder("minutos").fill(config('MINUTOS'))
    page.get_by_placeholder("segundos").click()
    page.get_by_placeholder("segundos").fill(config('SEGUNDOS'))
    page.get_by_role("button", name="Guardar").click()

    
    
