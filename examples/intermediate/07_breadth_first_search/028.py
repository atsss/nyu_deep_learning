import queue
N = int(input())

adj = [[]for i in range(N+1)]
depth = [-1] * (N+1)
for n in range(1,N+1):
    V = list(map(int,input().split()))
    for v in V[2:]:
        adj[n].append(v)

q = queue.Queue()
q.put((1,0)) # 番号、深さ
while(not q.empty()):
    x, d = q.get()
    if depth[x] != -1:
        continue
    depth[x] = d
    for next in adj[x]:
        if depth[next] == -1:
            q.put((next,d+1))

for i in range(1,N+1):
    print(i,depth[i])

# My answer
# 2021/04/25
# 写経
# import queue
#
# n = int(input())
# adj = []
#
# for i in range(n):
#     V = list(map(int, input().split()))
#     adj.append(V[2:])
#
# depth = [-1]*n
# q = queue.Queue()
# q.put((0,0)) # index と vertex を入力とプログラミングのどちらに合わせるべきか
#
# while not q.empty():
#     v, d = q.get()
#
#     if depth[v] != -1: continue
#
#     depth[v] = d
#     for next in adj[v]:
#         if depth[next-1] == -1:
#             q.put((next-1, d+1))
#
# for v, d in enumerate(depth, 1): print(v, d)

# 2021/04/30
# import queue
#
# n = int(input())
# adj = []
# for _ in range(n):
#     V = list(map(int, input().split()))
#     adj.append(V[2:])
#
# distance = [-1] * n
# q = queue.Queue()
# q.put((0, 0))
#
# while not q.empty():
#     v, d = q.get()
#     if distance[v] != -1: continue # この1文がないと、キューの中で待っている間に最短距離の計算が終わった頂点を上書いてしまう
#     else: distance[v] = d
#
#     for nxt in adj[v]:
#         if distance[nxt-1] == -1: q.put((nxt-1, d+1))
#
# for i in range(n):
#     print(str(i+1)+' '+str(distance[i]))
