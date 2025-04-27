#數學運算
# x=3.3
# print(round(x)) #四捨五入
# x=3.6
# print(round(x))
# x=-34
# print(abs(x))   #絕對值
# print(max(2,3,13)) #取最大值

#import math  #引入模組
import math
# x=3.3
# y=2
# z=225
# print(math.floor(x))  #無條件捨去
# print(math.ceil(x))  #無條件進入
# print(pow(y,5))    #次方
# print(pow(5,5))
# print(math.sqrt(z))  #開根號
# print(math.e)
# print(math.pi)

#運算子
#數學 + -  *  /  %餘數
# a=10
# b=6
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a+b)
# print(a)
# a=a+b
# print(a)

#比較 ==比較兩邊是否相等
a=10
b=6
v=0
# print(a>0)
# print(a==0)
# print(a<=0)
#邏輯
# print(a>0 and b>0)
# print(a<0 and b>0)
# print(not a)
# print(not v)

#確認空值的用法
# a=None
# print(not a)
# b=0
# print(not b)
# c=""
# print(not c)
# print(not v)

#圓周 2*pi*r
# r=float(input('請輸入半徑'))
# result=2*math.pi*r
# print('圓周長為',result)

#面積 pi*r*r
r=float(input('請輸入半徑'))
result=math.pi*r*r
print('面積為',result)
result2=math.pi*pow(r,3)
print('面積為',result2)



