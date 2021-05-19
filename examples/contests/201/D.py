H, W = map(int, input().split())
A = []
board = []

for _ in range(H): A.append(input())
for i in range(H):
    array1 = []
    for j in range(W):
        a = A[i][j]
        if a == "+":
            array1.append(1)
        else:
            array1.append(-1)
    board.append(array1)

dp = [[0]*W for _ in range(H)] # マス(i,j)のときの takahashi - aoki のスコア.takahashi は max, aoki は min にするように動く

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if i == H-1 and j == W-1: continue

        is_takahasi_turn = True if (i + j) % 2 == 0 else False

        if i + 1 < H and j + 1 < W:
            if is_takahasi_turn:
                dp[i][j] = max(dp[i+1][j] + board[i+1][j], dp[i][j+1] + board[i][j+1])
            else:
                dp[i][j] = min(dp[i+1][j] - board[i+1][j], dp[i][j+1] - board[i][j+1])
        elif i + 1 < H:
            if is_takahasi_turn:
                dp[i][j] = dp[i+1][j] + board[i+1][j]
            else:
                dp[i][j] = dp[i+1][j] - board[i+1][j]
        elif j + 1 < W:
            if is_takahasi_turn:
                dp[i][j] = dp[i][j+1] + board[i][j+1]
            else:
                dp[i][j] = dp[i][j+1] - board[i][j+1]

if dp[0][0] == 0:
    print('Draw')
elif dp[0][0] > 0:
    print('Takahashi')
else:
    print('Aoki')
