A, B, C = map(int, input().split())

# a_c = pow(A, C)
# b_c = pow(B, C)
#
# if a_c > b_c:
#     print('>')
# elif a_c < b_c:
#     print('<')
# else:
#     print('=')

if C % 2 == 0:
    if abs(A) == abs(B):
        print('=')
    elif abs(A) > abs(B):
        print('>')
    else:
        print('<')
else:
    if A == B:
        print('=')
    elif A > B:
        print('>')
    else:
        print('<')
