class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = [] 

        def dfs(i, curr):
            if i == len(s):
                res.append(curr[:])
                return
                
            if s[i].isnumeric():
                dfs(i+1, curr + s[i])
            else:
                dfs(i+1, curr + s[i].upper())
                dfs(i+1, curr + s[i].lower())       
        dfs(0, '')        
        return res


print(Solution().letterCasePermutation("a1b2"))