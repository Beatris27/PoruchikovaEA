from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
#

LOGIN_FIELD = (By.CSS_SELECTOR, '[data-test="username"]')
PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test="password"]')
SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
TITLE_LABEL = (By.CSS_SELECTOR, "[data-test='title']")
PRODUCT_BUTTON_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
PRODUCT_BUTTON_BIKE_LIGHT = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")
BASKET_BUTTON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="firstName"]')
LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="lastName"]')
ZIP_FIELD = (By.CSS_SELECTOR, '[data-test="postalCode"]')
CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.delete_all_cookies()
driver.find_element(*LOGIN_FIELD).send_keys("standard_user")
driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")
driver.find_element(*SUBMIT_BUTTON).click()
# cookies = driver.get_cookies()

# with open("cookies.json", "w") as file:
#     json.dump(cookies, file, indent=4)
with open("cookies.json", "r") as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

products_chek = driver.find_element(*TITLE_LABEL)
assert products_chek.text == "Products", f"Текст элемента не совпадает: ожидалось 'Products', получено '{products_chek.text}'"
driver.find_element(*PRODUCT_BUTTON_BACKPACK).click()
time.sleep(3)
driver.find_element(*PRODUCT_BUTTON_BIKE_LIGHT).click()
time.sleep(3)
driver.find_element(*BASKET_BUTTON).click()
basket_chek = driver.find_element(*TITLE_LABEL)
assert basket_chek.text == "Your Cart", f"Текст элемента не совпадает: ожидалось 'Your Cart', получено '{basket_chek.text}'"
driver.find_element(*CHECKOUT_BUTTON).click()
time.sleep(3)
checkout_chek = driver.find_element(*TITLE_LABEL)
assert checkout_chek.text == "Checkout: Your Information", f"Текст элемента не совпадает: ожидалось 'Checkout: Your Information', получено '{checkout_chek.text}'"
driver.find_element(*FIRST_NAME_FIELD).send_keys("ELENA")
driver.find_element(*LAST_NAME_FIELD).send_keys("PORUCHIKOVA")
driver.find_element(*ZIP_FIELD).send_keys("111")
time.sleep(3)
driver.find_element(*CONTINUE_BUTTON).click()
time.sleep(3)
overview_chek = driver.find_element(*TITLE_LABEL)
assert overview_chek.text == "Checkout: Overview", f"Текст элемента не совпадает: ожидалось 'Checkout: Overview', получено '{overview_chek.text}'"
driver.find_element(*FINISH_BUTTON).click()
complete_chek = driver.find_element(*TITLE_LABEL)
assert complete_chek.text == "Checkout: Complete!", f"Текст элемента не совпадает: ожидалось 'Checkout: Complete!', получено '{complete_chek.text}'"
time.sleep(10)