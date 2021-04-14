from itertools import accumulate
N = int(input())
A = [0] + list(map(int, input().split()))
csum = list(accumulate(A))

for i in range(1,N+1):
    ans = 0
    for j in range(N-i+1):
        diff = csum[j+i] - csum[j]
        ans = max(diff,ans)
    print (ans)
