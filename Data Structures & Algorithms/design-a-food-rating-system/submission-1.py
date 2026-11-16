from collections import defaultdict
from heapq import heapify, heappush, heappop

class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # highest rating + lex smallest == - rating + lex smallest as min heap
        # foods = [(f, i) for f, i in enumerate(foods)]
        # cuisines = [(c, i) for c, i in enumerate(cuisines)]
        # ratings = [(r, i) for r, i in enumerate(ratings)]
        
        # tgt = [(-ratings[i], cuisines[i], foods[i]) for i in range(len(foods))]
        # tgt.sort()
        self.heap = defaultdict(list)
        self.info = {} # food: cui, rating

        for f, c, r in zip(foods, cuisines, ratings):
            self.info[f] = (c, r)
            self.heap[c].append((-r, f))
        
        for heap in self.heap.values():
            heapify(heap)

        
    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.info[food]
        self.info[food] = (c, newRating)

        heap = self.heap[c]
        heappush(heap, (-newRating, food))

        while -heap[0][0] != self.info[heap[0][1]][1]:
            heappop(heap)

    def highestRated(self, cuisine: str) -> str:
        return self.heap[cuisine][0][1]
        
