# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        #  1 5 2 3
        prev = None
        while ptr:
            if not prev:
                prev = ptr
                ptr = ptr.next
            else:
                if prev.val > ptr.val:
                    # find where to put before prev 
                    new_ptr = head
                    if head.val > ptr.val:
                        tmp = head
                        head = ListNode(ptr.val)
                        head.next = tmp
                        prev.next = ptr.next 
                    else:
                        new_prev = None
                        while new_ptr:
                            if not new_prev:
                                new_prev = new_ptr
                                new_ptr = new_ptr.next
                            if new_ptr.val > ptr.val:
                                tmp = new_ptr
                                new_prev.next = ListNode(ptr.val)
                                new_prev.next.next = tmp
                                prev.next = ptr.next 
                                break
                            else:
                                new_prev = new_ptr 
                                new_ptr = new_ptr.next
                    ptr = prev.next
                else:
                    prev = ptr
                    ptr = ptr.next
                    
        return head