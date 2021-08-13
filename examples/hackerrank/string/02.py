import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    prev = s[0]
    ans = 0

    for i in range(1, len(s)):
        current = s[i]
        if current == prev: ans += 1
        prev = current

    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    result = []
    for q_itr in range(q):
        s = input()

        result.append(alternatingCharacters(s))

    for r in result: print(r)
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
