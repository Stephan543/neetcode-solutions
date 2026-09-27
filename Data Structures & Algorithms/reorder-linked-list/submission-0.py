# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # create an array of nodes in order
        # loop through the array, and build the new LL
        newHead = head
        store = []
        while head:
            store.append(head)
            head = head.next
        
        head = newHead
        n = len(store)
        i = 1
        inc = 2
        while n//2 >= i:
            if inc == 2:
                newHead.next = store[n-i]
                newHead = newHead.next
                inc -= 1
            elif inc == 1:
                if i == n - i: break
                newHead.next = store[i]
                newHead = newHead.next
                i +=1
                inc = 2
        newHead.next = None      
        
        return None
            
