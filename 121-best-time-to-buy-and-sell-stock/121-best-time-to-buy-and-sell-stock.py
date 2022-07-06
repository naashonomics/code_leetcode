class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minimum_so_far=prices[0]
        for i in range(1,len(prices)):
            currentprofit=prices[i]-minimum_so_far
            if currentprofit  > ans:
                ans=currentprofit
            minimum_so_far=min(minimum_so_far,prices[i])
        return ans 