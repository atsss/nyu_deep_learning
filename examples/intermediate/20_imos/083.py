import itertools
N, M = map(int, input().split())
P = list(map(int, input().split()))
A = []
B = []
C = []
for n in range(N-1):
    a,b,c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
imos = [0] * N
for m in range(M-1):
    if P[m] < P[m+1]:
        imos[P[m]-1] += 1
        imos[P[m+1]-1] -= 1
    else:
        imos[P[m]-1] -= 1
        imos[P[m+1]-1] += 1
csum = list(itertools.accumulate(imos))
ans = 0
for n in range(N-1):
    cnt = csum[n]
    ans += min(A[n]*cnt, B[n]*cnt+C[n])
print (ans)
