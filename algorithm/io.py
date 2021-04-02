n=int(input())  #数値入力 「N」だけの入力のとき
a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
c=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき
print(n, a, b, c)

a=100
b=0.987654321
print('{0:06d}-{1:6f}'.format(a,b))  # 0埋めのときの出力
#f-string
a=123
print(f'test {a} desu')

print(*c)  #リスト出力
for i in [['#','.','#'],['#','#','#']]:print(*i, sep='') #二次元リストで間を詰めたもの
