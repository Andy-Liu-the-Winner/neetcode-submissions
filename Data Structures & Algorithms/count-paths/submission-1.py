class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            matrix[i][n - 1] = 1
        for j in range(n):
            matrix[m - 1][j] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

        return matrix[0][0]