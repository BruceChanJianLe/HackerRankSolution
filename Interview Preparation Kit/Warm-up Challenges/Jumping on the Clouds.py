#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jump_count = 0
    i = 0
    c.extend('##')
    
    while i <= n - 1:
        if i == n - 1: break
        if c[i + 1] == 0 and c[i + 2] == 0:
            jump_count += 1
            i += 2
        elif c[i + 1] == 1:
            jump_count += 1
            i += 2
        else:
            jump_count += 1
            i += 1

    return jump_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))
    
    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
