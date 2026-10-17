class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = []
        c, d = newInterval
        # a b c d
        for a, b in intervals:
            if b < c:
                s.append([a, b])
            elif d < a:
                s.append([c, d])
                c, d = a, b
            else:
                c = min(a, c)
                d = max(b, d)
        s.append([c, d])
        return s