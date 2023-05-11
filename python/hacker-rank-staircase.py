#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    hashtags = range(1, n+1)
    hashtags_arr = [num * '#' for num in hashtags]
    
    spaces = range(n)
    range_spaces = [(space) for space in spaces]
    range_spaces.reverse()
    
    spaces_arr = [space * ' ' for space in range_spaces]
    
    
    for spaces, hashtags in zip(spaces_arr, hashtags_arr):
        print(spaces + hashtags)
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
