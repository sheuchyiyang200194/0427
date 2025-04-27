#8.將json轉成文字檔txt
import requests
#這是 KKday 顯示商品用的「AJAX API 路徑」，你透過這個網址就能拿到商品的資料（通常是 JSON 格式）。
url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
} #設定請求標頭（headers）

datas = requests.get(url, headers=header, verify=False) #發送GET請求，取得資料

# datas = datas.text
datas = datas.json()

# with open('kkday.json','w',encoding='utf-8') as file:
#     file.write(datas)
with open('kkday_txt.txt','w',encoding='utf-8') as file: #開啟 kkday_txt.txt 檔案
    for data in datas['data']:                           #逐筆讀取商品清單
        file.write(f"{data['name']}:{data['price']}\n")  #將文字寫入檔案，每筆一行

