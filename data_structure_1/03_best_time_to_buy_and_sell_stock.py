class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = (0,1)
        arr_len = len(prices)
        if arr_len<=1:
            return 0

        max_profit = prices[1] - prices[0]

        while r<arr_len:
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0 :
                l += 1
            else:
                r += 1
            max_profit = max(max_profit, curr_profit)
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,1]))

