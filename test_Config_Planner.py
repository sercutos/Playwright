from playwright.sync_api import Page
import pytest
import random
from decouple import config



def test_create_ECOE(page: Page):
    # LOGIN
    page.goto(config('SERVER'))
    page.get_by_placeholder("Correo electrónico").click()    
    page.get_by_placeholder("Correo electrónico").fill(config('EMAIL'))
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill(config('PASSWORD'))
    page.get_by_role("button", name="Iniciar sesión").click()
    # Stations
    page.locator("nz-card").filter(has_text=config('ECOE_NAME')).get_by_role("link").click()
    page.locator("nz-card").filter(has_text="Estaciones Configurar 12").get_by_role("button").click()   
    page.get_by_role("button", name="Configuración Cronómetros").click()
    
    page.get_by_role("button", name="Configuración Alumnos").click()
    page.get_by_role("button", name="Configuración Planificador").click()
    # Añadir Ronda
    # page.get_by_role("button", name="Añadir ronda").click()
    # page.get_by_label("Código").click()
    # page.get_by_label("Código").fill(config('CODIGO_RONDA'))
    # page.get_by_label("Código").click()
    # page.get_by_label("Descripción").click()
    # page.get_by_label("Descripción").fill(config('DESCRT_RONDA'))
    # page.get_by_role("button", name="Aceptar").click()
    # Añadir Turno
    page.get_by_role("button", name="Añadir turno").click()
    page.get_by_label("Código").click()
    page.get_by_label("Código").fill("TURNO_01")
    page.get_by_placeholder("Seleccionar fecha...").click()
    #page.get_by_title("30/6/2024").locator("div").click()
    page.get_by_role("button", name="Hoy").click()
    page.get_by_placeholder("Elegir hora...").click()
    # page.get_by_text("09").first.click()
    # page.get_by_text("30", exact=True).click()  
    page.get_by_text("Ahora").click()
    page.get_by_role("button", name="Aceptar").click()
    page.get_by_role("button", name="Autosignación de Alumnos").click()

    
