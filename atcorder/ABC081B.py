N = int(input())
A = list(map(int, input().split()))

count = 0
flag = True

while flag:
    for index, a in enumerate(A):
        if a % 2 == 0:
            A[index] = a / 2
        else:
            flag = False
    if flag: count += 1

print(count)
