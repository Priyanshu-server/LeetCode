class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
                
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
                
        # because if the right value is right most and left is right-1 then we will compare b/w
        # right-1 and right .. we cannot got for upper loop as if mid = right (len(nums)-1) then 
        #  It will give error at (mid+1) so for (left + right) // 2 it is always going to be 
        #  left if they are like ...n,n+1
        return left if nums[left] >= nums[right] else right 



print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([0,1,2,3]))
