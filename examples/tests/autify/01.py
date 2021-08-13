#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

#
# Complete the 'findAllDuplicates' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findAllDuplicates(arr):
    arr = [key for key,val in Counter(arr).items() if val > 1]
    return sorted(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findAllDuplicates(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
