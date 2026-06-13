class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        dp[0] = (prices[0], 0)

        for i in range(1, len(prices)):
            dp[i] = (min(dp[i - 1][0], prices[i]), max(dp[i - 1][1], prices[i] - dp[i - 1][0]))

        return dp[-1][1]
        