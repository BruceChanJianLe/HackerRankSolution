#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    # Create a variable to store the counts of minimum bribes
    bribe_count = 0
    
    # We can make the element match the index by
    # q = [e - 1 for e in q]
    # But I will stick will the same one to save time

    # Use enumerate to obtain the index and the value at the same time
    for i, v in enumerate(q):

        # The value cannot move more than 2 steps ahead
        if v - 3 > i:
            return 'Too chaotic'

        # If the value is within the range
        # We compare the values two steps ahead from the current index
        # Since if bribe happens that value that swaps cannot move
        # Further than the two step ahead position
        # If it is larger than the value at current position
        # Means bribe happened, add one to bribe_count

        for j in range(max(0, v - 3), i):
            if q[j] > v:
                bribe_count += 1


    return bribe_count

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)

        print(result)
