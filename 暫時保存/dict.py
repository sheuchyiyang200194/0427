#dict 是 鍵值對（key-value） 的資料結構，就像一本字典一樣：
#key（鍵）：唯一、不可重複（通常是字串或數字）
#value（值）：可以是任何資料型別（數字、字串、清單、甚至是另一個字典）
# s1 = [{
#     "name": "Alice",
#     "age": 18,
#     "grade": "A"
# },{"name": "BBB",
#     "age": 20,
#     "grade": "B"}
# ]
# print(s1)
# print(s1[0]) #取出第一個list
# print(s1[0]["name"]) #取出第一個list裡面,第一個dict的值

# s1 = {
#     "name": "Alice",
#     "age": 18,
#     "grade": "A"}
# print(s1.get("name"))  #讀取:如果 key 不存在會回傳 None
# print (s1["name"])     #讀取:如果 key 不存在會報錯 KeyError
# s1['skill']='aaa'      #新增:強制設定（新增或覆蓋）,覆蓋舊值
# print (s1)
# s1.setdefault('skil','bbb')  #新增：如果 key 不存在就新增，有的話保持原樣
# print (s1)
# s1 = {
#     "name": "Alice",
#     "age": 18,
#     "grade": "A"}
# print (s1.keys())
# print (s1.values())
# print (s1.items())

# for key, value in s1.items():   #重要:回傳所有 (key, value) 組合
#     print(value)
#     print(key,value)
#     print(f'{key},   {value}')

#兩層呼叫,由外而內
# s1 = [{
#     "name": "Alice",
#     "age": 18,
#     "grade": "A"
# },{"name": "BBB",
#     "age": 20,
#     "grade": "B"}
# ]
# for data in s1:
#     for k,v in data.items():
#         print(k,v)
# for data in s1:  # Python 的 for 迴圈語法，用來逐一取出 s1 裡面的每個元素
    #從 s1 這個清單中，一個一個取出元素，每次把目前的那個元素放進變數 data
    # for k,v in data.items():  #兩次迴圈取值
    # 注意:data.items它是 Python 字典 (dict) 的一個方法，用來取出所有的鍵值對（key-value pairs）
        # print(k,v)
        # print(f'{k:10},{v}')   #加入對齊排列
    # print('------------------') #放在外層,將每一筆資料間隔開
#多筆字典結合
s1={
    "name": "Alice",
    "age": 18,
    "grade": "A"}
s2={"name": "BBB",
    "age": 20,
    "grade": "B"}   #s2 的 key 會覆蓋 s1 的同名 key
# s2={"Hi": "kkk"}
users={**s1,**s2}   #注意:結合的語法
print(users)        #{'name': 'Alice', 'age': 18, 'grade': 'A', 'Hi': 'kkk'}














