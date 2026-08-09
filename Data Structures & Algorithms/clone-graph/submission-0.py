"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         if not node: return None
         mp = {}
         def dfs(n):
            if n in mp:
                return mp[n]
            c = Node(n.val)
            mp[n] = c
            c.neighbors = [dfs(nb) for nb in n.neighbors]
            return c 
         return dfs(node)

