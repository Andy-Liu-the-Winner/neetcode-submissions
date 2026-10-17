class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # form graph
        # delete ptr when transverse
        class node:
            def __init__(self, val, next = None):
                self.val = val
                self.next = next if next is not None else []
        
        node_set = set()
        node_list = {} # airport: node
        for i, (a, b) in enumerate(tickets):
            if a not in node_set:
                node_set.add(a)
                node_list[a] = node(a)
            if b not in node_set:
                node_set.add(b)
                node_list[b] = node(b)
            heapq.heappush(node_list[a].next, (b, i, node_list[b]))
        
        # transverse
        res = []

        def dfs(curr):
            while curr.next:
                _, _, nxt = heapq.heappop(curr.next)
                dfs(nxt)
            res.append(curr.val)
        dfs(node_list["JFK"])
        return res[::-1]