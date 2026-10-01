from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

url = "https://sagar-test-qa.vercel.app/"
driver.get(url)
try:
    # Wait until username is visible
    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("secret_user")

    # Wait until password is visible
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("secret_password")

    # Wait until login button is clickable
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
except:
    print("An error occurred:")
finally:
    print("Test completed.")
# Wait until JavaScript alert appears
alert = wait.until(EC.alert_is_present())

print(alert.text)
alert.accept()

driver.quit()