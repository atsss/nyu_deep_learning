import itertools
def transpose(mat): # 二次元のリストを転置する関数
    return list(zip(*mat))
M, N  = map(int, input().split())
K = int(input())
A = []
for m in range(M):
    a = input()
    A.append(a)

J = [[0] * (N+1) for _ in range(M+1)]
O = [[0] * (N+1) for _ in range(M+1)]
I=  [[0] * (N+1) for _ in range(M+1)]

for m in range(M):
    for n in range(N):
        if A[m][n]=='J':
            J[m+1][n+1] = 1
        elif A[m][n] == 'O':
            O[m+1][n+1] = 1
        else:
            I[m+1][n+1] = 1

def calc_csum_mat(A):
    B = []
    for a in A:
        csum = list(itertools.accumulate(a))
        B.append(csum)
    B = transpose(B)

    csum_mat = []
    for a in B:
        csum = list(itertools.accumulate(a))
        csum_mat.append(csum)
    csum_mat = transpose(csum_mat)
    return csum_mat

J = calc_csum_mat(J)
O = calc_csum_mat(O)
I = calc_csum_mat(I)
query = []
def calc_csum(mat,a,b,c,d):
    a -= 1
    b -= 1
    return str(mat[c][d] - mat[c][b] - mat[a][d] + mat[a][b])
for k in range(K):
    query.append(list(map(int,input().split())))
for q in query:
    a,b,c,d = q
    print (calc_csum(J,a,b,c,d) + ' ' + calc_csum(O,a,b,c,d) + ' ' + calc_csum(I,a,b,c,d))
