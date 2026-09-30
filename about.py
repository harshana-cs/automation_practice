from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://sagar-test-qa.vercel.app/about.html")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
full_name=driver.find_element(By.ID,"fullname")
phone=driver.find_element(By.ID,"phone")
email=driver.find_element(By.ID,"email")
hobby=driver.find_element(By.ID,"hobby")
submit=driver.find_element(By.XPATH,"//button[@type='submit']")

#Actions
full_name.send_keys("Harshana Bhandari")
time.sleep(1)
phone.send_keys("9847373171")
time.sleep(1)
email.send_keys("harshanabhandari2@gmail.com")
time.sleep(1)
hobby.send_keys("Singing")
time.sleep(1)
if submit.is_enabled:
    print("Button enabled")
else:
    print("Button disabled")
submit.click()
time.sleep(5)

driver.quit()

