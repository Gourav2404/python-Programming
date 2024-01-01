# cook your dish here
T = int(input())
for i in range(T):
    inp = input()
    N, K =inp.split(" ")
    N = int(N)
    K = int(K)
    if N < K:
        print("YES")
    else:
        print("NO")