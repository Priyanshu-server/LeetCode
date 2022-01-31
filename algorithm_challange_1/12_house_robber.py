class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0: 
                dp[i] = nums[i]
            elif i == 1: 
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


print(Solution().rob([1,2,3,1]))
