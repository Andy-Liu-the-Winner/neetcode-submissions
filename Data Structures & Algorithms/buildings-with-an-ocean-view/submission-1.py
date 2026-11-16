class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        m = 0
        res = []
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                m = heights[i]
                res.append(i)
            else:
                if heights[i] > m:
                    res.append(i)
                    m = heights[i]
                    
        res.sort()
        return res
            