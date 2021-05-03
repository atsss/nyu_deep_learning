N, M = map(int, input().split())
C = list(map(int,input().split()))
INF = 10**10
dp = [[INF]*(N+1) for _ in range(M+1)]
dp[0][0] = 0 # 左上から始まるから dp[0][0] にすれば良い
for m in range(M):
    for n in range(N+1):
        if n-C[m]>=0:
            dp[m+1][n] = min(dp[m+1][n-C[m]]+1, dp[m][n])
        else:
            dp[m+1][n] = dp[m][n]
print (dp[M][N])

# 2021/05/02
# N, M = map(int, input().split())
# D = list(map(int, input().split()))
# default = float('inf')
#
# dp = [[default]*(N+1) for _ in range(M+1)]
#
# for m in range(M):
#     d = D[m]
#     for n in range(N+1):
#         if n - d >= 0:
#             tmp = 0 if dp[m+1][n-d] == default else dp[m+1][n-d]
#             dp[m+1][n] = min(dp[m][n], tmp+1)
#         else:
#             dp[m+1][n] = dp[m][n]
#
# print(dp[M][N])
