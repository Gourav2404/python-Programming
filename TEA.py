# cook your dish here
# cook your dish here
a=int(input())
for r in range(a):
    b=list(map(int,input().split()))
    c=b[0]
    d=b[1]
    e=b[2]
    if c<=d:
        print(e)
    else:
        f=c%d
        if f!=0:
            g=(c//d)+1
            print(g*e)
        else:
            h=c//d
            print(h*e)