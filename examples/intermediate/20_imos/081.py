import itertools
N = int(input())
imos = [0] * (10**6 + 2)
for n in range(N):
    a, b = map(int,input().split())
    imos[a] += 1
    imos[b+1] -= 1
csum = list(itertools.accumulate(imos))
print (max(csum))
