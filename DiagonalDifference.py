#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    # dia1 = arr[0][0] + arr[1][1] + arr[2][2]
    # dia2 = arr[0][2] + arr[1][1] + arr[2][0]
    dia1 = 0
    dia2 = 0
    for i in range(0, len(arr)):
        dia1 = dia1 + arr[i][i]
        dia2 = dia2 + arr[i][len(arr) - 1 - i]

    return abs(dia1-dia2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
