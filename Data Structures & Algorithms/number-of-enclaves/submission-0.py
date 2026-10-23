class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def is_valid(i, j):
            if 0<=i<m and 0<=j<n: return True
            return False

        def dfs(i, j):
            if not is_valid(i, j): return True
            if grid[i][j] == 0 or (i, j) in seen:
                return False
            if (i, j) not in seen:
                seen.add((i,j))
                curr_set.add((i, j))
                escape = False
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    if dfs(i + di, j + dj):
                        escape = True

                return escape


        seen = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) in seen: continue
                    curr_set = set()
                    if dfs(i, j): continue
                    else:
                        count += len(curr_set)
        return count 