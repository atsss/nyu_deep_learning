import heapq
INF = 10**10

V, E, r = map(int,input().split())
adj = [[] for i in range(V)] # 隣接リスト

for e in range(E):
    s, t, d = map(int,input().split())
    adj[s].append((t,d))

dists  = [INF for i in range(V)] # 重みの和
dists[r] = 0
pq = [(0, r)] # 二分ヒープの実体はリストやタプルとして表現する
　            # (重みの和, ノード番号)
while(pq):
    d, node = heapq.heappop(pq)
    if (d > dists[node]): # 探索の対象にする必要があるか確認
        continue
    for next, cost in adj[node]:
        if d + cost < dists[next]:# 探索の対象にする必要があるか確認
            dists[next] = d + cost # 次のノードにおける重みの和
            heapq.heappush(pq, (dists[next],next))
for d in dists:
    if d == INF:
        print ('INF')
    else:
        print (d)

# My answer
# 2021/04/26
# 写経
# import heapq # 順番に出すだけなら sort で良い場合がある. 出し入れするなら heapq を使ったほうが早い
# INF = 10**10
#
# V, E, r = map(int, input().split())
# adj = [[] for _ in range(V)]
# for _ in range(E):
#     s, t, d = map(int, input().split())
#     adj[s].append((t,d))
#
# dists = [INF for _ in range(V)]
# dists[r] = 0
# pq = [(0, r)] # heapfiy の計算量がかからない　
#
# while pq:
#     d, node = heapq.heappop(pq) # heappop の計算量はツリーの修正があるので O(logN)
#     if d > dists[node]: continue
#
#     for next, cost in adj[node]:
#         if d + cost < dists[next]:
#             dists[next] = d + cost
#             heapq.heappush(pq, (dists[next], next)) # heappush の計算量は O(logN). sort は毎回 O(NlogN) かかるから N 倍早い
#
# for d in dists:
#     if d == INF: print('INF')
#     else: print(d)

# 2021/05/02
# import heapq
#
# V, E, r = map(int, input().split())
# adj = [[] for _ in range(V)]
# for _ in range(E):
#     s, t, d = map(int, input().split())
#     adj[s].append((d, t))
#
# hq = []
# INF = float('inf')
# visited = [INF]*V
# visited[r] = 0
# for d, t in adj[r]:
#     heapq.heappush(hq, (d, t))
#
# while hq:
#     d, t = heapq.heappop(hq)
#
#     if visited[t] != INF: continue # 訪問済みではなくて、d > visited[t] ならスキップ
#
#     visited[t] = d
#     for nd, nt in adj[t]:
#         # ここで次の頂点の重み付け先に行っておく
#         heapq.heappush(hq, (nd+d, nt))
#
# for ans in visited:
#     if ans == INF: print('INF')
#     else: print(ans)

# 2021/05/06
# import heapq
#
# V, E, r = map(int, input().split())
# adj = [[] for _ in range(V)]
# for _ in range(E):
#     s, t, d = map(int, input().split())
#     adj[s].append((t, d))
#
# dists = [-1] * V
# pq = []
# heapq.heappush(pq, (0, r))
#
# while pq:
#     d, v = heapq.heappop(pq)
#     if dists[v] != -1: continue # 判定ミス
#
#     dists[v] = d
#
#     for nv, nd in adj[v]:
#         if dists[nv] != -1: continue
#         heapq.heappush(pq, (d+nd, nv))
#
# for ans in dists:
#     if ans == -1: print('INF')
#     else: print(ans)
