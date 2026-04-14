class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for num in nums:
            nextDP = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                if t + num < target:
                    nextDP.add(t + num)
            dp = nextDP

        return target in dp