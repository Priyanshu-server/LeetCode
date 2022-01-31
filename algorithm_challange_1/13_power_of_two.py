import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        val = math.log2(n)
        if math.ceil(val) != math.floor(val):
            return False
        else:
            return True
    
    def isPowerOfTwo2(self, n: int) -> bool:

        if(n==0): return False

        while(n>1 and (n&1)==0):
            n>>=1
        
        return True if n==1 else False


print(Solution().isPowerOfTwo(12))
print(Solution().isPowerOfTwo(16))

print(Solution().isPowerOfTwo2(12))
print(Solution().isPowerOfTwo2(16))