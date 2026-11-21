class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        s_prime = set([i for i in range(1, len(grid[0] * len(grid)) + 1)])
        res = []
        for l in grid:
            for e in l:
                if e in s:
                    res.append(e)

                s.add(e)
        
        for e in s_prime:
            if e not in s:
                res.append(e)
                break
        print(s, s_prime)
        return res
