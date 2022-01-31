class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i,j = 0,0
        length_of_arr = len(nums)

        while(j<length_of_arr):
            
            if nums[j] != 0:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
            j += 1
            print(nums)

        return nums


sol = Solution()
solved = sol.moveZeroes([0,1,0,3,12])