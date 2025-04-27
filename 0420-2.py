#4.首次用chromedriver搭配selenium開啟頁面
# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# # driver.get('https://www.google.com')
# driver.get('https://mail.google.com/mail/u/0/#inbox')
# time.sleep(10)

#5.模擬人類在google輸入關鍵字搜尋(但容易被擋)
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys  #需引入這一個
#
# driver=webdriver.Chrome()
# driver.get('https://www.google.com')
# time.sleep(3)
# search=driver.find_element(By.CLASS_NAME,'gLFyf')
# time.sleep(2)
# search.send_keys('午')
# time.sleep(1)
# search.send_keys('餐')
# time.sleep(2)
# search.send_keys(Keys.ENTER)
# time.sleep(20)

#6.天瓏撈資料(有點慢但可以撈到了)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url='https://www.tenlong.com.tw/'
time.sleep(3)
driver.get(url)
time.sleep(3)
titles=driver.find_elements(By.CLASS_NAME,'title')
for title in titles:
    print(title.text)
