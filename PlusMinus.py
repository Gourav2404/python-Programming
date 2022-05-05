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
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos = pos + 1

        elif i < 0:
            neg = neg + 1

        else:
            zero = zero + 1

    print(round(float(pos / n), 6))
    print(round(float(neg / n), 6))
    print(round(float(zero / n), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
