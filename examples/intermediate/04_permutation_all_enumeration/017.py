from itertools import permutations
K = int(input())
N = 8
RC = []
for k in range(K):
    r, c = map(int,input().split())
    RC.append((r,c))

def diag(board): # 斜めの判定
    for i in range(2*N-1):
        sm = 0
        for j in range(i+1):
            if (i-j>=8 or j>=8):
                continue
            sm += board[i-j][j]
        if sm > 1:
            return False
    return True

def judge(ls):
    board = [[0]*N for _ in range(N)]
    for r in range(N):
        c = ls[r]
        board[r][c] = 1
    for r, c in RC: # 指定された箇所にクイーンを置いているか判定
        if board[r][c] == 0:
            return False

    if not diag(board):
        return False

    if not diag(board[::-1]): # 反転
        return False
    return True

for ls in permutations(range(N)):
    if judge(ls):
        for c in ls:
            s = ['.'] * N
            s[c] = 'Q'
            print (''.join(s))
        exit()

# My answer
# 2021/04/24
# from itertools import permutations
#
# N = 8
# k = int(input())
# # queens = (tuple(map(int, input().split())) for _ in range(k)) # tuple を明記しないと generator オブジェクトになる
# # queens = [tuple(map(int, input().split())) for _ in range(k)] # list はそのままで良い
# queens = tuple(tuple(map(int, input().split())) for _ in range(k))
# print(type(queens))
#
# def check_input_positions(generated_positions):
#     for r, c in queens:
#         if generated_positions[r] != c:
#             return False
#     return True
#
# def check_cross(board): # 理解不足
#     for i in range(2*N-1):
#         sm = 0
#         for j in range(i+1):
#             if (i-j>=8 or j>=8):
#                 continue
#             sm += board[i-j][j]
#         if sm > 1:
#             return False
#     return True
#
# positions = []
#
# for p in permutations(range(N)):
#     board = [[0]*N for _ in range(N)]
#
#     # 親の for loop を continue するときは子の for loop は関数にした方がバグりにくい
#     if not check_input_positions(p): continue
#
#     for r in range(N):
#         c = p[r]
#         board[r][c] = 1
#
#     if check_cross(board) and check_cross(board[::-1]):
#         positions = p
#         break
#
# print(positions)
# ans = []
# for pos in positions:
#     dots = ['.']*N
#     dots[pos] = 'Q'
#     ans.append(dots)
#
# for line in ans: print(''.join(line))
