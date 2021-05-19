N = int(input())
mountains = []
for _ in range(N):
    s, t = input().split()
    t = int(t)
    mountains.append((t,s))

mountains.sort()

print(mountains[-2][1])
