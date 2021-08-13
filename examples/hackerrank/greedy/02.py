import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    postive = 0
    negative = 0
    arr = []

    for pair in contests:
        l = pair[0]
        t = pair[1]

        if t == 0:
            postive += l
        else:
            arr.append(l)

    arr.sort(reverse=True)
    postive += sum(arr[:k])
    negative = sum(arr[k:])

    return postive - negative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
