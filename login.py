from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
# username=driver.find_element(By.ID,"user-name")
# USING CSS SELECTOR
# username=driver.find_element(By.CSS_SELECTOR,"#user-name")
# using xpath
username=driver.find_element(By.XPATH,"//*[@id='user-name']")

# password=driver.find_element(By.ID,"password")
password=driver.find_element(By.XPATH,"//*[@id='password']")
# login_button=driver.find_element(By.ID,"login-button")
login_button=driver.find_element(By.XPATH,"//*[@id='login-button']")

#Actions
username.send_keys("standard_user")
time.sleep(5)

password.send_keys("secret_sauce")
time.sleep(5)
if login_button.is_enabled:
    print("Button enabled")
else:
    print("Button disabled")
login_button.click()
time.sleep(5)

driver.quit()

# relative=//*[@id="user-name"]