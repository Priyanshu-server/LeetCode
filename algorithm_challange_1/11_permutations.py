class Solution:
    def permute(self,nums : list[int]) -> list[list[int]]:
        res = []
        
        # Base Case
        if len(nums) == 1:
            return [nums[:]]
            return

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            nums.append(n)
            res.extend(perms)
        return res


print(Solution().permute([1,2,3]))