import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

# checkbox = driver.find_element(By.CSS_SELECTOR, '.rct-checkbox')
# checkbox.click()

# YES_RADIO_BUTTON = (By.CSS_SELECTOR, "#yesRadio") # Для статуса
# YES_RADIO_LABEL = (By.CSS_SELECTOR, 'label[for="yesRadio"]') # Для взаимодействия
# IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
# NO_RADIO_BUTTON = (By.CSS_SELECTOR, '#noRadio')
#
# #assert driver.find_element(*NO_RADIO_BUTTON).is_enabled()
# driver.find_element(*YES_RADIO_LABEL).click()
# assert driver.find_element(*YES_RADIO_BUTTON).is_selected()
#
# DROPDOWN_ELEMENT = (By.CSS_SELECTOR, "#dropdown")
# dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))
# dropdown.select_by_index(2)
# http://the-internet.herokuapp.com/dropdown
MULTI_SELECT = (By.CSS_SELECTOR, "#react-select-4-input")
select = driver.find_element(*MULTI_SELECT)
select.send_keys("Green")
time.sleep(3)
assert select.get_attribute("value") == "Green", "Error :("
select.send_keys(Keys.ENTER)
time.sleep(3)
select.send_keys(Keys.ESCAPE)
time.sleep(3)

time.sleep(5)