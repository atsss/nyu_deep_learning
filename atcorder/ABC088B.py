N = int(input())
A = list(map(int, input().split()))

alice = 0
bob = 0

A.sort(reverse=True)

for index, a in enumerate(A):
    if index % 2 == 0: alice += a
    else: bob += a

print(alice - bob)
