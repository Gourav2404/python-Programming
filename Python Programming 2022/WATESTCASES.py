# cook your dish here
t=int(input())
for o in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    string=str(input())
    ans=max(arr)
    for i in range(len(arr)):
        if string[i]=='0':
            ans=min(ans,arr[i])
    print(ans)