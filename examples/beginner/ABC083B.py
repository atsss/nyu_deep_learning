# N, A, B = map(int, input().split())
#
# sum1 = 0
#
# for n in range(1, N+1):
#     sum2 = 0
#     target = n
#
#     while target % 10 != 0 or target >= 10:
#         sum2 += target % 10
#         target //= 10
#     else:
#         sum2 += target
#         if A <= sum2 <= B: sum1 += n
#
# print(sum1)

N, A, B = map(int, input().split())

print(sum(n for n in range(N+1) if A <= sum(int(i) for i in str(n)) <= B))
