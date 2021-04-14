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
