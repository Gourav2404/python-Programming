class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        test = 0 
        left = 0
        right = 0
        length = len(nums)
        while test <= length:
            lo = 0 
            # high = nums[len(nums)-1]
            high = length
            mid = (lo + high) // 2 
            print(mid)
            
            if mid == nums[0] :
                return -1
            
            else :
                for i in range(mid):
                    left = left + nums[i]
                print(left)
                
                for j in range(mid+1 , len(nums)):
                    right = right + nums[j]
                print(right)
                
            
                if right == left :
                    print(min)
            
                elif right > left:
                    mid = mid + 1
                    if mid == (nums[-1]):
                        return -1
                else :
                    mid = mid -1
                    if mid == nums[0] :
                        return -1
                # [1,7,3,6,5,6]
                length -= 1
                
            
                return mid
                