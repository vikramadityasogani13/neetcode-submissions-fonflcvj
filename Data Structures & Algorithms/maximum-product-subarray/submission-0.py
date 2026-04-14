class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                curMax, curMin = curMin, curMax
        
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)
            res = max(res, curMax)

        return res