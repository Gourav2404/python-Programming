class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r,l = 0,0 
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                r+=1
            if s[i] == "L":
                l+=1
            
            if r == l:
                count+=1
        return count 