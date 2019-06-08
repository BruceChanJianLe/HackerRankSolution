#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # The minimum hour glass is -9 * 7
    # Initial the max_sum as the minimal possible case
    # This is to include the cases where all sums are negative
    max_sum = -9 * 7
        
    for i in range(1, len(arr[0]) - 1):
        for j in range(1,len(arr) - 1):
            current_sum = 0
            current_sum += arr[i - 1][j]
            current_sum += arr[i - 1][j + 1]
            current_sum += arr[i - 1][j - 1]
            current_sum += arr[i][j]
            current_sum += arr[i + 1][j]
            current_sum += arr[i + 1][j + 1]
            current_sum += arr[i + 1][j - 1]
            
            if current_sum > max_sum:                
                max_sum = current_sum
             

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
