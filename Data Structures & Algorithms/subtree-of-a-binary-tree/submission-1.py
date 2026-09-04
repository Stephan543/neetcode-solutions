# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        d = deque([root])
        while d:
            for _ in range(len(d)):
                node = d.popleft()
                if node.val == subRoot.val and self.isEqual(node, subRoot):
                    return True
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return False


    def isEqual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)