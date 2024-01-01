# cook your dish here
from math import gcd
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    if gcd(x,y)%k == 0:print("YES")
    else:print("NO")