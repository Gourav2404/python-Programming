# cook your dish here
t=int(input())
for l in range(t):
    
    cntr1=0
    cntr2=0
    
    r1,w1,c1=map(int,input().split())
    r2,w2,c2=map(int,input().split())
    
    if(r1>r2):
	    cntr1+=1
    elif(r2>r1):
	    cntr2+=1
	    
    if(w1>w2):
	    cntr1+=1
    elif(w2>w1):
	    cntr2+=1
	    
    if(c1>c2):
	    cntr1+=1
    elif(c2>c1):
	    cntr2+=1
	    
	
    if(cntr1>cntr2):
	    print("A")
    elif(cntr2>cntr1):
	    print("B")