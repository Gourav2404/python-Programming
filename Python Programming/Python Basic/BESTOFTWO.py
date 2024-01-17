# cook your dish here
c=int(input())
for i in range(c):
    a,b=map(int,input().split(' '))
    if a>b:
        print(a)
    elif a<b:
        print(b)
    elif a==b:
        print(a)