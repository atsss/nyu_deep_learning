N, M = map(int, input().split())
INF = float('inf')
cost = [[INF]*N for _ in range(N)]
for n in range(N):
    cost[n][n] = 0
for m in range(M):
    a, b, t = map(int, input().split())
    cost[a][b] = t

for i in range(N): # 中継点
    for j in range(N): # 始点
        for k in range(N): # 終点
            cost[j][k] = min(cost[j][i]+cost[i][k], cost[j][k])

for n in range(N):
    if cost[n][n] < 0:
        print ('NEGATIVE CYCLE')
        exit()

for c in cost:
    c = [str(i).replace('inf','INF') for i in c]
    print(' '.join(c))

# My answer
# 2021/04/26
# V, E = map(int, input().split())
# adj = [tuple(map(int, input().split())) for _ in range(E)]
#
# INF = 10**10
# dists = [[INF]*V for _ in range(V)]
#
# for v in range(V): dists[v][v] = 0
# for s, t, d in adj: dists[s][t] = d
#
# for k in range(V):
#     for i in range(V):
#         for j in range(V):
#             dists[i][j] = min(dists[i][k]+dists[k][j], dists[i][j])
#
# for i, line in enumerate(dists):
#     if any([d < 0 for d in line]): # 閉経路の理解を間違っている
#         print('NEGATIVE CYCLE')
#         exit()
#
#     for j, element in enumerate(line):
#         if element == INF: dists[i][j] = 'INF'
#         else: dists[i][j] = str(dists[i][j]) # int を join 出来ないので str にする
#
# for line in dists:
#     print(" ".join(line))
