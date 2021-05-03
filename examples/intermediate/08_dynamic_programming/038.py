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
