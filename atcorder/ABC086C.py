N = int(input())
cordinates = [list(map(int, input().split())) for i in range(N)]

prev = [0, 0, 0]

for current in cordinates:
  dt = current[0] - prev[0]
  distance = abs(current[1] - prev[1]) + abs(current[2] - prev[2])

  if dt >= distance and (dt - distance) % 2 == 0:
    prev = current
  else:
    print('No')
    break
else:
  print('Yes')
