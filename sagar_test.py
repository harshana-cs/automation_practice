from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://sagar-test-qa.vercel.app/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
username=driver.find_element(By.ID,"username")
password=driver.find_element(By.ID,"password")
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")


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

