N = int(input())
n = N
ans = []
for i in range(2,int(N**0.5)+1): # intに変換すること
    while(n%i==0):
        n //= i #  整数除算(//)を使うこと
        ans.append(i)
if n!=1:
    ans.append(n)
ans = [str(a) for a in ans]
ans = str(N)+": " + " ".join(ans)
print (ans)
#         n /= i #  整数除算(//)を使うこと
#         ans.append(i)
# if n!=1:
#     ans.append(n)
# ans = [type(a) for a in ans]
# for an in ans:
#     print (an)
