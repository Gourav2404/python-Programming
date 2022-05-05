# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
setA = set(map(int, input().split()))

b = input()
setB = set(map(int, input().split()))

difA = setA.difference(setB)
diffB = setB.difference(setA)

sd = difA.union(diffB)

for i in sorted(list(sd)):
    print(i)
