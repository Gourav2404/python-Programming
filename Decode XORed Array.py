class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = []
        res.append(first)
        prev = first
        
        for num in encoded:
            val = prev ^ num
            res.append(val)
            prev = val
        return res