from itertools import combinations
N, K = map(int, input().split())
A = list(map(int, input().split()))
mn = 10**18
for B in combinations(range(1,N),K-1): # 一番左は固定
    mx = A[0] # 初期値は一番左の建物
    score = 0
    for n in range(1,N):
        if n in B: # 見えるようにすべき建物なら
            if A[n] <= mx: # 低ければ高くする
                mx += 1
                score += (mx - A[n])
            else: # 高さが十分なら何もしない。最大値を更新
                mx = A[n]
        else:
            mx = max(mx, A[n]) # 見えなくても良い建物なら、最大値を更新
    mn = min(mn, score)
print (mn)

# My answer
# 2021/04/22
# from itertools import product
#
# N, K = map(int, input().split())
# A = tuple(map(int, input().split()))
#
# minumum = A[0]
# ans = float("INF")
#
# for c in product([0,1], repeat=N):
#     if c[0] == 0: continue
#     if sum(c) != K: continue
#
#     total = 0
#     for index, flag in enumerate(c[1:], 1):
#         if A[index] > minumum:
#             minumum = A[index]
#         else:
#             if flag:
#                 minumum += 1
#                 total += minumum - A[index]
#
#     ans = min(ans, total)
#
# print(ans)
