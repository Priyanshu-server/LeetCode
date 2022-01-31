from collections import Counter


class Solution:
# Easy also not fastest but fast enough
    def checkInclusion2(self,s1:str,s2:str) -> bool:
        s1Counter = Counter(s1)
        i,j = 0,len(s1)

        while j<=len(s2):
            s2Counter = Counter(s2[i:j])
            if s1Counter == s2Counter:
                return True
            i += 1
            j += 1
        return False


# Fastest
    def checkInclusion3(self,s1:str,s2:str) -> bool:
        len_s1,len_s2 = len(s1),len(s2)
        if len_s2<len_s1:
            return False

        s1Hash,s2Hash = [0]*26,[0]*26
        left,right = 0,0

        while right < len_s1:
            s1Hash[ord(s1[right]) - ord('a')] += 1
            s2Hash[ord(s2[right]) - ord('a')] += 1
            right += 1
        print(s1Hash,s2Hash,sep = "\n")
        right -= 1

        while(right<len_s2):
            if(s1Hash==s2Hash):
                return True
            right += 1

            if(right!=len_s2):
                s2Hash[ord(s2[right])-ord('a')] += 1
            
            s2Hash[ord(s2[left]) - ord('a')] -= 1
            left += 1

        return False


# print(Solution().checkInclusion("ab","eidbaooo"))
# print(Solution().checkInclusion2("adc","dcda"))
# print(Solution().checkInclusion3("adc","dcda"))
print(Solution().checkInclusion3("ab","adcba"))


# print(Solution().checkInclusion2("abcdxabcde","abcdeabcdx"))



