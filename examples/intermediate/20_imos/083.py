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

# My answer
# 2021/05/04
# from itertools import accumulate
#
# N, M = map(int, input().split())
# P = tuple(map(int, input().split()))
# fare = [tuple(map(int, input().split())) for _ in range(N-1)]
#
# imos = [0] * N
# current = P[0] - 1
#
# for p in P[1:]:
#     nxt = p - 1
#     if nxt > current:
#         imos[current] += 1
#         imos[nxt] -= 1
#     else:
#         imos[current] -= 1
#         imos[nxt] += 1
#     current = nxt
#
# ac = list(accumulate(imos))
# ans = 0
#
# for i in range(N-1):
#     a, b, c = fare[i]
#     cost = min(a*ac[i], b*ac[i] + c)
#     ans += cost
#
# print(ans)
