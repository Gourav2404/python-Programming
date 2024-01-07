# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

A = int(input())
for i in range(A):
    n = (input())
    if re.search(r"^(\+|\-)?\d*\.\d+$" , n):
        print(True)
    else :
        print(False)
