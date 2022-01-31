class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        rowBegin = colBegin = 0
        rowEnd = colEnd = n-1

        counter = 1

        while(rowBegin<= rowEnd and colBegin<=colEnd):

            for i in range(colBegin,colEnd + 1):
                res[rowBegin][i] = counter
                counter += 1

            rowBegin += 1


            for i in range(rowBegin,rowEnd + 1):
                res[i][colEnd] = counter
                counter += 1
            
            colEnd -= 1

            for i in range(colEnd,colBegin-1,-1):
                res[rowEnd][i] = counter
                counter += 1
            rowEnd -= 1

            for i in range(rowEnd,rowBegin-1,-1):
                res[i][colBegin] = counter
                counter += 1

            colBegin += 1


        return res




print(Solution().generateMatrix(3))