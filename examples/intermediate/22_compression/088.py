N = int(input())
C = []
for n in range(N):
    c = int(input())
    C.append(c)

stack = []
old = None
for n in range(N):
    c = C[n]
    if (n%2==1): # iが偶数の場合（nが奇数）
        if old != c: # 色が異なれば
            stack.pop() # 反転させる（最後の反対色の記録を取り除く）
            if len(stack)==0: # スタックを空にしない
                stack.append(0)
    else:
        if old != c: # 違う色が出た時
            stack.append(n) # 色の始まりを記録する
    old = c
if old == 0: # スタック上の記録では、白黒は交互に格納されているので最後が白なら
    stack.append(n+1) # n+1を格納しておく。これは、後ほどストライド2で差分を計算するため
if len(stack)%2 == 1:
    stack.insert(0,0) # ストライド2で差分を計算するため、要素数を偶数にする
print (sum(stack[1::2]) - sum(stack[::2]))
