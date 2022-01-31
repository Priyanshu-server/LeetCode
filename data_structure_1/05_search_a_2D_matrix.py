from pickletools import markobject


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])

        def binarySeach(arr,target):
            low,high = 0, n-1
            while low<=high:
                mid = (high+low)//2

                if arr[mid] == target: return True
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid-1 

            return False

        for arr in matrix:
            if binarySeach(arr,target):
                return True
        return False



# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
print(Solution().searchMatrix([[1]],1))
