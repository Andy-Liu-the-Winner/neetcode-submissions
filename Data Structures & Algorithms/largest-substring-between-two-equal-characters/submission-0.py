class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        d = {}

        for i, char in enumerate(s):
            if char in d:
                res = max(res, i - d[char] - 1)
            else:
                d[char] = i
        return res 