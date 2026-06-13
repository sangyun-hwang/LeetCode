class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        stack = m * n - 1
        y, x, d = 0, 0, 0

        answer = [matrix[0][0]]
        matrix[0][0] = - 101
        while stack:
            dy, dx = directions[d]
            if 0 <= y + dy < m and 0 <= x + dx < n and matrix[y + dy][x + dx] != -101:
                y += dy
                x += dx
                answer.append(matrix[y][x])
                matrix[y][x] = -101
                stack -= 1
            else:
                d += 1
                if d > 3:
                    d = 0
        
        return answer


            
            


        