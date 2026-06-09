from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(start_y, start_x):
            q = deque([(start_y, start_x)])
            grid[start_y][start_x] = "0"

            while q:
                y, x = q.popleft()

                for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == "1":
                        grid[ny][nx] = "0"
                        q.append((ny, nx))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    answer += 1

        return answer

        