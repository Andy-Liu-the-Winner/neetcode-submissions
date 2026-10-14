class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])

        for w in words:
            c &= w
        return list(c.elements())
        