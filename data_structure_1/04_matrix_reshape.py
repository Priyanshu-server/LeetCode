class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        curr_shape = [len(mat),len(mat[0])]

        if r*c != curr_shape[0] * curr_shape[1] or [r,c] == curr_shape:
            return mat
        
        arr = [[0]*c for _ in range(r)]
        
        row_num,col_num = 0,0

        for i in range(curr_shape[0]):
            for j in range(curr_shape[1]):
                arr[row_num][col_num] = mat[i][j] 
                col_num += 1
                
                if col_num == c:
                    (row_num, col_num) = (row_num+1, 0)

        return arr

print(Solution().matrixReshape([[1,2],[3,4]],4,1))