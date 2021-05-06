from itertools import accumulate
N = int(input())
A = [0] + list(map(int, input().split()))
csum = list(accumulate(A))

for i in range(1,N+1):
    ans = 0
    for j in range(N-i+1):
        diff = csum[j+i] - csum[j]
        ans = max(diff,ans)
    print (ans)

# My answer
# 2021/04/28
# 写経
# from itertools import accumulate
#
# N = int(input())
# A = [0] + list(map(int, input().split()))
#
# csum = list(accumulate(A))
# print(csum)
#
# for i in range(1, N+1):
#     ans = 0
#     for j in range(N-i+1):
#         diff = csum[j+i] - csum[j]
#         ans = max(diff, ans)
#     print(ans)

# 2021/05/02
# from itertools import accumulate
#
# N = int(input())
# A = list(map(int, input().split()))
#
# ac = list(accumulate([0]+A))
# ans = []
#
# for k in range(1, N+1):
#     sm = 0
#     for s in range(N-k+1):
#         sm = max(sm, ac[s+k] - ac[s])
#     ans.append(sm)
#
# for a in ans: print(a)
