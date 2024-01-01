# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    u=0
    if a>=b:
        u=b+c  
        j=0
        if u>a:
            j=a+d 
            if j<u:
                print('s')
            else: print('n')
        else:
            j=u+d 
            if j>a:
                print('s')
            else: print('n')
        
            
        
   
    else: 
        j=0
        u=a+c
        if u>=b:
            j=b+d 
            if j<=u:
                print('n')
            else:
                print('s')
        else:
            j=u+d  
            if j>=b:
                print('n')
            else: 
                print('s')