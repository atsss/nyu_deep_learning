import itertools
MOD = 10**5
N, M = map(int, input().split())
D = [0] # 先頭に0を入れておくと、累積和の差分計算の際に楽
for n in range(N-1):
    d = int(input())
    D.append(d)
C = []
for m in range(M):
    c = int(input())
    C.append(c)

csum = list(itertools.accumulate(D))
cur = 1
ans = 0
for c in C:
    next = cur + c # 移動
    ans += abs(csum[next-1]-csum[cur-1]) # 絶対値を足す
    cur = next # 次の移動開始地点
    ans %= MOD
print (ans)

# My answer
# 2021/04/28
# from itertools import accumulate
#
# n, m = map(int, input().split())
# S = [0] + [int(input()) for _ in range(n-1)]
# A = [int(input()) for _ in range(m)]
# mod = 10**5
#
# csum = list(accumulate(S))
# ans = 0
# hotel = 0
#
# for a in A:
#     ans += abs(csum[hotel+a] - csum[hotel])
#     hotel += a
#     ans %= mod
#
# print(ans)

# 2021/05/04
# from itertools import accumulate
#
# MOD = 10**5
# n, m = map(int, input().split())
# S = [int(input()) for _ in range(n-1)]
# A = [int(input()) for _ in range(m)]
#
# ac = list(accumulate([0]+S))
# ans = 0
# prev = 0
#
# for a in A:
#     ans += abs(ac[prev+a]-ac[prev])
#     prev += a
#
# print(ans%MOD)
