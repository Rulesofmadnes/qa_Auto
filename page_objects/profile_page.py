from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    PROFILE_TAB = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']/div[@class='app-wrapper']//app-panel-layout//nav//a[@href='/panel/profile']")
    PROFILE_NAME = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']/div[@class='app-wrapper']/div[@class='app-content']/app-panel-layout//app-profile//p[.='ttotsewerty tttosewerty']")
    GARAGE_TAB = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']//app-panel-layout//nav/a[@href='/panel/garage']")

    def go_to_profile(self):
        self.click_element(self.PROFILE_TAB)

    def get_profile_name(self):
        profile_name_element = self.find_element(self.PROFILE_NAME)
        return profile_name_element.text.split()[0]

    def go_to_garage(self):
        self.click_element(self.GARAGE_TAB)
