from selenium import webdriver
import pytest
from pages.login import Loginpage
from pages.inventory import Inventorypage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_inventory(driver):
    login=Loginpage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    obj=Inventorypage(driver)
    obj.click_add_backpack()
    obj.click_cart()