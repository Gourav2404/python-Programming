# cook your dish here
for _ in range(int(input())):
    stacka=[]
    stackb=[]
    
    st=input()
    for i in st:
        if i=="(":
            continue
        elif i==")":
            stacka.append(stackb.pop())
            
        elif i=='+' or i=='-' or i=='/' or i=='*' or i=='^':
            stackb.append(i)
            
        else:
            stacka.append(i)
            
            
    print("".join(stacka))