class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l  = 0
        r = 1
        profit = 0
        while r < len(prices):
            if(prices[l] > prices[r]):
                l = r
            else:
                if prices[r] - prices[l] > profit:
                    profit = prices[r] - prices[l]
            r +=1
                
        return profit
      
      
#Runtime: 2532 ms, faster than 48.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 25 MB, less than 86.62% of Python3 online submissions for Best Time to Buy and Sell Stock.
