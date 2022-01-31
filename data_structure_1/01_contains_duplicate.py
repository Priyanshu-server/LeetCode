class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        return len(set(nums)) < len(nums)

sol  = Solution()

print(sol.containsDuplicate([1,2,3,1]))