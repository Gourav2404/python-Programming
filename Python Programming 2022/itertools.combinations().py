# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()
k = int(k)

for r in range(1, k+1):
    print('\n'.join(sorted(''.join(sorted(c)) for c in combinations(S, r))))
