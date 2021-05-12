V, E = map(int, input().split())
INF = 10**10
cost = [[INF]*V for _ in range(V)] # 重み
for e in range(E):
    s, t, d = map(int,input().split())
    cost[s][t] = d

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]

def dfs(S, v, dp):
    if dp[S][v] != -1: # 訪問済みならメモを返す
        return dp[S][v]
    if S==(1<<V)-1 and v==0: # 全ての頂点を訪れて頂点0に戻ってきた
        return 0 # もう動く必要はない

    res = INF
    for u in range(V):
        if S>>u & 1 == 0: # 未訪問かどうか
            res = min(res, dfs(S|1<<u, u, dp)+cost[v][u])
    dp[S][v] = res
    return res

ans = dfs(0, 0, dp) # 頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print (ans)

# My answer
# 2021/05/12
# V, E = map(int,input().split())
# G = [[float('inf')]*V for i in range(V)] # 存在しないパスはinfになるように、最初にすべてinfにしておく
# for i in range(E):
#     s,t,d = map(int,input().split())
#     G[s][t] = d # s,tは0以上V-1以下なので、デクリメントの必要はない
# dp = [[float('inf')]*V for i in range(2**V)] # dpの長さは2^V必要
# dp[0][0] = 0 # 0から出発するのでdp[0][0]を0にしておく
#
#
# for S in range(2**V): # Sは集合をbitで表している
#     for v in range(V): # vは配られる側の要素を表している
#         for u in range(V): # uは配る側の要素を表している
#             if not (S >> u) & 1 and S != 0: # ①
#                 continue
#             if (S >> v) & 1 == 0: # ②
#                 if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]:
#                     dp[S | (1 << v)][v] = dp[S][u] + G[u][v] # ③
#
# # 全ての要素が含まれていて、末項が0のものの最小コストを出力する
# # infだった場合は到達できないということなので-1を出力する
# if dp[2**V-1][0] != float('inf'):
#     print(dp[2**V-1][0])
# else:
#     print(-1)
