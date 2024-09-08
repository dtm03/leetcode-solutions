class Solution(object):
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res