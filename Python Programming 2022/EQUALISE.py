# cook your dish here
t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    c=max(p,q)
    d=min(p,q)
    if c == d:
        print("YES")
    else:
        while(c>d):
            d = d * 2
        if(c == d):
            print("YES")
        else:
            print("NO")