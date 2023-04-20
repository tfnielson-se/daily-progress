# [<0>]
#  HACKER RANK - MIN MAX SUM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max_value = get_max_value(arr.copy())
    min_value = get_min_value(arr.copy())
    print(min_value, max_value)


def get_min_value(arr):
    arr.pop()
    return sum(arr)


def get_max_value(arr):
    arr.pop(0)
    return sum(arr)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
