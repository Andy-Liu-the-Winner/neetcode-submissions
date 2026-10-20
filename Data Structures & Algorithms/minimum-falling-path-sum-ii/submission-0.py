class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            if i == 0:
                dp[0] = grid[0]
                continue
                
            for j in range(n):
                last_min = 99999999
                for k in range(n):
                    if k == j:
                        continue
                    last_min = min(last_min, dp[i - 1][k])
                dp[i][j] = last_min + grid[i][j]

        return min(dp[-1])
                    
                
