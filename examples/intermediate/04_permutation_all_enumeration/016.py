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
