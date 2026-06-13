class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2
            y = mid // len(matrix[0])
            x = mid % len(matrix[0])

            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
        