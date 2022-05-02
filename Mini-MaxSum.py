#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    test = sorted(arr)
    minimum = test[0]+test[1]+test[2]+test[3]
    maximum = test[4]+test[1]+test[2]+test[3]
    print(minimum, maximum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
