class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        lowestPrice=0
        highestPrice=1
        while highestPrice<len(prices):
            if prices[lowestPrice]<prices[highestPrice]:
                profit=prices[highestPrice]-prices[lowestPrice]
                maxProfit=max(maxProfit,profit)
            else:
                lowestPrice=highestPrice
            highestPrice=highestPrice+1
        return maxProfit
        