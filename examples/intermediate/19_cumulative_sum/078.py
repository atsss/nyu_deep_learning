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

# My answer
# 2021/05/04
# from itertools import accumulate
#
# M, N = map(int, input().split())
# K = int(input())
# mp = []
# for _ in range(M):
#     line = input()
#     mp.append(line)
# areas = [tuple(map(int, input().split())) for _ in range(K)]
#
# def string_to_int(mp, letter):
#     new_mp = []
#     for line in mp:
#         new_line = [0]*N
#         for i in range(N):
#             if line[i] == letter: new_line[i] = 1
#         new_mp.append(new_line)
#     return new_mp
#
# def transpose(mp):
#     return list(zip(*mp))
#
# def accumulate_map(mp):
#     ac_mp = []
#     tmp_ac_mp = []
#
#     for line in mp:
#         ac = list(accumulate(line))
#         tmp_ac_mp.append([0]+ac)
#
#     tmp_ac_mp = translate(tmp_ac_mp)
#
#     for line in tmp_ac_mp:
#         ac = list(accumulate(line))
#         ac_mp.append([0]+ac)
#
#     return translate(ac_mp)
#
# j_map = string_to_int(mp, 'J')
# o_map = string_to_int(mp, 'O')
# i_map = string_to_int(mp, 'I')
#
# ac_j_map = accumulate_map(j_map)
# ac_o_map = accumulate_map(o_map)
# ac_i_map = accumulate_map(i_map)
#
# for a, b, c, d in areas:
#     ans = []
#     ans.append(ac_j_map[c][d] + ac_j_map[a-1][b-1] - ac_j_map[c][b-1] - ac_j_map[a-1][d])
#     ans.append(ac_o_map[c][d] + ac_o_map[a-1][b-1] - ac_o_map[c][b-1] - ac_o_map[a-1][d])
#     ans.append(ac_i_map[c][d] + ac_i_map[a-1][b-1] - ac_i_map[c][b-1] - ac_i_map[a-1][d])
#     print(' '.join(list(map(str, ans))))
