N = int(input())
adj = [[] for i in range(N)]
for n in range(N):
    V = list(map(int, input().split()))
    for v in V[2:]: # u,k,v1,v2,...
        adj[n].append(v-1)
d = [0] * N # 発見時刻
f = [0] * N # 完了時刻

def dfs(v, t):
    t+=1 # 発見したらインクリメント
    d[v] = t
    for next in adj[v]:
        if d[next] == 0: # 未発見なら
            t = dfs(next, t)
    t+=1 # 完了してもインクリメント
    f[v] = t
    return t

t = 0
for n in range(N):
    if d[n]==0: # 未発見なら
        t = dfs(n,t)
    print (n+1,d[n],f[n])

# My answer
# 2021/04/25
# 写経
# N = int(input())
# adj = [[] for _ in range(N)]
# for i in range(N):
#     V = list(map(int, input().split()))
#     for v in V[2:]: adj[i].append(v-1)
#
# d = [0]*N
# f = [0]*N
#
# def dfs(v, t):
#     t += 1
#     d[v] = t
#
#     for next in adj[v]:
#         if d[next] == 0: t = dfs(next, t)
#
#     t += 1
#     f[v] = t
#     return t
#
# t = 0
# for n in range(N):
#     if d[n] == 0: t = dfs(n, t)
#     print(n+1, d[n], f[n])

# 2021/04/30
# n = int(input())
# adj = []
# for _ in range(n):
#     s = list(map(int, input().split()))
#     adj.append(s[2:])
#
# d = [0]*n
# f = [0]*n
#
# def dfs(v, t):
#     t += 1
#     d[v] = t
#     for next in adj[v]:
#         if d[next-1] == 0:
#             t = dfs(next-1, t)
#     t += 1
#     f[v] = t
#
#     return t
#
# dfs(0, 0) # 全ての頂点がつながっていない可能性があるので、ループを回す必要がある
#
# for i in range(n):
#     print(' '.join(map(str, [i+1, d[i], f[i]])))

# 2021/05/06
# n = int(input())
# adj = [[] for _ in range(n)]
# for i in range(n):
#     v = list(map(int, input().split()))
#     adj[i] = v[2:]
#
# d = [0]*n
# f = [0]*n
#
# def dfs(vertex, time):
#     if d[vertex]: return time
#
#     t = time + 1
#     d[vertex] = t
#
#     for nxt in adj[vertex]:
#         if d[nxt-1]: continue
#         t = dfs(nxt-1, t)
#
#     t += 1
#     f[vertex] = t
#     return t
#
# t = 0
# for i in range(n): t = dfs(i, t)
#
# for i in range(n):
#     ans = [i+1, d[i], f[i]]
#     print(' '.join(map(str, ans)))
