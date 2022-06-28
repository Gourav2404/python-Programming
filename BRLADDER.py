# cook your dish here
for i in range(int(input())):
    f,s = map(int, input().split())
    if (abs(f-s)==1 and min(f,s)%2==1) or (f%2==s%2 and abs(f-s) ==2):
        print('YES')
    else:
        print("NO")