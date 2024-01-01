# cook your dish here
t= int(input())
for i in range (t):
    (N, A, B)= map(int, input().split(' '))
    l=list(map(int, input().split()))
    a=l.count(A)
    b=l.count(B)
    s=(a*b)/(N*N)
    print("%.10f" %s)