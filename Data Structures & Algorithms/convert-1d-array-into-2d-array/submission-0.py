class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        res = []
        for i in range(m):
            l = []
            for j in range(n):
                l.append(original[i * n + j])
            res.append(l)
        return res 
