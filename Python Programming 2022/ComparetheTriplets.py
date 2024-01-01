#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0 
    
    for i in range(3):
        if a[i] > b[i]:
            alice = alice + 1
        
        elif a[i] < b[i] :
            bob = bob +1 
            
    print(alice , bob)
    
    
if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)