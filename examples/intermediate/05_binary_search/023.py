import bisect
N, M = map(int, input().split())
P = [0]
for n in range(N):
    P.append(int(input()))
P.sort()
S = []
for p1 in P:
    for p2 in P:
        S.append(p1+p2)
S.sort()
ans = 0
for s in S:
    if M < s:
        break
    i = bisect.bisect(S, M-s)-1
    ans = max(s+S[i], ans)
print (ans)
