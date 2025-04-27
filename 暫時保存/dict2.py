#小程式
menu={'apple':10,'bana':100,'kiwi':60}
cart=[]
total=0
# print('-----Menu-----')
# for k,v in menu.items():
#     print(f'{k:8}:{v}')
# print('---------------')
while True: #建立一個「無限迴圈」
    selected=input('請輸入品項(按q完成輸入)').lower() #加入lower指令,避免輸入大寫不會停止
    if selected=='q':
        break
    # elif menu.get(selected)is not None:
    elif selected in menu:  #更簡潔的寫法
        cart.append(selected)
    print(cart)
print('訂單內容')
for p in cart:
    print(p,end='\n')
    total=total+menu.get(p)
print(f'您共花費${total}元')

#小程式
# menu = [
#     {'id': 1,'name': '1.滷肉飯','price': 50,},
#     {'id': 2,'name': '2.牛肉麵','price': 120,},
#     {'id': 3,'name': '3.貢丸湯','price': 40,}]
# cart=[]
# total=0
# print('-----Menu-----')
# for item in menu:
#     print(item['name'],item['price'])
# print('---------------')
# while True:
#     selected=input('請輸入品項數字(按q完成輸入)').lower() #加入lower指令,避免輸入大寫不會停止
#     if selected=='q':
#         break
#     elif int(selected)>len(menu):
#         continue
#     elif menu[int(selected)-1] in menu:
#         cart.append(menu[int(selected)-1])
#     print(cart)
# for item in cart:
#     print(f'{item['name']}')
#     total+=item['price']
# print(total)


