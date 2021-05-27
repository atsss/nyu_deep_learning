A, B, C, X, Y = map(int, input().split())

ans = 10**10
for i in range(10**5+1):
    ans = min(ans, A*max(X-i, 0) + B*max(Y-i, 0) + 2*C*i)

print(ans)

# My answer
# 2021/04/21
# A, B, C, X, Y = map(int, input().split())
#
# ans = 10**10
# loop = 10**5 + 1
#
# for i in range(loop): ans = min(ans, A*max(X-i, 0) + B*max(Y-i, 0) + C*2*i)
#
# print(ans)

# 2021/04/30
# A, B, C, X, Y = map(int, input().split())
# ans = float('inf')
#
# for i in range(10**5+1):
#     price = max(0, X-i)*A + max(0, Y-i)*B + 2*i*C
#     ans = min(ans, price)
#
# print(ans)

# 2021/05/21
# A, B, C, X, Y = map(int, input().split())
#
# c_max = max(X, Y)
# ans = float('inf')
#
# for i in range(c_max + 1):
#     price = A*max(0, X-i) + B*max(0, Y-i) + C*2*i
#     ans = min(ans, price)
#
# print(ans)
