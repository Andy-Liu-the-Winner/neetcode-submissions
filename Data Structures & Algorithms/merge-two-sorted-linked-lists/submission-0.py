# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2= list1, list2
        if not ptr1 and not ptr2: return None
        res = None
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                curr = min(ptr1.val, ptr2.val)
                if ptr1.val < ptr2.val:
                    ptr1 = ptr1.next
                else:
                    ptr2 = ptr2.next
            elif not ptr1:
                curr = ptr2.val
                ptr2 = ptr2.next
            elif not ptr2:
                curr = ptr1.val
                ptr1 = ptr1.next
            if not res:
                res = ListNode(curr)
                ptr3 = res
            else:
                ptr3.next = ListNode(curr)
                ptr3 = ptr3.next

        return res