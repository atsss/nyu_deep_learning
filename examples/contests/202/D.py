A, B, K = map(int, input().split())

# a_indexes = list(combinations(range(A+B), A))
# indexes = a_indexes[K-1]
#
# ans = ''
# for i in range(A+B):
#     if i in indexes: ans += 'a'
#     else: ans += 'b'
#
# print(ans)

dp = [[0]*(B+1) for _ in range(A+1)]
dp[0][0] = 1

for i in range(A+1):
    for j in range(B+1):
        if i > 0: dp[i][j] += dp[i-1][j]
        if j > 0: dp[i][j] += dp[i][j-1]

def find_kth(a, b, k):
    if a == 0: return 'b' * b
    if b == 0: return 'a' * a

    if k <= dp[a - 1][b]:
        return 'a' + find_kth(a - 1, b, k)
    else:
        return 'b' + find_kth(a, b - 1, k - dp[a - 1][b])

print(find_kth(A, B, K))
