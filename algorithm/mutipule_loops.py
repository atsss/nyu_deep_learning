n,y=1000, 1234000
for i in range(n+1):
    for j in range(n-i+1):
        if y-10000*i-5000*j==1000*(n-i-j):
            print(i, j, n-i-j)
            break
    else:
        continue
    break
else:
    print('-1 -1 -1')
