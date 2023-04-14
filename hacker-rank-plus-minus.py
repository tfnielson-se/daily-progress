# [<0>]
#  HACKER RANK - PLUS MINUS

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    negatives = []
    positives = []
    zeros = []
    
    for num in arr:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)
    
    print("{:.6f}".format(len(positives) / len(arr)))    
    print("{:.6f}".format(len(negatives) / len(arr)))
    print("{:.6f}".format(len(zeros) / len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


