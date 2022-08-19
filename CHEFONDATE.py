# cook your dish here
testcases = int(input())
for testcase in range(testcases):
    cash, bill = map(int, input().split())
    if(cash >= bill):
        print("yes")
    else:
        print("No")