# Array must have one single number and other numbers cannot have more than one repetation
from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = Counter(nums)
        for i,v in counter.items():
            if v == 1:
                return i


    # we use the trick that 'x XOR 0' is x, also 'x XOR x' will be 0.
    # thus all the same numbers when XOR will itself return 0.
    def new_sol(self,nums):
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        
        return ans


print(Solution().singleNumber([2,2,1]))
print(Solution().new_sol([2,1,2]))
