class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = set()
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in d:
                d.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                d.remove(s[l])
                l += 1

        return res
