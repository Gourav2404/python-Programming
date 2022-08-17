# cook your dish here
n = int(input())
for i in range(n):
    myTuple = (input().split())
    min_age = myTuple[0]
    max_age = myTuple[1]
    real_age = myTuple[2]
    if (min_age <= real_age) and (real_age < max_age):
        print("YES")
    else:
        print("NO")