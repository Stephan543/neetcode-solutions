# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            s = [(root, 0)]
        else: 
            return []
        result = []
        
        while s:
            node, i = s.pop()
            if len(result)-1 >= i:
                result[i].append(node.val)
            else:
                result.append([node.val])

            if node.right:
                s.append((node.right, i + 1))
            if node.left:
                s.append((node.left, i + 1))
        
        return result
