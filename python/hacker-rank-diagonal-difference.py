#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_sum = arr_sum(arr)

    arr_rev = arr[::-1]
    secondary_sum = arr_sum(arr_rev)

    diff_sum = abs(primary_sum - secondary_sum)
    return diff_sum


def arr_sum(ar):
    ar_sum = 0
    for i in range(len(ar)):
        ar_sum = ar_sum + ar[i][i]
    return ar_sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
