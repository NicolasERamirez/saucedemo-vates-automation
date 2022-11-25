from selenium import webdriver
from src.pages.log_in_page import LogInPage


def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    log_in_page = LogInPage(driver)

    # Se ingresa las credenciales
    log_in_page.select_username()
    log_in_page.select_password()
    # Se seleccion el boton de log in
    log_in_page.click_login()
    # Se valida el inicio de sesion con una imagen
    log_in_page.validate_success()

    driver.quit()
