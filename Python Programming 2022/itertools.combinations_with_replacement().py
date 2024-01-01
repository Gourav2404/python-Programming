# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

a = input().split()

char = sorted(a[0])
n = int(a[1])

for i in combinations_with_replacement(char, n):
    print(''.join(i))
