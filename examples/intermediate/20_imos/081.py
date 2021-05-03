import itertools
N = int(input())
imos = [0] * (10**6 + 2)
for n in range(N):
    a, b = map(int,input().split())
    imos[a] += 1
    imos[b+1] -= 1
csum = list(itertools.accumulate(imos))
print (max(csum))

# My answer
# 2021/04/28
# from itertools import accumulate
#
# n = int(input())
# A = [tuple(map(int, input().split())) for _ in range(n)]
# sm = [0] * (10**6+2)
#
# for a, b in A:
#     sm[a] += 1
#     sm[b+1] -= 1
#
# ans = max(list(accumulate(sm)))
# print(ans)
