from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        answer = 0

        def bfs(y, x):
            q = deque([(y, x)])
            grid[y][x] = 0
            area = 1

            while q:
                y, x = q.popleft()
                for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == 1:
                        grid[ny][nx] = 0
                        area += 1
                        q.append((ny, nx))
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    answer = max(answer, bfs(i, j))

        return answer


        
        