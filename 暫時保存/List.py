#List 串列 有順序可重複且可索引
# L1=[]
# print(L1)
# print(type(L1))
#
# L1=['apple','bana']
# print(L1)
#
# L1=['apple',123,True]
# print(L1)
# print(L1[2])
# L1=['apple',123,0.98,True,True,123,444]
# print(L1[1:4])

#for 迴圈  for data in
#for 循环：for data in L1: 的意思是遍历 L1 中的所有元素，并将每个元素依次赋值给 data 变量
#列表中的不同类型：列表 L1 中的元素类型是多样的，包括字符串、整数、浮动数、布尔值等。
# for 循环会依次处理这些不同类型的元素
# for data in L1:
#     print(data)

#len,count,index
# L1=['apple',123,0.98,True,True,123,444]
# print(len(L1))
# print(L1.count(123))
# print(L1.index(True))

#append,extend 都是列表的方法，用于向列表中添加元素
#append() 方法用于将一个元素添加到列表的末尾。这个元素可以是任何类型的对象，
# 包括数字、字符串、列表等。需要注意的是，append() 会将整个元素作为一个单独的元素添加到列表中
# ，而不是解开它。

#extend() 方法用于将一个可迭代对象（如列表、元组、字符串等）中的所有元素添加到列表末尾。
# 与 append() 不同，extend() 会将可迭代对象中的每个元素逐一添加到列表中，
# 而不是将整个可迭代对象作为单一元素添加
# L1=['apple',123,0.98,True,True,123,444]
# L1.append('python')                   #只能塞一個
# print(L1)

# L1.append(['python','pycharm'])      #改成列表方式放進去,但是看起來很奇怪
# print(L1)

# L1.extend(['python','pycharm'])        #能塞多個進去
# print(L1)

# L1.extend('python')        #變成單一字元被拆開
# print(L1)

# L1=['apple',123,0.98,True,True,123,444]
#
# L1.insert(2,"phthon")   #在某個位置加入
# print(L1)
#
# L1.remove(123)                         #移除第一個123的值
# print(L1)
#
# L1.pop(0)                              #刪除索引值,列表第幾個...
# print(L1)
#
# L1.clear()                             #全部清空
# print(L1)

#sort,reverse
# L2=[1,6,2,8,4]
# L2.sort() #遞增排序
# print(L2)
#
# L2.reverse() #反轉,但是沒有遞減
# print(L2)
#
# L3=[1,6,2,8,4]
# L3.reverse()
# print(L3)

#copy就只是單純拷貝,但是=就是完全一樣的東西,數值改變同時會連動
# c1=[1,2,3,4]
# c2=c1.copy()
# print(c2)
# c1[0]='A'
# print(c1)
# print(c2)
# c3=c1
# print(c3)
#
# c1=[1,2,[3,4]]
# c2=c1.copy()
# print(c2)
# #c1[0]='A'
# c1[2][0]='A'
# print(c1)
# print(c2)          #這時候,c2會受到c1改變影響,因為淺拷貝的關係
# c3=c1
# print(c3)

# import copy               #帶入copy函數
# c1=[1,2,[3,4]]
# c2=copy.deepcopy(c1)       #這個指令需要跟著改變
# print(c2)
# #c1[0]='A'
# c1[2][0]='A'
# print(c1)
# print(c2)          #用import copy這個指令,就可以讓c2不會因為c1改變而影響
# c3=c1
# print(c3)

