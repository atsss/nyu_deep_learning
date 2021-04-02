from itertools import permutations, combinations,combinations_with_replacement,product
a=['a','b','C']
print(list(permutations(a)))
print(list(combinations(a,2)))
print(list(combinations_with_replacement(a,3)))

a=list(product(['+','-'],repeat=3))
print(a)
s=['5', '5', '3', '4']
for i in a:
    ans=s[0]+i[0]+s[1]+i[1]+s[2]+i[2]+s[3]
    if eval(ans)==7:
        print(ans+'=7')
        break
