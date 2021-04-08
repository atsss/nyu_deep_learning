from itertools import product
N, M = map(int,input().split())
S = []
for m in range(M):
    s = list(map(int,input().split()))
    S.append(s[1:])
P = list(map(int,input().split()))

ans = 0
for c in product([0,1],repeat=N):
    ok = True
    for m in range(M):
        sm = 0
        for s in S[m]:
            sm += c[s-1]
        if sm % 2 != P[m]:
            ok = False
            break
    if ok:
        ans += 1
print (ans)
