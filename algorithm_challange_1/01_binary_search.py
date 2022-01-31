class Solution:
    def search(self, nums: list[int], target: int) -> int:
        val = self._search(nums,target,0,len(nums)-1)
        return val

    def _search(self,nums:list[int], target:int, low:int ,high:int) -> int:
        mid =(low+high)//2

        if low>high:
            return -1
        
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return self._search(nums,target,mid+1,high)
        else:
            return self._search(nums,target,low,mid-1)



sol = Solution()

indx = sol.search([-1,0,3,5,9,12], 13)
print(indx)