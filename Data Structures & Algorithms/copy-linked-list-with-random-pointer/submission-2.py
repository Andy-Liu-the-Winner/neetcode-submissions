"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = {}

        # construct 
        ptr = head
        while ptr:
            h[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            new_node = h[ptr]
            new_node.next = h.get(ptr.next)
            new_node.random = h.get(ptr.random)
            ptr = ptr.next
        return h.get(head)
