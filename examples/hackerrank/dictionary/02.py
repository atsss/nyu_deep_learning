import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    alphabets = [chr(i) for i in range(97, 97+26)]
    master = {}
    for key in alphabets:
        master[key] = 0

    for s in s1:
        master[s] += 1

    for s in s2:
        if master[s] > 0:
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
