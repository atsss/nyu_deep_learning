import math
import os
import random
import re
import sys
# from itertools import combinations

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # ans = float('inf')
    # for e1, e2 in combinations(arr, 2):
    #     ans = min(ans, abs(e1-e2))
    # return ans
    arr.sort()
    ans = float('inf')
    prev = arr[0]

    for current in arr[1:]:
        ans = min(ans, current - prev)
        prev = current

    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
