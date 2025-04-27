#2 抓出nike的網頁裡的圖片
from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

url = 'https://www.nike.com/tw/'

driver = webdriver.Chrome()

driver.get(url)
htmlfile = driver.page_source

soup = BeautifulSoup(htmlfile, 'html.parser')

imgs = soup.find_all('img')

# imgs = driver.find_elements(By.TAG_NAME, 'img')
# data-landscape-url
print(imgs)
i = 1
for img in imgs:
    # print(img['data-landscape-url'])
    path = img['data-landscape-url']
    name = img['alt']
    source = requests.get(path)
    img_source = source.content
    os.makedirs('images', exist_ok=True)

    with open(f'images/{name}-{i}.jpg', 'wb') as f:
        f.write(img_source)

    i += 1