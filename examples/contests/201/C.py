from itertools import product

S = input()
N = 10
O = []
X = []
for i in range(N):
    if S[i] == 'o': O.append(i)
    if S[i] == 'x': X.append(i)

def check_O(pattern):
    for o in O:
        if not o in pattern:
            return False
    return True

def check_X(pattern):
    for x in X:
        if x in pattern:
            return False
    return True

ans = 0

for p in product(range(N), repeat=4):
    if not check_O(p): continue
    if not check_X(p): continue
    ans += 1

print(ans)
