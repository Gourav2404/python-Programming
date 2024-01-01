n = str(234567898)
# li=[]
# count = 0

# for i in n:
#     li.append(i)
# sort_li=sorted(li)

# for j in range(len(sort_li)-1):
#     if sort_li[j] == sort_li[j+1]:
#         count = count +1
# print(count)
p = 0
for i in set(n):
    if n.count(i)>1:
        p += 1
print(p)