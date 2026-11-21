# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = 1
        n1, n2 = 0, 0
        while l1:
            n1 += digit * l1.val
            l1 = l1.next
            digit *= 10

        digit = 1
        while l2:
            n2 += digit * l2.val
            l2 = l2.next
            digit *= 10
        ans = str(n1 + n2)[::-1]

        node = ListNode(0)
        tmp = node
        for i in range(len(ans)):
            node.next = ListNode(ans[i])
            node = node.next
        return tmp.next
            