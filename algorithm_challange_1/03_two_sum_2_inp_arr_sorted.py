class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length_of_arr = len(numbers)
        i,j = 0, length_of_arr-1

        while i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
                
            if numbers[i] + numbers[j] > target:
                j -=1

            else:
                i+= 1
        




sol = Solution()
print(sol.twoSum([2,7,11,15], 9))