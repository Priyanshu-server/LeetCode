class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if (r< 0 or r == rows or c<0 or c==cols or 
                grid[r][c] == 0 or (r,c) in visit):
                return 0

            # Adding only one's value will reduce the visited set space
            
            visit.add((r,c))

            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) )
        area = 0

        # Looping through every point in grid
        #  if the grid[r][c] value is not equals to 0 then we will check if the node is not visited
        # and if both the conditions will satisfy then we will calculate the area of the grid within the
        # boundary of 0's and add the 1's in there
        
        for r in range(rows):
            for c in range(cols):
                if (rows,cols) not in visit or grid[r][c] != 0:
                    area = max(area, dfs(r,c))
        return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]


print(Solution().maxAreaOfIsland(grid))
