MOD = 10**9+7
m, n = map(int, input().split())
# print (pow(m,n)%MOD) 遅い
print (pow(m,n,MOD))

# My answer
# 2021/04/26
# m, n = map(int, input().split())
# mod = 10**9 + 7
# print(pow(m, n, mod))

# 2021/05/02
# m, n = map(int, input().split())
# mod = 10**9 + 7
#
# print(pow(m, n, mod))
