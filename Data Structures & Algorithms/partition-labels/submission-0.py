class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {} # stores last index
        for i in range(len(s)):
            d[s[i]] = i
        i = 0
        currmax = 0
        res = []
        last_i = 0
        while i < len(s):
            c = s[i]
            j = d[c]
            currmax = max(currmax, j)
            if currmax <= i:
                # split
                res.append(currmax + 1 - last_i)
                last_i = currmax + 1

            i += 1
        return res