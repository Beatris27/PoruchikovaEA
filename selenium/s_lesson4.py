import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Создание экземпляра веб-драйвера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
driver.find_element(By.CSS_SELECTOR, "#alertButton").click()
alert = wait.until(EC.alert_is_present())
time.sleep(5)
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#timerAlertButton").click()
alert = wait.until(EC.alert_is_present())
time.sleep(5)
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#confirmButton").click()
alert = wait.until(EC.alert_is_present())
time.sleep(5)
alert.dismiss()

driver.find_element(By.CSS_SELECTOR, "#promtButton").click()
alert = wait.until(EC.alert_is_present())
time.sleep(5)
alert.send_keys("Elena")
alert.accept()
time.sleep(5)