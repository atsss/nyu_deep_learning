from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

for i,p in enumerate(permutations(range(1,N+1))): # (1,2,3,..)のように辞書順に並んでいるシーケンスを渡す
    if p==P:
        a = i
    if p==Q:
        b = i

print (abs(a-b))

# My answer
# 2021/04/24
# from itertools import permutations
#
# N = int(input())
# P = tuple(map(int, input().split()))
# Q = tuple(map(int, input().split()))
#
# a = 0
# b = 0
#
# # index を 1 から始める必要ない
# # index の指定がなければ list 化する必要もない
# for index, c in enumerate(list(permutations(range(1, N+1))), 1):
#     if c == P: a = index
#     if c == Q: b = index
#
# print(abs(a-b))
