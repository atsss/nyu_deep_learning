import math
a,b=map(int, input().split())
f=math.gcd(a,b)
f2=a*b//f
print(f,f2)
