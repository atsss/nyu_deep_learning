ys,xs=2,2
yg,xg=4,5

a=['########', '#......#', '#.######', '#..#...#', '#..##..#', '##.....#', '########']
n=[(ys-1,xs-1)]
route={n[0]:0}
p=[[1,0],[0,1],[-1,0],[0,-1]]
count=1

while route.get((yg-1,xg-1),0)==0 and count != 10000:
    n2=[]
    for i in n:
        for j in p:
            np=(i[0]+j[0],i[1]+j[1])
            # print(np, route.get(np,-1), a[np[0]][np[1]])
            if a[np[0]][np[1]]=='.' and route.get(np,-1)==-1:
                n2.append(np)
                route[np]=count
    n=n2
    count+=1
    # print(n)

print(n,route)
