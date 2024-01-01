class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        
        l = len(nums)
        for i in range(0,l,2):
            for j in range(nums[i]):
                res.append(nums[i+1])
        return res