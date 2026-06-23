class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices)):
            for j in reversed(range(0, len(prices))):
                if i == j:
                    break
                print(prices[j] - prices[i])
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        if profit < 0:
            return 0
        else:
            return profit
