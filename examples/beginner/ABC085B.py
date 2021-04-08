# from collections import Counter
#
# N = int(input())
#
# D = []
# for i in range(N): D.append(int(input()))
#
# counter = Counter(D)
#
# print(len(counter))

N = int(input())
D = [int(input()) for i in range(N)]

print(len(set(D)))
