
class Solution:
    def MissingNumber(self,array,n):
        # code here
        s=n*(n+1)//2
        s1=0
        for i in range(0,n-1):
            s1=s1+array[i]
          
        return s-s1
#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends