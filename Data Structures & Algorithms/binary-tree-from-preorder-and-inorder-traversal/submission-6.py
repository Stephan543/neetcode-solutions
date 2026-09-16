# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i

        def helper(pre: List[int], ino: List[int]):

            if not pre or not ino:
                return None
            
            root = TreeNode(pre[0])
            mid = ino.index(pre[0])

            root.left = self.buildTree(pre[1:mid+1], ino[:mid+1])
            root.right = self.buildTree(pre[mid+1:], ino[mid+1:])

            return root
        return helper(preorder, inorder)