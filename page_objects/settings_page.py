from .base_page import BasePage
from selenium.webdriver.common.by import By

class SettingsPage(BasePage):
    SETTINGS_TAB = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']/div[@class='app-wrapper']//app-panel-layout//nav//a[@href='/panel/settings']")  # Локатор вкладки "Settings"
    REMOVE_ACCOUNT_BUTTON = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']/div[@class='app-wrapper']/div[@class='app-content']/app-panel-layout/div[@class='panel-layout']//app-settings//button[@class='btn btn-danger-bg']")
    CONFIRM_REMOVE_BUTTON = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-remove-account-modal/div[3]/button[2]")

    def go_to_settings(self):
        self.click_element(self.SETTINGS_TAB)

    def remove_account(self):
        self.click_element(self.REMOVE_ACCOUNT_BUTTON)
        self.click_element(self.CONFIRM_REMOVE_BUTTON)
