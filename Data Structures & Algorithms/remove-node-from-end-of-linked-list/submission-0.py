# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next
        
        p = len(stack)-n
        if p == 0:
            return head.next

        stack[p-1].next = stack[p].next
        return head

