N = 45
dp = [0] * N
dp[0] = dp[1] = 1
for i in range(N-2):
    dp[i+2] = dp[i] + dp[i+1]
n = int(input())
print (dp[n])

# My answer
# 2021/04/25
# n = int(input())
# mx = 45
#
# fib = [0] * mx
# fib[0] = 1
# fib[1] = 1
#
# for i in range(2, mx): fib[i] = fib[i-1] + fib[i-2]
#
# print(fib[n])

# 2021/05/02
# n = int(input())
#
# dp = [0] * 45
# dp[0] = 1
# dp[1] = 1
#
# for i in range(2, 45): dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[n])
