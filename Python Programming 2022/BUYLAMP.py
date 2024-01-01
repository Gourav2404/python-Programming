# cook your dish here
T = int(input())
for t in range(T):
    (n, k, x, y) = map(int, input().split())
    r = (k*x)+min((n-k)*y, (n-k)*x)
    print(r)