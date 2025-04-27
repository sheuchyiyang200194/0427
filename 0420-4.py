#8 nike網站有無限滾動,先試抓
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# url ='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
#
# driver = webdriver.Chrome()
#
# driver.get(url)
#
# titles = driver.find_elements(By.CLASS_NAME,'product-card__link-overlay')
## titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')

# for title in titles:
#     print(title.text)

#9.抓取多頁_只有title
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'

driver = webdriver.Chrome()

driver.get(url)

n=0
while n<3:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1000)')
    time.sleep(3)
    n += 1

titles = driver.find_elements(By.CLASS_NAME,'product-card__link-overlay')
time.sleep(3)
for title in titles:
    print(title.text)