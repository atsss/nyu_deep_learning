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

# My answer
# 2021/04/30
# from bisect import bisect_left
#
# N, M = map(int, input().split())
# P = [int(input()) for _ in range(N)]
#
# P = [0] + P + [10**18+1]
# pair = []
# for i in P:
#     for j in P:
#         pair.append(i+j)
#
# pair.sort()
# ans = 0
# for p in pair:
#     if p > M: continue
#     index = bisect_left(pair, M-p) # 左端が0で固定されているので、bisect_right のほうが扱いやすそう.終端が厄介な時は bisect_right にして -1 することを検討する
#     if index == N: continue
#     ans = max(ans, p+pair[index])
#
# print(ans)

# 2021/05/06
# from bisect import bisect_right
#
# N, M = map(int, input().split())
# P = [int(input()) for _ in range(N)]
#
# P = [0] + P
# sm = []
# for p1 in P:
#     for p2 in P:
#         sm.append(p1+p2)
#
# sm.sort()
# ans = 0
#
# for score in sm:
#     if score > M: continue
#
#     left = M - score
#     index = bisect_right(sm, left)
#     ans = max(ans, score+sm[index-1])
#
# print(ans)
