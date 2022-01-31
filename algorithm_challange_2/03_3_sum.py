class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i,n in enumerate(nums):
            if i>0 and n== nums[i-1]:
                continue
            
            if n<=0:
                l,r = i+1, len(nums)-1

                while l<r:
                    total_sum = n + nums[l] + nums[r]
                    if total_sum == 0 :
                        res.append([n,nums[l],nums[r]])
                        l += 1
                        while l<r and nums[l] == nums[l-1]:
                            l+= 1
                    elif total_sum<0:
                        l += 1
                    else:
                        r -= 1
            else:
                break

        return res