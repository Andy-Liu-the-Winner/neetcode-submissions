class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: zeros.append((i, j))
        def set_row_col_zero(i, j):
            for a in range(m):
                matrix[a][j] = 0
            for b in range(n):
                matrix[i][b] = 0
        for i, j in zeros:
            set_row_col_zero(i, j)