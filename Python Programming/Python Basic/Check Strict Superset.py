# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())

for i in range(n):
    b = set(map(int, input().split()))
    if (a > b) and (a.issuperset(b)):
        flag = True
    else:
        flag = False
        break
         
print(flag)