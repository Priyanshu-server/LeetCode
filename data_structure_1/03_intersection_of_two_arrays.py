class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)

        counter = {}

        for i in nums1:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        sol = []

        for n in nums2:
            if n in counter and counter[n] > 0:
                sol.append(n)
                counter[n] -= 1
        return sol



print(Solution().intersect([1,2,2,1],[2,2]))