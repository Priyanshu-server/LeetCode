def isBadVersion(n:int):
    return n >= 5

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high = 0,n

        while(low<=high):
            mid = (low+high)//2
            
            if not isBadVersion(mid):
                low = mid +1
            else:
                high = mid -1
                
        return low


sol = Solution()
print(sol.firstBadVersion(130))
