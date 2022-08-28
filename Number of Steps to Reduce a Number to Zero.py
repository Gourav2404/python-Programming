class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0 :
            if num%2 == 0 :
                num = num/2 ;
                count = count + 1
            elif(num == 0):
                count = count +1 
                break
            else:
                num = num-1
                count = count +1 
                
        return count