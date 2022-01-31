class Solution:
    def reverseString(self, s: list[str]) -> None:
        (i,j) = (0, len(s)-1)
        while i<j:
            (s[i],s[j]) = (s[j],s[i])
            i += 1
            j -= 1
        return s


sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))