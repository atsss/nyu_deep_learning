def cost(x):
    return x + P * pow(2,-(x/1.5))

P = float(input())
left = 0
right = 10**18

for i in range(10**5):
    m1 = (2*left + right) / 3
    m2 = (left + 2*right) / 3
    if cost(m1) < cost(m2):
        right = m2
    else:
        left = m1

print(cost(left))

# My answer
# 2021/04/24
# import matplotlib.pyplot as plt
# import numpy as np
#
# P = 1000000000000000000
# N = 50
# xmin = 0
# xmax = 200
#
# def f(x):
#     return x + P/(2**(x/1.5))
#
# p = np.linspace(xmin, xmax, N)
# q = f(p)
# plt.plot(p, q)
# plt.show() # グラフの形状が下に凸になっているか確かめる
#
# P = float(input())
# loop = 10**5
# left = 0
# right = 10**18
#
# def f(x):
#     # return x + P/(2**(x/1.5)) # 複雑な指数関数は pow で処理する
#     return x + P * pow(2,-(x/1.5))
#
# for _ in range(loop):
#     x1 = left+(right-left)/3
#     x2 = left+2*(right-left)/3
#
#     if f(x1) > f(x2): left = x1
#     else: right = x2
#
# print(f(left))

# 2021/04/30
# # import matplotlib.pyplot as plt
# # import numpy as np
# #
# # P = 10 ** 3
# # N = 100
# # xmin = 0
# # xmax = 200
# #
# # def f(x):
# #     return x + P*pow(2, -x/1.5)
# #
# # p = np.linspace(xmin, xmax, N)
# # q = f(p)
# # plt.plot(p,q)
# # plt.show()
#
# P = float(input())
# loop = 10**5
# left_edge = 0
# right_edge = 10**5
#
# def f(x):
#     return x + P*pow(2, -x/1.5)
#
# for _ in range(loop):
#     left = left_edge + (right_edge-left_edge)/3
#     right = left_edge + 2*(right_edge-left_edge)/3
#
#     if f(left) > f(right): left_edge = left # f(right)<f(left) にしないとタイムアウトになる
#     else: right_edge = right
#
# print(f(left_edge))

# 2021/05/06
# # import matplotlib.pyplot as plt
# # import numpy as np
# #
# # def f(x):
# #     return x + P * pow(2, -x/1.5)
# #
# # P = 100
# # mx = 200
# # mn = 0
# # N = 100
# #
# # p = np.linspace(mn, mx, N)
# # q = f(p)
# # plt.plot(p,q)
# # plt.show()
#
# P = float(input())
#
# def f(x): return x + P * pow(2, -x/1.5)
#
# left = 0
# right = 10**5
#
# for _ in range(10**5):
#     m1 = left + (right-left)/3
#     m2 = left + 2*(right-left)/3
#     if f(m1) < f(m2):
#         right = m2
#     else:
#         left = m1
#
# print(f(left))
