import enum


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0] * (len(triangle) + 1) 
        
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))