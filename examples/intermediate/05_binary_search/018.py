import bisect

N = input()
INF = 10**10
S = list(map(int,input().split())) + [INF]
Q = input()
T = list(map(int,input().split()))

ans = 0

for t in T:
    i = bisect.bisect_left(S, t)
    if (S[i] == t): # Sにtが含まれれば挿入点の値と等しい
        ans += 1
print(ans)

# My answer
# 2021/04/24
# from bisect import bisect_left
#
# n = int(input())
# S = list(map(int, input().split()))
# q = int(input())
# T = list(map(int, input().split()))
#
# ans = 0
#
# for t in T:
#     index = bisect_left(S, t)
#     if S[index] == t: ans += 1
#
# print(ans)
