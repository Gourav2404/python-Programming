# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=max(a,b)
    y=max(c,d)
    print(x+y)