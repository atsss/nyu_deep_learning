# https://asukatagui-blog.com/abc145c/

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

# My answer
# 2021/04/24
# from itertools import combinations
#
# N = int(input())
# cities = (tuple(map(int, input().split())) for _ in range(N))
#
# sm = 0
#
# for c1, c2 in combinations(cities, 2):
#     sm += ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
#
# ans = 2 * sm / N
#
# print(ans)
