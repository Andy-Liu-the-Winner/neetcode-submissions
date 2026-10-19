class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        weak = set()
        for u, v in edges:
            weak.add(v)
        
        if n - len(weak) != 1:
            return -1
        
        for i in range(n):
            if i not in weak:
                return i