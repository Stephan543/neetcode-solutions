class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive DFS
        # add to local subset
        # add subset to res when (empty) nums is met

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res