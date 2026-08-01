class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # dict maps char to index list (sorted garunteed, increasing order)
        d = {}
        for i, char in enumerate(s):
            d.setdefault(char, []).append(i)

        need = Counter(t)
        for char in need:
            if char not in d:
                return ""

        positions = sorted((i, c) for c in need for i in d[c])

        have = Counter()
        formed = 0
        required = len(need)
        best = None
        left = 0
        for right in range(len(positions)):
            c = positions[right][1]
            have[c] += 1
            if have[c] == need[c]:
                formed += 1
            while formed == required:
                l_idx, r_idx = positions[left][0], positions[right][0]
                if best is None or r_idx - l_idx < best[1] - best[0]:
                    best = (l_idx, r_idx)
                lc = positions[left][1]
                have[lc] -= 1
                if have[lc] < need[lc]:
                    formed -=1
                left += 1
        return "" if best is None else s[best[0]: best[1] + 1] 

