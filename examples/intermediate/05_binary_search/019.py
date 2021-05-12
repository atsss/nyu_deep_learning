import bisect
d = int(input())
N = int(input())
M = int(input())
shop = [0]
home = []
for n in range(N-1):
    shop.append(int(input()))
for m in range(M):
    home.append(int(input()))
shop.sort()
shop.append(d)
ans = 0
for h in home:
    i = bisect.bisect(shop, h)
    ans += min(abs(shop[i-1]-h), abs(shop[i]-h))
print (ans)

# My answer
# 2021/04/24
# from bisect import bisect_left
#
# d = int(input())
# n = int(input())
# m = int(input())
# S = [0] + [int(input()) for _ in range(n-1)] + [d]
# K = [int(input()) for _ in range(m)]
#
# S.sort() # list の sort は nlog(n)
# ans = 0
#
# for k in K:
#     index = bisect_left(S, k)
#     ans += min(S[index]-k, k-S[index-1])
#
# print(ans)

# 2021/04/30
# from bisect import bisect_left
#
# d = int(input())
# n = int(input())
# m = int(input())
# shops = [int(input()) for _ in range(n-1)] # [0] 足すの忘れてる 
# destinations = [int(input()) for _ in range(m)]
#
# ans = 0
# shops.sort()
# shops.append(d)
#
# for des in destinations:
#     index = bisect_left(shops, des)
#     ans += min(abs(shops[index]-des), abs(des-shops[index-1]))
#
# print(ans)

# 2021/05/06
# from bisect import bisect_left
#
# d = int(input())
# n = int(input())
# m = int(input())
# stores = [int(input()) for _ in range(n-1)]
# homes = [int(input()) for _ in range(m)]
#
# stores = [0] + stores + [d]
# stores.sort()
# ans = 0
#
# for h in homes:
#     index = bisect_left(stores, h)
#     ans += min(stores[index]-h, h-stores[index-1])
#
# print(ans)
