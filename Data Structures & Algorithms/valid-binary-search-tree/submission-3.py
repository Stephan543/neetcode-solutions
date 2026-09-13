# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node:
                return True
            if not (node.val < upper and node.val > lower):
                return False
            
            return isValid(node.left, lower, min(node.val,upper)) and isValid(node.right, max(lower, node.val), upper)

        return isValid(root, float('-inf'), float('inf'))