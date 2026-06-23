# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            prev = head
            current = head.next
            prev.next = None
            next = None
            while current:
                if current.next:
                    next = current.next
                else:
                    next = None
                current.next = prev
                prev = current
                current = next
            return prev
            