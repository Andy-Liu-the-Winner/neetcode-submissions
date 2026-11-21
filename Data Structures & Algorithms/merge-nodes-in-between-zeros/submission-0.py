# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr= head
        v = 0
        start = False
        res = ListNode(0, None)
        tmp = res
        while ptr:
            if not ptr.val:
                # start or end
                if not start:
                    start = True
                else:
                    # end
                    res.next = ListNode(v)
                    res = res.next
                    v = 0
            if ptr.val:
                v += ptr.val 
            ptr = ptr.next
        return tmp.next
            