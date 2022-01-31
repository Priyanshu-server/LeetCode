def spiral_matrix(n:int) -> list[list[int]]:
    res = [[0 for _ in range(n)] for _ in range(n)]
    rowEnd = colEnd = n-1
    rowStart = colStart = 0
    val = 1

    while(rowStart<=rowEnd and colStart <= colEnd):

        for i in range(colStart,colEnd+1):
            res[rowStart][i] = val
            val += 1
        rowStart+=1

        for i in range(rowStart,rowEnd+1):
            res[i][colEnd] = val
            val += 1

        colEnd -= 1

        for i in range(colEnd,colStart-1,-1):
            res[rowEnd][i] = val
            val += 1
        rowEnd -= 1

        for i in range(rowEnd,rowStart-1,-1):
            res[i][colStart] = val
            val += 1

        colStart += 1
        

    return res



print(spiral_matrix(n = 3))