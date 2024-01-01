# cook your dish here
count = int(input())
for _ in range(count):
    a,b = map(int , input().split())
    if a == b :
        print(a)
    elif a > b :
        print(b)
    else :
        print(a)