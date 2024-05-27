from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-outline-white.header_signin")
    REGISTRATION_BUTTON = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-signin-modal/div[3]/button[1]")

    def go_to_registration(self):
        self.click_element(self.SIGN_IN_BUTTON)
        self.click_element(self.REGISTRATION_BUTTON)
