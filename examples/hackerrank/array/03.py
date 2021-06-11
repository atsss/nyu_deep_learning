#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    ans = 0

    for index, element in enumerate(q):
        original = element - 1
        current = index

        if original - current > 2:
            print('Too chaotic')
            return

        for k in q[max(0, original-1):current]: # オリジナルの位置より1つ前まで見れば良い
            if k > element: ans += 1

    print(ans)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
