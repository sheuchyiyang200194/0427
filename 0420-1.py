#1撈取政府開放平台資料,先找有json資料的網址,確認執行後是否有顯示200代表有撈取到
import requests
url='https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate%20desc&format=JSON'
results = requests.get(url, verify=False)
print(results)

#2.從json裡面撈取要的資料呈現出來
import requests
# import ssl

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'  #撈Ubike資料
# url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate%20desc&format=JSON'
# ssl._create_default_https_context = ssl._create_unverified_context
results = requests.get(url,verify=False)
results = results.json()

# for result in results['records']:     #撈空氣品質
#     print(f'{result['sitename']}:AQI {result['aqi']}')

for result in results:                  #撈Ubike資料
    print(f'{result['sna']}:可租借車輛{result['available_rent_bikes']}')
# print(results)