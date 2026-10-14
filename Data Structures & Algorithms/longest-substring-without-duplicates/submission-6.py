class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        d = {}
        l = 0
        r = 1
        if not n:
            return res
        d[s[0]] = 1
        while l < n and l <= r:
            right = s[r]
            if right not in d:
                r += 1
                if r == n:
                    break
                right = s[r]
                d[right] = 1
            else:
                l += 1
            res = max(res, r - l + 1)
        return res