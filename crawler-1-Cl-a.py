##1&2.初步確認網頁是否可以抓取資料->如果被擋->看下面的解決方式
# import urllib.request as req #是Python內建的模組，用來發送HTTP請求、抓取網頁資料
# url = 'https://www.momoshop.com.tw/main/Main.jsp'
#
# with req.urlopen(url) as response:
#     data = response.read()
#
# print(data)


##3.utf-8轉成看得懂的格式->模擬成人類進入網頁不要被擋住user-agent
   ##ps:通常只要放user-regent的request就可以,如果還是被擋,就要全放'要求標頭'
# import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index.html'
# request = req.Request(url,headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }) #請求頁面(url)同時送出header資訊,此為字典格式
# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
#
# print(data)

##4.BeautifulSoup解析資料
# import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index.html'
# request = req.Request(url,headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }) #請求頁面(url)同時送出header資訊,此為字典格式
# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
# print(data)
#
# import bs4
# root = bs4.BeautifulSoup(data, 'html.parser') #解析器
# print(root)

##5.網頁_元素_title和a和class
# import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index.html'
# request = req.Request(url,headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }) #請求頁面(url)同時送出header資訊,此為字典格式
# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
# # print(data)
#
# import bs4
# root = bs4.BeautifulSoup(data, 'html.parser') #解析器
#print(root) #顯示全部
#print(root.title.string) #找網頁元素裡面的title
#print(root.a.string) #找網頁元素裡面的<a





##6.抓多筆資料,用迴圈繞出來
import urllib.request as req
url = 'https://www.ptt.cc/bbs/movie/index.html'
request = req.Request(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }) #請求頁面(url)同時送出header資訊,此為字典格式
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data)

import bs4
root = bs4.BeautifulSoup(data, 'html.parser') #解析器
#print(root) #顯示全部
#print(root.title.string) #找網頁元素裡面的title
#print(root.a.string) #找網頁元素裡面的<a

# test=root.find('a',class_='right') #依特徵找到,只有一筆
# print(test)
# test=root.find('div',class_='title')  #抓到一筆title的資料
# print(test)
# title=root.find_all('div',class_='title')  #抓到多筆title的資料
# print(title)
#重要,常用的
# titles=root.find_all('div',class_='title')  #抓到多筆title的資料,set容器,要用迴圈抓出來
# dates=root.find_all('div',class_='date')
# triggers=root.find_all('div',class_='trigger')
#
# for title in titles:
#     print(title.a.string)
# for date in dates:
#     print(date.string)
# for trigger in triggers:
#     print(trigger.string)
















