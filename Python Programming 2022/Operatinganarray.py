# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    # Code here
    # for i in range(len(a)) :
        # if x == a[i]:
        if x in a:
            return 1
        else:
            return 0
# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    # Code here
    a.append(y)
    return 1 
        
# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    # Code here
    # print(a ,z)
    for i in range(z):
        if z in a:
            a.remove(z)
            return 1
        
        else :
            return -1
        
# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    # Code here
    # for i in range(len(a)) :
        # if x == a[i]:
        if x in a:
            return 1
        else:
            return 0
# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    # Code here
    a.append(y)
    return 1 
        
# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    # Code here
    # print(a ,z)
    for i in range(z):
        if z in a:
            a.remove(z)
            return 1
        
        else :
            return -1
        