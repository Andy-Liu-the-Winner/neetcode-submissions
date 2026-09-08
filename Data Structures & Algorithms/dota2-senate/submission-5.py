class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n = len(senate)
        r, d = 0, 0 # blocks
        count = 0
        q = deque(senate)
        rc, dc = senate.count("R"), senate.count("D")
        while dc > 0 and rc > 0:
            e = q.popleft()
            if e == 'R':
                if r > 0:
                    r -= 1
                    rc -= 1
                    continue
                d += 1
                q.append(e)
            else:
                if d > 0:
                    d -= 1
                    dc -= 1
                    continue
                r += 1
                q.append(e)
        return "Dire" if dc > 0 else "Radiant"
            

        