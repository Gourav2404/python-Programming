# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n=int(input())
    s=input()
    r=input()
    x = 1
    for i in range(n):
        if s[i] != r[i]:
            if x == 1:
                x = 0
            else:
                x = 1
    print(x)