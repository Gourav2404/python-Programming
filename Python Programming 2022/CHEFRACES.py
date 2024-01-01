# cook your dish here
t = int(input())
for i in range(t):
    x,y,a,b = map(int,input().split(" "))
    z = 0
    if x==a:
        z+=1 
    if x==b:
        z+=1 
    if y == a:
        z+=1 
    if y == b:
        z+=1 
    print(abs(z-2))