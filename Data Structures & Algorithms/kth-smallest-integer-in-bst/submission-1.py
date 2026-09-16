# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        decrement = False
       
        while stack:
            node = stack[-1]
            if not node.right and not node.left:
                decrement = True

            if decrement:
                leaf = stack.pop()
                k = k-1
                if k == 0:
                    return leaf.val

            if node.right:
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
            