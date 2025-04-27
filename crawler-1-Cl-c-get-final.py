##9.抓取多頁資料_函式_定義首頁定義次數
import urllib.request as req #負責送出 HTTP 請求，抓網站資料（內建模組）
import ssl

def getData(url):

    request = req.Request(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }) #請求頁面(url)同時送出header資訊,此為字典格式
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    import bs4
    root = bs4.BeautifulSoup(data, 'html.parser') #解析器
    items=root.find_all('div',class_='r-ent')
    for item in items:
        title=item.find('div',class_='title')
        date=item.find('div', class_='date')
        nrec=item.find('span', class_='hl')
        if nrec is None:      #用if else處理空值報錯
            nrec='0'
        else:
            nrec=nrec.string
        if title.a is None:
            title="本文已刪除"
        else:
            title=title.a.string
        print(f'{nrec:6} / {title:40} / {date.string:5}')
    nextPage=root.find('a',string='‹ 上頁')
    return nextPage['href']

pageURL='https://www.ptt.cc/bbs/movie/index10546.html'
count=0
while count<5:
    pageURL='https://www.ptt.cc'+getData(pageURL)
    count +=1
