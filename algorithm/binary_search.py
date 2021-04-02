import bisect
a = [1, 2, 3, 5, 6, 7, 8, 9]
b=bisect.bisect_left(a, 8)

print(b)
