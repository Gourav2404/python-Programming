n = [7,6,8,6,1,1]
num = [7,6,8,6,1,1]
n2=[]
n1=0

for i in range(len(n)):
    minx = i
    for j in range(i+1 , len(n)):
        if n[minx] > n[j]:
            minx = j
        
    n[i] , n[minx] = n[minx] , n[i]

#     for k in n :
#         n1 =n[0] + n[1]
#         n2.append(n1)

# print(n1 , n2)

print(n)

for k in range(len(n)-1) :
    n[k] =n[k] + n[k+1]
    # n2.append(n1)

print(n)


