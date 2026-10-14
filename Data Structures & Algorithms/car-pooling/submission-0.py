class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda l: l[1])
        heap = [] # heap, key = end, each elem: [end, num of elem]
        curr = 0
        for passenger, start, end in trips:
            while heap and heap[0][0] <= start:
                end, p = heapq.heappop(heap)
                curr -= p
            if curr + passenger > capacity:
                return False
            curr += passenger
            heapq.heappush(heap, [end, passenger])
        return True

            