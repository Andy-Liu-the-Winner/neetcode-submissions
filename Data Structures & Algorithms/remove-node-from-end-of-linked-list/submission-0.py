# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        l = 0
        while ptr:
            l += 1
            ptr = ptr.next
        ptr = head
        for i in range(l - n - 1):
            ptr = ptr.next
        if ptr.next == None:
            return None
        ptr.next = ptr.next.next
        return head
        