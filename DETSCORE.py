# cook your dish here
t = int(input())
for i in range(t):
    (x, n) = map(int, input().split())
    y = x//10
    z = y*n
    print(z)