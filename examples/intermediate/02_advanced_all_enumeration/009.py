SM = []
SN = []
M = int(input()) # 探したい星座
for m in range(M):
    x, y = map(int,input().split())
    SM.append((x,y))
N = int(input()) # 星空の写真
for n in range(N):
    x, y = map(int,input().split())
    SN.append((x,y))
st = set(SN) # inが高速
base = SM[0] # 探したい星座のうち基準となる星を設定
for sn in SN:
    dx, dy  = sn[0]-base[0], sn[1]-base[1] # 平行移動の方法
    ok = True
    for sm in SM:
        if not (sm[0]+dx, sm[1]+dy) in st: # さらに高速化 O(MN)
            ok = False
            break
    if (ok):
        print (dx,dy)
        exit()
print (ans)
