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
