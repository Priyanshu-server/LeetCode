from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in visited:
                return i
            visited.add(s[i])
        return -1

    def firstUniqChar_sol2(self, s: str) -> int:
        counter = Counter(s)
        for i,j in counter.items():
            if j==1:
                return s.index(i)
        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))


print(Solution().firstUniqChar_sol2("leetcode"))
print(Solution().firstUniqChar_sol2("loveleetcode"))
print(Solution().firstUniqChar_sol2("aabb"))
