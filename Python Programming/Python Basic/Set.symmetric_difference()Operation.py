n = int(int(input()))
nset = set(map(int, input().split(" ")))
b = int(input())
bset = set(map(int, input().split(" ")))

result = nset.symmetric_difference(bset)
print(len(result))