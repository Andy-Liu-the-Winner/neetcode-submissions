class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        d = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        res = float("inf")
        for char in d:
            res = min(res, c[char] // d[char])
        return res if res != float("inf") else 0