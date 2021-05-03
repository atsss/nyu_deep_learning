N = int(input())
n = N
ans = []
for i in range(2,int(N**0.5)+1): # intに変換すること
    while(n%i==0):
        n //= i #  整数除算(//)を使うこと
        ans.append(i)
if n!=1:
    ans.append(n)
ans = [str(a) for a in ans]
ans = str(N)+": " + " ".join(ans)
print (ans)

# My answer
# 2021/04/26
# 写経
# N = int(input())
# n = N
# ans = []
#
# for i in range(2, int(N**0.5)+1):
#     while n%i==0:
#         n //= i
#         ans.append(i)
#
# if n != 1: ans.append(n)
#
# print(str(N)+': '+' '.join(map(str, ans)))

# 2021/05/02
# n = int(input())
# N = n
#
# ans = []
# for i in range(2, int(N**0.5)+1):
#     while n % i == 0:
#         n //= i
#         ans.append(i)
#
# if n != 1: ans.append(n)
#
# print(str(N) + ': ' + ' '.join(map(str, ans)))
