from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter(nums)
        return max(counter, key = counter.get)


print(Solution().majorityElement([3,2,3,4,]))