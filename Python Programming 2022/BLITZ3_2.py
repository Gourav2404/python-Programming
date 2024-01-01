# cook your dish here
test=int(input())
for j in range(test):
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    print(2*(180+a)-(b+c))