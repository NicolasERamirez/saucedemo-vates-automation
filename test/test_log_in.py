from selenium import webdriver
from src.pages.log_in_page import LogInPage


def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    log_in_page = LogInPage(driver)

    log_in_page.select_username()
    log_in_page.select_password()
    log_in_page.click_login()

    driver.quit()
