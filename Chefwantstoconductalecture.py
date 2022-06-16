# cook your dish here
a = list(map(int, input().rstrip().split()))
for i in range(a[0]):
    b =list(map(int , input().rstrip().split()))
    sub = 30 - b[0]
    if sub >= 0 :
        print("NO")
    else :
        print("YES")
    