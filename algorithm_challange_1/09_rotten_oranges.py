from collections import deque

class Solution:
    def getting_queue_and_fresh(self,grid,rows,cols):
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r,c])
        return q,fresh

    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        # Here we are recieving queue with the co-ords of rotten oranges
        # and fresh orange count

        q,fresh  = self.getting_queue_and_fresh(grid,ROWS,COLS)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    row, col = dr+r,dc+c
                    if (row<0 or row == ROWS
                        or col<0 or col == COLS or
                        grid[row][col] != 1
                        ):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))