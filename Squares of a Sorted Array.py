class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqArr = [1] * len(nums)
        for i in range(len(nums)):
            sqArr[i] = nums[i] * nums[i]
        sqArr.sort()
        return sqArr