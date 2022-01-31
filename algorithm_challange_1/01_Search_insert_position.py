class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low < high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        if nums[mid] > target:
            return mid
        else:
            return mid+1


sol = Solution()

print(sol.searchInsert([1,3,5,6],7))