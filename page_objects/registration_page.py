from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@id='signupName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='signupLastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='signupEmail']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='signupPassword']")
    REENTER_PASSWORD_INPUT = (By.XPATH, "//input[@id='signupRepeatPassword']")
    REGISTER_BUTTON = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-signup-modal/div[@class='modal-footer']/button[@type='button']")

    def register_user(self, name, last_name, email, password):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.REENTER_PASSWORD_INPUT, password)
        self.click_element(self.REGISTER_BUTTON)
