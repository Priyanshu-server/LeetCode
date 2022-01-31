class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l,r = 0, len(matrix) - 1
        while l<r:
            for i in range(r-l):
                top,bottom = l,r

                #save the top left value
                top_left = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = top_left
            
            r,l = (r-1,l+1)
        return matrix

    def another_rotate(self, matrix: list[list[int]]) -> None:
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().another_rotate([[1,2,3],[4,5,6],[7,8,9]]))
