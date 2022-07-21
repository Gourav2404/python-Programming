# cook your dish here
n = int(input())
def sum(b):
    return (b*(b+1))/2
    
for i in range(n):
    a,b = map(int, input().split())
    for j in range(a):
        b = sum(b)
    print(int(b))