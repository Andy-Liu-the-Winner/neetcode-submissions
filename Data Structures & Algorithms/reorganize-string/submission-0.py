class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        for e in c:
            if c[e] > (len(s)  + 1)// 2:
                return ""
        res = ""
        while c:
            to_pop = []
            for e in sorted(c, key = c.get, reverse= True)[: 2]:
                res += e
                c[e] -= 1
                if c[e] == 0:
                    to_pop.append(e)
            for e in to_pop:
                del c[e]
        return res
                