class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, canBuy):
            if i >= n:
                return 0
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                memo[(i, canBuy)] = max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, True)
                skip = dfs(i + 1, False)
                memo[(i, canBuy)] = max(sell, skip)
            return memo[(i, canBuy)]

        return dfs(0, True)