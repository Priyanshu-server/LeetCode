class Solution:
    def sortedSquares(self, nums: list[int]) ->list[int]:
        squared_arr = list(map(lambda x: x**2,nums))
        return sorted(squared_arr)

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))