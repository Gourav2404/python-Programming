# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    if (x%2==0 or x%7==0):
        print("YES")
    elif(x>7):
        print("YES")
    else:
        print("NO ")
