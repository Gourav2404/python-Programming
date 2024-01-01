class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dict_ = {}
        for num in nums:
            dict_[num] = dict_.get(num,0) + 1 ##To keep the count of each num's occurence
        
        count = 0
        for num in nums:
            if dict_.get(num+diff) and dict_.get(num+diff*2): #Check if any number with 3 and 6 more than present in dictionary
                count += 1
        return count