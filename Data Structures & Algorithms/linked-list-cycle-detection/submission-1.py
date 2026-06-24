# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
            if fast == slow:
                return True
            else:
                slow = slow.next
        return False
            
            