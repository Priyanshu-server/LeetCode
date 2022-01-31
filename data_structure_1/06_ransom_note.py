from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counter = Counter(magazine)
        for i in ransomNote:
            if i in counter and counter[i] > 0:
                counter[i] -= 1
            else:
                return False
        return True
print(Solution().canConstruct("a","b"))
print(Solution().canConstruct("aa","ab"))
print(Solution().canConstruct("aa","aab"))