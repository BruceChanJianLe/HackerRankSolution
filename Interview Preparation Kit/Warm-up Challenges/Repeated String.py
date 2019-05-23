#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    a_instring = 0
    a_count = 0

    if n % len(s) == 0:
        for i in s:
            if i == 'a':
                a_instring += 1
        a_count = int(n / len(s)) * a_instring
    else:
        for i in s:
            if i == 'a':
                a_instring += 1
        a_count = int(n / len(s)) * a_instring

        a_instring = 0
        for i in range(n % len(s)):
            if s[i] == 'a':
                a_instring += 1
        a_count += a_instring
    
    return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
