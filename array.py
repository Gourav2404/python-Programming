import array 

arr = array.array( 'i' ,[1,2,3,4] )
print("The new created array is : ", end="")

for i in range(len(arr)):
    print( arr[i] , end="")

print("\n")

arr.append(5)
print("The new created array is " , end="")
for i in range(len(arr)):
    print(arr[i] , end = " " )

print("\n")

arr.insert(2 , 10) 
print("The new created array is " , end="")
for i in range(len(arr)):
    print(arr[i] , end = " " )
    
print("\n")

arr.pop(2)
print("The new created array is " , end="")
for i in range(len(arr)):
    print(arr[i] , end = " " )

print("\n")

arr.remove(2)
print("The new created array is " , end="")
for i in range(len(arr)):
    print(arr[i] , end = " " )

print("\n")


print("The index of array is " , end="")
print(arr.index(3) , end = " ")

print("\n")

arr.reverse()
print("The reversed array is " , end="")
for i in range(len(arr)):
    print(arr[i] , end = " " )

print("\n")


print(arr.typecode)

print(arr.itemsize)

print(arr.buffer_info())

print(arr.count(1))

arr1 = array.array('i' , [1,1,2,2,3,3]) 

print("the new array is " , end=" ")
for j in range(len(arr1)):
    print(arr1[j] , end=" ")

print("\n")

arr.extend(arr1)
print("The extended array is :- " , end= " ")
for j in range(len(arr)):
    print(arr[j] , end=" ")