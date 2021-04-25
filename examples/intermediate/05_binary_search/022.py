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
