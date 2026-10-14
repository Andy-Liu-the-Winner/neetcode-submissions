class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        matrix = [[0 if i != 0 and j != 0 else 1 for i in range(n)] for j in range(m)]
        q = []
        # initiating boundaries as 1
        for i in range(m):
            matrix[i][n - 1] = 1
        for j in range(n):
            matrix[m - 1][j] = 1
        def out_of_index(i, j):
            return i < 0 or j < 0 or i >= m or j >= n
        # could have "seen" so less compute but 
        def bfs(matrix, i, j):
            if out_of_index(i , j):
                return 
            # reverse bfs
            if i == 0 and j == 0:
                return matrix[0][1] + matrix[1][0]
            elif i != m - 1 and j != n - 1:
                matrix[i - 1][j] = matrix[i - 1][j] + matrix[i][j + 1] # right + down
                matrix[i][j - 1] = matrix[i][j] + matrix[i + 1][j - 1]
                bfs()


                
            


