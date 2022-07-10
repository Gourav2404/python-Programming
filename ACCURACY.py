a=int(input())
for r in range(a):
    b=int(input())
    c=b%3
    if c!=0:
        d=(b//3)+1
        e=d*3
        f=e-b
        print(f)
    else:
        print(0)