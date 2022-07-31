# cook your dish here
t=int(input())
for l in range(t):
    a,b=map(int,input().split())
    if(a%3==0 or b%3==0):
        print(0)
    elif(abs(a-b)%3==0):
        print(1)
    else:
        print(2)
    