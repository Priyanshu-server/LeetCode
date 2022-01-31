class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # res += n%2 #This will also work
            res += n&1
            n = n>>1
        return res



# print(Solution().hammingWeight(n))