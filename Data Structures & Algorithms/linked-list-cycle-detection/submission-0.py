# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = set()

        while head:
            if head.next and head.next in h:
                return True
            elif not head.next:
                return False
            h.add(head)
            head = head.next