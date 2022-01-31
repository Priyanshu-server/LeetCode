class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])

            m = (l + r) //2 
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res

print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([11,13,15,17]))

print(Solution().findMin([4,5,6,7,0,1,2]))