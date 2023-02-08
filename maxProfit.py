class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = math.inf
        maxx = 0
        profit = 0
        curr = 0
        for i in prices:
            if i < prev:
                if maxx != -math.inf:
                    profit += maxx
                    maxx = 0
                curr = i
            else:
                maxx = max(maxx, (i - curr))
         
            prev = i

        profit += maxx

        return profit
