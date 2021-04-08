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
