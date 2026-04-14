class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robLastFirst(arg):
            memo = {}
            def dfs(i):
                if i >= len(arg):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arg[i] + dfs(i + 2), dfs(i + 1))
                
                return memo[i]
            return dfs(0)
        return max(robLastFirst(nums[1:]), robLastFirst(nums[:-1]))