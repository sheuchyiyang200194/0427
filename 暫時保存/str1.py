# name="john"
# print(f'我的名字是{name}')
#
# a='hello%s' %'world'#s為string字串
# b='hello%d' %23 #d為10進位整數
# c='hello%f' %3.1415  #f為浮點數
# d='hello%s' %bin(3)# 使用 bin() 函数将整数转换为二进制字符串
# e='hello%x' %18  # 将整数转换为十六進位
# f='hello%o' %18  # 将整数转换为八進位
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
#
# a='hello%10s' %'world'#s為string字串,從左邊算起空10格
# print(a)
# a='hello%+10s' %'world'#s為string字串
# print(a)
# a='hello%-10s' %'world'#s為string字串,從右邊算起空10格
# print(a)
#
# c='hello%f' %3.1415926  #f為浮點數（四舍五入后显示6位小数）
# print(c)
# c='hello%.3f' %3.1415926  #f為浮點數,取道小數點3位（四舍五入后显示3位小数）。
# print(c)
# c='hello%10.3f' %3.1415926  #f為浮點數,從左邊算起10位並且小數點取3位
# print(c)

#新的字串用法
# a='john'
# b=13
# msg=(f'hello {a},今天氣溫{b}度')
# print(msg)

#舊的字串用法
# msg='hello %s 天氣氣溫為%.1f度'
# print(msg%('max',13))

#format()
# msg='hello{:^12s}'
# print(msg.format('John'))
#
# msg='hello{:-^20s}'
# print(msg.format('John'))
#
# msg='hello {},今天氣溫{}度'
# print(msg.format('John',10.3))
#重要
# msg='hello {name:^12s},今天氣溫{temp:.1f}度' #.1f表示浮點數取小數1位
# print(msg.format(name='John',temp=10.333))

#f-string
# name='john'
# temp=13
# print(f'hello{name},今天氣溫{temp}度')
#
# name='john'
# temp=13.333
# print(f'hello{name:^10s},今天氣溫{temp:10.2f}度')
#
# a='hello "john"'
# print(a)
# a='hello \'john\''
# print(a)
# a='hello john \nhellotom'  #\n是換行
# print(a)
# a='hello john\n\thello tom'  #\t是對齊
# print(a)
#
# a='F:\test'
# print(a)
#
# a=r'F:\test'   #前面加入r作為顯示原生字串,避免系統誤判為跳脫字元
# print(a)

#字串索引值
# s='2025-03-16'
# print('年',s[:4])
# print(s[5:7])
# print(s[-2:])
# print(s[-3])
# print(s[0:9])
# print(s[0:9:2])
# #语法是 s[start:end:step]，表示从索引 start 开始，到索引 end 之前结束，步长为 step。
s='hello'
#字串
print(len(s))        #字串裡面有幾個數字
print(s.count("o"))  #變數裡面有幾個o
print(s.index('e'))  #索引值在什麼位置

#判斷式
# print(s.isdigit())     #判斷字串內是否皆為數字
# print(s.isalpha())     #判斷字串內是否皆為英文
# print(s.endswith('w'))  #判斷結尾是否為定義的字
# print(s.startswith('h')) #判斷開頭是否為定義的字

#文字
# s='heLLo worLD'
# print(s.upper())      #全部大寫
# print(s.lower())      #全部小寫
# print(s.capitalize()) #第一個單字大寫,其餘小寫
# print(s.title())      #每個單字的第一個大小,其餘小寫
# print(s.find('L'))    #找出單字內有L的位置,與index相似
# print(s.replace('heLLo','Hello')) #取代變數裡某個特定字

#split()
# s2='hello world'
# print(s2.split()) #空格去拆
# q=s2.split()
# print(type(q))
# print(s2.split('o')) #o去拆
# print(s2.split())

#strip()
# s='  hello   dd '
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())



