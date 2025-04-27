#0413-1 cookie避開抓不到資料
import urllib.request as req

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'Cookie': 'over18=1; cf_clearance=over18=1'
}#cf_clearance 是必要的, 會在一段時間後失效（幾小時到幾天不等），屆時你要重新複製

request = req.Request(url, headers=header)

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

print(data)