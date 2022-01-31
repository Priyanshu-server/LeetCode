class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        max_len  = 0
        while r< len(s):
            if s[r] not in s[l:r]:
                r += 1
                max_len = max(max_len, r-l)
            else:
                l += 1
            
        return max_len



print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring(" "))