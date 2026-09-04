# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dp = deque()
        dq = deque()

        dp.append(p)
        dq.append(q)
        if len(dp) != len(dq):
            return False

        while dp and dq:
            for _ in range(len(dp)):
                nodep = dp.popleft()
                nodeq = dq.popleft()
                if not nodep and not nodeq:
                    continue
                elif not nodep or not nodeq:
                    return False 
                if nodep.val != nodeq.val:
                    return False

                dp.append(nodep.left)
                dp.append(nodep.right)
            
                dq.append(nodeq.left)
                dq.append(nodeq.right)

        return True