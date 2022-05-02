#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

def birthdayCakeCandles(candles):
    # Write your code here
    height = max(candles)
    print(candles.count(height))

birthdayCakeCandles(candles)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    
#     result = 
#     fptr.write(str(result) + '\n')

#     fptr.close()
    