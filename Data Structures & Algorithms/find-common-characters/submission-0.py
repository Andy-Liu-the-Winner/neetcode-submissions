class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
        for w in words:
            w = list(w)
            for c in res:
                if c not in w:
                    res.remove(c)
                else:
                    w.remove(c)
        return res