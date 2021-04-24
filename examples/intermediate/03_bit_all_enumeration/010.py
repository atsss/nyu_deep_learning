from itertools import product
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

create = [0] * 40001

for p in product([0,1], repeat=n):
    sm = 0
    for i in range(n):
        if p[i]==1:
            sm += A[i]
    create[sm] = 1

for m in M:
    if create[m]:
        print('yes')
    else:
        print ('no')

# My answer
# 2021/04/22
# from itertools import product
#
# n = int(input())
# A = tuple(map(int, input().split()))
# q = int(input())
# m = tuple(map(int, input().split()))
#
# ans = [0] * 2_001
#
# for p in product(range(2), repeat=n):
#     sm = 0
#
#     for i in range(n):
#         if p[i] == 1: sm += A[i]
#
#     if sm in m: ans[sm] = 1 # if 文自体必要ない
#
# for i in m:
#     if ans[i] == 1: print('yes') # 1, 0 は True, False で判定される　
#     else: print('no')
