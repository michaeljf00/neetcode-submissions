# Runtime Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        minNeetCoin = prices[0]
        for price in prices:
            maxProfit = max(maxProfit, max(0, price - minNeetCoin))
            minNeetCoin = min(minNeetCoin, price)

        return maxProfit


