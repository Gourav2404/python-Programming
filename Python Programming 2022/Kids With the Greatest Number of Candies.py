class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        a=max(candies) #
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=a:
                l.append(True)
            else:
                l.append(False)
        return l