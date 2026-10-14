class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        best = 1
        for i in range(len(s) - 1):
            d = {s[i] : 1}
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
                    best = max(count, best)
        return best
