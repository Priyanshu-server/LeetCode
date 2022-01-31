
class Solution:
    def reverseWords(self,s: str) -> str:
        split_s = s.split()
        split_2_s = [list(word) for word in split_s]
        new_str = '' 
        for word in split_2_s:
            (i,j) = (0,len(word)-1)
            while(i<j):
                (word[i],word[j]) = (word[j], word[i])
                i += 1
                j -= 1
            new_str += "".join(word) + " "
       
        return  new_str.strip()

    def new_reverseWords(self,s:str) -> str:
        return " ".join(s[::-1].split()[::-1])


s = "Let's take LeetCode contest"

# Both are the solution
# First one is using logic
# Second one is using pyhton methods
print(Solution().reverseWords(s))
print(Solution().new_reverseWords(s))