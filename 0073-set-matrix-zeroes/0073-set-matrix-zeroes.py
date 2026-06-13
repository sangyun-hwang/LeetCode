class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(matrix)
        cols = len(matrix[0])

        zeros = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for i, j in zeros:
            for dy, dx in directions:
                y, x = i, j
                while 0 <= y + dy < rows and 0 <= x + dx < cols:
                    y += dy
                    x += dx
                    matrix[y][x] = 0
        

