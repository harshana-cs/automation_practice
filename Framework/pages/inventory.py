from selenium.webdriver.common.by import By
import time
class Inventorypage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    def click_add_backpack(self):
        self.driver.find_element(*self.add_backpack).click()
        time.sleep(2)
    def click_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        time.sleep(2)