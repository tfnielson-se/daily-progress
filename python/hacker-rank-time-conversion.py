
# [<0>]
#  HACKER RANK - TIME CONVERSION
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    military_time = s[0:8]
    time = s[2:-2]
    first_two = int(s[0:2])

    if 'PM' in s:
        if first_two != 12:
            hr_convert = first_two + 12
            hr_to_str = str(hr_convert)
            military_time = hr_to_str + time

    if 'AM' in s:
        if first_two == 12:
            military_time = '00' + time

    return military_time


    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
