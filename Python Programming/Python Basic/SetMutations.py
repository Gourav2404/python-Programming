
num_data = input()
data = set(input().split())

num_operations = int(input())

for _ in range(num_operations):
    op = input().split()
    new_set = set(input().split())
    exec('data.'+op[0]+'(' +str(new_set) + ')')

print(sum(map(int, data)))
