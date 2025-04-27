#10 除了title之外,把其他東西也先一起抓下來
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'

driver = webdriver.Chrome()

driver.get(url)

# n = 0
# while n < 3:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1000)')
#     time.sleep(3)
#     n += 1

# product-card__info product-card__title product-card__price

info = driver.find_elements(By.CLASS_NAME,'product-card__info')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')


time.sleep(3)

# for title in titles:
#     print(title.text)

for item in info:
    print(item.text)