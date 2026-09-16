# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.seenMap = {}
        for i, v in enumerate(inorder):
            self.seenMap[v]=i
            
        def dfs(l, r) -> Optional[TreeNode]:
            if l > r:
                return None

            root = TreeNode(preorder[l])
            mid = self.seenMap[root.val]
            root.left = dfs(l+1,mid - 1)
            root.right = dfs(mid + 1, r)
        
        return dfs(0, len(inorder)-1)