import itertools
MOD = 10**5
N, M = map(int, input().split())
D = [0] # 先頭に0を入れておくと、累積和の差分計算の際に楽
for n in range(N-1):
    d = int(input())
    D.append(d)
C = []
for m in range(M):
    c = int(input())
    C.append(c)

csum = list(itertools.accumulate(D))
cur = 1
ans = 0
for c in C:
    next = cur + c # 移動
    ans += abs(csum[next-1]-csum[cur-1]) # 絶対値を足す
    cur = next # 次の移動開始地点
    ans %= MOD
print (ans)
