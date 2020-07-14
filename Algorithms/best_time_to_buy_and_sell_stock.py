class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        minPrice = prices[0]
        maxprofit = 0
        for num in prices:
            if num < minPrice:
                minPrice = num
            elif num-minPrice > maxprofit:
                maxprofit = num-minPrice
        return maxprofit
        