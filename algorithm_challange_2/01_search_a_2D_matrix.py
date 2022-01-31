class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])

        def binarySearch(arr,target):
            l,r = 0,len(arr)-1

            while l<=r:
                mid = (l + r)//2
                
                if arr[mid] == target:
                    return True

                if arr[mid]<target:
                    l = l +1
                else:
                    r = r-1
            return False

        for i in range(m):
            if target<=matrix[i][-1] and target>=matrix[i][0]:
                if binarySearch(matrix[i],target):
                    return True

        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]]))