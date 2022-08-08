# cook your dish here
for _ in range(int(input())):
    A,B,C=list(map(int,input().split()))
    if (A>=C and B>=A) or (C>=A and B>=C):
        print('YES')
    else:
        print('NO')