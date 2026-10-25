class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1, c2 = Counter(s), Counter(t)
        for c in c2:
            if c1[c] != c2[c]:
                return c