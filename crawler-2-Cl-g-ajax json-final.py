#11.json轉成excel檔
import requests
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

title = ['行程名稱','顯示價格','真正的價格']
ws.append(title)

for i in range(3):
    url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866&page='
    url = url + str(i+1)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    datas = requests.get(url, headers=header, verify=False)

    datas = datas.json()

    # with open('kkday_txt.txt','a',encoding='utf-8') as file:
    #     for data in datas['data']:
    #         file.write(f'{data['name']}:{data['price']}\n')
    for data in datas['data']:
        # item = []
        # item.append(data['name'])
        # item.append(data['price'])
        item = [data['name'],data['display_price'],data['display_sale_price']]

        ws.append(item)
    wb.save('qq.xlsx')