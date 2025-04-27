#9.抓取多筆資料json並轉成txt檔,用request
import requests

for i in range(10):
    url =('https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency='
          'TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat'
          '=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_'
          '028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score'
          '_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure='
          '&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866&page=')
    url = url + str(i+1)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    datas = requests.get(url, headers=header, verify=False)
#使用了 requests.get(..., verify=False) 來跳過 HTTPS 憑證驗證，這在安全性上是不推薦的，因為：
#無法確認你連的是不是正確的伺服器,可能有中間人攻擊（MITM）的風險
    datas = datas.json()

    with open('kkday_txt.txt','a',encoding='utf-8') as file:
        for data in datas['data']:
            file.write(f'{data['name']}:{data['price']}\n')





# 10.用urllib寫並做成換頁形式
# import urllib.request as req
# import ssl
# import json
# ssl._create_default_https_context = ssl._create_unverified_context
#
# for i in range(3):
#
#     url =f'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page={str(i+1)}&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#     }
#
#     request = req.Request(url, headers=header)
#
#     with req.urlopen(request) as response:
#         result = response.read().decode('utf-8')
#
#     data_json = json.loads(result)
#
#     with open('practice.txt','a',encoding='utf-8')as file:
#         file.write(f'---------第{i+1}頁---------\n')
#         for d in data_json['data']:
#             # print(d['name'])
#             file.write(f'{d['name']}:{d['price']}\n')
#         file.write('--------------------------------\n')











