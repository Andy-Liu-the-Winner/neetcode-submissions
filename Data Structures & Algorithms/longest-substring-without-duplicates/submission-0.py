class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 1
        for i in range(len(s) - 1):
            d = {}
            count = 1
            for j in range(i + 1, len(s)):
                curr = s[j]
                if curr in d:
                    count = max(count, len(d))
                    best = max(count, best)
                    break
                else:
                    d[curr] = 1
                    count += 1
        return best - 1
