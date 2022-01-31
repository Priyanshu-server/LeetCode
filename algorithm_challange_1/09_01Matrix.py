class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        R,C=len(mat),len(mat[0])
        
        output=[[0 for col in range(C)] for row in range(R)]
        cur_level=0
        cur_set={(row,col) for row in range(R) for col in range(C) if mat[row][col]==0}
        visited = cur_set.copy()
        
        while cur_set:
            cur_level+=1
            next_set=set()
            for row,col in cur_set:
                for new_row,new_col in {(row+1,col),(row-1,col),(row,col+1),(row,col-1)}:
                    if 0<=new_row<=R-1 and 0<=new_col<=C-1 and ((new_row,new_col) not in visited):
                        visited.add((new_row,new_col))
                        next_set.add((new_row,new_col))
                        output[new_row][new_col]=cur_level
            cur_set=next_set
            
        return output

print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

# See the area of island solution also ...

# Another Solution
import math

class Solution:
    def updateMatrix(self,mat):
        m, n = len(mat), len(mat[0])
        dp = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])

        return dp


print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
