class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque((tickets[i], i) for i in range(len(tickets)))
        t = 0
        while q:
            t += 1
            a, b = q.popleft()
            a -= 1
            if b == k and a == 0:
                return t
            if a > 0:
                q.append((a, b))

        

