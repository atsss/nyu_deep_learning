from itertools import accumulate

def time_to_seconds(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

ans = []
while(1):
    N = int(input())
    if N==0:
        break
    A = [0] * 86400
    for n in range(N):
        begin, end = input().split()
        begin = time_to_seconds(begin)
        end = time_to_seconds(end)
        A[begin] += 1
        A[end] -= 1
    cumsum = accumulate(A)
    ans.append(max(cumsum))

for a in ans:
    print(a)

# My answer
# 2021/04/28
# from itertools import accumulate
#
# def to_sec(time):
#     hour, minute, second = map(int, time.split(':'))
#     sec = hour * 60 * 60 + minute * 60 + second
#     return sec
#
# ans = []
# while True:
#     n = int(input())
#     if n == 0: break
#
#     times = []
#     for _ in range(n):
#         start, end = input().split()
#         start = to_sec(start)
#         end = to_sec(end)
#         times.append((start, end))
#
#     imos = [0] * (60*60*24+1)
#     for start, end in times:
#         imos[start] += 1
#         imos[end] -= 1 # 到着直後に出発可能なので end+1 でない.境界条件に気をつける
#
#     ans.append(max(accumulate(imos)))
#
# for a in ans:
#     print(a)
