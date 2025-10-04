import json
import time
from cookies_manager import CookieManager

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
#
driver = webdriver.Chrome(options=options)
driver.get("https://www.freeconferencecall.com/ru/ru/login")

# driver.delete_all_cookies()
#
# with open("cookies.json", "r") as file:
#     cookies = json.load(file)
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.refresh()
#
# time.sleep(10)



cookies_manager = CookieManager(driver)
cookies_manager.load()
time.sleep(10)

