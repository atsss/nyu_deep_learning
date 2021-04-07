# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())
#
# count = 0
#
# for a in range(A+1):
#     for b in range(B+1):
#         for c in range(C+1):
#             if a*500 + b*100 + c*50 == X: count += 1
#
# print(count)

A, B, C, X = [int(input()) for i in range(4)]

print(sum(a*500+b*100+c*50 == X for a in range(A+1) for b in range(B+1) for c in range(C+1)))
