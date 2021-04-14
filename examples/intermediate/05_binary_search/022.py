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
