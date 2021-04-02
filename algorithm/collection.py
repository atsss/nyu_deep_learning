from collections import Counter
a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
a=Counter(a)
for i in a.most_common(3):print(i)
