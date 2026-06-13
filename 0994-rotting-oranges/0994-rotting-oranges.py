from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()
        fresh = 0
        minutes = 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    queue.append((y, x, 0))
                elif grid[y][x] == 1:
                    fresh += 1

        while queue:
            y, x, time = queue.popleft()
            minutes = max(minutes, time)

            for dy, dx in directions:
                ny = y + dy
                nx = x + dx

                if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    fresh -= 1
                    queue.append((ny, nx, time + 1))

        if fresh > 0:
            return -1

        return minutes