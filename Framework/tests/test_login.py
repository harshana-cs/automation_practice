from selenium import webdriver
import pytest
from pages.login import Loginpage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    #generate and injects the driver means it calls the driver function and provides the driver instance to the test functions that require it. 
   #if not used the driver gets quit 
    yield driver
    driver.quit()
def test_login(driver):
    obj=Loginpage(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user",)
    obj.enter_password("secret_sauce")
    obj.click_login()

