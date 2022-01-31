
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {']':'[',')':'(','}':'{'}
        stack = []
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if stack == [] or dictionary[char]!=stack.pop():
                    return False
            else:
                return False

        return stack == []


print(Solution().isValid("()[]"))