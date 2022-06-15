# cook your dish here
a = list(map(int, input().rstrip().split()))
for i in range(a[0]):
    b = list(map(int, input().rstrip().split()))
    test = b[0]-b[1]
    if test >= 0 :
        print(test)
    else :
        print(0)
    