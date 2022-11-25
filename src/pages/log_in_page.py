from seleniumpagefactory.Pagefactory import PageFactory
import time


class LogInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'user_name': ('CSS', '#user-name'),
        'password': ('CSS', '#password'),
        'login_btn': ('CSS', '#login-button')
    }

    def select_username(self):
        self.user_name.set_text('standard_user\n')
        time.sleep(2)

    def select_password(self):
        self.password.set_text('secret_sauce\n')

    def click_login(self):
        self.login_btn.click()
        time.sleep(2)
