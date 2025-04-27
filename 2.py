#1 10:10 抓取圖片的方式
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

print(imgs)