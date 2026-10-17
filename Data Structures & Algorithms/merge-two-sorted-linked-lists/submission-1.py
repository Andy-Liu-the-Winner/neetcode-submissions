# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        dummy = ListNode(0)
        ptr = dummy
        while ptr1 or ptr2:
            if not ptr2:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
                ptr = ptr.next 
                continue
            if not ptr1:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
                ptr = ptr.next 
                continue
            if ptr1.val <= ptr2.val:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
                ptr = ptr.next 
            else:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
                ptr = ptr.next 
        return dummy.next
                