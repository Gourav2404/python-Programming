#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

input()
a = list(map(int, input().split()))
m = M = a[0]
x = y = 0
for i in a[1:]:
    if i > M:
        M = i
        x += 1
    elif i < m:
        m = i
        y += 1
print(x, y)
