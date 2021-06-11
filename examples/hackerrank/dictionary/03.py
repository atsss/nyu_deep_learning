# https://www.thepoorcoder.com/hackerrank-sherlock-and-anagrams-solution/

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    ans = 0
    sub = []
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            sub.append(''.join(sorted(s[j:j+i])))
    count = Counter(sub)

    # If a substring appears k times, then the total possible anagrams of that substring will be 1+2+3+......+(k-1)
    for value in count.values():
        for i in range(1, value):
            ans += i

    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
