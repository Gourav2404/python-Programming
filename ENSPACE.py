# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    N,X,Y=[int(N) for N in input().split(' ')]
    if (X+(2*Y))<=N:
        print("YES")
    else:
        print("NO")