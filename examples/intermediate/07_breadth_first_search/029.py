import sys
import queue
input = sys.stdin.readline
sys.setrecursionlimit(int(1E+7))
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # タプルやリストで持っておくと便利
R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
maze = []
visited = [ [0]*C for _ in range(R)]
for r in range(R):
    s = input()
    maze.append(s) # 二次元リストにせず、文字列のリストのままでOK
q = queue.Queue()
q.put((sy-1,sx-1,0)) # スタート地点をenqueue
while(not q.empty()):
    y, x, d = q.get()
    if x == gx-1 and y == gy-1: # ゴールにたどり着いたら終了
        ans = d
        break
    if visited[y][x] == 1: # 訪問済みの場合は無視する
        continue
    else:
        visited[y][x] = 1 # 訪問フラグを立てる
        for dx, dy in  dxdy:
            if (0<= x+dx < C) and (0<= y+dy < R): # 範囲内に収まっているか
                if visited[y+dy][x+dx] == 0 and maze[y+dy][x+dx]=='.': # 見訪問かつ通行可能か
                    q.put((y+dy,x+dx,d+1)) # 距離を+1してenqueue
print (ans)

# My answer
# 2021/04/25
# import queue
# # input = sys.stdin.readline # 処理が高速になる -> https://www.kumilog.net/entry/python-speed-comp
# # sys.setrecursionlimit(int(1E+7))
#
# R, C = map(int, input().split())
# start = tuple(map(int, input().split()))
# goal = tuple(map(int, input().split()))
# dxdy = ((1,0), (0,1), (-1,0), (0,-1))
#
# mp = []
# for _ in range(R):
#     line = input()
#     mp.append(line)
#
# distance = [[-1]*C for _ in range(R)]
# q = queue.Queue()
# q.put((start[0]-1, start[1]-1, 0))
#
# while not q.empty():
#     r, c, d = q.get()
#
#     if r == goal[0]-1 and c == goal[1]-1:
#         print(d)
#         break
#
#     distance[r][c] = d
#
#     for dx, dy in dxdy:
#         if mp[r+dy][c+dx] == '.' and distance[r+dy][c+dx] == -1:
#             q.put((r+dy, c+dx, d+1))

# 2021/04/30
# import queue
#
# R, C = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# mp = [input() for _ in range(R)]
#
# dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
# distance = [[-1]*C for _ in range(R)]
#
# q = queue.Queue()
# q.put((0, sx-1, sy-1))
#
# while not q.empty():
#     d, x, y = q.get()
#     if distance[y][x] != -1: continue
#     distance[y][x] = d
#
#     if x == gx-1 and y == gy-1: break
#
#     for dx, dy in dxdy:
#         nx = x+dx
#         ny = y+dy
#         if 0 <= nx < C and 0 <= ny < R:
#             if distance[ny][nx] == -1 and mp[ny][nx] == '.':
#                 q.put((d+1, nx, ny))
#
# print(distance[gy-1][gx-1])

# 2021/06/11
# import queue
#
# R, C = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# mp = [input() for _ in range(R)]
#
# dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
# dists = [[-1] * C for _ in range(R)]
#
# q = queue.Queue()
# q.put((sx-1, sy-1, 0))
#
# while not q.empty():
#     x, y, d = q.get()
#     if dists[y][x] == -1: dists[y][x] = d
#     else: continue
#
#     for dx, dy in dxdy:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < C and 0 <= ny < R and mp[ny][nx] == '.':
#             if dists[ny][nx] == -1: q.put((nx, ny, d+1))
#             else: continue
#
# print(dists[gy-1][gx-1])
