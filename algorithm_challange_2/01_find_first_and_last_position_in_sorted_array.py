class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        return list((self.binSearch(nums,target,True),self.binSearch(nums,target,False)))

    def binSearch(self,nums,target, leftBias):
        l,r = 0,len(nums) - 1
        i = -1
        while l<= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target< nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i


print(Solution().searchRange([5,7,7,8,8,10], 8))