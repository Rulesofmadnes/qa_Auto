from selenium.webdriver.common.by import By
from .base_page import BasePage

class GaragePage(BasePage):
    ADD_CAR_BUTTON = (By.XPATH, "//app-panel-layout//app-garage//button[contains(@class,'btn-primary')]")
    BRAND_SELECT = (By.XPATH, "/html//select[@id='addCarBrand']")
    MODEL_SELECT = (By.XPATH, "/html//select[@id='addCarModel']")
    MILEAGE_INPUT = (By.XPATH, "/html//input[@id='addCarMileage']")
    CONFIRM_ADD_CAR_BUTTON = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-add-car-modal/div[3]/button[2]")

    def click_add_car_button(self):
        add_car_button = self.find_element(self.ADD_CAR_BUTTON)
        add_car_button.click()

    def select_brand(self, brand):
        brand_select = self.find_element(self.BRAND_SELECT)
        brand_select.click()
        brand_option = self.find_element((By.XPATH, f"//select[@data-testid='car-brand']/option[text()='{brand}']"))
        brand_option.click()

    def select_model(self, model):
        model_select = self.find_element(self.MODEL_SELECT)
        model_select.click()
        model_option = self.find_element((By.XPATH, f"//select[@data-testid='car-model']/option[text()='{model}']"))
        model_option.click()

    def set_mileage(self, mileage):
        mileage_input = self.find_element(self.MILEAGE_INPUT)
        mileage_input.clear()
        mileage_input.send_keys(mileage)

    def click_confirm_add_car_button(self):
        confirm_button = self.find_element(self.CONFIRM_ADD_CAR_BUTTON)
        confirm_button.click()

    def add_car(self, brand, model, mileage):
        self.click_add_car_button()
        self.select_brand(brand)
        self.select_model(model)
        self.set_mileage(mileage)
        self.click_confirm_add_car_button()
