class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            maxFreq = max(maxFreq, d[s[r]])

            while (r - l + 1) - maxFreq > k:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
