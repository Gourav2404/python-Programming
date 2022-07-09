class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=[]
        z=0
        # print(len(nums))
        for i in range(len(nums)):
            z = z + nums[i]
            n.append(z)
            # print(z)
        return n
        
  