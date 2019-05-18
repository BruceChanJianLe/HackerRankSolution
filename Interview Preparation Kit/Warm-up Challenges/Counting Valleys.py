#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    # Regardless of up and down
    # As long as when it goes up it reaches sealevel zero
    # It is counted as a valley
    sealevel = valley_count =0
    
    # Loop through entire list
    for i in range(n):
        if s[i] == 'U':
            sealevel += 1
            if sealevel == 0:
                valley_count += 1
        else: sealevel -= 1
    
    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
