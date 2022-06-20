# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    
    d = min(a,b,c)
    
    if a == d:
        print("Draw")
    elif b == d:
        print("Bob")
    else:
        print("Alice")