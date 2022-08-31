def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                count += 1
        return count