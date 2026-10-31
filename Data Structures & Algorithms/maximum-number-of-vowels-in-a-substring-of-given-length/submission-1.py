class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window
        se = set(["a", "e", "i", "o", "u"])
        m = 0
        
        for i in range(k):
            if s[i] in se:
                m += 1

        res = m
        for i in range(k, len(s)):
            if s[i] in se:
                m += 1
            if s[i - k] in se:
                m -= 1
            res = max(res, m)
        return res
                