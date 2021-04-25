import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
ans = 0

for b in B:
    a = bisect.bisect_left(A, b) # 挿入点はどの同じ値よりも左
    c = bisect.bisect_right(C, b) # 挿入点はどの同じ値よりも右
    ans += a * (len(C)-c)

print (ans)

# My answer
# 2021/04/24
# from bisect import bisect_left, bisect_right
#
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
#
# A.sort()
# C.sort()
# ans = 0
#
# for b in B:
#     ia = bisect_left(A, b)
#     ic = bisect_right(C, b)
#     ans += ia * (N-ic)
#
# print(ans)
