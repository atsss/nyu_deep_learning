N = int(input())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

am = sorted(A)[N//2]
bm = sorted(B)[N//2]

ans = 0
for a,b in zip(A,B):
    ans += abs(a-b) # AからB
    ans += abs(a-am) # 入口からA
    ans += abs(b-bm) # 出口からB
print (ans)

# My answer
# 2021/04/21
# N = int(input())
# # A = B = [] # B が参照渡しになっている
# A = []
# B = []
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
#
# ans = 0
# s = sorted(A)[N//2]
# g = sorted(B)[N//2]
#
# for a, b in zip(A, B):
#     ans += abs(s-a)
#     ans += abs(b-a)
#     ans += abs(g-b)
#
# print(ans)

# 2021/04/30
# N = int(input())
# A = []
# B = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
#
# entrance = sorted(A)[N//2]
# exit = sorted(B)[N//2]
# ans = 0
#
# for a, b in zip(A, B):
#     ans += abs(a-entrance) + abs(b-a) + abs(exit-b)
#
# print(ans)

# 2021/05/21
# N = int(input())
# A = []
# B = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
#
# entrance = sorted(A)[N//2]
# exit = sorted(B)[N//2]
#
# ans = 0
# for a, b in zip(A, B):
#     ans += abs(a-entrance) + abs(b-a) + abs(exit-b)
#
# print(ans)
