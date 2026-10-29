class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sorted_phd = sorted([(positions[i], healths[i], directions[i]) for i in range(len(positions))],key=lambda x: x[0])
        s = []
        for p, h, d in sorted_phd:
            
            while s and s[-1][2] == "R" and d == "L":
                # -> <- 
                if s[-1][1] == h:
                    s.pop()
                    h = 0
                    break
                elif s[-1][1] > h:
                    # ->
                    p1, h1, d1 = s[-1]
                    s[-1] = (p1, h1 - 1, d1)
                    h = 0
                    break
                else:
                    # <-
                    s.pop()
                    h -= 1
            if h > 0:
                s.append((p, h, d))
        
        index = {positions[i]: i for i in range(len(positions))}
        s.sort(key=lambda x: index[x[0]])
        res = [s[i][1] for i in range(len(s))]
        return res
