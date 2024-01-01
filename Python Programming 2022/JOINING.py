# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    count=0
    if n>=k:
        if n==k:
            print("0")
        elif n<=5:
            print("0")
        else:
            for i in range(k,n):
                if i%5==0:
                    count+=1 
            print(count)