class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        sol = []

        for row in range(numRows):
            subSol = []
            for col in range(row+1):
                if col == 0 or col == row:
                    subSol.append(1)
                else:
                    subSol.append(sol[row-1][col-1] + sol[row-1][col])
            sol.append(subSol)



        return sol



print(Solution().generate(5))
         