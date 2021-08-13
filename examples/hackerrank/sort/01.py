import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
# for (int i = 0; i < n; i++) {
#
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#         }
#     }
#
# }

def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = tmp
                count += 1

    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
