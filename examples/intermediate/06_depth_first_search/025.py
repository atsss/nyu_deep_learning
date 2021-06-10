# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

import sys
sys.setrecursionlimit(10**7)

dxdy = ((0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1))
ans = []
while(1):
    W, H = map(int, input().split())
    if (W==0 and H==0):
        break
    mp = []
    for h in range(H):
        line = input()
        line = line.split()
        line = [-int(l) for l in line]
        mp.append(line)
    def dfs(h,w):
        mp[h][w] = k
        for dx, dy in dxdy:
            nw = w + dx
            nh = h + dy
            if (0 <= nh < H and 0 <= nw < W):
                if (mp[nh][nw] == -1):
                    dfs(nh, nw)
    k = 0
    for h in range(H):
        for w in range(W):
            if mp[h][w] == -1:
                k += 1
                dfs(h,w)
    ans.append(k)
for a in ans:
    print(a)

# My answer
# 2021/04/25
# 写経
# import sys
# sys.setrecursionlimit(10**7) # 再帰の上限を設定する -> https://note.nkmk.me/python-sys-recursionlimit/
#
# dxdy = ((0,1), (0,-1), (1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1))
# ans = []
#
# while(1):
#     W, H = map(int, input().split())
#     if W == 0 and H == 0: break
#
#     mp = []
#     counter = 0
#     for i in range(H):
#         C = list(map(int, input().split()))
#         line = [-1*c for c in C] # k のカウントと被るのでマイナスをかけておく
#         mp.append(line)
#
#     def dfs(h,w): # dfs の時は深ぼる変数だけを引く数に取ったほうが見通しが良い
#         mp[h][w] = counter
#         for dx, dy in dxdy:
#             nw = w + dx
#             nh = h + dy
#             if (0 <= nh < H and 0 <= nw < W):
#                 if (mp[nh][nw] == -1):
#                     dfs(nh, nw)
#
#     for h in range(H):
#         for w in range(W):
#             if mp[h][w] == -1:
#                 counter += 1
#                 dfs(h,w)
#
#     ans.append(counter)
#
# for a in ans: print(a)

# 2021/04/30
# dxdy = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))
# ans = []
#
# while True:
#     W, H = map(int, input().split())
#     if W == 0 and H == 0: break
#
#     C = [list(map(int, input().split())) for _ in range(H)]
#     count = 0
#     visited = [[0]*W for _ in range(H)]
#
#     def dfs(h, w, count):
#         visited[h][w] = count
#         for dx, dy in dxdy:
#             if 0 <= h+dy <= H-1 and 0 <= w+dx <= W-1:
#                 if C[h+dy][w+dx] == 1 and visited[h+dy][w+dx] == 0: dfs(h+dy, w+dx, count)
#
#     for h in range(H):
#         for w in range(W):
#             if C[h][w] == 1 and visited[h][w] == 0:
#                 count += 1
#                 dfs(h, w, count)
#
#     ans.append(count)
#
# for a in ans: print(a)

# 2021/06/10
# ans = []
# dxdy = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
#
# while True:
#     W, H = map(int, input().split())
#     if W == 0 and H == 0: break
#
#     mp = []
#     for _ in range(H):
#         line = list(map(int, input().split()))
#         mp.append(line)
#
#     visited = [[-1] * W for _ in range(H)]
#     count = 0
#
#     def dfs(h, w, num):
#         visited[h][w] = num
#
#         for dx, dy in dxdy:
#             nx = w + dx
#             ny = h + dy
#
#             if 0 <= nx < W and 0 <= ny < H:
#                 if mp[ny][nx] == 1 and visited[ny][nx] == -1:
#                     dfs(ny, nx, num)
#
#     for h in range(H):
#         for w in range(W):
#             if mp[h][w] == 0: continue
#             if visited[h][w] == -1:
#                 count += 1
#                 dfs(h, w, count)
#
#     ans.append(count)
#
# for a in ans: print(a)
