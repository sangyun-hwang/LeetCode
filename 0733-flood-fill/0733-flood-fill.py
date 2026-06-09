class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows = len(image)
        cols = len(image[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def dfs(y, x):
            if not (0 <= y < rows and 0 <= x < cols):
                return

            if image[y][x] != original_color:
                return

            image[y][x] = color

            for dy, dx in directions:
                dfs(y + dy, x + dx)

        dfs(sr, sc)

        return image

