class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # This will return me the digit for range
            # is 1 or 0
            # if it is 1 then we will add in res
            # at reverse location means 31-i
            
            bit = (n>>i) & 1
            res = res | (bit << 31-i)

        return res
        
print(Solution().reverseBits(10000000000000000000000000000000))
