#import modules
from selenium import webdriver
import time
#lauching the chrome browser
driver=webdriver.Chrome()
time.sleep(2)
#maximize the browser window
# driver.maximize_window()

url="https://www.google.com/"
driver.get(url)
driver.maximize_window()

#delays the time for 5 sec and closes the browser
time.sleep(5)
#printing the title of the page 
print("The title of the page is",driver.title)
print("The current URL is",driver.current_url)


driver.get("https://www.saucedemo.com/")
time.sleep(5)
#refresh the browser
driver.refresh()
time.sleep(5)
# goes back to the previous page
driver.back()
time.sleep(5)
#goes forward to the next page
driver.forward()
time.sleep(5)
print("The title of the page is",driver.title)
print("The current URL is",driver.current_url)

#Quiting Driver and brower
driver.quit()


