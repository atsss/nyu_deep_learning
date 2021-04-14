from collections import deque
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # タプルやリストで持っておくと便利
H, W, N = map(int,input().split())

maze = []

for h in range(H):
    s = input()
    maze.append(s) # 二次元リストにせず、文字列のリストのままでOK


def solve(sx ,sy, goal):
    dist = [ [-1]*W for _ in range(H)]
    dist[sy][sx] = 0
    q = deque()
    q.append((sy,sx)) # スタート地点をenqueue
    while(q):
        y, x = q.popleft()
        if maze[y][x] == goal: # ゴールにたどり着いたら終了
            break
        else:
            for dx, dy in  dxdy:
                if (0<= x+dx < W) and (0<= y+dy < H) and dist[y+dy][x+dx] == -1 and maze[y+dy][x+dx]!='X': # 見訪問かつ通行可能か
                    q.append((y+dy,x+dx))
                    dist[y+dy][x+dx] = dist[y][x] + 1 # 距離を記録
    return x,y,dist[y][x]

for i in range(H):
    for j in range(W):
        if maze[i][j]=='S':
            sx = j
            sy = i
ans = 0
for n in range(1,N+1):
    sx, sy, d = solve(sx, sy, str(n))
    ans += d
print (ans)
