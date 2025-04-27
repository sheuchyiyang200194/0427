# import urllib.request as req
# url='https://tw.yahoo.com/'
# with req.urlopen(url)as response:
#     data=response.read()
# print(data)

#對 PTT 首頁 發送請求/模擬了瀏覽器（加了 User-Agent）
#拿到原始 HTML 資料並解碼/用 BeautifulSoup 做了解析
import urllib.request as req
url = 'https://www.ptt.cc/bbs/AnimMovie/index.html'# 要爬的網址
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}# 設定 headers，模擬瀏覽器
request = req.Request(url, headers=headers)# 建立 Request 物件（加入 headers）
# 發送請求
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data)
import bs4
#html.parser 是 Python 內建的 HTML 解析器，不需要安裝，是 BeautifulSoup 預設使用的解析方式
root=bs4.BeautifulSoup(data,'html.parser') #用 BeautifulSoup 解析 HTML
# print(root)
# print(root.title.string)
# print(root.a.string)
items=root.find_all('div',class_='r-ent')
for item in items:
    title_tag = item.find('div', class_='title')
print(f'{title}')





