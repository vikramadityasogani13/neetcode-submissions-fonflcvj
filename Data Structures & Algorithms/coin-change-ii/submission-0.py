class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remain):
            if remain == 0:
                return 1
            if i == len(coins) or remain < 0:
                return 0
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            take = dfs(i, remain - coins[i])
            skip = dfs(i + 1, remain)

            memo[(i, remain)] = take + skip
            return memo[(i, remain)]
        return dfs(0, amount)