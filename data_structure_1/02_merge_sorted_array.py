class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # starting by filling from last as last elements are zeros so,
        # we do not need to replace any wanted digit
        
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1

            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # fill nums1 with leftover values of nums2
        while(n>0):
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
        
        return nums1

print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))