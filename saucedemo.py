from selenium import webdriver
import time
driver=webdriver.Edge()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.refresh()
time.sleep(5)
#driver closes only the current window
driver.close()
#Quiting Driver and brower
driver.quit()



# user-name
# password
#login-button