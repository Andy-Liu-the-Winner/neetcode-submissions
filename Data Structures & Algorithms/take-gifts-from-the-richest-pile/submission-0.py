class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        gifts = [-e for e in gifts]
        heapq.heapify(gifts)

        while k > 0:
            v = -heapq.heappop(gifts)
            v = math.floor(math.sqrt(v))
            heapq.heappush(gifts, - v)
            k -= 1
        return -sum(gifts)