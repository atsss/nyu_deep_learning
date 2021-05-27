S = input()
mp = { 0: 0, 1: 1, 6: 9, 8: 8, 9: 6 }

ans = []
for s in S:
    ans.append(mp[int(s)])

print(''.join(map(str, ans[::-1])))
