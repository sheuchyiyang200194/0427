#tuple tuple 是不可變的（immutable），一旦建立後，內容就不能更改
#元素有固定順序，可用索引取值,元素可以重複出現
#同時可以包含整數、字串、清單等不同資料型態
# t1=tuple()
# t2=(1,2,3,4,5)
# print(t2)
# print(t2[1])    #調用索引值

t4=True,"helli",123,0.2
t5=("hi")         #要在後面加逗號,t5 = ("hi") 實際上是個字串
                  #等同於 t5 = "hi"。要讓它成為一個只有一個元素的 tuple，必須加逗號
t6=t4+t5
print(t6)

# t4=list(t4)               #先用列表新增,再轉回tuple
# t4.append('hi')
# t4=tuple(t4)
# print(t4)
