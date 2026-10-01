from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Edge()
url="https://formy-project.herokuapp.com/"
driver.get(url)
driver.implicitly_wait(10)

driver.get("https://formy-project.herokuapp.com/autocomplete")
time.sleep(2)
wait=WebDriverWait(driver,10)
# try:
#     address=driver.find_element(By.ID,"autocomplete")
#     street_address=driver.find_element(By.ID,"street_number")
#     street_address2=driver.find_element(By.ID,"route")
#     city=driver.find_element(By.ID,"locality")
#     state=driver.find_element(By.ID,"administrative_area_level_1")
#     zip_code=driver.find_element(By.ID,"postal_code")
#     country=driver.find_element(By.ID,"country")
#     address.send_keys("Kathmandu")
#     street_address.send_keys("Kathmandu")
#     street_address2.send_keys("Kathmandu")
#     city.send_keys("Kathmandu")
#     state.send_keys("Bagmati")
#     zip_code.send_keys("44600")
#     country.send_keys("Nepal")
#     time.sleep(2)
# except:
#     print("An error occurred while filling the form.")
# finally:
#     print("Form filling completed.")
try:
    address = wait.until(EC.visibility_of_element_located((By.ID, "autocomplete")))
    address.send_keys("Kathmandu")
    time.sleep(2)

    street_address = wait.until(EC.visibility_of_element_located((By.ID, "street_number")))
    street_address.send_keys("Kathmandu")

    street_address2 = wait.until(EC.visibility_of_element_located((By.ID, "route")))
    street_address2.send_keys("Kathmandu")

    city = wait.until(EC.visibility_of_element_located((By.ID, "locality")))
    city.send_keys("Kathmandu")

    state = wait.until(EC.visibility_of_element_located((By.ID, "administrative_area_level_1")))
    state.send_keys("Bagmati")

    zip_code = wait.until(EC.visibility_of_element_located((By.ID, "postal_code")))
    zip_code.send_keys("44600")

    country = wait.until(EC.visibility_of_element_located((By.ID, "country")))
    country.send_keys("Nepal")
except:
    print("An error occurred while filling the form.")
finally:
    print("Form filling completed.")
driver.quit()