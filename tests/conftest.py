import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto.forstudy.space")
    yield driver
    driver.quit()
