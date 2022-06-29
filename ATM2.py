# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=""
    for m in l:
        if k-m>=0:
            s+='1'
            k=k-m
        else:
            s+='0'
    print(s)
        