#stament 判斷式
#一個判斷式
# x=10
# if x>0:
#     print('X是正數')
#二個判斷式
# x=-5
# if x>0:
#     print('X是正數')
# else:
#     print('X是負數')

#二個條件三個動作ˋ
# x=0
# if x>0:
#     print('X是正數')
# elif x<0:
#     print('x是負數')
# else:
#     print('X=0')

#匯率換算
m=input('日幣轉台幣請輸入1,台幣轉日幣請輸入2')
exc=0.22
if m=='1':
    d=float(input('請輸入日幣金額: '))
    result=d*exc
    result=round(result,0)
    print(f'日幣{d}約為{result}台幣')
else:
    d=float(input('請輸入台幣金額: '))
    result=d/exc
    result=round(result,0)
    print(f'台幣{d}約為{result}日幣')



