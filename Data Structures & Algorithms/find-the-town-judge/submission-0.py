class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {} # b : [all a s.t. trust b]
        two = set()
        for a, b in trust:
            d[b] = d.get(b, []) + [a]
            if len(d[b]) == n - 1:
                two.add(b)
        
        for a, b in trust:
            if a in two:
                two.remove(a)
        if len(two) != 0:
            return two.pop()
        return -1
        
