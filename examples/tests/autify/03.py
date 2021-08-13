#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fn' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def fn(prices):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    result = fn(prices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
