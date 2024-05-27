import pytest
from qa_Auto.page_objects.login_page import LoginPage
from qa_Auto.page_objects.registration_page import RegistrationPage
from qa_Auto.page_objects.profile_page import ProfilePage
from qa_Auto.page_objects.garage_page import GaragePage
from qa_Auto.page_objects.expenses_page import ExpensesPage
from qa_Auto.page_objects.settings_page import SettingsPage
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize("name, last_name, email, password", [("ttosewerty", "tttosewerty", "ttazassewerty@mail.com", "Qwertyui123!")])
def test_qa_auto(driver, name, last_name, email, password):
    login_page = LoginPage(driver)
    registration_page = RegistrationPage(driver)
    profile_page = ProfilePage(driver)
    garage_page = GaragePage(driver)
    expenses_page = ExpensesPage(driver)
    settings_page = SettingsPage(driver)

    try:
        login_page.go_to_registration()
        registration_page.register_user(name, last_name, email, password)


        profile_page.go_to_profile()


        assert profile_page.get_profile_name() == name


        profile_page.go_to_garage()


        garage_page.add_car("Audi", "TT", "123")


        garage_page.go_to_expenses()
        expenses_page.add_expense("Audi TT", "2024-05-26", "125", "15", "2")


        expenses_page.go_to_settings()
        settings_page.remove_account()
    except TimeoutException as e:
        driver.save_screenshot("test_failure_screenshot.png")
        raise e
