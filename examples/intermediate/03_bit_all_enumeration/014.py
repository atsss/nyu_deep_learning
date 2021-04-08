from itertools import combinations
N, K = map(int, input().split())
A = list(map(int, input().split()))
mn = 10**18
for B in combinations(range(1,N),K-1): # 一番左は固定
    mx = A[0] # 初期値は一番左の建物
    score = 0
    for n in range(1,N):
        if n in B: # 見えるようにすべき建物なら
            if A[n] <= mx: # 低ければ高くする
                mx += 1
                score += (mx - A[n])
            else: # 高さが十分なら何もしない。最大値を更新
                mx = A[n]
        else:
            mx = max(mx, A[n]) # 見えなくても良い建物なら、最大値を更新
    mn = min(mn, score)
print (mn)
