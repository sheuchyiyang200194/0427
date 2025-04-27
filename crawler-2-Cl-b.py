#模組request可以簡化語法,但結果一樣
import requests
import bs4
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

data=requests.get(url,headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'Cookie': 'over18=1; cf_clearance=BjXJNLXF5geWxuWzqa5zf.qCqkmmIbJzZwrWAQuPZI4-1744511918-1.2.1.1-Vp7fwR8R2Jrs9BVbTTD_vsOup7CjunQ5lMIumquML3MziGRmjJS9cNjzecYNmvLuGGQgxim3TaASf3YL4WcmEl8Iq5X2njFgidbf3.z7qL2Kkfoxl4PzMkIc5ZkoPbQB9wcieeT6ytZ6gmBQRhwn8XPgjvG.aUboJFgSToFiwxZ3kM6PRauZx4dsOTDjRrI2UJVLPvSj3pKx9o2tQohZe.Ce2nhRY3V9jJjnp6zNdIMjO8chIvZK9k_V2.P_UKunL72Hbt8xRAFrRh9nD_9O97Su2QdbEYRl8a__X250_Qu4IfN.oQIzKU4HpBex3cIVeJmKcVtC6ZnFqEMa352O.T6MSqm.1V74JpQNRfi4mUE'
})
data=data.text

htmlfile=bs4.BeautifulSoup(data,'html.parser')
titles=htmlfile.find_all('div',class_='title')
for title in titles:
    if title.a is None:
        print("本文已刪除")
    else:
        print(title.a.string)
