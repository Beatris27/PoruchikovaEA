import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
LEFT_CLICK_BUTTON = ("xpath", "//button[text()='Click Me']")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
wait = WebDriverWait(driver, 10, poll_frequency=1)

action = ActionChains(driver)

DOUBLE_CLICK_BUTTON_ELEMENT = driver.find_element(*DOUBLE_CLICK_BUTTON)
RIGHT_CLICK_BUTTON_ELEMENT = driver.find_element(*RIGHT_CLICK_BUTTON)
LEFT_CLICK_BUTTON_ELEMENT = driver.find_element(*LEFT_CLICK_BUTTON)
action.double_click(DOUBLE_CLICK_BUTTON_ELEMENT).perform()
action.context_click(RIGHT_CLICK_BUTTON_ELEMENT).perform()
action.click(LEFT_CLICK_BUTTON_ELEMENT).perform()
time.sleep(3)

#выбор в меню
# STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
# STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
# STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
#
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/menu#")
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# STEP_1 = driver.find_element(*STEP_1_LOCATOR)
# STEP_2 = driver.find_element(*STEP_2_LOCATOR)
# STEP_3 = driver.find_element(*STEP_3_LOCATOR)
#
# action = ActionChains(driver)
#
# action.move_to_element(STEP_1).pause(3).move_to_element(STEP_2).pause(3).move_to_element(STEP_3).perform()
#
# time.sleep(5)

#драгенддроп

# SOURCE_LOCATOR = (By.CSS_SELECTOR, "#draggable")
# TARGET_LOCATOR = (By.CSS_SELECTOR, "#droppable")
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# SOURCE = driver.find_element(*SOURCE_LOCATOR)
# TARGET = driver.find_element(*TARGET_LOCATOR)
#
# action = ActionChains(driver)
#
# action.drag_and_drop(SOURCE, TARGET).perform()
#
# time.sleep(5)