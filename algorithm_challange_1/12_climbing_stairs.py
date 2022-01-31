class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(target,memo):

            if target == n:
                return 1
            if target > n:
                return 0

            if target in memo:
                return memo[target]

            addition_of_steps = dfs(target+1,memo) + dfs(target+2,memo)

            return addition_of_steps

        sol = dfs(0,dict())

        return sol

    # Faster Solution
    # Understand with Tabulation
    def climb_stairs_tabulation(self,n: int) -> int:
        one,two = 1,1

        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

print(Solution().climbStairs(5))
print(Solution().climb_stairs_tabulation(5))