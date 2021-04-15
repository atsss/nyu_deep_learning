from itertools import combinations
INF = 10**10
ans = INF # 最小値を更新するのでINFで初期化
N, M = map(int,input().split())
c_n = []
c_m = []
for n in range(N):
    c_n.append(list(map(int,input().split())))
for m in range(M):
    c_m.append(list(map(int,input().split())))

def dist(c1,c2): # ユークリッド距離を返却する
    return pow(((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2),0.5)

for c1,c2 in combinations(c_m,2): # M個の円同士
    ans = min(ans,dist(c1,c2)/2) # 二点間の距離の半分

for c1 in c_n: # N個の円とM個の円
    ans = min(ans,c1[2]) # 半径が決まっている円もチェック対象
    for c2 in c_m:
        ans = min(dist(c1[:2],c2) - c1[2], ans) # 二点間の距離から半径が決まっている円の半径を引く
print (ans)
