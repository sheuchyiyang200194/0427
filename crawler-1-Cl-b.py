##7.本文刪除處置,依序取出人氣標題日期作者
# import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index10553.html'
# request = req.Request(url,headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }) #請求頁面(url)同時送出header資訊,此為字典格式
# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
# import bs4
# root = bs4.BeautifulSoup(data, 'html.parser') #解析器
# titles=root.find_all('div',class_='title')  #抓到多筆title的資料,set容器,要用迴圈抓出來
# for title in titles:
#     if title.a is not None:      #可以解決本文已刪除的問題
#         print(title.a.string)
#     else:                        #加入本文已被刪除的說明
#         print('本文已被刪除')
# items=root.find_all('div',class_='r-ent')
# for item in items:
#                                                                 # print(item)   #先確認r-ent想抓的地方,都有抓下來
#     title=item.find('div',class_='title')
#                                                                 # print(title)  #先測試title是否有被抓下來
#     date=item.find('div', class_='date')
#     nrec=item.find('span', class_='hl')
#     print(f'{nrec.string} / {title.a.string} / {date.string}')

##8.用if else處理空值報錯
# import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index10556.html'
# request = req.Request(url,headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }) #請求頁面(url)同時送出header資訊,此為字典格式
# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
# import bs4
# root = bs4.BeautifulSoup(data, 'html.parser') #解析器
# items=root.find_all('div',class_='r-ent')
# for item in items:
#     title=item.find('div',class_='title')
#     date=item.find('div', class_='date')
#     nrec=item.find('span', class_='hl')
#     if nrec is None:      #用if else處理空值報錯
#         nrec='0'
#     else:
#         nrec=nrec.string
#     if title.a is None:
#         title="本文已刪除"
#     else:
#         title=title.a.string
#     print(f'{nrec:6} / {title:40} / {date.string:5}')



