# cook your dish here
for i in range(int(input())):
    N,K,M=map(int,input().split(' '))
    d=N//(K*M)
    r=N%(K*M)
    
    if r!=0:
        print(d+1)
    else:
        print(d)