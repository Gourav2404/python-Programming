from unittest import skip


# num = [4,5,0,1.9,0,5,0]
num = [4,5,0,1,0,0,5]
# length = len(num)
# for i in range(length-1):
#     print(num[i] , num[i+1])
#     if num[i] < num[i+1]:
#         print(i)
#         #print(num[i] , num[i+1])
#         num[i] , num[i+1] = num[i+1] , num[i]
#     else:
#         print("skip")
# print(num)

num1 = sorted(num)
# num2 = [::-1]
print(num1[::-1])