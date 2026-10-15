class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find a path from top left to bottom right
        # that has min max
        # 2d dp
        m = len(grid) # m == b btw
        # dp[i][j] = min to reach i, j
        dp = [[float("inf")] * m for i in range(m)]
        dp[0][0] = grid[0][0]

        q = deque([(0, 0)])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            i, j = q.popleft()
            for di, dj in dir:
                ni, nj = i + di , j + dj
                if 0 <= ni < m and 0 <= nj < m:
                    new_max = max(dp[i][j], grid[ni][nj])

                    if new_max < dp[ni][nj]:
                        dp[ni][nj] = new_max
                        q.append((ni, nj))
        return dp[m - 1][m - 1]