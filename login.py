# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Edge()
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# # username=driver.find_element(By.ID,"user-name")
# # USING CSS SELECTOR
# # username=driver.find_element(By.CSS_SELECTOR,"#user-name")
# # using xpath
# username=driver.find_element(By.XPATH,"//*[@id='user-name']")

# # password=driver.find_element(By.ID,"password")
# password=driver.find_element(By.XPATH,"//*[@id='password']")
# # login_button=driver.find_element(By.ID,"login-button")
# login_button=driver.find_element(By.XPATH,"//*[@id='login-button']")

# #Actions
# username.send_keys("standard_user")
# time.sleep(2)

# password.send_keys("secret_sauce")
# time.sleep(2)
# # if login_button.is_enabled:
# #     print("Button enabled")
# # else:
# #     print("Button disabled")
# # login_button.click()
# # sort_options = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
# # select =Select(sort_options)
# # select.select_by_value("lohi")
# # time.sleep(5)
# # selected=select.first_selected_option
# # print("Selected option is:",selected.text)
# # select.deselect_by_value("lohi")
# actions=ActionChains(driver)
# actions.context_click(login_button).perform()
# driver.close()

# driver.quit()
# =====================================================================
#  SauceDemo End-to-End Automation (Beginner Friendly)
#  Flow: Login -> Inventory (sort + scroll) -> Add to Cart -> Cart
#        -> Checkout (info) -> Overview -> Finish -> Logout
#  Browser: Microsoft Edge
# =====================================================================

# ---------- 1. IMPORTS ----------
from selenium import webdriver
from selenium.webdriver.common.by import By                    # To locate elements (ID, XPATH, CSS...)
from selenium.webdriver.support.ui import Select               # To handle <select> dropdowns
from selenium.webdriver.common.action_chains import ActionChains  # For mouse actions (hover, move)
from selenium.webdriver.support.ui import WebDriverWait        # For smart waiting
from selenium.webdriver.support import expected_conditions as EC  # Conditions to wait for
import time                                                     # For simple pauses (so you can SEE what happens)


# ---------- 2. OPEN BROWSER AND WEBSITE ----------
driver = webdriver.Edge()                  # Open Edge browser
driver.maximize_window()                   # Make the window full screen
driver.get("https://www.saucedemo.com/")   # Open the website

# Smart wait: waits UP TO 10 seconds for an element, continues as soon as it appears.
# This is better than time.sleep() because it doesn't waste time.
wait = WebDriverWait(driver, 10)

time.sleep(2)  # Pause only so you can watch the browser (remove later)


# =====================================================================
#  STEP A: LOGIN PAGE
# =====================================================================
print("STEP A: Logging in...")

# Find username, password and login button (using XPATH like you did)
username = driver.find_element(By.XPATH, "//*[@id='user-name']")
password = driver.find_element(By.XPATH, "//*[@id='password']")
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")

# Type the username and password
username.send_keys("standard_user")
time.sleep(1)
password.send_keys("secret_sauce")
time.sleep(1)

# Check the button is enabled before clicking
# NOTE: is_enabled() needs brackets () - without them it is always "True"
if login_button.is_enabled():
    print("Login button is enabled")
    login_button.click()          # Normal LEFT click to log in
else:
    print("Login button is disabled")

# Verify login worked: the URL should now contain "inventory"
wait.until(EC.url_contains("inventory"))
print("Login successful! Current URL:", driver.current_url)
time.sleep(2)


# =====================================================================
#  STEP B: INVENTORY PAGE - SORT PRODUCTS
# =====================================================================
print("\nSTEP B: Sorting products (Price low to high)...")

# The sort dropdown is a <select> element, so we use the Select class
sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(sort_dropdown)
select.select_by_value("lohi")   # Options: "az", "za", "lohi", "hilo"

# After sorting, the page reloads the list, so find the dropdown again
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
print("Selected sort option:", select.first_selected_option.text)
time.sleep(2)


# =====================================================================
#  STEP C: INVENTORY PAGE - SCROLLING
# =====================================================================
print("\nSTEP C: Scrolling the page...")

# Method 1: Scroll down by a fixed number of pixels (0 = left/right, 500 = down)
driver.execute_script("window.scrollBy(0, 500);")
print("Scrolled down 500 pixels")
time.sleep(2)

# Method 2: Scroll to the very bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled to bottom of page")
time.sleep(2)

# Method 3: Scroll back to the top
driver.execute_script("window.scrollTo(0, 0);")
print("Scrolled back to top")
time.sleep(2)

# Method 4: Scroll until a SPECIFIC element is visible (most useful in real tests)
fleece_jacket = driver.find_element(By.ID, "item_5_title_link")   # "Sauce Labs Fleece Jacket"
driver.execute_script("arguments[0].scrollIntoView();", fleece_jacket)
print("Scrolled to:", fleece_jacket.text)
time.sleep(2)

# Bonus: Hover the mouse over that product using ActionChains
actions = ActionChains(driver)
actions.move_to_element(fleece_jacket).perform()
time.sleep(1)


# =====================================================================
#  STEP D: ADD PRODUCTS TO CART
# =====================================================================
print("\nSTEP D: Adding products to cart...")

# Print all product names and prices on the page (shows how to use find_elements)
product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
print("Total products on page:", len(product_names))
for name, price in zip(product_names, product_prices):
    print("  -", name.text, ":", price.text)

# Add 3 products using their button IDs
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print("Added: Sauce Labs Backpack")
time.sleep(1)

driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
print("Added: Sauce Labs Bike Light")
time.sleep(1)

# This one is lower on the page, so scroll to it first, then click
fleece_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
driver.execute_script("arguments[0].scrollIntoView();", fleece_button)
time.sleep(1)
fleece_button.click()
print("Added: Sauce Labs Fleece Jacket")
time.sleep(1)

# Verify: the red badge on the cart icon should show "3"
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
print("Cart badge count:", cart_badge.text)
if cart_badge.text == "3":
    print("PASS: 3 items in cart")
else:
    print("FAIL: Expected 3 items but found", cart_badge.text)

# Bonus: Remove one item to test the "Remove" button, then add it back
driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
print("Removed: Sauce Labs Bike Light, badge now:",
      driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
print("Added Bike Light back")
time.sleep(1)

# Scroll to top so the cart icon is visible, then open the cart
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)


# =====================================================================
#  STEP E: CART PAGE
# =====================================================================
print("\nSTEP E: Opening the cart...")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
wait.until(EC.url_contains("cart"))
print("On cart page:", driver.current_url)
time.sleep(2)

# List the items inside the cart
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
print("Items in cart:")
for item in cart_items:
    print("  -", item.text)

# Click the Checkout button
driver.find_element(By.ID, "checkout").click()
time.sleep(2)


# =====================================================================
#  STEP F: CHECKOUT - YOUR INFORMATION PAGE
# =====================================================================
print("\nSTEP F: Filling checkout information...")

# Wait until the First Name box is visible, then fill the form
first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
first_name.send_keys("Prashant")
time.sleep(1)

driver.find_element(By.ID, "last-name").send_keys("Test")
time.sleep(1)

driver.find_element(By.ID, "postal-code").send_keys("5000")
time.sleep(1)

# Click Continue
driver.find_element(By.ID, "continue").click()
time.sleep(2)


# =====================================================================
#  STEP G: CHECKOUT - OVERVIEW PAGE
# =====================================================================
print("\nSTEP G: Checking the order overview...")

wait.until(EC.url_contains("checkout-step-two"))

# Read the price details shown on the page
item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print(item_total)
print(tax)
print(total)

# Scroll down to see the Finish button
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Click Finish
driver.find_element(By.ID, "finish").click()
time.sleep(2)


# =====================================================================
#  STEP H: ORDER COMPLETE PAGE
# =====================================================================
print("\nSTEP H: Verifying order is complete...")

success_message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
).text
print("Message shown:", success_message)

if success_message == "Thank you for your order!":
    print("PASS: Order placed successfully!")
else:
    print("FAIL: Order not completed")

time.sleep(2)

# Go back to the products page
driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)


# =====================================================================
#  STEP I: LOGOUT
# =====================================================================
print("\nSTEP I: Logging out...")

# Open the side menu (the 3-line "hamburger" icon at top-left)
driver.find_element(By.ID, "react-burger-menu-btn").click()

# The menu slides in, so WAIT until the logout link is clickable
logout = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout.click()
time.sleep(2)

# After logout we should be back on the login page
if driver.find_element(By.ID, "login-button").is_displayed():
    print("PASS: Logged out successfully")


# ---------- CLOSE THE BROWSER ----------
print("\nAll steps finished!")
driver.quit()   # quit() closes ALL windows and ends the session (no need for close() too)