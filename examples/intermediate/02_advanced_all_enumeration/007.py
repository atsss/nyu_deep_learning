from itertools import combinations

N = int(input())
ls = []
for n in range(N):
    x, y = map(int,input().split())
    ls.append((x,y))

ls.sort() # 多分要らない?
st = set(ls)
ans = 0

for p1, p2 in combinations(ls, 2): # 組み合わせでOK
    x1, y1 = p1
    x2, y2 = p2
    if (x2 + y2 - y1, y2 + x1 - x2) in st and (x1 + y2 - y1, y1 + x1 - x2) in st:
        ans = max(ans, (x1-x2)**2+(y1-y2)**2)

print (ans)

# My answer
# 2021/04/21
# from itertools import combinations
#
# n = int(input())
# cordinates = { tuple(map(int, input().split())) for _ in range(n) }
# ans = 0
#
# for c1, c2 in combinations(cordinates, 2):
#     x1, y1 = c1
#     x2, y2 = c2
#     dx = x2 - x1
#     dy = y2 - y1
#
#     c3 = (x2 + dy, y2 - dx)
#     c4 = (x1 + dy, y1 - dx)
#
#     if c3 in cordinates and c4 in cordinates: ans = max(ans, dx**2 + dy**2)
#
# print(ans)

# My answer
# 2021/04/30
# from itertools import combinations
#
# n = int(input())
# coordinates = [tuple(map(int, input().split())) for _ in range(n)]
# ans = 0
#
# coordinates.sort()
# st = set(coordinates)
#
# for c1, c2 in combinations(coordinates, 2):
#     dx = c2[0] - c1[0]
#     dy = c2[1] - c1[1]
#     c3 = (c2[0]+dy, c2[1]-dx)
#     c4 = (c1[0]+dy, c1[1]-dx)
#
#     if c3 in st and c4 in st:
#         ans = max(ans, dx**2 + dy**2)
#
# print(ans)
