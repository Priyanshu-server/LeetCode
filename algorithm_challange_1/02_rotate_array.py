class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length  = len(nums)
        if k > length:
            k = k%length

        self.reverse(nums,0,length-1)
        print("First Reversed Array : ",nums)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,length-1)

        return nums

    def reverse(self,nums,start, end):
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end   -= 1


sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7],3))

"""
    Basic thing is that first if we reverse the array we will have the shifted last terms
    at one side and the after elements at next side then we will reverse the first k elems
    and then revers the next elems from k to len-1. This will give us the output.
"""