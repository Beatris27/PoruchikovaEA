# Домашнее задание
# Напишите опции и запускайте любой сайт с ними, посмотрите взаимодействие.
# Что касается загрузки файлов.
# Создайте в проекте файл и загрузить его.
# Страница для выполнения задания: https://demoqa.com/upload-download

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

upload_file = "#uploadFile"

upload_file_field = driver.find_element(By.CSS_SELECTOR, upload_file)
upload_file_field.send_keys(r"C:\Users\PoruchikovaEA\PycharmProjects\PoruchikovaEA\data.txt")