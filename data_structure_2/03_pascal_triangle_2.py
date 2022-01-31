class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []

        for row in range(rowIndex+1):
            subSol = []
            for col in range(row+1):
                if col==0 or col == row:
                    subSol.append(1)
                else:
                    subSol.append(res[row-1][col-1] + res[row-1][col])
            res.append(subSol)
        
        return res[-1]


# Only need to return the last row or i can say rowIndex(th) ROW

print(Solution().getRow(3))