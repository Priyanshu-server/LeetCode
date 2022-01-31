class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrace(start,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return 

            for i in range(start,n+1):
                comb.append(i)
                backtrace(i+1,comb)
                comb.pop()
        backtrace(1,[])
        return res


print(Solution().combine(4,2))