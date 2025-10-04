# Домашнее задание
# Закрепите пройденный материал на сайте https://demoqa.com/text-box
# Заполните все текстовые поля данными (почистить поля перед заполнением).
# Проверьте, что данные действительно введены, используя get_attribute() и assert.
# Нажимать на submit не нужно, просто поработайте с полями ввода

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

Full_Name = "#userName"
Email = "#userEmail"
Current_Address = "#currentAddress"
Permanent_Address = "#permanentAddress"

Full_Name_field = driver.find_element(By.CSS_SELECTOR, Full_Name)
Full_Name_field.clear()
assert Full_Name_field.get_attribute("value") == "", "Поле не очистилось"
Full_Name_field.send_keys("Elena")
assert "Elena" in Full_Name_field.get_attribute("value"), "Текст не ввелся в поле"

Email_field = driver.find_element(By.CSS_SELECTOR, Email)
Email_field.clear()
assert Email_field.get_attribute("value") == "", "Поле не очистилось"
Email_field.send_keys("11@mai.ru")
assert "11@mai.ru" in Email_field.get_attribute("value"), "Текст не ввелся в поле"

Current_Address_field = driver.find_element(By.CSS_SELECTOR, Current_Address)
Current_Address_field.clear()
assert Current_Address_field.get_attribute("value") == "", "Поле не очистилось"
Current_Address_field.send_keys("11@mai.ru")
assert "11@mai.ru" in Current_Address_field.get_attribute("value"), "Текст не ввелся в поле"

Permanent_Address_field = driver.find_element(By.CSS_SELECTOR, Permanent_Address)
Permanent_Address_field.clear()
assert Permanent_Address_field.get_attribute("value") == "", "Поле не очистилось"
Permanent_Address_field.send_keys("11@mai.ru")
assert "11@mai.ru" in Permanent_Address_field.get_attribute("value"), "Текст не ввелся в поле"

