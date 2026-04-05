class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        for val in nums:
            if val in seen:
                return val
            else:
                seen.append(val)