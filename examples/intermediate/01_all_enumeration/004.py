from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

ans = 0

for m1, m2 in combinations(range(M),2):
    score = 0
    for a in A: score += max(a[m1],a[m2])
    ans = max(ans, score)

print (ans)

# My answer
# 2021/04/20
# from itertools import combinations
#
# N, M = map(int, input().split())
# A = [tuple(map(int, input().split())) for _ in range(N)]
# ans = 0
#
# for c in combinations(range(M), 2):
#     sm = 0
#
#     for n in range(N): sm += max(A[n][c[0]], A[n][c[1]])
#
#     ans = max(ans, sm)
#
# print(ans)

# 2021/04/30
# from itertools import combinations
#
# N, M = map(int, input().split())
# A = [tuple(map(int, input().split())) for _ in range(N)]
# ans = 0
#
# for m1, m2 in combinations(range(M), 2):
#     score = 0
#     for a in A:
#         score += max(a[m1], a[m2])
#     ans = max(ans, score)
#
# print(ans)
