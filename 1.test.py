from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

# 目標網站首頁
base_url = 'https://www.horizonfuelcell.com/'

# 啟動瀏覽器
driver = webdriver.Chrome()
driver.get(base_url)

# 等待首頁載入
time.sleep(3)

# 抓首頁 HTML
htmlfile = driver.page_source
soup = BeautifulSoup(htmlfile, 'html.parser')

# 找所有超連結
links = soup.find_all('a', href=True)

# 過濾出 Horizon 網站內部連結
page_urls = set()
for link in links:
    href = link['href']
    if href.startswith('/'):
        full_url = urllib.parse.urljoin(base_url, href)
        page_urls.add(full_url)
    elif href.startswith(base_url):
        page_urls.add(href)

# 把首頁自己也加入（因為首頁也有圖片）
page_urls.add(base_url)

print(f'🔍 共找到 {len(page_urls)} 個子頁面！')

# 準備總存圖資料夾
save_folder = 'horizon_all_images'
os.makedirs(save_folder, exist_ok=True)

# 開始逐頁抓取圖片
page_count = 1
for page_url in page_urls:
    print(f'📄 正在處理第 {page_count} 頁：{page_url}')
    driver.get(page_url)
    time.sleep(2)

    page_html = driver.page_source
    page_soup = BeautifulSoup(page_html, 'html.parser')

    imgs = page_soup.find_all('img')

    # 以子頁面資料夾分類
    parsed_url = urllib.parse.urlparse(page_url)
    folder_name = parsed_url.path.strip('/').replace('/', '_') or 'homepage'
    page_folder = os.path.join(save_folder, folder_name)
    os.makedirs(page_folder, exist_ok=True)

    i = 1
    for img in imgs:
        path = img.get('src')
        if path is None:
            continue

        # 處理相對路徑
        full_img_url = urllib.parse.urljoin(page_url, path)

        # 確認是http開頭
        if not full_img_url.startswith('http'):
            continue

        # 取 alt 名稱
        name = img.get('alt', f'image_{i}')

        # 過濾非法字元
        safe_name = "".join(c if c.isalnum() else "_" for c in name)

        # 自動判斷副檔名
        ext = os.path.splitext(full_img_url)[-1]
        if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            ext = '.jpg'  # 如果不確定，預設成 jpg

        try:
            response = requests.get(full_img_url)
            img_source = response.content

            img_filename = os.path.join(page_folder, f'{safe_name}-{i}{ext}')
            with open(img_filename, 'wb') as f:
                f.write(img_source)

            print(f'✅ 已下載: {img_filename}')
            i += 1
        except Exception as e:
            print(f'❌ 下載失敗: {e}')

    page_count += 1

driver.quit()
print('🚀 全網站圖片抓取完成！')

#1532test上傳