class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell > buy:
                profit = max(profit, sell - buy)
            elif sell < buy:
                buy = sell
        return profit