class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # O(nlogn)
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:   
            lastEnd = output[-1][1]         

            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])

        return output


print(Solution().merge([[1,3],[15,18],[2,6],[8,10]]))