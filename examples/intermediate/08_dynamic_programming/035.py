N, W = map(int, input().split())
vw = []
for n in range(N):
    v, w = map(int,input().split())
    vw.append((v,w))
dp = [[0]*(W+1) for _ in range(N+1)]
for n in range(N):
    vn ,wn = vw[n]
    for w in range(W+1):
        if w-wn >= 0:
            dp[n+1][w] = max(dp[n][w-wn] + vn, dp[n][w])
        else:
            dp[n+1][w] = dp[n][w]
print (dp[N][W])

# My answer
# 2021/04/25
# 表の見方が分かった -> https://www.momoyama-usagi.com/entry/info/algo/dp
# N, W = map(int, input().split())
# items = []
# for _ in range(N):
#     v, w = map(int, input().split())
#     items.append((v, w))
#
# dp = [[0]*(W+1) for _ in range(N+1)]
#
# for i in range(N):
#     v, w = items[i]
#     for j in range(W+1):
#         if j-w >= 0:
#             dp[i+1][j] = max(dp[i][j-w] + v, dp[i][j])
#         else:
#             dp[i+1][j] = dp[i][j]
#
# print(dp[N][W])

# 2021/05/02
# N, W = map(int, input().split())
# items = [tuple(map(int, input().split())) for _ in range(N)]
#
# dp = [[0]*(W+1) for _ in range(N+1)]
#
# for i in range(N):
#     v, w = items[i]
#     for j in range(W+1):
#         if j - w >= 0:
#             dp[i+1][j] = max(dp[i][j], dp[i][j-w]+v)
#         else:
#             dp[i+1][j] = dp[i][j]
#
# print(dp[N][W])

# 2021/06/11
# N, W = map(int, input().split())
# items = [tuple(map(int, input().split())) for _ in range(N)]
#
# dp = [[0] * (W+1) for _ in range(N+1)]
#
# for i in range(N):
#     for w in range(W+1):
#         nv, nw = items[i]
#         if w >= nw:
#             dp[i+1][w] = max(dp[i][w], dp[i][w-nw] + nv)
#         else:
#             dp[i+1][w] = dp[i][w]
#
# print(dp[-1][-1])
