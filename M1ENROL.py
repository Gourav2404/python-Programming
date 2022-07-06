# cook your dish here
try:
    t=int(input())
    for i in range(t):
        x,y=(int(i) for i in input().split())
        if x>=y:
            print(0)
        else:
            print(y-x)
except: pass
