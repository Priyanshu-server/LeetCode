class Solution:
    def sortColors(self, nums: list[int]) -> None:
        self.mergeSort(nums)
        return nums
        

    def mergeSort(self,arr):
        if len(arr) > 1:
            r = len(arr)//2
            L = arr[:r]
            R = arr[r:]
            
            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i< len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+= 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i<len(L):
                arr[k]  = L[i]
                i += 1
                k += 1
            
            while j<len(R):
                arr[k] = R[j]
                j += 1
                k += 1



print(Solution().sortColors([2,0,2,1,1,0]))