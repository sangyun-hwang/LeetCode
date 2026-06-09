from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if 0 <= ny < rows and 0 <= nx < cols and image[ny][nx] == original_color:
                    image[ny][nx] = color
                    q.append((ny, nx))
        
        return image

