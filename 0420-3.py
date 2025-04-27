#7.利用 CSS 選擇器 .keywords-list a 找出「熱門關鍵字連結」的 <a> 標籤
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.tenlong.com.tw/'
time.sleep(3)
driver.get(url)

titles = driver.find_elements(By.CSS_SELECTOR, '.keywords-list a')
# print(titles.text)
for title in titles:
    print(title.text)

# kw = driver.find_element(By.ID,'keyword')
# kw.send_keys('PYTHON')

# CLASS_NAME
# TAG_NAME
# ID

time.sleep(5)