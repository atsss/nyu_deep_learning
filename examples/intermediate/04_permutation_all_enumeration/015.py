from itertools import combinations
N = int(input())
town = []
for n in range(N):
    x, y = map(int,input().split())
    town.append((x,y))

ans = 0
for i,j in combinations(town,2):
    ans += ((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5
print (2*ans/N)
