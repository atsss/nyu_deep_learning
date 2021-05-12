# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp

Q = int(input())

def lcs(X, Y):
    dp = [[0] * (len(X)+1) for _ in range(len(Y)+1)]
    for i in range(1,len(Y)+1):
        for j in range(1,len(X)+1):
            if X[j-1]==Y[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

ans = []
for q in range(Q):
    X = input()
    Y = input()
    ans.append(lcs(X,Y))
for a in ans:
    print(a)

# My answer
# 2021/04/25
# これがわかりやすい -> https://naoya-2.hatenadiary.org/entry/20090328/1238251033

# 2021/05/02
# q = int(input())
# S = []
# for _ in range(q):
#     X = input()
#     Y = input()
#     S.append((X, Y))
# ans = []
#
# for X, Y in S:
#     dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
#
#     for xi in range(1, len(X)+1): # ナップザック問題と違って、一つ前から現在の値を求める
#         for yi in range(1, len(Y)+1):
#             if X[xi-1] == Y[yi-1]:
#                 dp[xi][yi] = dp[xi-1][yi-1] + 1
#             else:
#                 dp[xi][yi] = max(dp[xi-1][yi], dp[xi][yi-1])
#
#     ans.append(dp[len(X)][len(Y)])
#
# for a in ans: print(a)

# 2021/05/02
# q = int(input())
# A = []
# B = []
# for _ in range(q):
#     a = input()
#     b = input()
#     A.append(a)
#     B.append(b)
#
# for i in range(q):
#     a = A[i]
#     b = B[i]
#     dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
#
#     for ia in range(1, len(a)+1): # スタートが1から始まる
#         for ib in range(1, len(b)+1):
#             if a[ia-1] == b[ib-1]:
#                 dp[ia][ib] = dp[ia-1][ib-1] + 1
#             else:
#                 dp[ia][ib] = max(dp[ia-1][ib], dp[ia][ib-1])
#     print(dp[-1][-1])
