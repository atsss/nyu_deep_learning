from collections import Counter

N = int(input())
A = list(map(int, input().split()))

col = Counter(A)

for i in range(1, N+1):
    if col[i] == 1:
        continue
    else:
        print('No')
        break
else:
    print('Yes')
