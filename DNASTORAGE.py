# cook your dish her
def solution():
    N = int(input())
    string = input()[:N]
    for i in range(0, N, 2):
        print('A' if('00' == string[i: i+2]) else 'T' if('01' == string[i: i+2]) else 'C' if('10' == string[i: i+2]) else 'G', end = "")
    print()

for i in range(int(input())):
    solution()


