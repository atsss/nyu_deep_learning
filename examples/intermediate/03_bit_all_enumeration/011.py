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

# My answer
# 2021/04/22 # from itertools import product
#
# N, M = map(int, input().split())
# S = []
#
# for _ in range(M):
#     s = tuple(map(int, input().split()))
#     S.append(s[1:])
#
# P = tuple(map(int, input().split()))
#
# ans = 0
#
# for x in product(range(2), repeat=N):
#     for m in range(M):
#         sm = 0
#         s = S[m]
#         p = P[m]
#
#         for index, element in enumerate(x, 1):
#             if element: # 0,1 で判定するならそのまま足せば良い
#                 if index in s:
#                     sm += 1
#
#         if sm % 2 != p: break
#         if m == list(range(M))[-1]: ans += 1 # break の後に続きがあるのはバグりやすい
#
# print(ans)

# 2021/04/30
# from itertools import product
#
# N, M = map(int, input().split())
# S = []
# for _ in range(M):
#     s = list(map(int, input().split()))
#     S.append(s[1:])
# P = list(map(int, input().split()))
# ans = 0
#
# for c in product(range(2), repeat=N):
#     flag = True
#
#     for i in range(M):
#         count = 0
#         for s in S[i]:
#             count += c[s-1]
#         if P[i] != count % 2:
#             flag = False # この後に break するべき
#
#     if flag: ans += 1
#
# print(ans)

# 2021/06/08
# from itertools import product
#
# N, M = map(int, input().split())
# S = []
# for _ in range(M):
#     s = list(map(int, input().split()))
#     S.append(s[1:])
# P = list(map(int, input().split()))
#
# ans = 0
# for c in product([0, 1], repeat=N):
#     flag = True
#
#     for i in range(M):
#         count = 0
#         for s in S[i]:
#             count += c[s-1]
#         if count % 2 != P[i]:
#             flag = False
#             break
#
#     if flag: ans += 1
#
# print(ans)
