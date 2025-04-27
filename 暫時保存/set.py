#set 重點用在去掉重複的地方
#s={}
# s1={1,1,1,2,2,2,3,3,3,3,}
# city=set(s1)  #轉set去掉重複
# print(city)
# city=list(city)
# print(city)    #轉列表方便處理
# city.append(5)
# print(city)

#集合其他用法
# s1={1,1,1,2,2,2,3,3,3,3,}
# s1.add(5)           #新增5這個數字
# print(s1)           #{1, 2, 3, 5}
# print(s1.add(5))    #None add() 是「就地修改」的方法，不會有回傳值，只回傳 None

# s1.remove(5) #移除,且報錯
# print(s1)
# s1.discard(5) #移除,但不報錯
# print(s1)
# s1.pop() #隨機移除

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# result=s1.intersection(s2) #交集（兩集合都有的）
# print(result)
# result=s1.union(s2) #聯集（兩集合所有元素，去除重複）
# print(result)
# result=s1.difference(s2) #差集（s1 有但 s2 沒有的）
# print(result)
# result=s1.symmetric_difference(s2)
# print(result) #對稱差集（兩集合不重疊的元素）







