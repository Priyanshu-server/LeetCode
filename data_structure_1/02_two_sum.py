class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i,num in enumerate(nums):
            diff = target-num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        return -1

print(Solution().twoSum([2,7,11,15],9))