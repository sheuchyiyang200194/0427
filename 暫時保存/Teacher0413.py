# request方法
# import requests
#
# url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#
# }
#
# datas = requests.get(url, headers=header, verify=False)
#
# # datas = datas.text
# datas = datas.json()

# print(datas)

## urllib 方法

import urllib.request as req
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

request = req.Request(url, headers=header)

with req.urlopen(request) as response:
    result = response.read().decode('utf-8')

data_json = json.loads(result)
print(data_json)