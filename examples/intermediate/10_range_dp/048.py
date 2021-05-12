ans = []
while(1):
    N = int(input())
    if N==0:
        break
    W = list(map(int,input().split()))
    dp = [[0]*N for _ in range(N)]
    for d in range(1,N):
        for i in range(N-d):
            j = i+d
            if d%2==1:
                if dp[i+1][j-1]==d-1:
                    if abs(W[i] - W[j])<=1:
                        dp[i][j] = d+1
                    else:
                        dp[i][j] = d-1
                for k in range(i+1,j):
                    new = dp[i][k]+dp[k+1][j]
                    if new > dp[i][j]:
                        dp[i][j] = new
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    ans.append(dp[0][-1])
for a in ans:
    print(a)

# My answer
# 2021/05/11
# http://kutimoti.hatenablog.com/entry/2018/03/10/220819
# ans = []
# while(1):
#     N = int(input())
#     if N==0: break
#
#     W = list(map(int,input().split()))
#     dp = [[0]*N for _ in range(N)]
#     for d in range(1,N):
#         for i in range(N-d):
#             j = i+d
#             if dp[i+1][j-1]==d-1 and abs(W[i] - W[j])<=1: dp[i][j] = d+1
#             else:
#                 for k in range(i+1,j):
#                     dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j])
#
#     ans.append(dp[0][-1])
# for a in ans:
#     print(a)

# 2021/05/11
# ans = []
#
# while True:
#     n = int(input())
#     if not n: break
#
#     W = list(map(int, input().split()))
#     dp = [[0]*n for _ in range(n)]
#
#     for d in range(1, n): # 区間を徐々に広げるようにメモ化を行うので区間 DP
#         for i in range(n-d):
#             j = i+d
#             if abs(W[i]-W[j]) <= 1 and dp[i+1][j-1] == d-1:
#                 dp[i][j] = d+1
#             else:
#                 for k in range(i, j):
#                     # dp[i][j] = max(dp[i][k], dp[k+1][j])
#                     dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j]) # 一つで扱えないので分割して足し込む
#     ans.append(dp[0][-1]) # 区間 DP では右上の値が答えになる
#
# for a in ans: print(a)
