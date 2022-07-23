# cook your dish here
t = int(input())
for i in range(t):
    n, m = tuple(map(int, input().split()))
    p1 = max(n,m)
    p2 = min(n,m)
    tiles22 = (p1//2)*(p2//2)
    tiles11 = p1*p2 - (2*(p1//2)*2*(p2//2))
    tiles = tiles11 + tiles22
    print(tiles11)