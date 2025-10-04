from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://demoqa.com/dynamic-properties")
AFTER_5_SECOND_BUTTON = "#visibleAfter"
VISIBLE_AFTER_5_SECOND_BUTTON = (By.CSS_SELECTOR, AFTER_5_SECOND_BUTTON)

driver.find_element(*VISIBLE_AFTER_5_SECOND_BUTTON).click()

wait = WebDriverWait(driver, 30, poll_frequency=1)

ENABLE_AFTER_5_SECOND = "#enableAfter"
ENABLE_AFTER_5_SECOND_BUTTON = (By.CSS_SELECTOR, ENABLE_AFTER_5_SECOND)

wait.until(EC.element_to_be_clickable(ENABLE_AFTER_5_SECOND_BUTTON)) # Ждем пока кнопка станет кликабельной
driver.find_element(*ENABLE_AFTER_5_SECOND_BUTTON).click()

COLOR_CHANGE = "#colorChange"
COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, COLOR_CHANGE)

wait.until(EC.element_to_be_clickable(COLOR_CHANGE_BUTTON)) # Ждем пока кнопка станет кликабельной
driver.find_element(*COLOR_CHANGE_BUTTON).click()