from .base_page import BasePage
from selenium.webdriver.common.by import By

class ExpensesPage(BasePage):
    EXPENSES_TAB = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']//app-panel-layout//nav/a[@href='/panel/expenses']")  # Локатор вкладки "Fuel expenses"
    ADD_EXPENSE_BUTTON = (By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']/div[@class='app-wrapper']/div[@class='app-content']/app-panel-layout//app-fuel-expenses//button[@class='btn btn-primary']")
    VEHICLE_SELECT = (By.XPATH, "/html//select[@id='addExpenseCar']")
    DATE_INPUT = (By.XPATH, "/html//input[@id='addExpenseDate']")
    MILEAGE_INPUT = (By.XPATH, "/html//input[@id='addExpenseMileage']")
    LITERS_INPUT = (By.XPATH, "/html//input[@id='addExpenseLiters']")
    COST_INPUT = (By.XPATH, "/html//input[@id='addExpenseTotalCost']")
    ADD_BUTTON = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-add-expense-modal/div[3]/button[2]")

    def go_to_expenses(self):
        self.click_element(self.EXPENSES_TAB)

    def add_expense(self, vehicle, date, mileage, liters, cost):
        self.click_element(self.ADD_EXPENSE_BUTTON)
        self.send_keys(self.VEHICLE_SELECT, vehicle)
        self.send_keys(self.DATE_INPUT, date)
        self.send_keys(self.MILEAGE_INPUT, mileage)
        self.send_keys(self.LITERS_INPUT, liters)
        self.send_keys(self.COST_INPUT, cost)
        self.click_element(self.ADD_BUTTON)