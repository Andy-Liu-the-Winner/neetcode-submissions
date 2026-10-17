class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        waiting = defaultdict(list)
        # l = {e: elem s.t. greater than e and further (index) than e}
        for i, (a, b) in enumerate(queries):
            if a == b:
                res[i] = a
            else:
                a, b = min(a, b), max(a, b)
                # idx >= b
                if heights[b] > heights[a]:
                    res[i] = b
                else:

                    waiting[b].append((heights[a], i))

        heap = []
        
        for j in range(len(heights)):
            for item in waiting[j]:
                heapq.heappush(heap, item)
            while heap and heap[0][0] < heights[j]:
                h, i = heapq.heappop(heap)
                res[i] = j
        return res
                


