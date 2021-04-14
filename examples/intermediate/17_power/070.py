MOD = 10**9+7
m, n = map(int, input().split())
# print (pow(m,n)%MOD) 遅い
print (pow(m,n,MOD))
