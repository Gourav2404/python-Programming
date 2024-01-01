# cook your dish here
t=int(input())
for _ in range(t):
    (n,m)=map(int,input().split())
    b=list(map(int,input().split()))
    a = 0
    for i in b:
        if i > m:
            a = a + 1
    print(a)