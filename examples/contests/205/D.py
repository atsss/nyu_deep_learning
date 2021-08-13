# from collections import Counter
#
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# K = [int(input()) for _ in range(Q)]
#
# st = set(K)
# col = Counter(A)
# col_index = 1
# k_index = 0
# length = 0
# ans = {}
#
# while True:
#     if col[col_index] == 0:
#         k_index += 1
#
#         if k_index in st:
#             length += 1
#             ans[k_index] = col_index
#
#         if length == Q:
#             break
#
#     col_index += 1
#
# for k in K: print(ans[k])

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# K = [int(input()) for _ in range(Q)]
#
# arr = []
# A.sort()
# prev = 0
# for current in A:
#     arr += list(range(prev+1, current))
#     prev = current
#
# length = len(arr)
# ans = {}
# for k in K:
#     if k > length:
#         ans[k] = A[-1] + (k - length)
#     else:
#         ans[k] = arr[k-1]
#
# for k in K: print(ans[k])

import bisect

n, q = map(int, input().split())
arr = list(map(int, input().split()))
dp = []
dp.append(arr[0] - 1)
for i in range(1, n):
    dp.append(dp[-1] + arr[i] - arr[i - 1] - 1)
dp.append(float("inf"))
for _ in range(q):
    cq = int(input())
    k = bisect.bisect_left(dp, cq)
    if k == 0:
        print(cq)
    else:
        print(arr[k - 1] + cq - dp[k - 1])
