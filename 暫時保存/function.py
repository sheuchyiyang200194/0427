# def foo():
#     print('function')
# foo()  #foo() 是呼叫這個函式
#
# def area(w,h):
#     print(w*h)
# area(10,23)
from tkinter.font import names


#print()只是顯示在畫面上給人看，無法存變數
#return把結果傳回給呼叫者，可以存變數、再運算
# def area(w,h):
#     return w*h  # 回傳 w 和 h 相乘的結果(不能用print)
# result=area(10,23) # 呼叫函式，將結果存到 result 變數中
# print(f'面積是{result}平方公分')

#default arguments（預設參數）,預設參數要放在後面
# def aaa(dollar,rate=0.25):
#     return dollar*rate
# print(aaa(10000))

#設計倒數計時器
# s=int(input('請輸入秒數'))
# import time
# def count(second):
#     for x in range(second,0,-1):  #加上 -1 表示倒數
#         print(x)
#         time.sleep(1)
#     print("時間到！")
# count(s)

# def greeting(first,last):
#     print(f'hello,{first}   {last}')
# # greeting(first='mar',last='aaa')
# greeting('mar','mary')

# def foo(*args):  #「*不定數量參數」的用法，讓函式可以接收任意多個參數
#     #print(args)
#     for item in args:
#         print(item,end='') #不換行印出每個項目
# foo('1','3','aaa',5,555)

#**kwargs = 關鍵字參數（keyword arguments）
#它會把傳入的 key=value 參數打包成一個 字典（dict）
# def foo2(**kwargs):
#     #print(kwargs)
#     for item in kwargs.items(): ## item 是一個 tuple，例如 ('name', 'tim')
#         print(item,end=',')   #印出每一對 key-value，用逗號隔開
# foo2(name='tim',mail='sheu@gmai.com')

#
# def foo3(x,y,*args,**kwargs):
#     print(x,y,*args,**kwargs)
# foo3(1,2,222,222,name="Alice")




