import math
import os
import random
import re
import sys
from itertools import accumulate

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # dp = [[0] * (k+1) for _ in range(len(prices)+1)]
    # for i in range(len(prices)):
    #     price = prices[i]
    #     for j in range(k+1):
    #         if j >= price:
    #             dp[i+1][j] = max(dp[i][j], dp[i][j-price] + 1)
    #         else:
    #             dp[i+1][j] = dp[i][j]
    # return dp[-1][-1]
    prices = [0] + prices
    prices.sort()

    ans = 0
    csum = list(accumulate(prices))
    for i in range(len(prices)+1):
        if csum[i] <= k: ans = i
        else: break
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
