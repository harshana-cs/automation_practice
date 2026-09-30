from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Edge()
driver_url="https://www.saucedemo.com/"
driver.get(driver_url)
time.sleep(10)
# driver.implicitly_wait(10)

driver.find_element(By.ID,"user-name").send_keys("secret_user")
wait=WebDriverWait(driver,10)
login_button=wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

##assertion
# if driver.current_url=="https://www.saucedemo.com/inventory.html":
#     print("Login Scucessfull")
# else:
#     print("Login unsecessfull")

# if "inventory" in driver_url:
#     print("Login Sucessfull")
# else:
#     print("Login Unsucessfull")

assert "inventory" in driver.driver_url,"Invalid credentials"


driver.close()
driver.quit()



### yo bujena keai ni 