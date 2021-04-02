w=[[4, 5], [1, 2] , [3, 6], [2, 6], [5, 7]]
print(w)

w.sort()
print(w)

w.sort(key=lambda x:x[1],reverse=True)  #二個目の要素で降順並び替え
print(w)

